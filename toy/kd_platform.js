/* =====================================================================
 * KDPlatform —— 平台适配层（B站 Toy 版《御剑斩妖录》）
 *
 * 游戏里所有「身份 / 存档 / 排行榜」都只经过这里；游戏代码不直接碰 localStorage，也不发任何网络请求。
 * 在 B站 Toy 里：用 Toy JS SDK（window.toy）——B站昵称头像、云存档、平台排行榜。
 * 不在 B站环境（本地调试、SDK 没加载上、没登录）：自动退回本机实现，照样能玩。
 * SDK 用官方给的接入方式加载：<script src="//s1.hdslb.com/bfs/seed/toy/app/sdk/toy-sdk.js">（B站自己的域名，构建脚本负责插在本段前面）。
 *
 * 接口一览（都返回 Promise，接口形状和本机版一致，游戏代码不用动）：
 *   KDPlatform.isLocal                 true = 本机实现；SDK 可用时为 false
 *   KDPlatform.BOARDS                  排行榜定义（5 个，对应平台榜位 1–5）
 *   KDPlatform.ready()                 SDK 检测完成（isLocal 在这之后才准）
 *   KDPlatform.getUser()               → {id, name, avatar}
 *   KDPlatform.load(key)               → 存档数据（没有时为 null）
 *   KDPlatform.save(key, data)         → true/false
 *   KDPlatform.flush()                 切后台 / 存档退出时调用：把还没上传的存档立即传上去
 *   KDPlatform.submitScore(board, value, extra?) → {ok, improved, best}
 *   KDPlatform.getRank(board)          → {board, local, rows:[{rank,id,name,avatar,value,extra,me}], mine}
 * ===================================================================== */
window.KDPlatform = (function () {
  'use strict';
  var NS = 'kd_xian_';   // 本机存储的键名前缀
  var mem = {};          // localStorage 用不了时退回内存，至少这次打开能正常玩

  function lsGet(k) {
    try { var v = localStorage.getItem(NS + k); if (v != null) return v; } catch (e) {}
    return Object.prototype.hasOwnProperty.call(mem, k) ? mem[k] : null;
  }
  function lsSet(k, v) {
    mem[k] = v;
    try { localStorage.setItem(NS + k, v); return true; } catch (e) { return false; }
  }
  function readJSON(k) { var s = lsGet(k); if (s == null) return null; try { return JSON.parse(s); } catch (e) { return null; } }
  function writeJSON(k, v) { try { return lsSet(k, JSON.stringify(v)); } catch (e) { return false; } }
  function withTimeout(p, ms) {
    return new Promise(function (res, rej) {
      var t = setTimeout(function () { rej(new Error('timeout')); }, ms);
      p.then(function (v) { clearTimeout(t); res(v); }, function (e) { clearTimeout(t); rej(e); });
    });
  }

  /* ---------- 预置道号：拿不到 B站昵称时系统随机分配，玩家不能自己输入（平台规定不许自建昵称） ---------- */
  var NAME_A = ['青云', '玄霄', '紫阳', '太虚', '凌霄', '清风', '明月', '流云', '寒山', '长空',
                '碧落', '苍梧', '听雪', '问剑', '归藏', '丹霞', '星河', '白鹤', '松风', '秋水',
                '玉衡', '天枢', '云中', '沧浪', '无尘', '落霞', '抱朴', '守拙', '观澜', '踏月'];
  var NAME_B = ['子', '真人', '散人', '道人', '居士', '剑仙', '上人', '客', '君', '仙子'];
  function pick(a) { return a[Math.floor(Math.random() * a.length)]; }
  function randName() { return pick(NAME_A) + pick(NAME_B); }
  function randId() { return 'local_' + Date.now().toString(36) + Math.random().toString(36).slice(2, 8); }

  /* ---------- 排行榜定义：slot = 平台榜位（1–5）。order：desc 越大越好，asc 越小越好 ----------
   * 平台每个榜只留每人的最高分，所以 asc 榜（速通用时）上报时取负数，读回来再取反。 */
  var BOARDS = [
    { id: 'realm',  slot: 1, name: '境界榜', desc: '比最高境界',       order: 'desc' },
    { id: 'score',  slot: 2, name: '得分榜', desc: '比单个存档最高得分', order: 'desc' },
    { id: 'wave',   slot: 3, name: '波次榜', desc: '比打到的最高波次',   order: 'desc' },
    { id: 'clear',  slot: 4, name: '速通榜', desc: '比最快证道成圣用时', order: 'asc'  },
    { id: 'clears', slot: 5, name: '通关榜', desc: '比证道成圣次数',     order: 'desc' }
  ];
  var SCORE_MAX = 16777215;
  function boardOf(id) { for (var i = 0; i < BOARDS.length; i++) if (BOARDS[i].id === id) return BOARDS[i]; return null; }
  function toPlat(b, v) { v = Math.round(v); if (b.order === 'asc') v = -v; return Math.max(-SCORE_MAX, Math.min(SCORE_MAX, v)); }
  function fromPlat(b, v) { v = +v || 0; return b.order === 'asc' ? -v : v; }

  /* ---------- SDK 检测（只做一次） ---------- */
  var api = { isLocal: true };
  var sdkP = null;
  function sdk() {
    if (sdkP) return sdkP;
    sdkP = (function () {
      var t = window.toy;
      if (!t || typeof t.isSupport !== 'function') return Promise.resolve(null);
      return withTimeout(Promise.all([t.isSupport('getCloudStorage'), t.isSupport('submitScore'), t.isSupport('getRankList')]), 4000)
        .then(function (r) { var ok = r[0] && r[1] && r[2]; api.isLocal = !ok; return ok ? t : null; })
        .catch(function () { return null; });
    })();
    return sdkP;
  }

  /* ---------- 用户信息 ---------- */
  var userP = null;
  function localUser() {
    var u = readJSON('user'), isNew = false;
    if (!u || !u.id || !u.name) { u = { id: randId(), name: randName(), avatar: '' }; isNew = true; writeJSON('user', u); }
    return { id: String(u.id), name: String(u.name), avatar: u.avatar || '', isNew: isNew };
  }
  function getUser() {
    if (userP) return userP;
    userP = sdk().then(function (t) {
      var lu = localUser();
      if (!t) return lu;
      // 平台：已授权过就直接给；没授权过要用户点一下才弹确认窗，这里拿不到就先用随机道号（排行榜上显示的是平台自己给的 B站昵称）
      return withTimeout(t.getUserProfile(), 3000).then(function (p) {
        if (!p || !p.nickname) return lu;
        return { id: String(p.toyOpenId || lu.id), name: String(p.nickname), avatar: p.avatar || '', isNew: false };
      }).catch(function () { return lu; });
    });
    return userP;
  }

  /* ---------- 存档：本机每次都写；云端节流上传。云存储单值 ≤1024 字节，所以切块存 ---------- */
  var CHUNK = 900;              // 每块字符数（按 UTF-8 留余量；存档 JSON 基本是 ASCII）
  var UPLOAD_GAP = 90 * 1000;   // 两次上传至少隔 90 秒，平台按整个 Toy 共享额度限流
  var pending = {}, lastUp = 0, upTimer = null;

  function cloudKeys(key) { return { n: 's_' + key + '_n' }; }
  function packCloud(key, data) {
    var s = JSON.stringify(data), items = {}, n = Math.ceil(s.length / CHUNK) || 1;
    for (var i = 0; i < n; i++) items['s_' + key + '_' + i] = s.slice(i * CHUNK, (i + 1) * CHUNK);
    items[cloudKeys(key).n] = String(n);
    return items;
  }
  function unpackCloud(key, all) {
    var n = +all[cloudKeys(key).n];
    if (!n) return null;
    var s = '';
    for (var i = 0; i < n; i++) { var part = all['s_' + key + '_' + i]; if (part == null) return null; s += part; }
    try { return JSON.parse(s); } catch (e) { return null; }
  }
  // 两份存档按槽位合并：每个槽位取 updated 较新的那份（断网时玩的进度不会被云端旧档盖掉）
  function mergeSlots(a, b) {
    if (!a || typeof a !== 'object') return b || null;
    if (!b || typeof b !== 'object') return a;
    var out = {}, k;
    for (k in a) out[k] = a[k];
    for (k in b) { if (!out[k] || ((b[k] && b[k].updated) || 0) > ((out[k] && out[k].updated) || 0)) out[k] = b[k]; }
    return out;
  }

  function load(key) {
    var local = readJSON('save_' + key);
    return sdk().then(function (t) {
      if (!t) return local;
      return withTimeout(t.getCloudStorage(), 5000).then(function (all) {
        var cloud = unpackCloud(key, all || {});
        var merged = mergeSlots(local, cloud);
        if (merged) writeJSON('save_' + key, merged);
        return merged;
      }).catch(function () { return local; });
    });
  }
  function upload() {
    upTimer = null;
    var keys = Object.keys(pending);
    if (!keys.length) return Promise.resolve(true);
    return sdk().then(function (t) {
      if (!t) { pending = {}; return true; }
      var items = {};
      keys.forEach(function (k) { var it = packCloud(k, pending[k]); for (var x in it) items[x] = it[x]; });
      var snap = pending; pending = {}; lastUp = Date.now();
      return t.setCloudStorage(items).then(function () { return true; }, function () {
        // 失败（没登录、限流）：放回去，下次再传；不立即重试
        for (var k in snap) if (!pending[k]) pending[k] = snap[k];
        return false;
      });
    });
  }
  function schedule() {
    if (upTimer) return;
    var wait = Math.max(0, UPLOAD_GAP - (Date.now() - lastUp));
    upTimer = setTimeout(upload, wait);
  }
  function save(key, data) {
    var ok = writeJSON('save_' + key, data);
    if (!api.isLocal) { pending[key] = data; schedule(); }
    return Promise.resolve(ok);
  }
  function flush() {
    if (upTimer) { clearTimeout(upTimer); upTimer = null; }
    return upload();
  }

  /* ---------- 排行榜 ---------- */
  function submitScore(board, value, extra) {
    var b = boardOf(board);
    value = +value;
    if (!b || !isFinite(value)) return Promise.resolve({ ok: false, improved: false, best: null });
    var all = readJSON('rank') || {};
    var cur = all[board];
    var improved = !cur || (b.order === 'asc' ? value < cur.value : value > cur.value);
    var sent = cur && cur.sent;
    if (improved) { all[board] = cur = { value: value, extra: extra || null, at: Date.now(), sent: false }; writeJSON('rank', all); sent = false; }
    if (sent) return Promise.resolve({ ok: true, improved: false, best: cur.value });
    // 只把还没报上去的本机最好成绩报给平台（平台只留最高分，重复报同分也耗额度）
    return sdk().then(function (t) {
      if (!t) return { ok: true, improved: improved, best: cur.value };
      return t.submitScore({ board: b.slot, score: toPlat(b, cur.value) }).then(function () {
        var a2 = readJSON('rank') || {}; if (a2[board] && a2[board].value === cur.value) { a2[board].sent = true; writeJSON('rank', a2); }
        delete rankCache[board];
        return { ok: true, improved: improved, best: cur.value };
      }, function () { return { ok: true, improved: improved, best: cur.value }; });
    });
  }

  var rankCache = {};           // 榜单拉一次本地复用 60 秒（平台不让轮询）
  function localRank(board, u) {
    var r = (readJSON('rank') || {})[board];
    var row = r ? { rank: 1, id: u.id, name: u.name, avatar: u.avatar, value: r.value, extra: r.extra, me: true } : null;
    return { board: board, local: true, rows: row ? [row] : [], mine: row };
  }
  function getRank(board) {
    var b = boardOf(board);
    return Promise.all([getUser(), sdk()]).then(function (x) {
      var u = x[0], t = x[1];
      if (!t || !b) return localRank(board, u);
      var c = rankCache[board];
      if (c && Date.now() - c.at < 60000) return c.res;
      var mineLocal = (readJSON('rank') || {})[board];
      return Promise.all([
        t.getRankList({ board: b.slot, period: 'all', limit: 50 }),
        t.getMyRank({ board: b.slot, period: 'all' }).catch(function () { return { ranked: false }; })
      ]).then(function (r) {
        var list = r[0] || [], my = r[1] || {};
        var rows = list.map(function (it) {
          var me = !!(my.ranked && +it.rank === +my.rank);
          return { rank: +it.rank, id: '', name: it.nickname || '无名道友', avatar: it.avatar || '', value: fromPlat(b, it.score),
                   extra: me && mineLocal ? mineLocal.extra : null, me: me };
        });
        var mine = null;
        if (my.ranked) {
          mine = rows.filter(function (row) { return row.me; })[0] ||
                 { rank: +my.rank, id: u.id, name: u.name, avatar: u.avatar, value: fromPlat(b, my.score), extra: mineLocal ? mineLocal.extra : null, me: true };
          if (rows.indexOf(mine) < 0) rows.push(mine);
        }
        var res = { board: board, local: false, rows: rows, mine: mine };
        rankCache[board] = { at: Date.now(), res: res };
        return res;
      }).catch(function () { return localRank(board, u); });
    });
  }

  api.BOARDS = BOARDS;
  api.ready = function () { return sdk().then(function () { return !api.isLocal; }); };
  api.getUser = getUser;
  api.load = load;
  api.save = save;
  api.flush = flush;
  api.submitScore = submitScore;
  api.getRank = getRank;
  sdk();
  return api;
})();

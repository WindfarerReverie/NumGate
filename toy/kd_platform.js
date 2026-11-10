/* =====================================================================
 * KDPlatform —— 平台适配层（B站 Toy 版《御剑斩妖录》）
 *
 * 游戏里所有「身份 / 存档 / 排行榜」都只经过这里；游戏代码不直接碰 localStorage，也不发任何网络请求。
 * 现在是「本机实现」：道号由系统随机分配，存档和成绩都存在这台设备的浏览器里。
 *
 * 拿到 Toy SDK 文档后只改这一段：把标了 TODO(Toy SDK·…) 的地方换成 SDK 调用。
 * 所有方法都返回 Promise，接口形状不变，游戏代码不用动。
 * 注意：SDK 的 js 文件要放进上传包里、用相对路径引用，不能从站外加载（平台不允许站外请求）。
 *
 * 接口一览：
 *   KDPlatform.isLocal                 true = 本机实现；接入 SDK 后改成 false
 *   KDPlatform.BOARDS                  排行榜定义（最多 5 个）
 *   KDPlatform.getUser()               → {id, name, avatar}
 *   KDPlatform.load(key)               → 存档数据（没有时为 null）
 *   KDPlatform.save(key, data)         → true/false
 *   KDPlatform.flush()                 切后台 / 存档退出时调用：把还没上传的存档立即传上去
 *   KDPlatform.submitScore(board, value, extra?) → {ok, improved, best}
 *   KDPlatform.getRank(board)          → {board, local, rows:[{rank,id,name,avatar,value,extra,me}], mine}
 * ===================================================================== */
window.KDPlatform = (function () {
  'use strict';
  var NS = 'kd_xian_';   // 本机存储的键名前缀（Toy 里每个作品是独立的域，加前缀只是为了清楚）
  var mem = {};          // localStorage 用不了时（隐私模式、iframe 禁止存储）退回内存，至少这次打开能正常玩

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

  /* ---------- 预置道号：系统随机分配，玩家不能自己输入（平台规定不许自建昵称） ---------- */
  var NAME_A = ['青云', '玄霄', '紫阳', '太虚', '凌霄', '清风', '明月', '流云', '寒山', '长空',
                '碧落', '苍梧', '听雪', '问剑', '归藏', '丹霞', '星河', '白鹤', '松风', '秋水',
                '玉衡', '天枢', '云中', '沧浪', '无尘', '落霞', '抱朴', '守拙', '观澜', '踏月'];
  var NAME_B = ['子', '真人', '散人', '道人', '居士', '剑仙', '上人', '客', '君', '仙子'];
  function pick(a) { return a[Math.floor(Math.random() * a.length)]; }
  function randName() { return pick(NAME_A) + pick(NAME_B); }
  function randId() { return 'local_' + Date.now().toString(36) + Math.random().toString(36).slice(2, 8); }

  /* ---------- 排行榜定义（最多 5 个榜）。order：desc 越大越好，asc 越小越好 ---------- */
  var BOARDS = [
    { id: 'realm',  name: '境界榜', desc: '比最高境界',       order: 'desc' },
    { id: 'score',  name: '得分榜', desc: '比单个存档最高得分', order: 'desc' },
    { id: 'wave',   name: '波次榜', desc: '比打到的最高波次',   order: 'desc' },
    { id: 'clear',  name: '速通榜', desc: '比最快证道成圣用时', order: 'asc'  },
    { id: 'clears', name: '通关榜', desc: '比证道成圣次数',     order: 'desc' }
  ];
  function boardOf(id) { for (var i = 0; i < BOARDS.length; i++) if (BOARDS[i].id === id) return BOARDS[i]; return null; }

  /* ---------- SDK 初始化 ---------- */
  function sdk() {
    // TODO(Toy SDK·初始化)：在这里初始化 Toy SDK（只初始化一次，缓存结果），成功返回 SDK 对象；
    //   失败或不在 B站环境里（本地调试）返回 null，下面各方法就走本机实现。
    return Promise.resolve(null);
  }

  /* ---------- 用户信息 ---------- */
  var userP = null;
  function getUser() {
    if (userP) return userP;
    userP = sdk().then(function () {
      // TODO(Toy SDK·用户信息)：SDK 可用时，改成调用「获取当前用户信息」，
      //   返回 {id: B站用户的唯一标识, name: B站昵称, avatar: 头像地址}，头像地址只用平台给的。
      //   拿不到（未登录、拒绝授权）再退回下面的本机随机道号。
      var u = readJSON('user');
      var isNew = false;
      if (!u || !u.id || !u.name) { u = { id: randId(), name: randName(), avatar: '' }; isNew = true; writeJSON('user', u); }
      return { id: String(u.id), name: String(u.name), avatar: u.avatar || '', isNew: isNew };
    });
    return userP;
  }

  /* ---------- 存档 ---------- */
  function load(key) {
    return sdk().then(function () {
      // TODO(Toy SDK·云存档)：SDK 可用时，改成「读取云存档」。
      //   建议云端、本机各读一份：游戏存档每个槽位都带 updated 时间戳，按槽位取较新的那份，
      //   这样断网时玩的进度也不会被云端旧档盖掉。
      return readJSON('save_' + key);
    });
  }
  function save(key, data) {
    // 本机这份同步写入：关页面前的最后一次存档也不会丢
    var ok = writeJSON('save_' + key, data);
    // TODO(Toy SDK·云存档)：在这里再调用「写入云存档」。游戏存得很勤（每 30 秒、每次买东西都存），
    //   接入时请节流合并（例如 1～2 分钟内只上传最后一份），并留意 SDK 的大小和频率限制。
    return Promise.resolve(ok);
  }
  function flush() {
    // TODO(Toy SDK·云存档)：把节流中还没上传的那份存档立即上传（游戏在切后台、存档退出时调用）。
    return Promise.resolve(true);
  }

  /* ---------- 排行榜 ---------- */
  function submitScore(board, value, extra) {
    var b = boardOf(board);
    value = +value;
    if (!b || !isFinite(value)) return Promise.resolve({ ok: false, improved: false, best: null });
    var all = readJSON('rank') || {};
    var cur = all[board];
    var improved = !cur || (b.order === 'asc' ? value < cur.value : value > cur.value);
    if (improved) { all[board] = { value: value, extra: extra || null, at: Date.now() }; writeJSON('rank', all); }
    // TODO(Toy SDK·排行榜)：improved 为 true 时，调用「上报分数」把 value 报到对应的平台排行榜
    //   （平台榜单 id 和这里的 board 对应起来；extra 里是存档号、第几世、倒下次数，SDK 支持附加信息就一起带上）。
    //   只在破纪录时上报，避免频繁调用。
    return Promise.resolve({ ok: true, improved: improved, best: improved ? value : cur.value });
  }
  function getRank(board) {
    return getUser().then(function (u) {
      // TODO(Toy SDK·排行榜)：SDK 可用时，改成「拉取排行榜」：rows 放前若干名（每行 rank、id、name、avatar、value、extra），
      //   mine 放自己那一行（含名次，没上榜为 null），local 改成 false。
      var r = (readJSON('rank') || {})[board];
      var row = r ? { rank: 1, id: u.id, name: u.name, avatar: u.avatar, value: r.value, extra: r.extra, me: true } : null;
      return { board: board, local: true, rows: row ? [row] : [], mine: row };
    });
  }

  return {
    isLocal: true,   // TODO(Toy SDK)：接入后，SDK 可用时改成 false（界面会改显示「存档跟着B站账号走」）
    BOARDS: BOARDS,
    getUser: getUser,
    load: load,
    save: save,
    flush: flush,
    submitScore: submitScore,
    getRank: getRank
  };
})();

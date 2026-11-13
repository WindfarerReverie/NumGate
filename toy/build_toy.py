#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
把仓库根目录的最新版游戏（xian.html 修仙界、girl.html 星愿界）转换成 B站 Toy 上传包：toy/pkg/
  toy/pkg/index.html   修仙界（Toy 入口，平台要求 ≤1MB）
  toy/pkg/girl.html    星愿界（两个世界互通：同一个 Toy 里用相对地址互相跳）
  toy/pkg/fonts/       书法字（原来内嵌在 HTML 里，抽出来才能把入口压到 1MB 以内）
  toy/pkg/art/         图片、音效、配音、背景音乐（游戏原样用相对路径读，同一个 Toy 里不算站外）
上传时把 toy/pkg 整个文件夹打成 zip（根目录就是 index.html）。

和网站版的区别：
  - 没有昵称+密码登录、没有 Supabase；身份 / 云存档 / 排行榜都走 B站 Toy SDK（适配层 kd_platform.js）
  - 本机存档照旧用浏览器存储，另外同步一份到 B站云存档；两边按每个存档的更新时间取新的
  - 排行榜 5 个：波次、境界、得分、速通、通关（平台每个榜只留每人最高分）
  - 去掉所有站外请求（Google 字体、Supabase、版本检查）
每一处替换都检查“原文恰好出现 1 次”，游戏以后改了对不上会直接报错，提醒人工核对。

用法：python3 toy/build_toy.py
"""
import base64, os, re, shutil, sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(HERE, 'pkg')
RUSSO = os.path.join(HERE, 'fonts', 'russo-one-latin-400-normal.woff2')
ADAPTER = os.path.join(HERE, 'kd_platform.js')
SDK_TAG = '<script src="//s1.hdslb.com/bfs/seed/toy/app/sdk/toy-sdk.js"></script>\n'   # B站 Toy 官方接入方式（站内域名）

s = ''
def rep(old, new, count=1):
    global s
    n = s.count(old)
    if n != count:
        sys.exit('[%s] 替换失败：期望出现 %d 次，实际 %d 次：%r' % (CUR, count, n, old[:90]))
    s = s.replace(old, new)

def cut(start, end, new, keep_end=True):
    global s
    i = s.find(start)
    if i < 0 or s.find(start, i + 1) >= 0:
        sys.exit('[%s] 段落起点找不到或不唯一：%r' % (CUR, start[:90]))
    j = s.find(end, i)
    if j < 0:
        sys.exit('[%s] 段落终点找不到：%r' % (CUR, end[:90]))
    if not keep_end:
        j += len(end)
    s = s[:i] + new + s[j:]


SAVE_RANK = r'''
/* ================= Toy 版：存档同步 / 身份 / 排行榜（全部经过文件开头的 KDPlatform） ================= */
const Me={id:'',name:''};
async function syncCloud(){   // 云端那份和本机按每个存档的更新时间取新的
  try{const c=await KDPlatform.load('slots');if(!c||typeof c!=='object')return;let ch=false;
    for(const k in c){const R=c[k];if(!R||R.deleted)continue;const L=Save.slots[k];
      if(!L||(R.updated||0)>(L.updated||0)){Save.slots[k]=norm(JSON.parse(JSON.stringify(R)));ch=true}}
    if(ch)saveLocal()}catch(e){}
}
function commit(i){if(Save.slots[i])Save.slots[i].updated=Date.now();saveLocal();KDPlatform.save('slots',Save.slots)}
function acctUI(){$('acctBar').hidden=false;$('acctName').textContent=Me.name?'道号：'+Me.name:'';
  $('syncNote').textContent=KDPlatform.isLocal?'存档保存在这台设备上（在B站App里打开，存档跟着B站账号走）':'存档跟着你的B站账号走，换设备也能继续'}
async function boot(){   // 打开就能玩：先拿名字，再把云端存档合进来
  try{const u=await KDPlatform.getUser();if(u){Me.id=u.id;Me.name=u.name}}catch(e){}
  await syncCloud();
  Save.ready=true;acctUI();renderSlots();if(!$('ovHub').hidden)renderHub();openFromHash();
}
/* 排行榜：5 个榜。平台每个榜只留每人最高分，所以按存档里最好的那条报 */
const RANK_FMT={wave:v=>'第'+fmt(v)+'<small>波</small>',realm:v=>wRealm(MYW,v),score:v=>fmt(v)+'<small>分</small>',clear:v=>mmss(v),clears:v=>fmt(v)+'<small>次</small>'};
const RANK_IC={wave:'🌊',realm:'⛰',score:'⭐',clear:'⏱',clears:'🏆'};
function slotScores(i){const d=Save.slots[i];if(!d||!(d.bestRealm||d.runs))return null;
  const r={wave:d.bestWave||0,realm:d.bestRealm||0,score:d.bestScore||0};
  if(d.clears){r.clears=d.clears;if(d.bestClear)r.clear=Math.round(d.bestClear)}
  return {r,ex:{slot:i,world:d.world||MYW,life:d.life||1,deaths:d.deaths||0}}}
async function pushScores(){
  const jobs=[];for(let i=1;i<=SLOTS;i++){const x=slotScores(i);if(!x)continue;for(const b in x.r)if(x.r[b]>0)jobs.push(KDPlatform.submitScore(b,x.r[b],x.ex))}
  try{await Promise.all(jobs)}catch(e){}}
function extraTxt(x){if(!x||typeof x!=='object')return '';const a=[];
  if(x.slot)a.push('存档'+(x.slot|0));if(x.world&&WD[x.world])a.push(WD[x.world].w);if(x.life>1)a.push('第'+CNN(x.life|0)+'世');
  if(x.deaths!=null)a.push(x.deaths?'重修 '+(x.deaths|0)+' 次':'<b class="nd">不死</b>');return a.join(' · ')}
function rankRows(el,res,board,max){
  el.innerHTML='';const rows=(res&&res.rows)||[],f=RANK_FMT[board]||fmt;
  rows.forEach((r,i)=>{if(i>=max&&!r.me)return;const d=document.createElement('div');d.className='rk'+(i<3?' t'+(i+1):i<10?' t10':'')+(r.me?' me':'');
    d.innerHTML='<b class="no">'+(i<3?['🥇','🥈','🥉'][i]:((+r.rank)||i+1))+'</b><div><div class="who"></div><div class="what">'+extraTxt(r.extra)+'</div></div><span class="sc">'+f(+r.value||0)+'</span>';
    d.querySelector('.who').textContent=(r.name||'无名道友');el.appendChild(d)});
  if(!rows.length)el.innerHTML='<p class="sync">还没有记录，打一局就有了</p>';
}
let rankBoard='wave',rankBack='ovTitle';
function rankTabs(){const box=$('rankTabs');box.innerHTML='';
  for(const b of KDPlatform.BOARDS){const t=document.createElement('button');t.className='sb'+(b.id===rankBoard?'':' ghost');t.id='rk_'+b.id;
    t.textContent=b.name;t.onclick=()=>{rankBoard=b.id;showRankBoard()};box.appendChild(t)}}
async function showRankBoard(){
  rankTabs();const B=KDPlatform.BOARDS.find(b=>b.id===rankBoard)||{};
  $('rankList').innerHTML='<p class="sync">加载中…</p>';
  try{const res=await KDPlatform.getRank(rankBoard);if(rankBoard!==res.board)return;
    $('rankNote').textContent=(B.desc||'')+(res.local?' · 现在是本机记录（在B站App里登录打开，就能和大家一起比）':'');
    rankRows($('rankList'),res,rankBoard,50)}
  catch(e){$('rankList').innerHTML='<p class="sync">排行榜暂时加载不了</p>'}
}
async function showRank(back){rankBack=back;$('rankList').innerHTML='';show('ovRank');await pushScores();showRankBoard()}
async function endRank(){   // 结算页：每个榜上自己的成绩和名次
  const el=$('rRank');el.hidden=false;el.innerHTML='<p class="sync">记录成绩中…</p>';
  try{await pushScores();const box=document.createElement('div');box.style.cssText='display:flex;flex-direction:column;gap:4px';let local=false;
    for(const b of KDPlatform.BOARDS){const res=await KDPlatform.getRank(b.id),m=res&&res.mine;if(!m)continue;local=local||res.local;
      const d=document.createElement('div');d.className='rk';
      d.innerHTML='<b>'+(RANK_IC[b.id]||'•')+'</b><div><div class="who"></div><div class="what">'+(res.local?'本机最好':'第 '+((+m.rank)||'-')+' 名')+(extraTxt(m.extra)?' · '+extraTxt(m.extra):'')+'</div></div><span class="sc">'+(RANK_FMT[b.id]||fmt)(+m.value||0)+'</span>';
      d.querySelector('.who').textContent=b.name;box.appendChild(d)}
    el.innerHTML='';el.appendChild(box);
    if(local){const p=document.createElement('p');p.className='sync';p.textContent='本机记录 · 在B站App里登录打开，成绩会上B站排行榜';el.appendChild(p)}
  }catch(e){el.innerHTML='<p class="sync">排行榜暂时加载不了</p>'}
}

'''


def build(src_name, out_name, font_name):
    global s, CUR
    CUR = src_name
    s = open(os.path.join(ROOT, src_name), encoding='utf-8').read()

    # ---------- 头部：Supabase 配置 → Toy SDK + 平台适配层；去掉版本检查、Google 字体
    adapter = open(ADAPTER, encoding='utf-8').read().strip()
    cut('<script>window.NG_CFG=', '</script>\n', SDK_TAG + '<script>\n' + adapter + '\n</script>\n', keep_end=False)
    cut('<script>(function(){var B="', '</script>\n', '', keep_end=False)
    s = re.sub(r'<link[^>]*fonts\.g(?:oogleapis|static)\.com[^>]*>\n?', '', s)

    # ---------- 字体：书法字抽成单独文件（入口 ≤1MB）；Russo One 内嵌；Ma Shan Zheng 换成同款内嵌的 NGBrush
    m = re.search(r"(@font-face\{font-family:'NGBrush';src:url\()data:font/woff2;base64,([A-Za-z0-9+/=]+)(\))", s)
    if not m:
        sys.exit('[%s] 找不到内嵌书法字' % CUR)
    os.makedirs(os.path.join(OUT, 'fonts'), exist_ok=True)
    open(os.path.join(OUT, 'fonts', font_name), 'wb').write(base64.b64decode(m.group(2)))
    s = s[:m.start()] + m.group(1) + "'fonts/" + font_name + "'" + m.group(3) + s[m.end():]
    russo = base64.b64encode(open(RUSSO, 'rb').read()).decode()
    rep("/*BRUSHFONT_END*/",
        "/*BRUSHFONT_END*/\n/* Russo One（数字字体，SIL OFL 1.1，内嵌，原来从 Google Fonts 加载） */"
        "@font-face{font-family:'Russo One';src:url(data:font/woff2;base64," + russo + ") format('woff2');font-display:swap;"
        "unicode-range:U+0000-00FF,U+0131,U+0152-0153,U+02BB-02BC,U+02C6,U+02DA,U+02DC,U+0304,U+0308,U+0329,U+2000-206F,U+20AC,U+2122,U+2191,U+2193,U+2212,U+2215,U+FEFF,U+FFFD}")
    rep('font-family:"Ma Shan Zheng",var(--display)', 'font-family:"NGBrush",var(--display)')
    rep(':root{--brush:"NGBrush","Ma Shan Zheng",var(--body)}', ':root{--brush:"NGBrush",var(--body)}')
    rep("const BRUSH='\"NGBrush\",\"Ma Shan Zheng\",'+CN;", "const BRUSH='\"NGBrush\",'+CN;")
    rep("g.font='13px \"Ma Shan Zheng\",serif'", "g.font='13px \"NGBrush\",serif'")

    # ---------- 样式：去掉输入框样式，加排行榜分榜按钮
    # （.inp 样式留着：「回到第 N 波」的数字框还在用）
    rep('.rank{display:flex', '.rtabs{display:flex;flex-wrap:wrap;gap:6px;justify-content:center}'
        '.rtabs .sb{padding:6px 10px;font-size:12.5px}\n.rank{display:flex')

    # ---------- 页面：去掉登录界面；排行榜加分榜按钮；账号栏只留名字和排行榜
    cut('  <div class="ov" id="ovLogin" hidden>', '  <div class="ov" id="ovRank" hidden>', '')
    cut('  <div class="ov" id="ovRank" hidden>', '  <div class="ov" id="ovHelp" hidden>',
        '''  <div class="ov" id="ovRank" hidden>
    <div class="card">
      <h2>排行榜</h2>
      <div class="rtabs" id="rankTabs"></div>
      <p class="sync" id="rankNote"></p>
      <div class="rank" id="rankList"></div>
      <button class="go alt" id="bRankBack">返 回</button>
    </div>
  </div>
''')
    rep('<div class="acct" id="acctBar" hidden><span id="acctName"></span><button class="sb ghost" id="bRankT">排行榜</button><button class="sb ghost" id="bLogout">退出</button></div>',
        '<div class="acct" id="acctBar"><span id="acctName"></span><button class="sb ghost" id="bRankT">排行榜</button></div>')
    rep('<button class="go alt" id="bRankH" hidden>排行榜</button>', '<button class="go alt" id="bRankH">排行榜</button>')

    # ---------- 存档 / 世界互通 / 账号 / 排行榜
    # Claude 页面云存档（window.claude）整段换成同步 B站云存档
    cut('async function cloudWrite(i){', '/* ================= ONLINE', '', keep_end=True)
    # （commit、initCloud、setSync 都在上面这段里，一起去掉；commit 在下面重新定义）
    # 两个世界在同一个 Toy 里：index.html 是修仙界，girl.html 是星愿界，用相对地址跳
    cut('function worldURL(w){', 'async function goWorld(i){',
        "function worldURL(w){return w==='girl'?'girl.html':'index.html'}\n")
    rep("  if(Net.on){try{clearTimeout(Net.t);await timeout(netPush(),8000)}catch(e){}}\n",
        "  try{await timeout(KDPlatform.flush(),5000)}catch(e){}\n")
    # Supabase 账号、云存档、排行榜整段换掉
    cut('const Net={sb:null,', ' / collection =', SAVE_RANK); s = s.replace(SAVE_RANK + ' / collection =', SAVE_RANK + '/* ================= 图鉴 / collection =', 1) if CUR == 'xian.html' else s.replace(SAVE_RANK + ' / collection =', SAVE_RANK + '/* ================= 衣橱图鉴 / collection =', 1)
    rep('/* ================= ONLINE (GitHub 版：Supabase 账号 + 云存档 + 排行榜) ================= */\n', '')
    rep('const NG_CFG=window.NG_CFG&&window.NG_CFG.url?window.NG_CFG:null;\n', '')

    # 平台存档读回来之前，不让点「新游戏」，免得被随后读回的存档覆盖
    rep("function renderSlots(){\n  const box=$('slots');box.innerHTML='';\n",
        "function renderSlots(){\n  const box=$('slots');box.innerHTML='';\n  if(!Save.ready){box.innerHTML='<p class=\"sync\">读取存档中…</p>';return}\n")
    rep("'ovLogin','ovRank',", "'ovRank',")
    cut("  rank:{t:'排行榜',d:'", "\n",
        "  rank:{t:'排行榜',d:'五个榜：波次榜（打到最远的波次）、境界榜（最高境界）、得分榜、速通榜（最快证道成圣）、通关榜（证道次数）。每个存档的成绩都算，自己那一行后面显示是哪个存档、哪个世界、重修几次，一次都没倒过的显示「不死」。在B站App里登录打开，成绩直接上B站排行榜。'},\n",
        keep_end=False)
    cut("$('bLogin').onclick=", "$('bOverHub').onclick=",
        "$('bRankT').onclick=()=>showRank('ovTitle');$('bRankH').onclick=()=>showRank('ovHub');\n"
        "$('bRankBack').onclick=()=>{if(rankBack==='ovHub')renderHub();else renderSlots();show(rankBack||'ovTitle')};\n")
    rep("$('bQuit').onclick=()=>{saveRun();if(Net.on)netPush();", "$('bQuit').onclick=()=>{saveRun();pushScores();KDPlatform.flush();")
    rep("document.addEventListener('visibilitychange',()=>{if(document.hidden){if(running)saveRun();if(Net.on)netPush()}});",
        "document.addEventListener('visibilitychange',()=>{if(document.hidden){if(running)saveRun();pushScores();KDPlatform.flush()}});")
    rep("if(NG_CFG)initNet();else{initCloud();openFromHash()}", "boot();")

    # ---------- 自检：不许残留站外地址、登录、输入框、Claude 页面接口
    bad = []
    # 允许：音量滑条（range）和「回到第 N 波」（number）——都不是自由输入文字
    for pat in [r'https?://', r'supabase', r'(?<!window\.)\bNG_CFG\b', r'window\.NG_CFG\s*=', r'\bNet\.', r'<input(?![^>]*type="(?:range|number)")', r'<textarea', r'contenteditable',
                r'sessionStorage', r'version\.json', r'serviceWorker', r'Ma Shan Zheng', r'window\.claude',
                r'fetch\(\s*[\'"]https?', r'\bnetPush\b', r'\binitNet\b', r'\bdoAuth\b', r'cloudWrite']:
        if re.search(pat, s, re.I):
            bad.append(pat)
    if bad:
        sys.exit('[%s] 产物里还残留：%s' % (CUR, bad))
    open(os.path.join(OUT, out_name), 'w', encoding='utf-8').write(s)
    kb = len(s.encode('utf-8')) / 1024
    print('已生成 toy/pkg/%s（%.1f KB）' % (out_name, kb))
    if out_name == 'index.html' and kb > 1000:
        sys.exit('入口 index.html 超过平台 1MB 上限')


if os.path.isdir(OUT):
    shutil.rmtree(OUT)
os.makedirs(OUT)
build('xian.html', 'index.html', 'ngbrush_xian.woff2')
build('girl.html', 'girl.html', 'ngbrush_girl.woff2')
shutil.copytree(os.path.join(ROOT, 'art'), os.path.join(OUT, 'art'))
total = sum(os.path.getsize(os.path.join(dp, f)) for dp, _, fs in os.walk(OUT) for f in fs)
print('上传包 toy/pkg 合计 %.1f MB（平台上限 50 MB）' % (total / 1048576))

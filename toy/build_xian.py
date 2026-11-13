#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
把仓库根目录的 xian.html（网页版：昵称+密码登录、Supabase 存档和排行榜）
转换成 B站 Toy 上传包：toy/xian/index.html。

为什么用脚本而不是手改一份：xian.html 以后还会继续更新玩法，
重新运行本脚本就能再生成一份 Toy 版，不用每次手工同步。
每一处替换都会检查“原文恰好出现 1 次”，原文变了脚本会直接报错，提醒人工核对。

用法：python3 toy/build_xian.py
产物：toy/xian/index.html（单文件，图片、字体全部内嵌，无任何站外请求）
"""
import base64
import os
import re
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SRC = os.path.join(ROOT, 'xian.html')
OUT_DIR = os.path.join(ROOT, 'toy', 'xian')
OUT = os.path.join(OUT_DIR, 'index.html')
HERE = os.path.dirname(os.path.abspath(__file__))
RUSSO = os.path.join(HERE, 'fonts', 'russo-one-latin-400-normal.woff2')
ADAPTER = os.path.join(HERE, 'kd_platform.js')

s = open(SRC, encoding='utf-8').read()


def rep(old, new, count=1):
    """精确替换，并检查原文出现次数，防止原文件改动后悄悄替换错地方。"""
    global s
    n = s.count(old)
    if n != count:
        sys.exit('替换失败：期望出现 %d 次，实际 %d 次：%r' % (count, n, old[:80]))
    s = s.replace(old, new)


def cut(start, end, new, keep_end=True):
    """把从 start 开始、到 end 之前（keep_end=True 时保留 end）的整段换成 new。"""
    global s
    i = s.find(start)
    if i < 0 or s.find(start, i + 1) >= 0:
        sys.exit('段落起点找不到或不唯一：%r' % start[:80])
    j = s.find(end, i)
    if j < 0:
        sys.exit('段落终点找不到：%r' % end[:80])
    if not keep_end:
        j += len(end)
    s = s[:i] + new + s[j:]


# ---------------------------------------------------------------- 头部
# 1) 去掉 Supabase 配置（含项目地址和 key），换成平台适配层 KDPlatform（集中写在文件开头）
adapter = open(ADAPTER, encoding='utf-8').read().strip()
SDK_TAG = '<script src="//s1.hdslb.com/bfs/seed/toy/app/sdk/toy-sdk.js"></script>\n'   # B站 Toy 官方接入方式（站内域名）
cut('<script>window.NG_CFG=', '</script>\n', SDK_TAG + '<script>\n' + adapter + '\n</script>\n', keep_end=False)

# 2) 去掉 version.json 自动刷新（Toy 包是静态上传的，不需要也不能这样拉新版本）
cut('<script>(function(){var B="', '</script>\n', '', keep_end=False)

# 3) 去掉 Google Fonts 外链
rep('<link rel="preconnect" href="https://fonts.googleapis.com">\n', '')
rep('<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>\n', '')
cut('<link rel="stylesheet" href="https://fonts.googleapis.com/css2?', '>\n', '', keep_end=False)

# 4) 字体：
#   - 书法字 NGBrush 本来就是内嵌的「马善政体」子集，覆盖了游戏里用到的所有汉字，
#     所以原来写的 "Ma Shan Zheng"（从 Google 加载的同一款字体）直接换成 NGBrush，画面一致；
#   - 数字用的 Russo One 只有 7KB，直接内嵌进来。
russo = base64.b64encode(open(RUSSO, 'rb').read()).decode()
rep("/*BRUSHFONT_END*/",
    "/*BRUSHFONT_END*/\n/* Russo One（数字字体，SIL OFL 1.1，内嵌，原来从 Google Fonts 加载） */"
    "@font-face{font-family:'Russo One';src:url(data:font/woff2;base64," + russo + ") format('woff2');font-display:swap;"
    "unicode-range:U+0000-00FF,U+0131,U+0152-0153,U+02BB-02BC,U+02C6,U+02DA,U+02DC,U+0304,U+0308,U+0329,U+2000-206F,U+20AC,U+2122,U+2191,U+2193,U+2212,U+2215,U+FEFF,U+FFFD}")
rep('font-family:"Ma Shan Zheng",var(--display)', 'font-family:"NGBrush",var(--display)')
rep(':root{--brush:"NGBrush","Ma Shan Zheng",var(--body)}', ':root{--brush:"NGBrush",var(--body)}')
rep("const BRUSH='\"NGBrush\",\"Ma Shan Zheng\",'+CN;", "const BRUSH='\"NGBrush\",'+CN;")
rep("g.font='13px \"Ma Shan Zheng\",serif'", "g.font='13px \"NGBrush\",serif'")

# 5) 去掉输入框样式，加排行榜分榜按钮的样式
cut('.inp{width:100%;', '.rank{display:flex', '.rtabs{display:flex;flex-wrap:wrap;gap:6px;justify-content:center}'
    '.rtabs .sb{padding:6px 10px;font-size:12.5px}\n')

# ---------------------------------------------------------------- 页面结构
# 6) 删掉整个「昵称+密码」登录界面
cut('  <div class="ov" id="ovLogin" hidden>', '  <div class="ov" id="ovRank" hidden>', '')

# 7) 排行榜界面：加 5 个分榜按钮和说明小字
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

# 8) 标题页账号栏：只显示系统分配的道号 + 排行榜按钮（没有登录/退出）
rep('<div class="acct" id="acctBar" hidden><span id="acctName"></span><button class="sb ghost" id="bRankT">排行榜</button><button class="sb ghost" id="bLogout">退出</button></div>',
    '<div class="acct" id="acctBar"><span id="acctName"></span><button class="sb ghost" id="bRankT">排行榜</button></div>')
# 9) 存档主页的排行榜按钮一直显示
rep('<button class="go alt" id="bRankH" hidden>排行榜</button>', '<button class="go alt" id="bRankH">排行榜</button>')

# ---------------------------------------------------------------- 脚本
# 10) 存档 / 账号 / 排行榜：整段换成只经过 KDPlatform 的版本
#     （原来这里是 localStorage 直读写、Claude 云存档、Supabase 登录、云存档和排行榜）
cut("let LKEY='ng_slots';", '/* ================= 图鉴 / collection', r'''/* ================= 存档 / 道号 / 排行榜（Toy 版：全部只经过文件开头的 KDPlatform） ================= */
const SAVE_KEY='slots';
const Me={id:'',name:'',avatar:''};
function applySlots(j){Save.slots={};if(j&&typeof j==='object'){for(const k in j)if(j[k])norm(j[k]);Save.slots=j}}
function saveLocal(){KDPlatform.save(SAVE_KEY,Save.slots)}
function commit(i){if(Save.slots[i])Save.slots[i].updated=Date.now();saveLocal()}
function acctUI(){$('acctName').textContent=Me.name?'道号：'+Me.name:'';
  $('syncNote').textContent=KDPlatform.isLocal?'存档保存在这台设备上':'存档跟着你的B站账号走，换设备也能继续'}
async function boot(){   // 打开就能玩：先拿道号（首次进入系统随机分配），再读存档
  try{const u=await KDPlatform.getUser();if(u){Me.id=u.id;Me.name=u.name;Me.avatar=u.avatar||''}}catch(e){}
  try{applySlots(await KDPlatform.load(SAVE_KEY))}catch(e){applySlots(null)}
  Save.ready=true;acctUI();renderSlots();if(!$('ovHub').hidden)renderHub();
}
/* 排行榜：5 个榜（见 KDPlatform.BOARDS）。倒下次数、第几世作为附加信息跟着成绩一起记 */
const RANK_FMT={realm:v=>rName(rFromCode(v)),score:v=>fmt(v)+'<small>分</small>',wave:v=>'第'+fmt(v)+'<small>波</small>',clear:v=>mmss(v),clears:v=>fmt(v)+'<small>次</small>'};
const RANK_IC={realm:'⛰',score:'⭐',wave:'🌊',clear:'⏱',clears:'🏆'};
function slotScores(i){const d=Save.slots[i];if(!d||!(d.bestRealm||d.runs))return null;
  const r={realm:d.bestRealm||0,score:d.bestScore||0,wave:d.bestWave||0};
  if(d.clears){r.clears=d.clears;if(d.bestClear)r.clear=Math.round(d.bestClear)}
  return {r,ex:{slot:i,life:d.life||1,deaths:d.deaths||0}}}
async function pushScores(){   // 把各存档的最好成绩交给平台（平台层自己判断是不是新纪录）
  const jobs=[];for(let i=1;i<=SLOTS;i++){const x=slotScores(i);if(!x)continue;for(const b in x.r)if(x.r[b]>0)jobs.push(KDPlatform.submitScore(b,x.r[b],x.ex))}
  try{await Promise.all(jobs)}catch(e){}}
function extraTxt(x){if(!x||typeof x!=='object')return '';const a=[];
  if(x.slot)a.push('存档'+(x.slot|0));if(x.life>1)a.push('第'+CNN(x.life|0)+'世');
  if(x.deaths!=null)a.push(x.deaths?'倒下 '+(x.deaths|0)+' 次':'<b class="nd">不死</b>');return a.join(' · ')}
function rankRows(el,res,board,max){
  el.innerHTML='';const rows=(res&&res.rows)||[],f=RANK_FMT[board]||fmt;
  rows.forEach((r,i)=>{if(i>=max&&!r.me)return;const d=document.createElement('div');d.className='rk'+(r.me?' me':'');
    d.innerHTML='<b>'+((+r.rank)||i+1)+'</b><div><div class="who"></div><div class="what">'+extraTxt(r.extra)+'</div></div><span class="sc">'+f(+r.value||0)+'</span>';
    d.querySelector('.who').textContent=(r.name||'无名道友');el.appendChild(d)});
  if(!rows.length)el.innerHTML='<p class="sync">还没有记录，打一局就有了</p>';
}
let rankBoard='realm',rankBack='ovTitle';
function rankTabs(){const box=$('rankTabs');box.innerHTML='';
  for(const b of KDPlatform.BOARDS){const t=document.createElement('button');t.className='sb'+(b.id===rankBoard?'':' ghost');t.id='rk_'+b.id;
    t.textContent=b.name;t.onclick=()=>{rankBoard=b.id;showRankBoard()};box.appendChild(t)}}
async function showRankBoard(){
  rankTabs();const B=KDPlatform.BOARDS.find(b=>b.id===rankBoard)||{};
  $('rankList').innerHTML='<p class="sync">加载中…</p>';
  try{const res=await KDPlatform.getRank(rankBoard);if(rankBoard!==res.board)return;
    $('rankNote').textContent=(B.desc||'')+(res.local?' · 现在是本机记录（没连上B站排行榜，登录B站后再打开就能和大家一起比）':'');
    rankRows($('rankList'),res,rankBoard,50)}
  catch(e){$('rankList').innerHTML='<p class="sync">排行榜暂时加载不了</p>'}
}
async function showRank(back){rankBack=back;$('rankList').innerHTML='';show('ovRank');await pushScores();showRankBoard()}
async function endRank(){   // 结算页：列出每个榜上自己的成绩
  const el=$('rRank');el.hidden=false;el.innerHTML='<p class="sync">记录成绩中…</p>';
  try{await pushScores();const box=document.createElement('div');box.style.cssText='display:flex;flex-direction:column;gap:4px';let local=false;
    for(const b of KDPlatform.BOARDS){const res=await KDPlatform.getRank(b.id),m=res&&res.mine;if(!m)continue;local=local||res.local;
      const d=document.createElement('div');d.className='rk';
      d.innerHTML='<b>'+(RANK_IC[b.id]||'•')+'</b><div><div class="who"></div><div class="what">'+(res.local?'本机最好':'第 '+((+m.rank)||'-')+' 名')+(extraTxt(m.extra)?' · '+extraTxt(m.extra):'')+'</div></div><span class="sc">'+(RANK_FMT[b.id]||fmt)(+m.value||0)+'</span>';
      d.querySelector('.who').textContent=b.name;box.appendChild(d)}
    el.innerHTML='';el.appendChild(box);
    if(local){const p=document.createElement('p');p.className='sync';p.textContent='本机记录 · 登录B站后成绩会上B站排行榜';el.appendChild(p)}
  }catch(e){el.innerHTML='<p class="sync">排行榜暂时加载不了</p>'}
}

''')

# 11) 存档选择：平台存档还没读回来之前，不让点「新游戏」，免得被随后读回的存档覆盖
rep("function renderSlots(){\n  const box=$('slots');box.innerHTML='';\n",
    "function renderSlots(){\n  const box=$('slots');box.innerHTML='';\n  if(!Save.ready){box.innerHTML='<p class=\"sync\">读取存档中…</p>';return}\n")

# 12) 界面列表里去掉登录界面
rep("const OVS=['ovLogin','ovRank',", "const OVS=['ovRank',")

# 13) 玩法说明里排行榜那条，换成 5 个榜的说法
cut("  rank:{t:'排行榜',d:'", "\n",
    "  rank:{t:'排行榜',d:'五个榜：境界榜（最高境界）、得分榜、波次榜、速通榜（最快证道成圣）、通关榜（证道次数）。每个存档的成绩都算，自己那一行后面显示「倒下 N 次」，一次都没倒过的显示「不死」。在B站里玩，成绩直接上B站排行榜；没登录时先记在这台设备上。'},\n",
    keep_end=False)

# 14) 按钮事件：去掉登录/注册/单机/退出，排行榜返回改用新变量
cut("$('bLogin').onclick=", "$('bOverHub').onclick=",
    "$('bRankT').onclick=()=>showRank('ovTitle');$('bRankH').onclick=()=>showRank('ovHub');\n"
    "$('bRankBack').onclick=()=>{if(rankBack==='ovHub')renderHub();else renderSlots();show(rankBack||'ovTitle')};\n")
rep("$('bQuit').onclick=()=>{saveRun();if(Net.on)netPush();", "$('bQuit').onclick=()=>{saveRun();pushScores();KDPlatform.flush();")
rep("document.addEventListener('visibilitychange',()=>{if(document.hidden){if(running)saveRun();if(Net.on)netPush()}});",
    "document.addEventListener('visibilitychange',()=>{if(document.hidden){if(running)saveRun();pushScores();KDPlatform.flush()}});")

# 15) 启动：不再登录，打开就能玩
rep("loadLocal();renderSlots();resize();", "renderSlots();resize();")
rep("if(NG_CFG)initNet();else initCloud();", "boot();")

# ---------------------------------------------------------------- 自检
bad = []
for pat in [r'https?://', r'supabase', r'NG_CFG', r'\bNet\.', r'<input', r'<textarea', r'contenteditable',
            r'localStorage', r'sessionStorage', r'fetch\(', r'version\.json', r'serviceWorker', r'Ma Shan Zheng', r'window\.claude']:
    # localStorage 只允许出现在 KDPlatform 适配层里
    body = s
    if pat == 'localStorage':
        a = s.find('KDPlatform —— 平台适配层')
        b = s.find('</script>', a)
        body = s[:a] + s[b:]
    if re.search(pat, body, re.I):
        bad.append(pat)
if bad:
    sys.exit('产物里还残留：%s' % bad)

os.makedirs(OUT_DIR, exist_ok=True)
open(OUT, 'w', encoding='utf-8').write(s)
print('已生成 %s（%.1f KB）' % (os.path.relpath(OUT, ROOT), len(s.encode('utf-8')) / 1024))

#!/usr/bin/env python3
# 11-02 23:08 John 全面美术自查 · 第二部分：小兵、护法剑环、流派光阵、飞剑坐骑、被动光罩/火焰、技能特效、巨剑/炮弹
import sys
P = '/home/claude/numgate/index.html'
s = open(P, encoding='utf-8').read()
n_ok = 0
def rep(old, new, cnt=1):
    global s, n_ok
    c = s.count(old)
    if c != cnt:
        print('MISS(%d):' % c, old[:120]); sys.exit(1)
    s = s.replace(old, new); n_ok += 1

# ---- 巨剑/巨箭（剑气纵横）→ 被动本体的手绘图；机关炮弹 → 火球图 ----
rep("""function drawBulletsSpecial(){
  for(const b of S.bullets){if(!b.big)continue;ctx.save();""",
"""function drawBulletsSpecial(){
  const JI=ART_ON&&S.path==='ti'?cmpArt('jj',Math.max(0,psForm('jj'))):null,FB=aI('fx_1');
  for(const b of S.bullets){if(b.big&&JI){const ga=ctx.globalAlpha;ctx.globalAlpha=ga*.45;ctx.globalCompositeOperation='lighter';sprH(ctx,JI,b.x,b.y+14,70,0,.5);ctx.globalCompositeOperation='source-over';ctx.globalAlpha=ga;sprH(ctx,JI,b.x,b.y,58,0,.2)}
    else if(b.shell&&FB)sprH(ctx,FB,b.x,b.y,30,Math.atan2(b.vx||0,-(b.vy||-1))+Math.PI,.3)}   /* 巨剑/巨箭用「剑气纵横」本体那张图飞出去；炮弹用火球图 */
  for(const b of S.bullets){if(!b.big||JI)continue;ctx.save();""")
rep("  for(const b of S.bullets){if(!b.shell)continue;\n    ctx.fillStyle='rgba(255,140,40,.35)';",
    "  for(const b of S.bullets){if(!b.shell||FB)continue;\n    ctx.fillStyle='rgba(255,140,40,.35)';")

# ---- 护法剑环（攻速 3 级起绕身的小剑）→ 弹道手绘图 ----
rep("function drawSwordRing(x,y,t,n,rad){\n",
"""function swRingArt(x,y,t,n,rad){const im=ART_ON&&pjImg();if(!im)return false;for(let i=0;i<n;i++){const a=t*2.4+i*6.283/n;sprH(ctx,im,x+Math.cos(a)*rad,y+Math.sin(a)*rad*.45,18,Math.sin(a)*.2)}return true}
function drawSwordRing(x,y,t,n,rad){if(swRingArt(x,y,t,n,rad))return;
""")

# ---- 修仙版小兵 → 小剑侍/小道童背影图 ----
rep("""  let i=0;
  for(let rI=0;rI<rows;rI++){
    const inRow=Math.min(cols,n-i);
    for(let c=0;c<inRow;c++,i++){
      const R=Math.min(HERO.length-1,S.rR),HP=HERO[R],""",
"""  let i=0;const SQI=aI(S.path==='fa'?'sq_fa':'sq_ti');
  if(SQI){for(let rI=0;rI<rows;rI++){const inRow=Math.min(cols,n-i);for(let c=0;c<inRow;c++,i++){const x=S.x+(c-(inRow-1)/2)*cell+(rI%2?cell*.25:0),y=squadY+10+rI*cell*.8+Math.sin(S.t*14+i)*.8;sprH(ctx,SQI,x,y+5,16,0,1)}}i=n;}   /* 小兵：手绘背影 */
  for(let rI=0;rI<rows&&i<n;rI++){
    const inRow=Math.min(cols,n-i);
    for(let c=0;c<inRow;c++,i++){
      const R=Math.min(HERO.length-1,S.rR),HP=HERO[R],""")

# ---- 流派：体修背后的剑、法修脚下法阵、法修环绕的符 ----
rep("""    g.save();g.translate(x-14,y-ht*.55);g.rotate(-.5);g.fillStyle='#e9eef5';g.fillRect(-3,-ht*.55,6,ht*.75);g.fillStyle='#ffd677';g.fillRect(-9,ht*.2,18,4);g.fillStyle='#8a5a2a';g.fillRect(-2.5,ht*.2+4,5,12);g.restore();
    g.strokeStyle='rgba(255,214,119,'+(.35+.25*p)+')';g.lineWidth=2;g.beginPath();g.ellipse(x,y+2,ht*.42,ht*.12,0,0,6.283);g.stroke()}""",
"""    if(!sprH(g,aI('pj_ti'),x-16,y-ht*.5,ht*.95,-.45)){
    g.save();g.translate(x-14,y-ht*.55);g.rotate(-.5);g.fillStyle='#e9eef5';g.fillRect(-3,-ht*.55,6,ht*.75);g.fillStyle='#ffd677';g.fillRect(-9,ht*.2,18,4);g.fillStyle='#8a5a2a';g.fillRect(-2.5,ht*.2+4,5,12);g.restore();
    g.strokeStyle='rgba(255,214,119,'+(.35+.25*p)+')';g.lineWidth=2;g.beginPath();g.ellipse(x,y+2,ht*.42,ht*.12,0,0,6.283);g.stroke()}}""")
rep("""  else{const rot=t*.6;g.save();g.translate(x,y+2);g.scale(1,.32);""",
"""  else if(aI('fx_10')){g.save();g.translate(x,y+2);g.scale(1,.32);g.rotate(t*.6);const ga=g.globalAlpha;g.globalAlpha=ga*.8;fxImg(g,10,0,0,ht*1.1);g.globalAlpha=ga;g.restore()}   /* 法修脚下：太极法阵图 */
  else{const rot=t*.6;g.save();g.translate(x,y+2);g.scale(1,.32);""")
rep("""function drawPathFront(g,x,y,r,t){if(!S||S.path!=='fa')return;const ht=heroTop(r)*1.35;
  for(let i=0;i<3;i++){const a=t*1.6+i*2.094,px=x+Math.cos(a)*ht*.42,py=y-ht*.55+Math.sin(a)*ht*.12;if(Math.sin(a)<0)continue;g.save();g.translate(px,py);g.rotate(Math.sin(t*2+i)*.2);""",
"""function drawPathFront(g,x,y,r,t){if(!S||S.path!=='fa')return;const ht=heroTop(r)*1.35,FU=aI('ic_fu');
  for(let i=0;i<3;i++){const a=t*1.6+i*2.094,px=x+Math.cos(a)*ht*.42,py=y-ht*.55+Math.sin(a)*ht*.12;if(Math.sin(a)<0)continue;if(FU){sprH(g,FU,px,py,20,Math.sin(t*2+i)*.2);continue}g.save();g.translate(px,py);g.rotate(Math.sin(t*2+i)*.2);""")

# ---- 选流派动画 ----
rep("""    for(let i=0;i<3;i++){const rr=((u*1.2+i*.33)%1)*H*.7;ctx.strokeStyle='rgba(255,214,119,'+(1-rr/(H*.7))+')';ctx.lineWidth=5;ctx.beginPath();ctx.arc(hx,hy,rr,Math.PI,0);ctx.stroke()}
    for(let i=0;i<14;i++){""",
"""    if(aI('fx_16')&&aI('fx_9')){const ga=ctx.globalAlpha;for(let i=0;i<3;i++){const k=(u*1.2+i*.33)%1;ctx.globalAlpha=ga*(1-k);fxImg(ctx,16,hx,hy,k*H*1.3+20,u)}ctx.globalAlpha=ga*.9;fxImg(ctx,9,hx,hy+10,H*.55,0,.95);ctx.globalAlpha=ga}else{
    for(let i=0;i<3;i++){const rr=((u*1.2+i*.33)%1)*H*.7;ctx.strokeStyle='rgba(255,214,119,'+(1-rr/(H*.7))+')';ctx.lineWidth=5;ctx.beginPath();ctx.arc(hx,hy,rr,Math.PI,0);ctx.stroke()}}
    if(!aI('fx_9'))for(let i=0;i<14;i++){""")
rep("""  else{const R0=40+H*.25*Math.min(1,u/.8);ctx.save();ctx.translate(hx,hy);ctx.scale(1,.38);ctx.rotate(u*1.5);ctx.strokeStyle='rgba(140,200,255,.9)';ctx.lineWidth=4;for(const k of [1,.75,.5]){ctx.beginPath();ctx.arc(0,0,R0*k,0,6.283);ctx.stroke()}
    for(let i=0;i<8;i++){const an=i*6.283/8;ctx.beginPath();ctx.moveTo(Math.cos(an)*R0,Math.sin(an)*R0);ctx.lineTo(Math.cos(an+2.356)*R0,Math.sin(an+2.356)*R0);ctx.stroke()}ctx.restore();""",
"""  else{const R0=40+H*.25*Math.min(1,u/.8);ctx.save();ctx.translate(hx,hy);ctx.scale(1,.38);ctx.rotate(u*1.5);if(aI('fx_10'))fxImg(ctx,10,0,0,R0*2.2);else{ctx.strokeStyle='rgba(140,200,255,.9)';ctx.lineWidth=4;for(const k of [1,.75,.5]){ctx.beginPath();ctx.arc(0,0,R0*k,0,6.283);ctx.stroke()}
    for(let i=0;i<8;i++){const an=i*6.283/8;ctx.beginPath();ctx.moveTo(Math.cos(an)*R0,Math.sin(an)*R0);ctx.lineTo(Math.cos(an+2.356)*R0,Math.sin(an+2.356)*R0);ctx.stroke()}}ctx.restore();""")
rep("""      ctx.save();ctx.translate(px,py);ctx.rotate(an);ctx.fillStyle='#ffe9a8';ctx.fillRect(-6,-11,12,22);""",
"""      if(sprH(ctx,aI('ic_fu'),px,py,28,an))continue;ctx.save();ctx.translate(px,py);ctx.rotate(an);ctx.fillStyle='#ffe9a8';ctx.fillRect(-6,-11,12,22);""")

# ---- 修仙主角飞起来后脚下的飞剑 ----
rep("if(r>=6){g.fillStyle=P.glow;g.globalAlpha=.45;g.fillRect(-18*sc,fly*sc+2,36*sc,3);",
    "const XP=r>=6&&aI('xplat');if(XP){const w2=50*sc,h2=w2*XP.naturalHeight/XP.naturalWidth;g.drawImage(XP,-w2/2,fly*sc+3-h2*.45,w2,h2)}else if(r>=6){g.fillStyle=P.glow;g.globalAlpha=.45;g.fillRect(-18*sc,fly*sc+2,36*sc,3);")

# ---- 被动：剑罡/星光护盾 光罩，战意/勇气 火焰 ----
rep("""    {const f=psForm('gang');if(f>=0){const ht=heroTop(S.rR)*1.35,c=""",
"""    {const f=psForm('gang'),GI=f>=0&&aI('gang_'+(f+1));if(GI){const ht=heroTop(S.rR)*1.35,p=.5+.5*Math.sin(t*3),ga=ctx.globalAlpha;ctx.globalAlpha=ga*(.5+.18*p);sprH(ctx,GI,S.x,squadY-ht*.42,ht*(1.45+.1*f)*(1+.02*p));ctx.globalAlpha=ga}   /* 剑罡 / 星光护盾：手绘光罩 */
     else if(f>=0){const ht=heroTop(S.rR)*1.35,c=""")
rep("""    {const f=psForm('zhan');if(f>=0){const k=.35+.65*(1-clamp(S.hpF,0,1)),n=5+f*2,w=sw()*.55+16;""",
"""    {const f=psForm('zhan'),ZI=f>=0&&aI('zhan_'+(f+1));if(ZI){const k=.35+.65*(1-clamp(S.hpF,0,1)),w=(sw()*.55+16)*2+24,h=w*ZI.naturalHeight/ZI.naturalWidth,ga=ctx.globalAlpha;
       for(let j=0;j<2;j++){const fl=.8+.25*Math.sin(t*(9+j*4)+j*2),hh=h*(.7+.5*k)*fl;ctx.globalAlpha=ga*(.55+.35*k)*(j?.6:1);ctx.drawImage(ZI,S.x-w/2*(j?.85:1),squadY+18-hh,w*(j?.85:1),hh)}ctx.globalAlpha=ga}   /* 战意 / 勇气：手绘火焰，越残血越旺 */
     else if(f>=0){const k=.35+.65*(1-clamp(S.hpF,0,1)),n=5+f*2,w=sw()*.55+16;""")

# ---- 技能特效 ----
# 火符：去掉代码光团；落点虚线圈 → 法阵图
rep("""    ctx.fillStyle=f.crow?'rgba(255,110,40,.4)':'rgba(255,160,60,.35)';ctx.beginPath();ctx.arc(x,y,18*sc,0,6.283);ctx.fill();
    {const u2""", """    if(!aI('fx_1')){ctx.fillStyle=f.crow?'rgba(255,110,40,.4)':'rgba(255,160,60,.35)';ctx.beginPath();ctx.arc(x,y,18*sc,0,6.283);ctx.fill()}
    {const u2""")
rep("""    ctx.strokeStyle='rgba(255,120,40,.5)';ctx.lineWidth=2;ctx.setLineDash([4,4]);ctx.beginPath();ctx.arc(f.x,f.y,f.R||85,0,6.283);ctx.stroke();ctx.setLineDash([])}""",
"""    if(aI('fx_8')){ctx.save();ctx.translate(f.x,f.y);ctx.scale(1,.5);const ga=ctx.globalAlpha;ctx.globalAlpha=ga*.4;fxImg(ctx,8,0,0,(f.R||85)*2,S.t);ctx.globalAlpha=ga;ctx.restore()}else{
    ctx.strokeStyle='rgba(255,120,40,.5)';ctx.lineWidth=2;ctx.setLineDash([4,4]);ctx.beginPath();ctx.arc(f.x,f.y,f.R||85,0,6.283);ctx.stroke();ctx.setLineDash([])}}""")
# 火海里的小火星点 → 光屑
rep("""    for(let i=0;i<3;i++){const ax=f.x+rand(-f.r*.7,f.r*.7),ay=f.y+rand(-f.r*.5,f.r*.5);ctx.fillStyle='rgba(255,200,90,'+a*.7+')';ctx.beginPath();ctx.arc(ax,ay,3,0,6.283);ctx.fill()}}""",
"""    {const SP=aI('spark');for(let i=0;i<3;i++){const ax=f.x+rand(-f.r*.7,f.r*.7),ay=f.y+rand(-f.r*.5,f.r*.5);if(SP){const ga=ctx.globalAlpha;ctx.globalAlpha=ga*a*.8;sprH(ctx,SP,ax,ay,12);ctx.globalAlpha=ga;continue}ctx.fillStyle='rgba(255,200,90,'+a*.7+')';ctx.beginPath();ctx.arc(ax,ay,3,0,6.283);ctx.fill()}}}""")
# 剑罡反击弧 → 斩击图
rep("""  if(S.fxGang)for(const f of S.fxGang){const a=f.t/.35;ctx.strokeStyle""",
"""  if(S.fxGang&&aI('fx_6'))for(const f of S.fxGang){const a=f.t/.35,ga=ctx.globalAlpha;ctx.globalAlpha=ga*a;fxImg(ctx,6,f.x,f.y-8,60*(1.3-a),-.3);ctx.globalAlpha=ga}
  else if(S.fxGang)for(const f of S.fxGang){const a=f.t/.35;ctx.strokeStyle""")
# 宠物灵珠
rep("""  if(S.petOrbs)for(const o of S.petOrbs){ctx.fillStyle""",
"""  if(S.petOrbs&&aI('porb'))for(const o of S.petOrbs)sprH(ctx,aI('porb'),o.x,o.y,20,S.t*3);
  else if(S.petOrbs)for(const o of S.petOrbs){ctx.fillStyle""")
# 宠物出手：爪 → 斩击图，吐息 → 火焰图，其余 → 冲击波图
rep("""  if(S.fxPet)for(const f of S.fxPet){const a=f.t/.45,col=""",
"""  if(S.fxPet&&aI('fx_6'))for(const f of S.fxPet){const a=f.t/.45,ga=ctx.globalAlpha;ctx.globalAlpha=ga*Math.min(1,a*1.4);
    if(f.k==='claw'){for(const o of [-9,0,9])fxImg(ctx,6,f.x+o,f.y+o*.3,46,.9)}
    else if(f.k==='breath')fxImg(ctx,2,f.x,f.y,(f.R||40)*2.2*(1.1-.3*a),0,.6);
    else{const WV=aI('wave');if(WV)sprH(ctx,WV,f.x,f.y,(f.R||40)*2.3*(1.1-.3*a),0,.5,.55);else fxImg(ctx,16,f.x,f.y,(f.R||40)*2.3*(1.1-.3*a))}
    ctx.globalAlpha=ga}
  else if(S.fxPet)for(const f of S.fxPet){const a=f.t/.45,col=""")
# 护法灵珠射线 → 飞出去的剑/星弹
rep("""  if(S.fxOrb)for(const f of S.fxOrb){const a=f.t/.2;ctx.strokeStyle""",
"""  if(S.fxOrb&&ART_ON&&pjImg())for(const f of S.fxOrb){const a=f.t/.2,u=1-a,x0=S.x,y0=squadY-40,px=x0+(f.x-x0)*u,py=y0+(f.y-y0)*u;sprH(ctx,pjImg(),px,py,24,Math.atan2(f.x-x0,-(f.y-y0)),.3)}
  else if(S.fxOrb)for(const f of S.fxOrb){const a=f.t/.2;ctx.strokeStyle""")
# 护法飞剑/守护星（绕身）→ 弹道图
rep("""ctx.save();ctx.translate(ox,oy);ctx.rotate(an+1.57);const sc=1+.18*OF;ctx.scale(sc,sc);if(OF>=2){""",
"""{const PJ=ART_ON&&pjImg();if(PJ){if(OF>=2){const ga=ctx.globalAlpha;ctx.globalAlpha=ga*.5;ctx.globalCompositeOperation='lighter';sprH(ctx,PJ,ox,oy,26*(1+.18*OF),an+3.14);ctx.globalCompositeOperation='source-over';ctx.globalAlpha=ga}sprH(ctx,PJ,ox,oy,20*(1+.18*OF),an+3.14);continue}}ctx.save();ctx.translate(ox,oy);ctx.rotate(an+1.57);const sc=1+.18*OF;ctx.scale(sc,sc);if(OF>=2){""")
# 雷云：去掉代码折线，换落雷图
rep("""    ctx.strokeStyle='rgba(220,230,255,'+a+')';ctx.lineWidth=3;ctx.beginPath();let x=cx;ctx.moveTo(x,H*.14);for(let y=H*.14;y<squadY;y+=30){x=cx+rand(-(f.x1-f.x0)*.25,(f.x1-f.x0)*.25);ctx.lineTo(x,y)}ctx.stroke()}""",
"""    if(aI('fx_3')){ctx.globalAlpha=a;fxImg(ctx,3,cx,H*.14,squadY-H*.14,0,0);ctx.globalAlpha=1}else{
    ctx.strokeStyle='rgba(220,230,255,'+a+')';ctx.lineWidth=3;ctx.beginPath();let x=cx;ctx.moveTo(x,H*.14);for(let y=H*.14;y<squadY;y+=30){x=cx+rand(-(f.x1-f.x0)*.25,(f.x1-f.x0)*.25);ctx.lineTo(x,y)}ctx.stroke()}}""")
# 法术（fxSpell）：线+圆 → 弹道图 + 落点冲击
rep("""  if(S.fxSpell){const f=S.fxSpell,a=f.t/.35;ctx.strokeStyle""",
"""  if(S.fxSpell&&ART_ON&&pjImg()){const f=S.fxSpell,a=f.t/.35,u=Math.min(1,(1-a)*1.6),x0=S.x,y0=squadY-20;if(u<1)sprH(ctx,pjImg(),x0+(f.x-x0)*u,y0+(f.y-y0)*u,30,Math.atan2(f.x-x0,-(f.y-y0)),.3);else{const ga=ctx.globalAlpha;ctx.globalAlpha=ga*a*1.5;fxImg(ctx,16,f.x,f.y,50*(1.3-a),S.t);ctx.globalAlpha=ga}}
  else if(S.fxSpell){const f=S.fxSpell,a=f.t/.35;ctx.strokeStyle""")
# 雷（fxBolt）：有落雷图时不再画代码折线
rep("""    ctx.strokeStyle='rgba(255,255,255,'+a+')';ctx.lineWidth=4;ctx.beginPath();let x=cx;ctx.moveTo(x,0);
    for(let y=0;y<squadY;y+=28){x=cx+rand(-(f.x1-f.x0)*.3,(f.x1-f.x0)*.3);ctx.lineTo(x,y)}ctx.stroke()}""",
"""    if(!aI('fx_3')){ctx.strokeStyle='rgba(255,255,255,'+a+')';ctx.lineWidth=4;ctx.beginPath();let x=cx;ctx.moveTo(x,0);
    for(let y=0;y<squadY;y+=28){x=cx+rand(-(f.x1-f.x0)*.3,(f.x1-f.x0)*.3);ctx.lineTo(x,y)}ctx.stroke()}}""")
# 护盾：有光罩图时不再画代码半圆
rep("""  if(S.shieldT>0){const p=.5+.5*Math.sin(S.t*8);ctx.strokeStyle""",
    """  if(S.shieldT>0&&!aI('fx_7')){const p=.5+.5*Math.sin(S.t*8);ctx.strokeStyle""")
# 定身：每只妖身上的代码圆圈 → 冰晶图
rep("""    ctx.strokeStyle='rgba(190,235,255,.85)';ctx.lineWidth=2;for(const z of S.objs)if(z.k==='z'&&!z.dead){ctx.beginPath();ctx.arc(z.x,z.y,z.r+4,0,6.28);ctx.stroke()}}""",
"""    const IC=aI('fx_4');if(IC){const ga=ctx.globalAlpha;ctx.globalAlpha=ga*.55;for(const z of S.objs)if(z.k==='z'&&!z.dead&&z.y>-30)sprH(ctx,IC,z.x,z.y,z.r*2.6);ctx.globalAlpha=ga}else{
    ctx.strokeStyle='rgba(190,235,255,.85)';ctx.lineWidth=2;for(const z of S.objs)if(z.k==='z'&&!z.dead){ctx.beginPath();ctx.arc(z.x,z.y,z.r+4,0,6.28);ctx.stroke()}}}""")
# 葫芦吸妖：线+点 → 光屑沿弧线飞进葫芦
rep("""    for(const [px,py] of f.pts){ctx.strokeStyle='rgba(220,170,255,'+(a*.7)+')';""",
"""    const SPg=aI('spark');if(SPg)for(const [px,py] of f.pts){for(let j=0;j<3;j++){const u=Math.max(0,1-a-j*.12),qx=px+(gx-px)*u,qy=py+(gy-py)*u+Math.sin(u*3.14)*-30;ctx.globalAlpha=a*(1-j*.3);sprH(ctx,SPg,qx,qy,14-j*3)}}ctx.globalAlpha=1;
    if(!SPg)for(const [px,py] of f.pts){ctx.strokeStyle='rgba(220,170,255,'+(a*.7)+')';""")
# 镇妖钟：代码圆弧 → 冲击波图（fxAdd(16) 已经另外叠了一层）
rep("""  if(S.fxBell>0){const a=Math.min(1,S.fxBell/.9);for(const d of [0,.15]){""",
"""  if(S.fxBell>0){const a=Math.min(1,S.fxBell/.9),WV=aI('wave');if(WV){for(const d of [0,.15]){const k=Math.max(0,a-d);ctx.globalAlpha=k;sprH(ctx,WV,S.x,squadY,Math.max(10,(1-a+d)*H*1.8),0,.5,.5)}ctx.globalAlpha=1}else for(const d of [0,.15]){""")
# 雷劫符/九霄神雷：代码大圆环 → 冲击波图
rep("""    ctx.strokeStyle='rgba(255,180,80,'+a+')';ctx.lineWidth=10;ctx.beginPath();ctx.arc(W*.7,H*.45,r,0,6.28);ctx.stroke()}""",
"""    const WV=aI('wave');if(WV){ctx.globalAlpha=a;sprH(ctx,WV,W*.7,H*.45,r*2.1);ctx.globalAlpha=1}else{
    ctx.strokeStyle='rgba(255,180,80,'+a+')';ctx.lineWidth=10;ctx.beginPath();ctx.arc(W*.7,H*.45,r,0,6.28);ctx.stroke()}}""")

# ---- 商店里拖尾/光环预览：代码圆点 → 小兵图 ----
rep("""  g.fillStyle=ART_PRE==='g_'?'#ffd0ea':'#ffe9a8';g.beginPath();g.arc(kind==='tr'?x:W2/2,kind==='tr'?y-8:H2*.6-14,9,0,6.283);g.fill()}}""",
"""  {const im=aI('sq_ti');if(im)sprH(g,im,kind==='tr'?x:W2/2,kind==='tr'?y+4:H2*.6+2,30,0,1);else{g.fillStyle=ART_PRE==='g_'?'#ffd0ea':'#ffe9a8';g.beginPath();g.arc(kind==='tr'?x:W2/2,kind==='tr'?y-8:H2*.6-14,9,0,6.283);g.fill()}}}}""")

open(P, 'w', encoding='utf-8').write(s)
print('part2 ok', n_ok)

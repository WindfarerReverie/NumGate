#!/usr/bin/env python3
# 11-02 23:08 John：全面自查代码画的美术 → 统一换手绘图（图没加载出来才退回代码画）
import sys
P = '/home/claude/numgate/index.html'
s = open(P, encoding='utf-8').read()
n_ok = 0
def rep(old, new, cnt=1):
    global s, n_ok
    c = s.count(old)
    if c != cnt:
        print('MISS(%d):' % c, old[:110]); sys.exit(1)
    s = s.replace(old, new); n_ok += 1

# ---- 0 公共小工具 ----
rep("function artDraw(g,im,cx,bottom,h,alpha,oc){",
"""/* 11-02 23:08 John「不要再让我看出来哪个是代码画的」→ 下面各处一律先用手绘图，图没加载出来才退回原来的代码画法 */
function aI(k){return ART_ON?artImg(k):null}
function sprH(g,im,x,y,h,rot,ay,sy){if(!im)return false;const w=h*im.naturalWidth/im.naturalHeight;g.save();g.translate(x,y);if(rot)g.rotate(rot);if(sy)g.scale(1,sy);g.drawImage(im,-w/2,-h*(ay==null?.5:ay),w,h);g.restore();return true}   /* 按高度画一张图（rot 旋转，ay 锚点，sy 纵向压扁） */
function sprW(g,im,x,y,w,h,a){if(!im)return false;const ga=g.globalAlpha;if(a!=null)g.globalAlpha=ga*a;g.drawImage(im,x,y,w,h);g.globalAlpha=ga;return true}
function artDraw(g,im,cx,bottom,h,alpha,oc){""")

# ---- 1 打击粒子：方块 → 光屑图 ----
old = "for(const p of S.parts){ctx.globalAlpha=clamp(p.life/p.l0,0,1);ctx.fillStyle=p.col;ctx.fillRect(p.x-p.size/2,p.y-p.size/2,p.size,p.size)}"
rep(old, "{const SPK=aI('spark');if(SPK){const go=ctx.globalCompositeOperation;ctx.globalCompositeOperation='lighter';for(const p of S.parts){ctx.globalAlpha=clamp(p.life/p.l0,0,1);const z=p.size*3.4;ctx.drawImage(SPK,p.x-z/2,p.y-z/2,z,z)}ctx.globalCompositeOperation=go}else " + old + "}")

# ---- 2 背景飘落物 ----
rep("function bgDeco(T){const t=S0t();ctx.save();",
"""function bgDeco(T){const t=S0t();ctx.save();
  {const G=ART_PRE==='g_',D=T.deco,im=!ART_ON?null:D==='leaf'?(aI('leaf')||aI('tr_peach')):D==='petal'?aI('tr_peach'):D==='snow'?aI('tr_frost'):D==='ember'?aI('tr_fire'):(D==='firefly'||D==='gold'||D==='star'||D==='void')?aI('spark'):null;
   if(im){const N=D==='snow'?26:D==='star'||D==='void'?30:D==='ember'?18:14;for(let i=0;i<N;i++){let x,y,z,a,rot=0;
     if(D==='leaf'||D==='petal'){y=((i*97+t*40)%(H+40))-20;x=((i*61+Math.sin(t*.8+i)*30)%W+W)%W;z=12+(i%3)*3;a=.75;rot=t*1.5+i}
     else if(D==='snow'){y=((i*53+t*30)%(H+20))-10;x=((i*29+Math.sin(t+i)*14)%W+W)%W;z=7+(i%3)*3;a=.8;rot=t*.6+i}
     else if(D==='ember'){y=H-((i*71+t*36)%(H+20));x=((i*43+Math.sin(t*1.3+i)*20)%W+W)%W;z=8+(i%3)*2;a=.45+.3*Math.sin(t*3+i)}
     else if(D==='star'||D==='void'){x=(i*67.3)%W;y=((i*113.7+scroll*.05)%H+H)%H;z=6+(i%3)*2;a=.25+.5*Math.abs(Math.sin(t*.9+i))}
     else{x=((i*83+Math.sin(t*.5+i)*40)%W+W)%W;y=((i*139+Math.cos(t*.4+i)*30)%H+H)%H;z=10;a=.3+.3*Math.sin(t*2+i*1.7)}
     ctx.globalAlpha=Math.max(0,a);sprH(ctx,im,x,y,z,rot)}ctx.globalAlpha=1;ctx.restore();return}}   /* 树叶、花瓣、雪、火星、萤火、星点 → 手绘小图 */""")

# ---- 3 门：边框图 + 锁图 ----
rep("function lockIcon(x,y){", "function lockIcon(x,y){if(sprH(ctx,aI('lock'),x,y+2,17))return;")
rep("""  ctx.fillStyle='rgba('+fill+','+(o.fl>0?.55:.32)+')';rr(x,y,w,h,8);ctx.fill();
  ctx.lineWidth=3;ctx.strokeStyle=col;ctx.stroke();""",
"""  const GF=aI(T.bad?'gatef_bad':'gatef_good');
  ctx.fillStyle='rgba('+fill+','+(o.fl>0?.55:GF?.26:.32)+')';rr(x,y,w,h,8);ctx.fill();
  if(GF){const ga=ctx.globalAlpha;if(locked)ctx.globalAlpha=ga*.55;ctx.drawImage(GF,x-w*.08,y-h*.1,w*1.16,h*1.2);ctx.globalAlpha=ga}   /* 门框：手绘边框（锁住的门边框变暗） */
  else{ctx.lineWidth=3;ctx.strokeStyle=col;ctx.stroke()}""")
rep("  ctx.fillStyle='#d7dbe4';ctx.fillRect(x-2,y-5,4,h+10);ctx.fillRect(x+w-2,y-5,4,h+10);\n}",
    "  if(!GF){ctx.fillStyle='#d7dbe4';ctx.fillRect(x-2,y-5,4,h+10);ctx.fillRect(x+w-2,y-5,4,h+10)}\n}")

# ---- 4 大妖进化特效：有大妖手绘图时，代码画的翅膀/光环/火冠/环绕珠换成特效图 ----
rep("""function bossEvoBack(o,wingCol,glowCol){
  const L=o.look,r=o.r,t=S.t,x=o.x,y=o.y,ri=L.ri||0;""",
"""function bossEvoBack(o,wingCol,glowCol){
  const L=o.look,r=o.r,t=S.t,x=o.x,y=o.y,ri=L.ri||0;
  if(aI('boss_'+L.bi)&&aI('fx_15')){const ga=ctx.globalAlpha;
    if(ri>=4||L.cosmic){ctx.globalAlpha=ga*(.32+.08*Math.sin(t*2));fxImg(ctx,15,x,y-r*.1,r*(2.8+(ri>=10?.5:0)),t*.4)}
    if(ri>=13){ctx.globalAlpha=ga*.45;fxImg(ctx,16,x,y-r*.1,r*3.4,-t*.6)}
    if(ri>=15||L.cosmic){const SP=aI('spark');if(SP)for(let i=0;i<10;i++){const a=i*.628+t*.25,d=r*(1.5+.25*Math.sin(t*2+i));ctx.globalAlpha=ga*(.35+.35*Math.sin(t*3+i));sprH(ctx,SP,x+Math.cos(a)*d,y+Math.sin(a)*d*.8,10+(i%3)*4)}}
    ctx.globalAlpha=ga;return}   /* 大妖本身是手绘图：身后改为旋涡/金环/光屑特效图，不再叠代码翅膀 */""")
rep("""function bossEvoFront(o,glowCol){
  const L=o.look,r=o.r,t=S.t,x=o.x,y=o.y,ri=L.ri||0;""",
"""function bossEvoFront(o,glowCol){
  const L=o.look,r=o.r,t=S.t,x=o.x,y=o.y,ri=L.ri||0;
  if(aI('boss_'+L.bi)){const ga=ctx.globalAlpha;
    if((ri>=10||L.flame)&&aI('fx_2')){ctx.globalAlpha=ga*(.7+.15*Math.sin(t*9));fxImg(ctx,2,x,y-r*.95,r*1.3*(1+.05*Math.sin(t*7)),0,.8)}
    if(ri>=12){const PB=aI('porb'),n=Math.min(6,ri-10);if(PB)for(let i=0;i<n;i++){const a=t*1.6+i*6.283/n;ctx.globalAlpha=ga*.95;sprH(ctx,PB,x+Math.cos(a)*r*1.45,y+Math.sin(a)*r*.55,14+ri*.6)}}
    ctx.globalAlpha=ga;return}""")
# 大妖光环（L.aura）在手绘大妖下：金环图
rep("const BI=artImg('boss_'+L.bi);if(BI){if(L.aura){const p=.5+.5*Math.sin(t*4);ctx.strokeStyle='hsla('+L.hue+',90%,60%,'+(.25+.3*p)+')';ctx.lineWidth=6;ctx.beginPath();ctx.arc(x,y,r*1.35+p*6,0,6.28);ctx.stroke()}",
    "const BI=artImg('boss_'+L.bi);if(BI){if(L.aura){const p=.5+.5*Math.sin(t*4);if(aI('fx_16')){const ga=ctx.globalAlpha;ctx.globalAlpha=ga*(.35+.3*p);fxImg(ctx,16,x,y,r*2.9+p*10,t*.3);ctx.globalAlpha=ga}else{ctx.strokeStyle='hsla('+L.hue+',90%,60%,'+(.25+.3*p)+')';ctx.lineWidth=6;ctx.beginPath();ctx.arc(x,y,r*1.35+p*6,0,6.28);ctx.stroke()}}")

# ---- 5 妖怪：阶数金菱 → 印记图；高阶光圈 → 金环图 ----
rep("if(tier>=5&&!o.boss){ctx.strokeStyle=pal[0];",
    "if(tier>=5&&!o.boss&&aI('fx_16')){const ga=ctx.globalAlpha;ctx.globalAlpha=ga*(.3+.2*Math.sin(S.t*5+o.ph));fxImg(ctx,16,o.x+wob,o.y,r*2.6,S.t);ctx.globalAlpha=ga}else if(tier>=5&&!o.boss){ctx.strokeStyle=pal[0];")
rep("if(ZB>0&&!o.mini){ctx.fillStyle='#ffd677';",
    "if(ZB>0&&!o.mini&&aI('pip')){const PI2=aI('pip');for(let i=0;i<ZB;i++)sprH(ctx,PI2,X+(i-(ZB-1)/2)*9,Y+r*1.05+4,10)}else if(ZB>0&&!o.mini){ctx.fillStyle='#ffd677';")
rep("if(o.enr||o.dashT>0||o.hasteT>0){ctx.fillStyle='rgba(255,70,40,'+(.22+.1*Math.sin(S.t*12))+')';ctx.beginPath();ctx.ellipse(X,Y,r*1.5,r*1.3,0,0,6.283);ctx.fill()}",
    "if(o.enr||o.dashT>0||o.hasteT>0){if(aI('fx_2')){const ga=ctx.globalAlpha;ctx.globalAlpha=ga*(.45+.15*Math.sin(S.t*12));fxImg(ctx,2,X,Y+r*.9,r*2.6,0,.85);ctx.globalAlpha=ga}else{ctx.fillStyle='rgba(255,70,40,'+(.22+.1*Math.sin(S.t*12))+')';ctx.beginPath();ctx.ellipse(X,Y,r*1.5,r*1.3,0,0,6.283);ctx.fill()}}   /* 狂暴：脚下燃起火焰图 */")

# ---- 6 妖怪技能：护法范围、护法标、咒怨旋涡、大妖冲锋 ----
rep("""  if(o.type==='guard'){ctx.strokeStyle='rgba(140,200,255,'+(.35+.15*Math.sin(t*4+o.ph))+')';""",
"""  if(o.type==='guard'&&aI('fx_7')){const ga=ctx.globalAlpha;ctx.globalAlpha=ga*(.16+.06*Math.sin(t*4+o.ph));fxImg(ctx,7,o.x,o.y+20,130,0,.62);ctx.globalAlpha=ga;sprH(ctx,aI('ic_t_guard'),o.x,o.y-o.r-9,16);outlined('护法',o.x,o.y+o.r+10,10,'#bfe3ff',CN)}
  else if(o.type==='guard'){ctx.strokeStyle='rgba(140,200,255,'+(.35+.15*Math.sin(t*4+o.ph))+')';""")
rep("""  if(o.type==='hex'){ctx.strokeStyle='rgba(200,120,255,.8)';ctx.lineWidth=2;ctx.beginPath();ctx.arc(o.x,o.y,o.r+5,t*3,t*3+4);ctx.stroke();""",
"""  if(o.type==='hex'){if(aI('fx_15')){const ga=ctx.globalAlpha;ctx.globalAlpha=ga*.5;fxImg(ctx,15,o.x,o.y,o.r*2.7,t*3);ctx.globalAlpha=ga}else{ctx.strokeStyle='rgba(200,120,255,.8)';ctx.lineWidth=2;ctx.beginPath();ctx.arc(o.x,o.y,o.r+5,t*3,t*3+4);ctx.stroke()}""")
rep("if(o.boss&&o.dash>0){ctx.strokeStyle='rgba(255,90,110,.6)';",
    "if(o.boss&&o.dash>0&&aI('fx_6')){const ga=ctx.globalAlpha;ctx.globalAlpha=ga*.7;for(const dx of [-o.r*.6,o.r*.6])fxImg(ctx,6,o.x+dx,o.y-o.r-24,o.r*1.1,-Math.PI/2);ctx.globalAlpha=ga}else if(o.boss&&o.dash>0){ctx.strokeStyle='rgba(255,90,110,.6)';")

open(P, 'w', encoding='utf-8').write(s)
print('part1 ok', n_ok)

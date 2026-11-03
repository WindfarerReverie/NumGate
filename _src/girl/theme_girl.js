/* ===================== 女生版主题：星愿魔法少女 =====================
   Injected inside the game closure by build_girl.py. Mutates shared tables and
   replaces drawing functions; gameplay code is untouched. */
const _xDZ=drawZ,_xDB=drawBoss,_xDC=drawCover,_xGI=gateIcon;   /* 修仙版的贴图画法，女生版有图时借用 */
Object.assign(C,{plus:'#7ab8ff',minus:'#ff6b8a',gold:'#ffd36e',div:'#9a7aff',buff:'#5ee0c0',
  roadL:'#3a3152',roadR:'#2a2440',zomb:'#ffb3d9',zombDark:'#7a5a8a',boss:'#c79bff'});
{const G={qi:['#ff7eb6','255,126,182'],vein:['#5ee0c0','94,224,192'],brk:['#ffcf5a','255,207,90'],art:['#8ab8ff','138,184,255'],
  fb:['#ffab7a','255,171,122'],fu:['#ffe066','255,224,102'],xin:['#9a88c0','154,136,192'],zou:['#ff9a5a','255,154,90'],jie:['#8a7aff','138,122,255']};
 for(const k in G)if(GT[k]){GT[k].col=G[k][0];GT[k].fill=G[k][1]}}
{const N=['暴躁乌云王','失眠夜枭','焦虑八爪鱼','拖延巨熊','熬夜蝙蝠','冷漠冰雪人','嫉妒魔镜','丧丧深海鲸','内耗旋涡','雷暴乌云王','噩梦夜枭','恐慌巨章鱼','摆烂熊王','通宵蝠王','冰封雪魔','比较魔镜','深渊丧丧鲸','永夜之心'];
 const ART=[0,1,2,3,4,5,6,7,8,0,1,2,3,4,5,6,7,9];   // realms 9+ reuse a mood's body, but with wings, crown of sparks and orbiting orbs (bossEvo*)
 BOSSES.forEach((b,i)=>{b.n=N[i];b.gi=ART[i]})}
BT[0]=['255,170,220',3];BT[1]=['255,220,130',4];BT[2]=['255,140,205',5];BT[3]=['205,165,255',6];

/* ---------- outfits: 18 looks, each a clear step up ---------- */
const OUT=[
 {hair:'#5a3a2a',hs:'pony',top:'#ffffff',sk:'#4a6ab0',st:'pleat',glow:'#ffd6ea'},          // 平凡少女: school uniform
 {hair:'#6a3a2a',hs:'pony',top:'#ff9ec7',sk:'#ffffff',st:'short',glow:'#ffc2dd',band:1},    // 元气少女: pink hoodie
 {hair:'#8a4a3a',hs:'twin',top:'#b48aff',sk:'#7a5ad0',st:'a',glow:'#d8c4ff',hat:'witch'},  // 见习魔法生
 {hair:'#c0705a',hs:'twin',top:'#a8d8ff',sk:'#7ab0ff',st:'frill',glow:'#cfe8ff',clip:1},    // 星光学徒
 {hair:'#3a3a6a',hs:'long',top:'#3a4a8a',sk:'#2a3470',st:'a',glow:'#c8d4ff',hat:'moon',cape:'#26305a'}, // 月光魔女
 {hair:'#e07a9a',hs:'long',top:'#ffc2dc',sk:'#ff8fbf',st:'frill',glow:'#ffd0e4',flower:1,cape:'#ff9ec7'}, // 花语魔女
 {hair:'#ff9ec7',hs:'twin',top:'#ffffff',sk:'rainbow',st:'layer',glow:'#fff0b0',ribbon:1}, // 彩虹魔导师
 {hair:'#6a5ad0',hs:'long',top:'#2a2a6a',sk:'#1e1e50',st:'star',glow:'#b8b0ff',ribbon:1},  // 星辰魔导师
 {hair:'#f0d080',hs:'long',top:'#e8fff2',sk:'#9fe8c0',st:'ball',glow:'#c8ffe0',tiara:1,wing:'fairy'}, // 精灵公主
 {hair:'#f0a0c0',hs:'bun',top:'#ffd6ea',sk:'#ff9ec7',st:'ball',glow:'#ffe0ef',tiara:1,flower:1,wing:'fairy'}, // 花之公主
 {hair:'#d8d8f0',hs:'long',top:'#eae6ff',sk:'#c8c0f0',st:'ball',glow:'#eef0ff',tiara:2,wing:'fairy'}, // 月之公主
 {hair:'#ffe08a',hs:'wave',top:'#fffaf0',sk:'#ffe7a8',st:'ball',glow:'#fff3c4',tiara:3,wing:'feather'}, // 星之公主
 {hair:'#c07ad8',hs:'bun',top:'#e8b0ff',sk:'#b05ad0',st:'ball',glow:'#f0d0ff',crown:1,cape:'#7a2aa8',wing:'feather'}, // 梦境女王
 {hair:'#5ad0d0',hs:'wave',top:'#bff4f0',sk:'#2a8a9a',st:'starball',glow:'#d6fff8',crown:1,cape:'#1a4a6a',wing:'feather'}, // 星海女王
 {hair:'#c8b8ff',hs:'wave',top:'#e6dcff',sk:'galaxy',st:'starball',glow:'#e8dcff',crown:2,cape:'#2a1a5a',wing:'feather'}, // 银河女王
 {hair:'#fff4fa',hs:'wave',top:'#ffffff',sk:'#f4f0ff',st:'goddess',glow:'#ffffff',halo:1,wing:'big'},  // 星辰女神
 {hair:'#ffe9a8',hs:'wave',top:'#fff6d0',sk:'#ffe08a',st:'goddess',glow:'#fff0b0',halo:2,wing:'big'},  // 光明女神
 {hair:'#ffffff',hs:'wave',top:'#ffffff',sk:'prism',st:'goddess',glow:'#ffffff',halo:3,wing:'prism'}]; // 创世女神
OUT.forEach((o,i)=>{if(HERO[i]){HERO[i].robe=typeof o.sk==='string'&&o.sk[0]==='#'?o.sk:o.top;HERO[i].trim=o.hair;HERO[i].glow=o.glow}});
const RAIN=['#ff8a8a','#ffc27a','#ffe680','#9fe8a0','#8ad0ff','#b49aff'];
function skFill(g,o,y0,y1,t){
  if(o.sk==='rainbow'){const gr=g.createLinearGradient(0,y0,0,y1);RAIN.forEach((c,i)=>gr.addColorStop(i/5,c));return gr}
  if(o.sk==='galaxy'){const gr=g.createLinearGradient(-14,y0,14,y1);gr.addColorStop(0,'#2a1a5a');gr.addColorStop(.5,'#6a4ac0');gr.addColorStop(1,'#1a2a6a');return gr}
  if(o.sk==='prism'){const gr=g.createLinearGradient(-16,y0,16,y1);const p=(t*.2)%1;RAIN.forEach((c,i)=>gr.addColorStop((i/5+p)%1,c));return gr}
  return o.sk;
}
drawHero=function(g,x,y,r,t,scl=1){
  r=clamp(r|0,0,OUT.length-1);const o=OUT[r],sc=scl*(1+.02*r),bob=Math.sin(t*2.2)*1.2,fly=r>=6?-6+bob:0,skin='#ffe2d0';
  g.save();g.translate(x,y);g.scale(sc,sc);
  const circ=(cx,cy,R,c)=>{g.fillStyle=c;g.beginPath();g.arc(cx,cy,R,0,6.283);g.fill()},A=a=>g.globalAlpha=a;
  const star=(cx,cy,R,c,rot=0)=>{g.fillStyle=c;g.beginPath();for(let i=0;i<10;i++){const a=rot-Math.PI/2+i*Math.PI/5,rr2=i%2?R*.45:R;g.lineTo(cx+Math.cos(a)*rr2,cy+Math.sin(a)*rr2)}g.fill()};
  const heart=(cx,cy,R,c)=>{g.fillStyle=c;g.beginPath();g.moveTo(cx,cy+R*.9);g.bezierCurveTo(cx-R*1.4,cy-R*.1,cx-R*.6,cy-R*1.2,cx,cy-R*.35);g.bezierCurveTo(cx+R*.6,cy-R*1.2,cx+R*1.4,cy-R*.1,cx,cy+R*.9);g.fill()};
  /* --- aura & background --- */
  if(r>=17){g.save();g.translate(0,-30+fly);g.rotate(t*.3);for(let i=0;i<12;i++){g.rotate(Math.PI/6);A(.35);g.fillStyle=RAIN[i%6];g.beginPath();g.moveTo(-2.5,-18);g.lineTo(0,-40);g.lineTo(2.5,-18);g.fill()}g.restore();A(1)}
  if(r>=16){g.save();g.translate(0,-30+fly);g.rotate(-t*.25);A(.4);g.fillStyle='#ffe680';for(let i=0;i<16;i++){g.rotate(Math.PI/8);g.beginPath();g.moveTo(-1.5,-16);g.lineTo(0,-32);g.lineTo(1.5,-16);g.fill()}g.restore();A(1)}
  if(r>=14){g.save();g.translate(0,-24+fly);g.rotate(-t*.5);for(let arm=0;arm<3;arm++)for(let i=0;i<13;i++){const a=arm*2.094+i*.34,rd=6+i*2.4;A(.85-i*.05);circ(Math.cos(a)*rd,Math.sin(a)*rd*.8,2-i*.08,i%3?'#d8c8ff':'#fff')}g.restore();A(1)}
  if(o.wing){const wc=o.wing==='prism'?null:o.glow,big=o.wing==='big'||o.wing==='prism'?1.5:o.wing==='feather'?1.15:.8;
    for(const s of [-1,1]){const fl=Math.sin(t*3)*.12;g.save();g.translate(s*3,-22+fly);g.rotate(s*fl);g.scale(s*big,big);
      if(o.wing==='fairy'){A(.55);g.fillStyle=wc;g.beginPath();g.ellipse(9,-5,10,6,-.6,0,6.283);g.fill();g.beginPath();g.ellipse(8,5,7,4,.5,0,6.283);g.fill();
        A(.8);g.strokeStyle='#ffffff';g.lineWidth=.8;g.beginPath();g.ellipse(9,-5,10,6,-.6,0,6.283);g.stroke()}
      else{for(let f=0;f<5;f++){A(.6+f*.05);g.fillStyle=o.wing==='prism'?RAIN[(f+Math.floor(t*2))%6]:(f%2?'#ffffff':wc);g.beginPath();g.ellipse(6+f*3.6,-6+f*2.2,4,13-f*1.6,.9-f*.12,0,6.283);g.fill()}}
      g.restore()}A(1)}
  if(o.halo){A(.5+.15*Math.sin(t*3));g.strokeStyle=o.halo>=3?RAIN[Math.floor(t*3)%6]:'#fff3a8';g.lineWidth=o.halo>=2?3:2;g.beginPath();g.ellipse(0,-44+fly,10+o.halo*2,3.5,0,0,6.283);g.stroke();A(1);
    if(o.halo>=2){A(.3);circ(0,-33+fly,16,o.glow);A(1)}}
  if(r>=10&&!o.halo){A(.3+.1*Math.sin(t*3));circ(0,-33+fly,r>=12?14:11,o.glow);A(1)}
  /* --- ground: shadow / magic circle / cloud --- */
  if(r>=3){g.save();g.translate(0,2);g.scale(1,.3);g.rotate(t*.8);A(.55);g.strokeStyle=o.glow;g.lineWidth=2;g.beginPath();g.arc(0,0,13+r*.5,0,6.283);g.stroke();
    for(let i=0;i<6;i++){g.rotate(1.047);star(0,-(13+r*.5),3,o.glow)}g.restore();A(1)}
  else{A(.3);g.fillStyle='#000';g.beginPath();g.ellipse(0,2,9,2.5,0,0,6.283);g.fill();A(1)}
  if(r>=6){A(.85);for(const [cx,R] of [[-8,5],[0,6.5],[8,5]])circ(cx,fly+3,R,'#ffffff');A(1)}
  g.translate(0,fly);
  /* --- capes & long hair (behind body) --- */
  if(o.cape){const long=r>=12;g.fillStyle=o.cape;g.beginPath();g.moveTo(-6,-26);g.quadraticCurveTo(-14+Math.sin(t*3)*2,-8,long?-16:-11,long?3:-6);g.lineTo(long?16:11,long?3:-6);g.quadraticCurveTo(14+Math.sin(t*3+1)*2,-8,6,-26);g.fill();
    if(long){A(.6);for(let i=0;i<6;i++)circ(-10+i*4,-4+Math.sin(i*2)*3,.9,'#fff');A(1)}}
  if(o.hs==='long'||o.hs==='wave'){g.fillStyle=o.hair;g.beginPath();g.moveTo(-7,-36);g.quadraticCurveTo(-11,-20,-9+(o.hs==='wave'?Math.sin(t*2)*1.5:0),-14);g.lineTo(9,-14);g.quadraticCurveTo(11,-20,7,-36);g.fill()}
  /* --- legs & shoes --- */
  const gown=o.st==='ball'||o.st==='starball'||o.st==='goddess';
  if(!gown){g.fillStyle=skin;g.fillRect(-4,-9,2.6,9);g.fillRect(1.4,-9,2.6,9);g.fillStyle=r<=1?'#ffffff':'#ff7eb6';g.fillRect(-5,-1.5,4,2.5);g.fillRect(1,-1.5,4,2.5)}
  /* --- skirt --- */
  const sf=skFill(g,o,-16,0,t);g.fillStyle=sf;g.beginPath();
  if(o.st==='pleat'||o.st==='short'){g.moveTo(-5,-16);g.lineTo(5,-16);g.lineTo(8,-9);g.lineTo(-8,-9)}
  else if(o.st==='a'){g.moveTo(-5,-17);g.lineTo(5,-17);g.lineTo(9,-6);g.lineTo(-9,-6)}
  else if(o.st==='frill'||o.st==='layer'||o.st==='star'){g.moveTo(-5,-17);g.lineTo(5,-17);g.lineTo(10,-5);g.lineTo(-10,-5)}
  else{const w=o.st==='goddess'?14:13;g.moveTo(-5,-18);g.lineTo(5,-18);g.quadraticCurveTo(w-2,-8,w,1);g.lineTo(-w,1);g.quadraticCurveTo(-w+2,-8,-5,-18)}
  g.fill();
  if(o.st==='pleat'){g.strokeStyle='rgba(0,0,0,.25)';g.lineWidth=.8;g.beginPath();for(const px of [-4,-1,2,5]){g.moveTo(px*.8,-16);g.lineTo(px*1.4,-9)}g.stroke()}
  if(o.st==='frill'||o.st==='layer'){g.fillStyle='#ffffff';for(let i=-4;i<=4;i++){g.beginPath();g.arc(i*2.3,-5,1.5,0,Math.PI);g.fill()}}
  if(o.st==='star'||o.st==='starball'||o.sk==='galaxy'){A(.9);for(const [sx,sy] of [[-5,-12],[3,-9],[-2,-6],[6,-4],[-7,-3],[1,-14]])star(sx,sy,1.3,'#fff8c0',t);A(1)}
  if(gown){g.fillStyle='rgba(255,255,255,.55)';for(let i=-3;i<=3;i++){g.beginPath();g.arc(i*3.6,1,2.1,Math.PI,0);g.fill()}
    if(o.st==='goddess'){A(.5);g.strokeStyle='#ffffff';g.lineWidth=1;for(const sx of [-6,0,6]){g.beginPath();g.moveTo(sx*.4,-16);g.quadraticCurveTo(sx,-8,sx*1.6,0);g.stroke()}A(1)}}
  /* --- bodice & arms --- */
  g.fillStyle=o.top;g.beginPath();g.moveTo(-5,-27);g.lineTo(5,-27);g.lineTo(4.5,-16.5);g.lineTo(-4.5,-16.5);g.fill();
  if(r===0){g.fillStyle='#d8344a';g.beginPath();g.moveTo(0,-25);g.lineTo(-3,-23);g.lineTo(0,-21);g.lineTo(3,-23);g.fill();g.fillStyle='#4a6ab0';g.fillRect(-5,-27,10,1.6)}
  else if(r===1){g.fillStyle='#ffffff';g.fillRect(-1,-26,.8,6);g.fillRect(.4,-26,.8,6)}
  else{heart(0,-23,2.2,r>=8?'#ffd36e':'#ff7eb6');g.fillStyle=r>=8?'#ffd36e':'rgba(255,255,255,.8)';g.fillRect(-4.5,-17.5,9,1.4)}
  g.strokeStyle=r===1?o.top:skin;g.lineWidth=2.4;g.lineCap='round';g.beginPath();g.moveTo(-5,-25);g.lineTo(-8,-16);g.moveTo(5,-25);g.lineTo(8,-19);g.stroke();
  if(r>=2&&r!==1){g.strokeStyle=o.top;g.lineWidth=3;g.beginPath();g.moveTo(-5,-25.5);g.lineTo(-6.2,-22.5);g.moveTo(5,-25.5);g.lineTo(6.2,-22.5);g.stroke()}
  /* --- head --- */
  circ(0,-33,6,skin);
  g.fillStyle=o.hair;g.beginPath();g.arc(0,-34,6.4,Math.PI*1.02,Math.PI*1.98);g.fill();   // top
  g.beginPath();g.moveTo(-6.3,-35);g.quadraticCurveTo(-3,-31,0,-33.5);g.quadraticCurveTo(3,-31,6.3,-35);g.lineTo(6.3,-37);g.lineTo(-6.3,-37);g.fill();   // bangs
  g.fillRect(-6.6,-35,2,7);g.fillRect(4.6,-35,2,7);   // side locks
  if(o.hs==='pony'){g.beginPath();g.moveTo(5,-38);g.quadraticCurveTo(13,-36+Math.sin(t*4),10,-26);g.quadraticCurveTo(9,-32,4,-36);g.fill()}
  if(o.hs==='twin'){for(const s of [-1,1]){g.beginPath();g.moveTo(s*5,-37);g.quadraticCurveTo(s*13,-34+Math.sin(t*4+s),s*10,-22);g.quadraticCurveTo(s*9,-30,s*4,-35);g.fill()}
    g.fillStyle='#ff7eb6';circ(-5.5,-37,1.6,'#ff7eb6');circ(5.5,-37,1.6,'#ff7eb6')}
  if(o.hs==='bun'){circ(0,-41,3.6,o.hair)}
  // face
  g.fillStyle='#3a2a4a';g.beginPath();g.ellipse(-2.3,-32.5,1.1,1.5,0,0,6.283);g.ellipse(2.3,-32.5,1.1,1.5,0,0,6.283);g.fill();
  g.fillStyle='#fff';g.fillRect(-2.6,-33.6,.7,.7);g.fillRect(2,-33.6,.7,.7);
  A(.5);circ(-3.8,-30.6,1.2,'#ff9ab8');circ(3.8,-30.6,1.2,'#ff9ab8');A(1);
  g.strokeStyle='#c0506a';g.lineWidth=.7;g.beginPath();g.arc(0,-30.5,1.1,.2,Math.PI-.2);g.stroke();
  /* --- head accessories --- */
  if(o.band){g.fillStyle='#ff4f8f';g.fillRect(-6,-38.6,12,1.6);heart(4.5,-39.5,1.8,'#ff4f8f')}
  if(o.clip)star(-4.5,-37.5,2.2,'#ffe066',t);
  if(o.hat==='witch'||o.hat==='moon'){g.fillStyle=o.hat==='moon'?'#26305a':'#5a3a9a';g.beginPath();g.ellipse(0,-38.5,9,2.2,0,0,6.283);g.fill();
    g.beginPath();g.moveTo(-5,-39);g.lineTo(3,-51);g.lineTo(5,-39);g.fill();
    if(o.hat==='moon'){g.fillStyle='#ffe680';g.beginPath();g.arc(1,-44,2.4,0,6.283);g.fill();g.fillStyle='#26305a';g.beginPath();g.arc(2,-44.6,2.2,0,6.283);g.fill()}
    else star(1.5,-44,1.8,'#ffe066')}
  if(o.flower){for(let i=0;i<5;i++){const a=Math.PI*(1.05+i*.22);circ(Math.cos(a)*6.5,-34+Math.sin(a)*6.5,1.6,['#ff7eb6','#fff','#ffd36e','#fff','#ff7eb6'][i])}}
  if(o.tiara){g.fillStyle='#ffd36e';g.beginPath();g.moveTo(-4.5,-38.5);g.lineTo(-3,-41.5);g.lineTo(-1.5,-39.5);g.lineTo(0,-43.5);g.lineTo(1.5,-39.5);g.lineTo(3,-41.5);g.lineTo(4.5,-38.5);g.fill();
    if(o.tiara===2){g.fillStyle='#fff';g.beginPath();g.arc(0,-43,1.6,0,6.283);g.fill();g.fillStyle=o.top;g.beginPath();g.arc(.7,-43.3,1.4,0,6.283);g.fill()}
    else if(o.tiara===3)star(0,-44.5,2.2,'#fff8c0',t);else circ(0,-42,1,'#ff7eb6')}
  if(o.crown){g.fillStyle='#ffd36e';g.beginPath();g.moveTo(-5.5,-38);g.lineTo(-5.5,-44);g.lineTo(-3,-41);g.lineTo(0,-47);g.lineTo(3,-41);g.lineTo(5.5,-44);g.lineTo(5.5,-38);g.fill();
    circ(0,-42,1.3,o.crown>=2?'#b49aff':'#ff4f8f');if(o.crown>=2){circ(-4,-40.5,.9,'#8ad0ff');circ(4,-40.5,.9,'#8ad0ff')}}
  /* --- held item --- */
  g.save();g.translate(8.5,-19);
  if(r>=2&&r<=7){g.strokeStyle='#ffffff';g.lineWidth=1.3;g.beginPath();g.moveTo(0,4);g.lineTo(0,-10);g.stroke();A(.4+.2*Math.sin(t*6));circ(0,-12,4.5,o.glow);A(1);star(0,-12,3.2,'#ffe066',t*2);g.fillStyle='#ff7eb6';g.fillRect(-1.2,1,2.4,1.2)}
  else if(r>=8&&r<=13){g.strokeStyle='#ffd36e';g.lineWidth=1.6;g.beginPath();g.moveTo(0,5);g.lineTo(0,-12);g.stroke();A(.4+.2*Math.sin(t*6));circ(0,-15,5,o.glow);A(1);heart(0,-15,3.4,'#ff4f8f');g.strokeStyle='#ffd36e';g.lineWidth=1;g.beginPath();g.arc(0,-15,4.2,0,6.283);g.stroke()}
  else if(r>=14){g.strokeStyle='#ffffff';g.lineWidth=1.8;g.beginPath();g.moveTo(0,8);g.lineTo(0,-16);g.stroke();A(.5+.2*Math.sin(t*6));circ(0,-20,7,o.glow);A(1);star(0,-20,5,'#fff8c0',t*1.5);g.strokeStyle='#ffd36e';g.lineWidth=1;g.beginPath();g.arc(0,-20,6.5,0,6.283);g.stroke()}
  g.restore();
  /* --- sparkles & orbiting stars --- */
  if(r>=1){const n=r>=7?7:3;for(let i=0;i<n;i++){const a=t*1.4+i*6.283/n;A(.45+.4*Math.sin(t*5+i));star(Math.cos(a)*16,-20+Math.sin(a)*10,1.4,i%2?'#fff':o.glow,t)}A(1)}
  if(r>=13){const ns=r>=15?8:4;for(let i=0;i<ns;i++){const a=t*1.6+i*6.283/ns;A(Math.sin(a)>0?1:.5);star(Math.cos(a)*22,-20+Math.sin(a)*7,2.6,RAIN[i%6],t*2)}A(1)}
  if(r===5||r===9){for(let i=0;i<4;i++){const ph=(t*.6+i*.25)%1;A(1-ph);heart(-12+i*8+Math.sin(t+i)*3,-40+ph*40,1.6,'#ff9ec7')}A(1)}
  g.restore();
};

/* ---------- fairies (the little squad) ---------- */
drawSquad=function(){
  const w=sw(),n=Math.min(S.count,30),cell=10,cols=Math.max(1,Math.min(n,Math.floor(w/cell))),rows=Math.ceil(n/cols);
  const inL=S.x<mid;
  ctx.fillStyle=inL?'rgba(255,158,199,.18)':'rgba(180,154,255,.18)';
  ctx.beginPath();ctx.ellipse(S.x,squadY+rows*cell*.35,w*.62,rows*cell*.5+12,0,0,6.28);ctx.fill();
  if(S.lv.rate>=3)drawSwordRing(S.x,squadY-6,S.t,S.lv.rate>=6?8:4,w*.55+10);
  const R=Math.min(OUT.length-1,S.rR),O=OUT[R];let i=0;const SQI=aI(S.path==='fa'?'sq_fa':'sq_ti');
  if(SQI){for(let rI=0;rI<rows;rI++){const inRow=Math.min(cols,n-i);for(let c=0;c<inRow;c++,i++){const x=S.x+(c-(inRow-1)/2)*cell+(rI%2?cell*.25:0),y=squadY+10+rI*cell*.8+Math.sin(S.t*6+i)*1.4;sprH(ctx,SQI,x,y+5,18,0,1)}}i=n}   /* 11-02 23:08：小精灵用手绘背影 */
  for(let rI=0;rI<rows&&i<n;rI++){const inRow=Math.min(cols,n-i);
    for(let c=0;c<inRow;c++,i++){
      const x=S.x+(c-(inRow-1)/2)*cell+(rI%2?cell*.25:0),y=squadY+10+rI*cell*.8+Math.sin(S.t*6+i)*1.4;
      const fl=Math.abs(Math.sin(S.t*18+i))*.9+.3;
      ctx.globalAlpha=.75;ctx.fillStyle='#ffffff';ctx.beginPath();ctx.ellipse(x-2.6,y-2.5,2.6,1.6*fl,-.5,0,6.28);ctx.ellipse(x+2.6,y-2.5,2.6,1.6*fl,.5,0,6.28);ctx.fill();
      ctx.globalAlpha=.35;ctx.fillStyle=O.glow;ctx.beginPath();ctx.arc(x,y,4.4,0,6.28);ctx.fill();ctx.globalAlpha=1;
      ctx.fillStyle=typeof O.sk==='string'&&O.sk[0]==='#'?O.sk:O.top;ctx.beginPath();ctx.arc(x,y,2.6,0,6.28);ctx.fill();
      ctx.fillStyle='#ffe2d0';ctx.beginPath();ctx.arc(x,y-3.4,1.7,0,6.28);ctx.fill();
      if(R>=8){ctx.fillStyle='#ffd36e';ctx.fillRect(x-1,y-5.8,2,.9)}
    }}
  {const pl=Math.min(petCount(),S.rR||0);if(pl>=1)drawFaxiang(ctx,mechX(),squadY-2,.9+.03*pl,S.t,pl)}
  drawBurstFx(S.x,squadY+2,false);drawHero(ctx,S.x,squadY+2,S.rR,S.t,1.35);drawBurstFx(S.x,squadY+2,true);
  const by=squadY-heroHH()-32,txt=(S.life>1?'第'+CNN(S.life)+'季 · ':'')+rName(realmOf(S.count));
  ctx.font='bold 15px '+CN;const tw=ctx.measureText(txt).width+20;
  const PX=clamp(S.x,tw/2+6,W-tw/2-6);   /* 名牌不出屏 */
  ctx.fillStyle='rgba(30,20,48,.88)';rr(PX-tw/2,by-14,tw,28,14);ctx.fill();
  ctx.strokeStyle=S.bottle?'#ffd36e':inL?'#ff9ec7':'#b49aff';ctx.lineWidth=2;ctx.stroke();
  ctx.fillStyle='#fff';ctx.textAlign='center';ctx.textBaseline='middle';ctx.fillText(txt,PX,by+1);
  drawLayerBar(by,tw,PX);
};
const girlTop=r=>(r>=14?82:r>=11?74:r>=8?62:r>=6?58:r>=2?52:46)*(1+.02*r);
drawSwordRing=function(x,y,t,n,rad){if(swRingArt(x,y,t,n,rad))return;for(let i=0;i<n;i++){const a=t*2.4+i*6.283/n,sx=x+Math.cos(a)*rad,sy=y+Math.sin(a)*rad*.45;
  ctx.fillStyle=i%2?'#fff8c0':'#ffb3d9';ctx.beginPath();for(let k=0;k<10;k++){const b=-Math.PI/2+k*Math.PI/5+t,r2=k%2?2:4.6;ctx.lineTo(sx+Math.cos(b)*r2,sy+Math.sin(b)*r2)}ctx.fill()}};

/* ---------- pets (replace 法相) ---------- */
const PETS=[
 {n:'小猫',b:'#ffb36b',e:'cat',tl:'thin'},{n:'兔兔',b:'#ffffff',e:'bunny',tl:'puff'},{n:'小狐',b:'#ff8a4a',e:'fox',tl:'fluffy'},
 {n:'小鹿',b:'#d9a066',e:'deer',ant:1,tl:'puff'},{n:'独角兽',b:'#fff4fb',e:'horse',horn:1,mane:'rainbow',tl:'mane'},{n:'天马',b:'#f2f6ff',e:'horse',wing:1,mane:'#9fd8ff',tl:'mane'},
 {n:'小龙',b:'#9fe0b0',e:'none',horns:1,wing:1,tl:'dragon'},{n:'九尾狐',b:'#fffaf0',e:'fox',tl:'nine',glow:'#ffe0ef'},{n:'月兔',b:'#f4f0ff',e:'bunny',tl:'puff',moon:1,glow:'#d8ccff'},
 {n:'凤凰',bird:1,b:'#ff7a4a',glow:'#ffd080'},{n:'星鲸',whale:1,b:'#6a8aff',glow:'#c8d8ff'},{n:'星辰麒麟',b:'#ffe9a8',e:'horse',horn:1,wing:1,mane:'#ffcf4a',tl:'mane',glow:'#fff3c4'},
 {n:'花仙鹿',b:'#ffc8e0',e:'deer',ant:1,tl:'puff',glow:'#ffe0f0',wing:1},{n:'冰晶龙',b:'#bfe8ff',e:'none',horns:1,wing:1,tl:'dragon',glow:'#e0f6ff',big:1},{n:'彩虹星鲸',whale:1,b:'#ff9ec7',glow:'#ffffff',big:1},
 {n:'银河天马',b:'#efe6ff',e:'horse',wing:1,mane:'rainbow',tl:'mane',glow:'#d8c8ff',big:1},{n:'创世神兽',b:'#fff6d6',e:'horse',horn:1,wing:1,mane:'rainbow',tl:'nine',glow:'#fff3c4',moon:1,big:1}];
drawFaxiang=function(g,x,y,sc,t,lvl){
  lvl=clamp(lvl|0,1,PETS.length);const P=PETS[lvl-1],bob=Math.sin(t*3)*2;
  g.save();g.translate(x,y-6+bob);g.scale(sc*(P.big?1.2:1),sc*(P.big?1.2:1));
  const circ=(cx,cy,R,c)=>{g.fillStyle=c;g.beginPath();g.arc(cx,cy,R,0,6.283);g.fill()};
  if(P.glow){g.globalAlpha=.35+.15*Math.sin(t*4);circ(0,-12,20,P.glow);g.globalAlpha=1}
  if(P.bird){for(const s of [-1,1]){g.fillStyle=s<0?'#ff9a4a':'#ffb84a';g.beginPath();g.moveTo(0,-14);g.quadraticCurveTo(s*22,-30+Math.sin(t*6)*5,s*26,-12);g.quadraticCurveTo(s*14,-14,0,-8);g.fill()}
    g.fillStyle='#ffd84a';for(let i=0;i<3;i++){g.beginPath();g.moveTo(-2+i*2,-4);g.quadraticCurveTo(-6+i*6,8,-4+i*4+Math.sin(t*4+i)*2,16);g.lineTo(i*2,-4);g.fill()}
    g.fillStyle=P.b;g.beginPath();g.ellipse(0,-12,6,9,0,0,6.283);g.fill();circ(0,-23,5,P.b);g.fillStyle='#ffd84a';g.beginPath();g.moveTo(4,-23);g.lineTo(9,-22);g.lineTo(4,-21);g.fill();
    g.fillStyle='#ffd84a';for(const a of [-.5,0,.5]){g.beginPath();g.moveTo(Math.sin(a)*3,-27);g.lineTo(Math.sin(a)*7,-35);g.lineTo(Math.sin(a)*3+1,-27);g.fill()}
    circ(1.8,-24,1,'#3a2a4a');g.restore();return}
  if(P.whale){g.fillStyle=P.b;g.beginPath();g.ellipse(0,-12,18,10,0,0,6.283);g.fill();g.beginPath();g.moveTo(-15,-12);g.lineTo(-26,-20+Math.sin(t*3)*3);g.lineTo(-24,-8);g.fill();
    g.fillStyle='#c8d8ff';g.beginPath();g.ellipse(2,-7,13,4,0,0,Math.PI);g.fill();circ(10,-14,1.6,'#2a2a5a');g.fillStyle='#fff';
    for(const [sx,sy] of [[-6,-17],[0,-19],[-10,-13],[5,-18]])circ(sx,sy,1,'#ffffff');g.strokeStyle='#c8e8ff';g.lineWidth=1.5;g.beginPath();g.moveTo(6,-22);g.quadraticCurveTo(4,-30,0,-32);g.moveTo(6,-22);g.quadraticCurveTo(9,-30,13,-31);g.stroke();g.restore();return}
  if(P.wing){for(const s of [-1,1]){g.globalAlpha=.85;g.fillStyle=P.e==='none'?'#7ac890':'#ffffff';g.beginPath();g.moveTo(-2,-16);g.quadraticCurveTo(-6+s*2,-34+Math.sin(t*5)*4,6+s*4,-30);g.quadraticCurveTo(4,-20,2,-16);g.fill()}g.globalAlpha=1}
  // tail
  g.fillStyle=P.b;g.strokeStyle=P.b;
  if(P.tl==='nine'){for(let i=0;i<9;i++){const a=-2.4+i*.18;g.beginPath();g.ellipse(-10+Math.cos(a)*7,-12+Math.sin(a)*7,6,2.4,a,0,6.283);g.fill()}}
  else if(P.tl==='fluffy'){g.beginPath();g.ellipse(-14,-14,7,4,-.6,0,6.283);g.fill();circ(-18,-17,2.6,'#ffffff')}
  else if(P.tl==='puff')circ(-11,-11,3.2,'#ffffff');
  else if(P.tl==='mane'){g.lineWidth=3;g.strokeStyle=P.mane==='rainbow'?'#ff9ec7':P.mane;g.beginPath();g.moveTo(-10,-12);g.quadraticCurveTo(-18,-14,-15,-4);g.stroke()}
  else if(P.tl==='dragon'){g.lineWidth=3;g.beginPath();g.moveTo(-10,-10);g.quadraticCurveTo(-18,-6,-20,-14);g.stroke();g.fillStyle='#ff9ec7';g.beginPath();g.moveTo(-20,-14);g.lineTo(-24,-18);g.lineTo(-21,-11);g.fill()}
  else{g.lineWidth=2;g.beginPath();g.moveTo(-10,-11);g.quadraticCurveTo(-16,-12,-14,-20);g.stroke()}
  // body & legs
  g.fillStyle=P.b;g.beginPath();g.ellipse(-1,-10,11,7,0,0,6.283);g.fill();
  for(const lx of [-7,-3,3,6]){g.fillRect(lx-1.2,-5,2.4,6+Math.sin(t*8+lx)*.8)}
  // head
  circ(8,-18,6.5,P.b);
  if(P.e==='cat'||P.e==='fox'){for(const s of [-1,1]){g.beginPath();g.moveTo(8+s*2,-23);g.lineTo(8+s*5.5,-29);g.lineTo(8+s*6,-21);g.fill()}}
  if(P.e==='bunny'){for(const s of [-1,1]){g.beginPath();g.ellipse(8+s*2.6,-29,1.8,6,s*.15,0,6.283);g.fill()}g.fillStyle='#ffc2dd';for(const s of [-1,1]){g.beginPath();g.ellipse(8+s*2.6,-29,.8,4.2,s*.15,0,6.283);g.fill()}}
  if(P.e==='deer'||P.e==='horse'){for(const s of [-1,1]){g.beginPath();g.ellipse(8+s*3.5,-24,1.6,3,s*.5,0,6.283);g.fill()}}
  if(P.ant){g.strokeStyle='#8a5a3a';g.lineWidth=1.2;for(const s of [-1,1]){g.beginPath();g.moveTo(8+s*2,-23);g.lineTo(8+s*4,-30);g.lineTo(8+s*7,-32);g.moveTo(8+s*4,-28);g.lineTo(8+s*1,-31);g.stroke()}}
  if(P.horn){g.fillStyle='#ffd36e';g.beginPath();g.moveTo(9,-23);g.lineTo(11,-33);g.lineTo(12,-23);g.fill()}
  if(P.horns){g.fillStyle='#fff3c4';for(const s of [-1,1]){g.beginPath();g.moveTo(8+s*2,-23);g.lineTo(8+s*4,-29);g.lineTo(8+s*4,-22);g.fill()}}
  if(P.mane){g.lineWidth=2.4;for(let i=0;i<4;i++){g.strokeStyle=P.mane==='rainbow'?RAIN[i]:P.mane;g.beginPath();g.moveTo(5-i*2,-22+i*2);g.quadraticCurveTo(1-i*2,-20+i*2,2-i*2,-14+i*2);g.stroke()}}
  if(P.moon){g.fillStyle='#ffe680';g.beginPath();g.arc(-2,-26,4,0,6.283);g.fill();g.fillStyle=P.glow;g.beginPath();g.arc(-.5,-27,3.6,0,6.283);g.fill()}
  // face
  circ(10.5,-19,1.3,'#3a2a4a');circ(10.9,-19.4,.4,'#ffffff');g.globalAlpha=.5;circ(11.5,-16.5,1.3,'#ff9ab8');g.globalAlpha=1;circ(14,-17.5,.8,'#ff7a9a');
  g.restore();
};

/* ---------- worries (normal enemies): purified, not killed ---------- */
const WPAL=[['#b8b0d8','#6a5a8a'],['#a8a0d0','#5a4a80'],['#9a90c8','#4e3e78'],['#8a7ec0','#42346e'],['#7a6ab4','#382a64'],['#6a58a8','#2e2058'],['#5a469a','#24184c']];
drawZ=function(o){
  if(o.boss&&o.look){drawBoss(o);return}
  const r=o.boss?o.r:o.r*(S.zSc||1),wob=Math.sin(S.t*6+o.ph)*1.5,tier=o.tier||0,pal=WPAL[tier]||WPAL[0],X=o.x+wob,Y=o.y,hit=o.hit>0;
  ctx.fillStyle='rgba(0,0,0,.25)';ctx.beginPath();ctx.ellipse(o.x,o.y+r*.85,r*.85,r*.3,0,0,6.28);ctx.fill();
  let body=pal[0],edge=pal[1];
  if(o.type==='run'){body='#ff9a6a';edge='#a84a2a'}else if(o.type==='hex'){body='#c8a8f0';edge='#6a4aa0'}else if(o.type==='guard'){body='#ffc8d8';edge='#b06a88'}else if(o.type==='brute'){body='#8aa0b8';edge='#4a5a70'}else if(o.type==='elite'){body='#7a4ab0';edge='#2a1050'}
  if(o.type==='run'){ctx.strokeStyle='rgba(255,220,200,.5)';ctx.lineWidth=2;ctx.beginPath();for(const dx of [-r*.5,0,r*.5]){ctx.moveTo(X+dx,Y-r-3);ctx.lineTo(X+dx,Y-r-20)}ctx.stroke()}
  if(o.type==='elite'){ctx.strokeStyle='rgba(200,150,255,'+(.4+.3*Math.sin(S.t*6+o.ph))+')';ctx.lineWidth=2;ctx.beginPath();for(let k=0;k<30;k++){const a=S.t*4+k*.35,rd=r+2+k*.25;ctx.lineTo(X+Math.cos(a)*rd,Y+Math.sin(a)*rd)}ctx.stroke()}
  ctx.fillStyle=hit?'#ffffff':body;ctx.strokeStyle=edge;ctx.lineWidth=2;ctx.beginPath();
  const bumps=o.type==='brute'?7:o.type==='run'?6:9;
  for(let k=0;k<=bumps*2;k++){const a=k/(bumps*2)*6.283,rd=r*(k%2?1:.9)*(o.type==='run'?(1+.15*Math.cos(a*1)):1);ctx.lineTo(X+Math.cos(a)*rd,Y+Math.sin(a)*rd*(o.type==='brute'?.85:1))}
  ctx.closePath();ctx.fill();ctx.stroke();
  // faces
  const ey=Y-r*.12;ctx.fillStyle='#2a1a3a';ctx.strokeStyle='#2a1a3a';ctx.lineWidth=Math.max(1.2,r*.12);
  if(o.type==='brute'){ctx.beginPath();ctx.moveTo(X-r*.5,ey);ctx.lineTo(X-r*.15,ey);ctx.moveTo(X+r*.15,ey);ctx.lineTo(X+r*.5,ey);ctx.stroke();
    ctx.fillStyle='#ffffff';ctx.font='bold '+Math.round(r*.6)+'px sans-serif';ctx.fillText('z',X+r*.7,Y-r*.9+Math.sin(S.t*2)*2)}
  else if(o.type==='elite'){for(const sd of [-1,1]){ctx.beginPath();for(let k=0;k<14;k++){const a=k*.6+S.t*5,rd=k*.22*r*.12;ctx.lineTo(X+sd*r*.32+Math.cos(a)*rd,ey+Math.sin(a)*rd)}ctx.stroke()}}
  else{ctx.beginPath();ctx.arc(X-r*.3,ey,r*.13,0,6.28);ctx.arc(X+r*.3,ey,r*.13,0,6.28);ctx.fill();
    ctx.beginPath();if(o.type==='run'){ctx.moveTo(X-r*.5,ey-r*.35);ctx.lineTo(X-r*.15,ey-r*.18);ctx.moveTo(X+r*.5,ey-r*.35);ctx.lineTo(X+r*.15,ey-r*.18)}else{ctx.moveTo(X-r*.45,ey-r*.25);ctx.lineTo(X-r*.15,ey-r*.33);ctx.moveTo(X+r*.45,ey-r*.25);ctx.lineTo(X+r*.15,ey-r*.33)}ctx.stroke()}
  ctx.beginPath();ctx.lineWidth=Math.max(1,r*.09);for(let k=0;k<=6;k++){const mx=X-r*.3+k*r*.1,my=Y+r*.3+(k%2?-1:1)*r*.05;k?ctx.lineTo(mx,my):ctx.moveTo(mx,my)}ctx.stroke();
  if(tier>=3&&o.type==='n'){ctx.fillStyle='#8ab8ff';ctx.beginPath();ctx.arc(X+r*.75,Y-r*.6,r*.15,0,6.28);ctx.fill()}   // sweat drop
  if(o.type==='brute'||o.type==='elite'){const sec=Math.max(0,o.hp)/Math.max(1e-9,dps()*dmgMul(o));outlined((sec<10?sec.toFixed(1):Math.round(sec))+'秒',o.x,o.y-r-7,11,'#fff',CN);
    if(o.type==='elite')outlined('内耗怪·'+REALMS[o.realm||0],o.x,o.y-r-20,10,o.realm>S.rR?C.minus:'#e6d2ff',CN)}
};
dZ=function(x,y,r,col,hp){dg.fillStyle='#b8b0d8';dg.strokeStyle='#6a5a8a';dg.lineWidth=2;dg.beginPath();for(let k=0;k<=18;k++){const a=k/18*6.283,rd=r*(k%2?1:.88);dg.lineTo(x+Math.cos(a)*rd,y+Math.sin(a)*rd)}dg.closePath();dg.fill();dg.stroke();
  dg.fillStyle='#2a1a3a';dg.beginPath();dg.arc(x-r*.3,y-r*.1,r*.14,0,6.28);dg.arc(x+r*.3,y-r*.1,r*.14,0,6.28);dg.fill()};

/* ---------- bosses: big bad moods ---------- */
drawBoss=function(o){
  const L=o.look,r=o.r,t=S.t,x=o.x,y=o.y,hit=o.hit>0,gi=L.gi??0,st=L.stage||0;
  const C2=(cx,cy,R,c)=>{ctx.fillStyle=c;ctx.beginPath();ctx.arc(cx,cy,R,0,6.283);ctx.fill()};
  const eyes=(ex,ey,R,col,pup)=>{for(const sd of [-1,1]){C2(x+sd*ex,ey,R,col);C2(x+sd*ex,ey,R*.45,pup)}};
  if(st>=1||L.aura){ctx.strokeStyle='rgba(200,150,255,'+(.25+.25*Math.sin(t*4))+')';ctx.lineWidth=5;ctx.beginPath();ctx.arc(x,y,r*1.35,0,6.28);ctx.stroke()}
  ctx.fillStyle='rgba(0,0,0,.3)';ctx.beginPath();ctx.ellipse(x,y+r*.95,r,r*.3,0,0,6.28);ctx.fill();
  bossEvoBack(o,'rgba(200,170,255,.75)','#ffd6f0');
  const W=hit?'#ffffff':null;
  if(gi===0){for(const [dx,dy,R] of [[-.6,.1,.55],[.6,.1,.55],[0,-.25,.7],[-.3,.3,.55],[.3,.3,.55]])C2(x+dx*r,y+dy*r,R*r,W||'#5a5a78');
    eyes(r*.3,y-r*.05,r*.16,'#ffd84a','#2a1a1a');ctx.strokeStyle='#2a1a1a';ctx.lineWidth=3;ctx.beginPath();ctx.moveTo(x-r*.5,y-r*.32);ctx.lineTo(x-r*.12,y-r*.18);ctx.moveTo(x+r*.5,y-r*.32);ctx.lineTo(x+r*.12,y-r*.18);ctx.stroke();
    if(Math.sin(t*7)>.3){ctx.fillStyle='#ffe34a';ctx.beginPath();ctx.moveTo(x-r*.2,y+r*.6);ctx.lineTo(x-r*.45,y+r*1.05);ctx.lineTo(x-r*.28,y+r*1.05);ctx.lineTo(x-r*.5,y+r*1.5);ctx.lineTo(x-r*.05,y+r*.95);ctx.lineTo(x-r*.22,y+r*.95);ctx.fill()}}
  else if(gi===1){ctx.fillStyle=W||'#6a5a4a';ctx.beginPath();ctx.ellipse(x,y,r*.85,r,0,0,6.283);ctx.fill();for(const sd of [-1,1]){ctx.beginPath();ctx.moveTo(x+sd*r*.5,y-r*.75);ctx.lineTo(x+sd*r*.75,y-r*1.25);ctx.lineTo(x+sd*r*.2,y-r*.85);ctx.fill()}
    ctx.fillStyle='#e8d8c0';ctx.beginPath();ctx.ellipse(x,y+r*.3,r*.5,r*.55,0,0,6.283);ctx.fill();eyes(r*.35,y-r*.3,r*.3,'#ffffff','#3a1a1a');ctx.strokeStyle='#ff6a8a';ctx.lineWidth=2;for(const sd of [-1,1]){ctx.beginPath();ctx.arc(x+sd*r*.35,y-r*.3,r*.34,.2,Math.PI-.2);ctx.stroke()}
    ctx.fillStyle='#ffb84a';ctx.beginPath();ctx.moveTo(x-r*.1,y-r*.08);ctx.lineTo(x,y+r*.12);ctx.lineTo(x+r*.1,y-r*.08);ctx.fill()}
  else if(gi===2){ctx.strokeStyle=W||'#9a6ad0';ctx.lineWidth=Math.max(4,r*.18);ctx.lineCap='round';for(let i=0;i<8;i++){const bx=x-r*.8+i*r*.23;ctx.beginPath();ctx.moveTo(bx,y+r*.3);ctx.quadraticCurveTo(bx+Math.sin(t*4+i)*r*.3,y+r*.9,bx+Math.sin(t*3+i)*r*.2,y+r*1.3);ctx.stroke()}
    C2(x,y-r*.1,r*.85,W||'#a87ae0');eyes(r*.3,y-r*.15,r*.2,'#ffffff','#2a1a3a');ctx.fillStyle='#8ab8ff';for(const sd of [-1,1]){ctx.beginPath();ctx.ellipse(x+sd*r*.75,y-r*.55,r*.08,r*.14,0,0,6.283);ctx.fill()}
    ctx.strokeStyle='#2a1a3a';ctx.lineWidth=2;ctx.beginPath();for(let k=0;k<=8;k++){const mx=x-r*.25+k*r*.0625;k?ctx.lineTo(mx,y+r*.28+(k%2?-3:3)):ctx.moveTo(mx,y+r*.28)}ctx.stroke()}
  else if(gi===3){C2(x,y+r*.1,r,W||'#8a6a5a');C2(x-r*.7,y-r*.7,r*.28,W||'#8a6a5a');C2(x+r*.7,y-r*.7,r*.28,W||'#8a6a5a');C2(x,y+r*.25,r*.45,'#c8a890');
    ctx.strokeStyle='#2a1a1a';ctx.lineWidth=3;ctx.beginPath();ctx.moveTo(x-r*.45,y-r*.15);ctx.lineTo(x-r*.15,y-r*.15);ctx.moveTo(x+r*.15,y-r*.15);ctx.lineTo(x+r*.45,y-r*.15);ctx.stroke();
    ctx.fillStyle='#5a7ad0';ctx.beginPath();ctx.moveTo(x-r*.55,y-r*.75);ctx.quadraticCurveTo(x,y-r*1.6,x+r*.6,y-r*.75);ctx.fill();C2(x+r*.85,y-r*1.15,r*.14,'#ffffff');
    ctx.fillStyle='#fff';ctx.font='bold '+Math.round(r*.45)+'px sans-serif';ctx.fillText('Z z',x+r*1.1,y-r*.4+Math.sin(t*2)*4)}
  else if(gi===4){ctx.fillStyle=W||'#4a3a6a';for(const sd of [-1,1]){ctx.beginPath();ctx.moveTo(x,y-r*.2);ctx.quadraticCurveTo(x+sd*r*1.2,y-r*1.1+Math.sin(t*8)*r*.2,x+sd*r*1.6,y-r*.1);ctx.lineTo(x+sd*r*1.2,y+r*.1);ctx.lineTo(x+sd*r*1.0,y-r*.05);ctx.lineTo(x+sd*r*.7,y+r*.25);ctx.closePath();ctx.fill()}
    C2(x,y,r*.6,W||'#5a4a7a');for(const sd of [-1,1]){ctx.beginPath();ctx.moveTo(x+sd*r*.3,y-r*.45);ctx.lineTo(x+sd*r*.5,y-r*.9);ctx.lineTo(x+sd*r*.05,y-r*.55);ctx.fill()}
    eyes(r*.22,y-r*.1,r*.14,'#ff6a8a','#2a0a1a');ctx.strokeStyle='#2a1a3a';ctx.lineWidth=2;for(const sd of [-1,1]){ctx.beginPath();ctx.arc(x+sd*r*.22,y+r*.02,r*.16,.3,Math.PI-.3);ctx.stroke()}
    ctx.fillStyle='#8ad0ff';ctx.globalAlpha=.6;ctx.fillRect(x-r*.12,y+r*.25,r*.24,r*.36);ctx.globalAlpha=1}
  else if(gi===5){C2(x,y+r*.35,r*.75,W||'#e8f4ff');C2(x,y-r*.45,r*.55,W||'#f4faff');ctx.fillStyle='#5a7ab0';ctx.fillRect(x-r*.5,y-r*1.05,r,r*.18);ctx.fillRect(x-r*.3,y-r*1.4,r*.6,r*.4);
    ctx.fillStyle='#2a3a5a';C2(x-r*.2,y-r*.5,r*.07,'#2a3a5a');C2(x+r*.2,y-r*.5,r*.07,'#2a3a5a');ctx.fillRect(x-r*.18,y-r*.28,r*.36,r*.04);
    ctx.strokeStyle='#a8d8ff';ctx.lineWidth=2;for(let i=0;i<6;i++){const a=t+i*1.05,sx=x+Math.cos(a)*r*1.2,sy=y+Math.sin(a)*r*.9;ctx.beginPath();ctx.moveTo(sx-3,sy);ctx.lineTo(sx+3,sy);ctx.moveTo(sx,sy-3);ctx.lineTo(sx,sy+3);ctx.stroke()}}
  else if(gi===6){ctx.fillStyle=W||'#6a4a8a';ctx.beginPath();ctx.ellipse(x,y-r*.15,r*.8,r*.95,0,0,6.283);ctx.fill();ctx.fillRect(x-r*.12,y+r*.7,r*.24,r*.5);
    const gr=ctx.createLinearGradient(x-r*.6,y-r,x+r*.6,y+r*.6);gr.addColorStop(0,'#a8ffd0');gr.addColorStop(1,'#2a8a5a');ctx.fillStyle=gr;ctx.beginPath();ctx.ellipse(x,y-r*.15,r*.62,r*.77,0,0,6.283);ctx.fill();
    eyes(r*.25,y-r*.25,r*.15,'#ffffff','#1a5a2a');ctx.strokeStyle='#1a3a2a';ctx.lineWidth=2.5;ctx.beginPath();ctx.moveTo(x-r*.42,y-r*.5);ctx.lineTo(x-r*.1,y-r*.42);ctx.moveTo(x+r*.42,y-r*.5);ctx.lineTo(x+r*.1,y-r*.42);ctx.stroke();
    ctx.beginPath();ctx.arc(x,y+r*.2,r*.2,Math.PI+.4,-.4);ctx.stroke()}
  else if(gi===7){ctx.fillStyle=W||'#2a4a8a';ctx.beginPath();ctx.ellipse(x,y,r*1.1,r*.7,0,0,6.283);ctx.fill();ctx.beginPath();ctx.moveTo(x-r,y);ctx.lineTo(x-r*1.6,y-r*.6+Math.sin(t*3)*r*.15);ctx.lineTo(x-r*1.5,y+r*.4);ctx.fill();
    ctx.fillStyle='#8ab0e0';ctx.beginPath();ctx.ellipse(x+r*.1,y+r*.3,r*.8,r*.25,0,0,Math.PI);ctx.fill();C2(x+r*.5,y-r*.15,r*.12,'#ffffff');C2(x+r*.5,y-r*.13,r*.06,'#1a1a3a');
    ctx.fillStyle='#8ad0ff';ctx.beginPath();ctx.ellipse(x+r*.55,y+r*.08+((t*30)%20),r*.06,r*.1,0,0,6.283);ctx.fill();
    ctx.strokeStyle='#2a1a3a';ctx.lineWidth=2;ctx.beginPath();ctx.arc(x+r*.75,y+r*.15,r*.12,Math.PI+.5,-.3);ctx.stroke()}
  else if(gi===8){for(let k=0;k<3;k++){ctx.strokeStyle=['#7a4ab0','#9a6ad0','#c8a0ff'][k];ctx.lineWidth=r*.18;ctx.beginPath();for(let j=0;j<40;j++){const a=t*(2+k)+j*.3,rd=r*(1.1-k*.3)*(j/40);ctx.lineTo(x+Math.cos(a)*rd,y+Math.sin(a)*rd)}ctx.stroke()}
    eyes(r*.28,y-r*.1,r*.15,'#ffffff','#3a1a5a')}
  else{C2(x,y,r,W||'#1a1030');ctx.fillStyle='#0a0618';for(let i=0;i<10;i++){const a=i/10*6.283+t*.3;ctx.beginPath();ctx.moveTo(x+Math.cos(a)*r*.8,y+Math.sin(a)*r*.8);ctx.lineTo(x+Math.cos(a+.15)*r*1.4,y+Math.sin(a+.15)*r*1.4);ctx.lineTo(x+Math.cos(a+.3)*r*.8,y+Math.sin(a+.3)*r*.8);ctx.fill()}
    for(let i=0;i<7;i++){const a=i/7*6.283+t*.6,ex=x+Math.cos(a)*r*.5,ey=y+Math.sin(a)*r*.45;C2(ex,ey,r*.1,'#c8a0ff');C2(ex,ey,r*.05,'#ffffff')}
    ctx.fillStyle='#b49aff';ctx.beginPath();const cy=y-r*1.02;ctx.moveTo(x-r*.45,cy+8);for(let i=0;i<=4;i++)ctx.lineTo(x-r*.45+i*r*.225,cy-(i%2?0:r*.3));ctx.lineTo(x+r*.45,cy+8);ctx.fill()}
  for(let i=0;i<st;i++){const a=t*2+i*2.09;ctx.fillStyle='#ffd36e';ctx.beginPath();ctx.arc(x+Math.cos(a)*r*1.25,y+Math.sin(a)*r*.6,3,0,6.283);ctx.fill()}
  const w=r*3.2,p=clamp(o.hp/o.hp0,0,1);
  ctx.fillStyle='rgba(0,0,0,.6)';ctx.fillRect(x-w/2,y-r-16,w,7);ctx.fillStyle=C.minus;ctx.fillRect(x-w/2,y-r-16,w*p,7);
  outlined(L.name+' · '+REALMS[o.realm||0]+(S.fb.mirror?' · 许愿镜 +'+30*S.fb.mirror+'%':''),x,y-r-40,13,o.realm>S.rR?C.minus:'#ffd677',CN);{const sec=Math.max(0,o.hp)/Math.max(1e-9,dps()*dmgMul(o));outlined('需 '+(sec<10?sec.toFixed(1):Math.round(sec))+' 秒',x,y-r-26,13,'#fff',CN)}
  bossEvoFront(o,'#ffe9a8');
  {const E=bossEta(o);outlined((E!=null?E+' 秒后冲破结界 · ':'冲破结界')+'扣 '+Math.round(bossHpF()*newbBoss()*100)+'% 元气',x,y+r+18,E!=null&&E<=6?15:12,C.minus,CN)}
};

/* ---------- gate icons ---------- */
gateIcon=function(g,o,cx,cy,s,t,dim,cc){
  const c=cc||ctx;c.save();c.translate(cx,cy);c.scale(s,s);const BA=dim?.55:1;c.globalAlpha=BA;
  const C2=(x,y,r,col)=>{c.fillStyle=col;c.beginPath();c.arc(x,y,r,0,6.283);c.fill()};
  const star=(x,y,R,col,rot=0)=>{c.fillStyle=col;c.beginPath();for(let i=0;i<10;i++){const a=rot-Math.PI/2+i*Math.PI/5,r2=i%2?R*.45:R;c.lineTo(x+Math.cos(a)*r2,y+Math.sin(a)*r2)}c.fill()};
  const heart=(x,y,R,col)=>{c.fillStyle=col;c.beginPath();c.moveTo(x,y+R*.9);c.bezierCurveTo(x-R*1.4,y-R*.1,x-R*.6,y-R*1.2,x,y-R*.35);c.bezierCurveTo(x+R*.6,y-R*1.2,x+R*1.4,y-R*.1,x,y+R*.9);c.fill()};
  if(g==='qi'){   // 星光糖: wrapped candy with a star
    c.fillStyle='#ff9ec7';for(const sd of [-1,1]){c.beginPath();c.moveTo(sd*7,0);c.lineTo(sd*15,-6);c.lineTo(sd*15,6);c.fill()}
    const gr=c.createRadialGradient(-3,-3,1,0,0,9);gr.addColorStop(0,'#ffffff');gr.addColorStop(.5,'#ff9ec7');gr.addColorStop(1,'#d0407a');C2(0,0,8.5,gr);star(0,0,4.5,'#fff8c0',t);
    c.globalAlpha=BA*(.5+.5*Math.sin(t*5));star(12,-11,2.2,'#fff');c.globalAlpha=BA}
  else if(g==='vein'){   // 愿望水晶: faceted heart crystal
    c.globalAlpha=BA*.35;C2(0,0,14,'#7ff0d0');c.globalAlpha=BA;heart(0,1,10,'#5ee0c0');heart(-1.5,-.5,6,'#c8fff0');
    c.strokeStyle='rgba(255,255,255,.8)';c.lineWidth=1;c.beginPath();c.moveTo(-6,-4);c.lineTo(0,4);c.lineTo(6,-4);c.stroke();star(9,-10,2.4,'#fff',t)}
  else if(g==='brk'){   // 变身星冠: glowing tiara
    c.save();c.rotate(t*.6);c.fillStyle='rgba(255,214,119,.5)';for(let i=0;i<8;i++){c.rotate(.785);c.beginPath();c.moveTo(-1.6,-10);c.lineTo(0,-17);c.lineTo(1.6,-10);c.fill()}c.restore();
    c.fillStyle='#ffcf5a';c.beginPath();c.moveTo(-11,6);c.lineTo(-11,-4);c.lineTo(-6,1);c.lineTo(0,-11);c.lineTo(6,1);c.lineTo(11,-4);c.lineTo(11,6);c.closePath();c.fill();
    C2(0,-2,2.6,'#ff7eb6');C2(-6,3,1.6,'#8ad0ff');C2(6,3,1.6,'#8ad0ff')}
  else if(g==='art'){   // 魔法书 by skill
    const k=o&&o.up;c.fillStyle='#7a6ad8';c.fillRect(-11,-9,22,17);c.fillStyle='#fff8f0';c.fillRect(-10,-8,9.4,15);c.fillRect(.6,-8,9.4,15);c.fillStyle='#5a4ab0';c.fillRect(-.6,-9,1.2,17);
    if(k==='rate'){for(const sd of [-1,1]){c.fillStyle='#8ad0ff';c.beginPath();c.ellipse(sd*5,-14,5,2.6,sd*-.5,0,6.283);c.fill()}star(0,-14,3.4,'#ffe066',t)}
    else if(k==='dmg'){c.globalAlpha=BA*(.6+.3*Math.sin(t*6));heart(0,-14,6,'#ff6a9a');c.globalAlpha=BA;heart(0,-14,4,'#ff3a7a')}
    else if(k==='spread'){for(const [sx,d] of [[-7,0],[0,-3],[7,0]]){star(sx,-14+d,2.8,'#ffe066',t);c.strokeStyle='rgba(255,230,120,.6)';c.lineWidth=1;c.beginPath();c.moveTo(sx+2,-12+d);c.lineTo(sx+6,-18+d);c.stroke()}}
    else if(k==='pierce'){c.strokeStyle='#ffcf5a';c.lineWidth=1.6;c.beginPath();c.moveTo(-12,-8);c.lineTo(12,-20);c.stroke();heart(0,-14,4,'#ff6a9a');c.fillStyle='#ffcf5a';c.beginPath();c.moveTo(12,-20);c.lineTo(8,-20);c.lineTo(10,-17);c.fill()}
    else star(0,-14,3.4,'#ffe066',t)}
  else if(g==='fb'){const k=o&&o.fbk;
    if(k==='gourd'){C2(0,4,9,'#ffffff');C2(0,-6,7.5,'#ffffff');for(const sd of [-1,1]){c.beginPath();c.moveTo(sd*3,-11);c.lineTo(sd*6.5,-16);c.lineTo(sd*7,-8);c.fill()}
      c.fillStyle='#ffffff';c.save();c.translate(8,-4);c.rotate(Math.sin(t*5)*.5);c.fillRect(-1.5,-7,3,7);c.restore();
      C2(-2.5,-6,1,'#2a1a2a');C2(2.5,-6,1,'#2a1a2a');C2(0,1,2.2,'#ff4f6a');C2(0,6,2.6,'#ffd36e')}
    else if(k==='mirror'){c.fillStyle='#ff9ec7';c.fillRect(-1.8,6,3.6,9);C2(0,-2,11,'#ff9ec7');const gr=c.createLinearGradient(-8,-10,8,6);gr.addColorStop(0,'#ffffff');gr.addColorStop(.5,'#ffe0f0');gr.addColorStop(1,'#c8a8ff');C2(0,-2,8.5,gr);heart(0,-2,3,'#ff7eb6')}
    else{c.fillStyle='#ffb3d0';c.fillRect(-10,-4,20,12);c.fillStyle='#ff7eb6';c.fillRect(-10,-6,20,3);c.fillStyle='#ffe066';c.save();c.translate(0,-6);c.rotate(-.5+Math.sin(t*2)*.1);c.fillRect(-10,-2,20,2);c.restore();
      c.fillStyle='#ffffff';for(let i=0;i<3;i++){const ph=(t*.8+i*.33)%1;c.globalAlpha=BA*(1-ph);c.font='bold 8px sans-serif';c.fillText('♪',-6+i*6,-10-ph*10)}c.globalAlpha=BA}}
  else if(g==='fu'){   // 魔法卡
    c.save();c.rotate(Math.sin(t*2)*.08);c.fillStyle='#fff6d0';c.fillRect(-8,-12,16,24);c.strokeStyle='#ffcf5a';c.lineWidth=1.4;c.strokeRect(-6.5,-10.5,13,21);const k=o&&o.fu;
    if(k==='bomb')star(0,0,6,'#ff7eb6',t);
    else if(k==='bolt'){for(let i=0;i<4;i++){c.strokeStyle=RAIN[i+1];c.lineWidth=1.6;c.beginPath();c.arc(0,4,7-i*1.6,Math.PI,0);c.stroke()}}
    else if(k==='shield'){c.globalAlpha=BA*.7;C2(0,0,6,'#a8e0ff');c.globalAlpha=BA;C2(-2,-2,1.6,'#ffffff')}
    else{c.fillStyle='#ffd36e';c.beginPath();c.arc(0,0,6,0,6.283);c.fill();c.fillStyle='#fff6d0';c.beginPath();c.arc(2.5,-1.5,5.4,0,6.283);c.fill()}
    c.restore()}
  else if(g==='xin'){   // 负能量: sulky raincloud
    c.fillStyle='#6a6488';for(const [x,y,r] of [[-7,-2,6],[0,-6,7.5],[7,-2,6],[0,0,7]])C2(x,y,r,'#6a6488');
    c.fillStyle='#2a1a3a';C2(-3,-1,1.2,'#2a1a3a');C2(3,-1,1.2,'#2a1a3a');c.strokeStyle='#2a1a3a';c.lineWidth=1.2;c.beginPath();c.arc(0,4,2.5,Math.PI+.4,-.4);c.stroke();
    c.fillStyle='#8ab8ff';for(let i=0;i<3;i++){const ph=(t*1.5+i*.33)%1;c.beginPath();c.ellipse(-6+i*6,8+ph*8,1.2,2,0,0,6.283);c.fill()}}
  else if(g==='zou'){   // 熬夜: coffee & moon, sleepy
    c.fillStyle='#ffffff';c.fillRect(-8,-2,13,11);c.strokeStyle='#ffffff';c.lineWidth=2;c.beginPath();c.arc(6,3,3.5,-1.4,1.4);c.stroke();c.fillStyle='#8a5a3a';c.fillRect(-7,-1,11,2.5);
    c.strokeStyle='rgba(255,255,255,.7)';c.lineWidth=1.2;for(let i=0;i<2;i++){c.beginPath();c.moveTo(-4+i*5,-4);c.quadraticCurveTo(-6+i*5+Math.sin(t*3)*2,-8,-4+i*5,-12);c.stroke()}
    c.fillStyle='#ffe680';c.beginPath();c.arc(9,-11,5,0,6.283);c.fill();c.fillStyle='rgba(255,154,90,1)';c.beginPath();c.arc(11,-12.5,4.5,0,6.283);c.fill()}
  else if(g==='jie'){   // 流星考验: meteor
    c.save();c.rotate(-.6);const gr=c.createLinearGradient(0,0,0,-22);gr.addColorStop(0,'rgba(255,200,120,.9)');gr.addColorStop(1,'rgba(255,120,200,0)');c.fillStyle=gr;c.beginPath();c.moveTo(-5,0);c.lineTo(0,-24);c.lineTo(5,0);c.fill();c.restore();
    C2(3,4,7,'#c8a0ff');C2(1,2,3,'#e8d8ff');star(3,4,3,'#ffffff',t)}
  c.restore();
};

/* ---------- background: night dream path ---------- */
draw=function(){
  ctx.save();
  
  if(S&&S.shake>.3)ctx.translate(rand(-S.shake,S.shake),rand(-S.shake,S.shake));
  drawRealmBg();
  ctx.fillStyle='#f6d8ea';ctx.fillRect(mid-5,0,10,H);ctx.fillStyle='#e0a8c8';ctx.fillRect(mid-5,0,1.5,H);ctx.fillRect(mid+3.5,0,1.5,H);
  {const SI=artImg('deco_seal');if(SI)for(let y=(scroll%96)-96;y<H;y+=96)ctx.drawImage(SI,mid-9,y+26,18,18)}
  if(!artImg('deco_seal'))for(let y=(scroll%48)-48;y<H;y+=48){ctx.fillStyle='#ff7eb6';const hx=mid,hy=y+12;ctx.beginPath();ctx.moveTo(hx,hy+5);ctx.bezierCurveTo(hx-7,hy,hx-3,hy-6,hx,hy-2);ctx.bezierCurveTo(hx+3,hy-6,hx+7,hy,hx,hy+5);ctx.fill()}
  if(S){
    const line=squadY-sw()*.18;
    drawWard(line);
    for(const o of S.objs)if(o.k!=='z')drawGate(o);
    S.zc=0;for(const o of S.objs)if(o.k==='z')S.zc++;
    for(const o of S.objs)if(o.k==='z'){drawZ(o);drawZFx(o)}
    if(S.hexT>0)outlined('星速 −25% '+Math.ceil(S.hexT)+'s',S.x,squadY+sw()*.3+40,13,C.minus,CN);
    if(S.stunT>0)outlined('晕乎乎 '+S.stunT.toFixed(1)+'s',S.x,squadY-heroHH()-60,18,C.minus,CN);
    if(S.xinT>0)outlined('负能量缠身 星力 −35% '+Math.ceil(S.xinT)+'s',S.x,squadY+sw()*.3+(S.hexT>0?58:40),13,C.minus,CN);
    if(S.shieldT>0)outlined('泡泡护盾 '+Math.ceil(S.shieldT)+'s',S.x,squadY+sw()*.3+40+18*((S.hexT>0)+(S.xinT>0))+(S.hexT>0?14:0),14,'#ffb6e6',CN);
    if(S.temp&&tempOn(S.temp.k))outlined(TEMPS[S.temp.k].n+' 生效中',S.x,squadY+sw()*.3+56,13,'#ffb347',CN);
    drawBullets();drawSquadT();
    if(tip&&S.tipObj)drawRing(S.tipObj);
    for(const p of S.parts){ctx.globalAlpha=clamp(p.life/p.l0,0,1);ctx.fillStyle=p.col;const z=p.size;ctx.beginPath();ctx.moveTo(p.x,p.y+z*.6);ctx.bezierCurveTo(p.x-z,p.y,p.x-z*.5,p.y-z*.8,p.x,p.y-z*.25);ctx.bezierCurveTo(p.x+z*.5,p.y-z*.8,p.x+z,p.y,p.x,p.y+z*.6);ctx.fill()}
    ctx.globalAlpha=1;
    {const ci=ART_ON&&artImg('fx_12');if(ci)for(const c of S.cfx)fxImg(ctx,12,c.x,c.y,18,0)}   /* 11-02 15:25：女生版也用手绘星钻 */
    if(!(ART_ON&&artImg('fx_12')))for(const c of S.cfx){ctx.fillStyle='#bff4ff';ctx.beginPath();ctx.moveTo(c.x,c.y-6);ctx.lineTo(c.x+5,c.y);ctx.lineTo(c.x,c.y+6);ctx.lineTo(c.x-5,c.y);ctx.closePath();ctx.fill();ctx.strokeStyle='#5aa8d8';ctx.lineWidth=1.2;ctx.stroke()}
    ctx.globalAlpha=1;
  }
  const g=ctx.createLinearGradient(0,0,0,H*.2);g.addColorStop(0,'rgba(26,20,48,.95)');g.addColorStop(1,'rgba(26,20,48,0)');
  ctx.fillStyle=g;ctx.fillRect(0,0,W,H*.2);
  if(S){drawSkillFx();drawSprFx();drawTexts()}   /* 11-02 15:25：女生版之前漏了手绘特效（g_fx_*）的绘制 */
  if(S&&S.flash>0){ctx.fillStyle='rgba(255,90,140,'+(S.flash*.4)+')';ctx.fillRect(0,0,W,H)}
  ctx.restore();
};

/* ---------- tutorial text, rewritten for this theme ---------- */
Object.assign(TIPS,{
  intro:{t:'怎么玩',d:'按住屏幕左右拖动，带着小精灵们换道。小精灵会自动往前发射星光。手指按下的地方会出现一个小摇杆，圆钮跟着手指，告诉你正往哪边走；不用划很远就能横跨两边。嫌慢可以点右上角的「×1」切到 1.5 倍、2 倍速度，随时能切回来。'},
  qi:{t:'星光糖',d:'撞上去，魔力涨几颗星。门上的数字可以用星光打涨。两扇都是星光糖时，挑数字大的。'},
  n:{t:'烦恼球',d:'坏情绪小怪从右边往下走，冲破结界会扣你的元气。去右边用星光把它净化成小花，还能涨魔力。'},
  xin:{t:'负能量',d:'撞上去掉一大截魔力，还会负能量缠身 6 秒（星力 −35%）。用星光打它能把掉的魔力减到六成。能避开就别撞。'},
  art:{t:'三选一强化',d:'净化大噩梦或变身时会暂停，给你 3 个强化选 1 个。选之前会告诉你下一波是什么，标着“克制下一波”的那个最划算。强化上限随称号提高。'},
  surge:{t:'噩梦潮',d:'每隔一阵会来一波噩梦潮，二十秒内坏情绪又多又强。撑过去，就有一段轻松的时间吃门、攒魔力。'},
  bomb:{t:'星光爆发',d:'屏幕下方的星光爆发：星光炸开，从离结界最近的小怪净化起，一下清掉一大片，大噩梦最多掉 20% 的血。小怪刚压上来时用最值。只能存 1 发，用完要重新充能：时间、净化小怪、撑过噩梦潮都会充，充满才能再放。'},
  boss:{t:'大噩梦',d:'噩梦潮过后，大噩梦会单独登场。每个称号遇到的大噩梦都不一样，称号越高越凶。血很厚、走得慢，提前去右边打它；打掉一半血它会暴怒，还会召来一群烦恼球。让它冲破结界，扣 20%～40% 元气（称号越高扣得越多）、跌 3 星魔力。'},
  run:{t:'急躁鬼',d:'跑得特别快，留意右边上方，看到就去打。'},
  bottle:{t:'变身前夕',d:'星星攒满九颗就卡住了，再吃糖也不涨。净化这一波的大噩梦，就能华丽变身，换上下一套衣装。'},
  brk:{t:'变身星冠',d:'卡在变身前夕时才会出现。打开锁撞上去，直接变身，不用打大噩梦。'},
  bolt:{t:'彩虹光束',d:'屏幕下方新魔法：一道彩虹扫过右边一整列，离结界近的先被净化。用完要等二十秒。'},
  four:{t:'四条道都是坏门',d:'这一排四条道都是坏门，躲不掉，挑最轻的那扇撞。'},
  brute:{t:'拖延懒懒',d:'皮厚，冲破结界扣的元气比烦恼球多。看到它优先打。'},
  fb:{t:'魔法道具',d:'在三选一里可以选招财猫（定时吸走一只怪）、许愿镜（打内耗怪和大噩梦更痛）、安眠音乐盒（定时把坏情绪推远），自动帮你，等级上限随称号提高。'},
  dodge:{t:'坏门错开了：可以全躲',d:'左右两边的坏门没有同时到。先待在晚到的那一侧，等早到的一冲破结界，立刻横移过去，一扇都不用撞。'},
  elite:{t:'内耗怪',d:'冲破结界扣一大截元气，还会吸走你的魔力（最多一整颗星）。头上写着它的称号，称号比你高时，你打它很吃力。'},
  zou:{t:'熬夜',d:'撞上去，星速变慢一段时间。打它能缩短时间。'},
  shield:{t:'泡泡护盾',d:'屏幕下方新魔法：六秒内小怪冲破结界不会伤你，大噩梦也不例外。用完要等四十五秒。'},
  vein:{t:'愿望水晶（带锁）',d:'愿望水晶是左边最赚的门：吃一颗 = 吃 6 颗星光糖的魔力（门上写着能涨多少魔力），想快点变身全靠它。代价是必须先把锁打开才能吃——锁没开撞上去没用，而打锁的这几秒没人管右边，小怪会压过来。怎么选：右边没什么小怪、危险度低，就开锁吃水晶；右边吃紧、危险度高，先吃眼前的星光糖保平安，下一颗水晶再说。'},
  trap:{t:'右边的负能量',d:'右边也会飘来负能量，只占半条道。打小怪时侧身让开就行。'},
  freeze:{t:'时光凝结',d:'屏幕下方新魔法：给整场噩梦按下暂停键，全场小怪定住三秒半，趁机净化。用完要等三十五秒。'},
  fu:{t:'魔法卡（带锁）',d:'撞上去：星光爆发充能 +50%，或者让某个魔法马上能再用。如果这个魔法本来就能用，撞上会直接自动放出来，不会浪费。'},
  jie:{t:'流星考验',d:'从见习魔法生起，每个称号里大约每 7 分钟，左边会来一次流星考验（来之前约 6 秒，左边上方会亮紫光倒计时预告）：走得很慢、锁很厚（要集中火力打一阵，右边的小怪这时会压上来）。打开后冲过去＝通过考验：魔力直接 +1.2 星、星力永久 ×1.08、回 10% 元气；没打开就撞上去，扣 15% 元气、掉魔力。不想冒险就躲到右边——但不去考验，变身会慢很多。'},
  hex:{t:'瞌睡精',d:'头上会读条，读满后你的星速 −25%，持续 4 秒。看到就先净化它。'},
  guard:{t:'黏人怪',d:'身边一圈里的小怪受到的伤害减少 40%。先打黏人怪，再清其他。'},
  cast:{t:'大噩梦的技能',d:'第三波起大噩梦会放技能：召唤小怪、冲刺、瞌睡咒（星速 −25%）、封印（某个魔法 6 秒不能用）。读条时打掉它 8% 的血就能打断。'},
  mech:{t:'萌宠',d:'主页「萌宠」里有两条养成路线：毛绒线（小猫 → 小狐 → … → 创世神兽，贴身扑扑，20 级起带冲击）和飞羽线（兔兔 → 月兔 → … → 彩虹星鲸，远程追踪魔法泡泡，越养魔法泡泡越多）。用星钻沿路线喂养，每级战力 +12%，每 5 级进化成下一个样子，等级不封顶。上场只带一只，哪个魔法系都能带。暂停页也能直接喂养。'}});
petName=l=>(PETS[l-1]||PETS[0]).n;

/* ---------- 封面：粉紫星空、彩虹、魔法少女和萌宠 ---------- */
drawCover=function(g,w,h,t){
  let gr=g.createLinearGradient(0,0,0,h);gr.addColorStop(0,'#2a1650');gr.addColorStop(.5,'#6a3a8a');gr.addColorStop(1,'#e88ab8');g.fillStyle=gr;g.fillRect(0,0,w,h);
  const mx=w*.78,my=h*.22;gr=g.createRadialGradient(mx,my,8,mx,my,95);gr.addColorStop(0,'rgba(255,240,250,.6)');gr.addColorStop(1,'rgba(255,240,250,0)');g.fillStyle=gr;g.fillRect(0,0,w,h);
  g.save();g.beginPath();g.rect(0,0,w,h);g.arc(mx+12,my-8,25,0,6.283,true);g.clip('evenodd');g.fillStyle='#fff6e0';g.beginPath();g.arc(mx,my,28,0,6.283);g.fill();g.restore();   // crescent
  const star=(x,y,R,col,rot)=>{g.fillStyle=col;g.beginPath();for(let i=0;i<10;i++){const a=rot-Math.PI/2+i*Math.PI/5,r2=i%2?R*.45:R;g.lineTo(x+Math.cos(a)*r2,y+Math.sin(a)*r2)}g.fill()};
  for(let i=0;i<34;i++){const sx=(i*89.7)%w,sy=(i*41.3)%(h*.6),k=.5+.5*Math.sin(t*2.4+i*1.7);if(i%5===0)star(sx,sy,2+2.5*k,'rgba(255,240,200,'+(.5+.5*k)+')',t*.5+i);else{g.fillStyle='rgba(255,255,255,'+(.3+.5*k)+')';g.fillRect(sx,sy,1.6,1.6)}}
  // rainbow
  const RB=['#ff8fb0','#ffb37a','#ffe680','#9fe8a8','#8ad0ff','#b49aff'];g.lineWidth=7;g.globalAlpha=.55;
  for(let i=0;i<RB.length;i++){g.strokeStyle=RB[i];g.beginPath();g.arc(w*.5,h*1.05,w*.62-i*7,Math.PI*1.05,Math.PI*1.95);g.stroke()}g.globalAlpha=1;
  // fluffy clouds
  const cloud=(cx,cy,s,a)=>{g.fillStyle='rgba(255,236,248,'+a+')';for(const [dx,dy,r] of [[-1.2,.2,.7],[-.4,-.25,.95],[.5,-.1,.85],[1.25,.25,.65],[0,.35,.8]]){g.beginPath();g.arc(cx+dx*s,cy+dy*s,r*s,0,6.283);g.fill()}};
  cloud(((t*10)%(w+120))-60,h*.62,22,.55);cloud(((t*7+w*.6)%(w+120))-60,h*.78,28,.7);cloud(w*.1,h*.92,34,.85);cloud(w*.85,h*.9,36,.85);
  // floating hearts & bubbles
  for(let i=0;i<8;i++){const x=(i*61+20)%w,y=h-((t*18+i*40)%(h+30)),R=4+i%3*2;g.strokeStyle='rgba(255,255,255,.5)';g.lineWidth=1.2;g.beginPath();g.arc(x+Math.sin(t+i)*6,y,R,0,6.283);g.stroke()}
  // heroine on a star wand trail, with her pet
  const hx=w*.3+Math.sin(t*.8)*8,hy=h*.5+Math.sin(t*1.4)*5;
  gr=g.createLinearGradient(hx-160,hy+40,hx,hy);gr.addColorStop(0,'rgba(255,200,240,0)');gr.addColorStop(1,'rgba(255,230,250,.9)');g.strokeStyle=gr;g.lineWidth=5;g.lineCap='round';
  g.beginPath();g.moveTo(hx-160,hy+46);g.quadraticCurveTo(hx-70,hy+30,hx+6,hy+4);g.stroke();
  for(let i=0;i<9;i++){const a=t*3+i;star(hx-24-i*15+Math.sin(a)*3,hy+12+i*4+Math.cos(a)*3,2+((i+1)%3),'rgba(255,240,180,'+(.5+.4*Math.sin(a))+')',a)}
  drawHero(g,hx,hy,12,t,.95);
  drawFaxiang(g,hx+46,hy-2,1.25,t,5);
  star(hx+18+Math.sin(t*3)*3,hy-58,6,'#fff3a0',t*2);
  gr=g.createLinearGradient(0,h*.6,0,h);gr.addColorStop(0,'rgba(60,20,70,0)');gr.addColorStop(1,'rgba(60,20,70,.6)');g.fillStyle=gr;g.fillRect(0,h*.6,w,h*.4);
};
/* 流派形象（女生版）：星弓系＝粉色星光 + 长弓；咒语系＝紫色魔法阵 + 环绕星星 */
drawPathBack=function(g,x,y,r,t){if(!S||!S.path)return;const ht=heroTop(r)*1.35;
  if(S.path==='ti'){const p=.5+.5*Math.sin(t*3),gr=g.createRadialGradient(x,y-ht*.45,4,x,y-ht*.45,ht*.75);gr.addColorStop(0,'rgba(255,170,210,'+(.32+.1*p)+')');gr.addColorStop(1,'rgba(255,140,200,0)');g.fillStyle=gr;g.beginPath();g.ellipse(x,y-ht*.45,ht*.55,ht*.75,0,0,6.283);g.fill();
    g.save();g.translate(x-ht*.32,y-ht*.5);g.strokeStyle='#ffd6ec';g.lineWidth=3;g.beginPath();g.arc(0,0,ht*.34,-1.2,1.2);g.stroke();g.strokeStyle='rgba(255,255,255,.8)';g.lineWidth=1;g.beginPath();g.moveTo(Math.cos(-1.2)*ht*.34,Math.sin(-1.2)*ht*.34);g.lineTo(Math.cos(1.2)*ht*.34,Math.sin(1.2)*ht*.34);g.stroke();g.restore();
    g.strokeStyle='rgba(255,180,220,'+(.35+.25*p)+')';g.lineWidth=2;g.beginPath();g.ellipse(x,y+2,ht*.42,ht*.12,0,0,6.283);g.stroke()}
  else{g.save();g.translate(x,y+2);g.scale(1,.32);g.strokeStyle='rgba(200,150,255,.8)';g.lineWidth=2.5;g.beginPath();g.arc(0,0,ht*.5,0,6.283);g.stroke();g.rotate(t*.6);g.beginPath();
    for(let i=0;i<=10;i++){const a=i*Math.PI/5-Math.PI/2,rr=i%2?ht*.2:ht*.46;g.lineTo(Math.cos(a)*rr,Math.sin(a)*rr)}g.stroke();g.restore()}};
drawPathFront=function(g,x,y,r,t){if(!S||S.path!=='fa')return;const ht=heroTop(r)*1.35;
  for(let i=0;i<3;i++){const a=t*1.6+i*2.094,px=x+Math.cos(a)*ht*.42,py=y-ht*.55+Math.sin(a)*ht*.12;if(Math.sin(a)<0)continue;g.fillStyle='#fff3a0';g.beginPath();
    for(let k=0;k<=10;k++){const b=k*Math.PI/5-Math.PI/2+t,rr=k%2?2.6:6.5;g.lineTo(px+Math.cos(b)*rr,py+Math.sin(b)*rr)}g.fill()}};
/* 萌宠路线（女生版）：毛绒线 / 飞羽线 */
PET_LINES.beast.forms=[0,2,3,4,7,11,12,13,16];PET_LINES.spirit.forms=[1,8,5,6,9,10,15,14];
try{document.body.classList.remove('ink')}catch(e){}

/* 女生版场景：水彩绘本色调，按称号换景 */
BG_THEMES.splice(0,BG_THEMES.length,
 {sky:['#fdf1f4','#f3dbe6'],ink:'150,110,140',mist:'255,250,252',lane:['150,110,140','120,100,160'],deco:'petal',light:1},
 {sky:['#fff0ec','#fbd8d0'],ink:'170,100,110',mist:'255,250,248',lane:['160,100,110','120,96,150'],deco:'petal',light:1},
 {sky:['#eefaf4','#d2efe4'],ink:'90,140,130',mist:'250,255,252',lane:['90,130,120','110,96,150'],deco:'firefly',light:1},
 {sky:['#eef4fd','#d4e2f6'],ink:'110,120,170',mist:'255,255,255',lane:['110,120,170','130,100,160'],deco:'cloud',light:1},
 {sky:['#2a2246','#41326a'],ink:'20,14,40',mist:'200,170,240',lane:['50,40,80','70,40,90'],deco:'star',light:0},
 {sky:['#fbf0f8','#ead6ef'],ink:'140,100,150',mist:'255,250,255',lane:['140,100,150','120,90,160'],deco:'petal',light:1},
 {sky:['#fff6e8','#f2dcf0'],ink:'150,110,150',mist:'255,252,248',lane:['150,110,140','120,100,160'],deco:'ray',light:1},
 {sky:['#1a2142','#2c3866'],ink:'10,14,34',mist:'160,180,240',lane:['36,44,80','60,40,90'],deco:'star',light:0},
 {sky:['#eef6e6','#d3e6c8'],ink:'90,120,80',mist:'252,255,248',lane:['90,120,80','110,96,140'],deco:'firefly',light:1},
 {sky:['#fdeef3','#f6d2df'],ink:'160,100,130',mist:'255,250,252',lane:['150,100,130','120,96,160'],deco:'petal',light:1},
 {sky:['#241d3e','#3c2f62'],ink:'16,10,34',mist:'210,180,250',lane:['46,36,76','66,40,90'],deco:'star',light:0},
 {sky:['#f4f0ff','#dcd2f6'],ink:'120,100,170',mist:'255,255,255',lane:['120,100,170','140,96,160'],deco:'gold',light:1},
 {sky:['#f7eefc','#e4d6f2'],ink:'130,100,160',mist:'255,252,255',lane:['130,100,160','140,90,150'],deco:'cloud',light:1},
 {sky:['#2b2040','#463066'],ink:'16,10,30',mist:'220,170,250',lane:['50,36,80','70,40,90'],deco:'void',light:0},
 {sky:['#fff5e6','#f6e0c4'],ink:'160,120,80',mist:'255,252,244',lane:['150,120,90','140,96,140'],deco:'gold',light:1},
 {sky:['#eef2fb','#d6dcf2'],ink:'100,120,160',mist:'255,255,255',lane:['100,120,160','120,100,160'],deco:'snow',light:1},
 {sky:['#1d1830','#33285a'],ink:'10,8,24',mist:'210,180,250',lane:['40,34,70','64,40,90'],deco:'star',light:0},
 {sky:['#fffaf2','#f6e8f4'],ink:'150,120,140',mist:'255,252,250',lane:['150,120,140','130,100,160'],deco:'ray',light:1});
ART_ON=true;ART_PRE='g_';   /* 11-02：女生版自己的一套手绘图 art/g_*.webp；没有的图继续用代码画 */
BOSS_LORE.length=0;   // 女生版大噩梦设定另写，先不显示修仙版的描述

/* 11-02：战场与小怪进阶（女生版名字） */
PLACES.splice(0,PLACES.length,['樱花小镇','清晨的樱花街道，烦恼球在角落里冒出来'],['樱花小镇 · 放学路上','落满花瓣的放学路，烦恼球跟着书包一路滚'],['樱花小镇 · 黄昏河堤','晚霞照着河堤，第一批大噩梦从桥下冒出来'],
  ['星光魔法学院','学院花园的彩窗下，坏心情越聚越多'],['晚霞花海','金色晚霞铺满花海，急躁鬼在花丛里乱窜'],['冰晶湖畔','湖面结满冰晶，冷冰冰的怪排队走来'],
  ['彩虹天空城','彩虹桥连着天空城，怪物们也跟着爬了上来'],['紫水晶洞窟','闪着紫光的洞窟深处，内耗怪越变越多'],['云朵城堡','软绵绵的云朵城堡，瞌睡精在这里打转'],
  ['精灵森林','发光蘑菇和萤火点亮森林，黏人怪成群结队'],['雷云之巅','乌云和闪电的山顶，每一步都要勇气'],['月光湖','月光洒在湖面，噩梦从水底浮上来'],
  ['梦境星海','漂浮的小岛与星光，梦里的怪也来捣乱'],['薰衣草宫殿','紫色花香的宫殿，坏心情躲在每个角落'],['银河星港','银河边的星港，怪物大军坐着流星来了'],
  ['星辰神殿','璀璨星河下的神殿，最强的坏心情在聚集'],['晨曦之门','天亮之前最暗的地方，再坚持一下'],['创世之庭','一切开始的地方，最后的大敌在等你']);
Object.assign(MON_V,{n:['烦恼球','带刺烦恼球','双生烦恼球','雷云烦恼球','水晶烦恼球','暗星烦恼球'],run:['急躁鬼','火苗急躁鬼','闪电急躁鬼','旋风急躁鬼','火箭急躁鬼','流星急躁鬼'],
  brute:['拖延懒懒','枕头懒懒','沙发懒懒','被窝懒懒','石头懒懒','冰山懒懒'],elite:['内耗怪','毛线团内耗怪','漩涡内耗怪','镜面内耗怪','迷宫内耗怪','黑洞内耗怪'],
  hex:['瞌睡精','小绵羊瞌睡精','月亮瞌睡精','枕头瞌睡精','梦泡瞌睡精','星云瞌睡精'],guard:['黏人怪','果冻黏人怪','蜂蜜黏人怪','棉花糖黏人怪','口香糖黏人怪','果冻骑士']});

/* 11-02：女生版接手绘图——有图用图，没图用原来的代码画 */
{const _z=drawZ;drawZ=function(o){if(o.boss&&o.look)return drawBoss(o);const tt=tierOf(o);if((tt&&artImg('mon_'+o.type+'_'+tt))||artImg('mon_'+o.type))return _xDZ(o);return _z(o)}}
{const _b=drawBoss;drawBoss=function(o){if(o.look&&artImg('boss_'+o.look.bi))return _xDB(o);return _b(o)}}
{const _c=drawCover;drawCover=function(g,w,h,t){if(artImg('bg_cover'))return _xDC(g,w,h,t);return _c(g,w,h,t)}}
{const _h=drawHero;drawHero=function(g,x,y,r,t,scl=1){r=clamp(r|0,0,REALMS.length-1);const im=artImg(heroArtKey(r));if(!im)return _h(g,x,y,r,t,scl);
  const hh=heroTop(r)*1.25*scl,br=Math.sin(t*2.4),fl=r>=8?-5+Math.sin(t*2.2)*1.5:0;g.save();g.translate(x,y);
  g.globalAlpha=.25;g.fillStyle='#6a3a8a';g.beginPath();g.ellipse(0,2,13*scl,3.5*scl,0,0,6.283);g.fill();g.globalAlpha=1;
  {const k=.5+.5*Math.sin(t*3),cy=fl-hh*.45,R=hh*.62,gr=g.createRadialGradient(0,cy,R*.1,0,cy,R);gr.addColorStop(0,'rgba(48,18,80,'+(.62+.06*k)+')');gr.addColorStop(.72,'rgba(48,18,80,.38)');gr.addColorStop(1,'rgba(70,28,110,0)');g.fillStyle=gr;g.beginPath();g.ellipse(0,cy,R*.78,R,0,0,6.283);g.fill()}   /* 11-02 19:45：人物身后一圈深紫底光，浅色衣服在粉背景上也看得清 */
  const yb=fl+3;g.translate(0,yb);g.scale(1-.008*br,1+.018*br);artDraw(g,im,0,0,hh,null,OL_F(g));g.restore()}}
{const _f=drawFaxiang;drawFaxiang=function(g,x,y,sc,t,lvl){lvl=clamp(lvl|0,1,PETS.length);const im=artImg('pet_'+(lvl-1));if(!im)return _f(g,x,y,sc,t,lvl);
  const P=PETS[lvl-1],bob=Math.sin(t*3)*2,go=S&&S.pet&&S.pet.st==='go',yb=y+2+bob*.5,hh=(P.bird||P.whale?44:38)*sc*(P.big?1.15:1);
  if(P.glow){g.globalAlpha=.22+.1*Math.sin(t*4);g.fillStyle=P.glow;g.beginPath();g.ellipse(x,y-16*sc,26*sc,20*sc,0,0,6.283);g.fill();g.globalAlpha=1}
  g.save();g.translate(x,yb);g.scale(go?1.16:1,go?.9:1);g.translate(-x,-yb);artDraw(g,im,x,yb,hh,null,OL_F(g));g.restore()}}
{const _gi=gateIcon;gateIcon=function(g,o,cx,cy,s,t,dim,cc){const ik=g==='fb'&&o&&o.fbk?'ic_'+o.fbk:g==='fu'&&o&&o.fu&&artImg('ic_'+o.fu)?'ic_'+o.fu:'ic_'+g;if(artImg(ik))return _xGI(g,o,cx,cy,s,t,dim,cc);return _gi(g,o,cx,cy,s,t,dim,cc)}}

/* 11-02 17:55：被动的四个形态（女生版名字） */
PS_NAMES={crow:['星星小鸟','彩虹小鸟','星光青鸟','月光凤凰'],orb:['守护星','星座守护','星环守护','银河守护'],cloud:['彩虹云','七彩云','棉花糖云宫','梦幻天穹'],
  gang:['星光护盾','水晶护盾','钻石护盾','银河护盾'],zhan:['勇气','闪亮勇气','勇者之心','传说之心'],jj:['星光纵横','流光纵横','彗星纵横','银河之箭']};
TIPS.psform={t:'被动进化',d:'被动魔法（星星小鸟、守护星、彩虹云）和星弓系被动（星光护盾、勇气、星光纵横）在 Lv8、Lv14、Lv20 各进化一次：改名字、换样子、威力也变强。星星小鸟、彩虹云、星光纵横的巨箭会跟在你身边，小鸟从身边飞出去；守护星绕身，形态越高越大越亮；星光护盾是身上的光罩，勇气是脚下的火焰（元气越低越旺）。魔法按钮右上角是等级，Lv8 银框、Lv14 金框、Lv20 彩虹框。'};
FB_NAMES={gourd:['招财猫','金铃招财猫','幸运招财猫','黄金招财猫'],mirror:['许愿镜','星星许愿镜','月光魔镜','彩虹魔镜'],bell:['安眠音乐盒','星空音乐盒','月光音乐盒','梦幻旋转木马']};
TIPS.psform.d=TIPS.psform.d.replace('魔法按钮右上角','魔法道具（招财猫、许愿镜、安眠音乐盒）也一样，Lv8、Lv14、Lv20 进化，绕着你浮在身边。魔法按钮右上角');

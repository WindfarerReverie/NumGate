import asyncio,sys,json
from playwright.async_api import async_playwright
SRCF=sys.argv[1] if len(sys.argv)>1 else '/home/claude/numgate/index.html'
RUNS=int(sys.argv[2]) if len(sys.argv)>2 else 1
LIFE=int(sys.argv[4]) if len(sys.argv)>4 else 1
NOSK=len(sys.argv)>5 and sys.argv[5]=='noskill'
RND=len(sys.argv)>5 and sys.argv[5]=='randpick'
FB=len(sys.argv)>5 and sys.argv[5]=='fabao'
TMP=len(sys.argv)>5 and sys.argv[5]=='temp'
TMAX=float(sys.argv[3]) if len(sys.argv)>3 else 3600
SRC=open(SRCF).read().replace("(()=>{\nconst $=","(()=>{\nwindow.__X={get S(){return S},update:dt=>update(dt),gr:o=>gateResult(o),press:()=>pressure(),geo:()=>({mid,lmid,roadX,roadW,squadY,H}),bomb:()=>useBomb(),bolt:()=>useBolt(),shield:()=>useShield(),freeze:()=>useFreeze(),realm:()=>realmOf(S.count),rname:x=>rName(x),GT:()=>GT,running:()=>running,REALMS:()=>REALMS,slot:()=>slot(),sw:()=>sw(),dg:()=>dangerTick(.2),pk:sm=>{pop=null;S.brkPend=0;pickScan();if(pickOpts){const tr=nextTrait();const c=(window.__path&&pickOpts.find(k=>k==='path_'+window.__path))||(window.__fb&&pickOpts.find(k=>['gourd','bell','mirror'].includes(k)))||(window.__tmp&&pickOpts.find(k=>k.startsWith('t_')))||(sm&&tr&&pickOpts.find(k=>TRAITS[tr].c.includes(k)))||pickOpts[ri(0,pickOpts.length-1)];choosePick(c)}},bm:()=>build()/expBuild(),fire:()=>useFire(),ice:()=>useIce(),sword:()=>useSword(),jump:(r,p)=>{S.maxR=r;S.count=RBASE*Math.pow(2,RSTART[r])*1.0001;S.rR=r;S.path=p;S.pathV2=S.pathV3=S.pathV4=true;S.fa={};S.mp=100;S.t=Math.max(S.t,PRE+CYC*8+1);S.hpF=1;let g=0;while(build()/expBuild()<(window.__bq||1)&&g++<400){S.pickQ=1;pop=null;S.brkPend=0;pickScan();if(pickOpts){const c=(window.__nofa?pickOpts.find(k=>!k.startsWith('t_')&&k!=='coin'&&!k.startsWith('fa_')):pickOpts.find(k=>k.startsWith('fa_')))||pickOpts.find(k=>!k.startsWith('t_')&&k!=='coin')||pickOpts[0];choosePick(c)}}pop=null;paused=false;return [g,+(build()/expBuild()).toFixed(2),JSON.stringify(S.fa)]},share:()=>{const d=S.dsrc||{},t=Object.values(d).reduce((a,b)=>a+b,0)||1,f=a=>Math.round(a.reduce((x,k)=>x+(d[k]||0),0)/t*100);return 'atk'+f(['atk'])+'/act'+f(['fire','sword','bolt','bomb'])+'/auto'+f(['pet','gourd','crow','orb','cloud'])+'/sys'+f(['sys'])}};window.__dps=()=>dps();\nconst $=",1)
HTML='<!doctype html><html><head><meta charset=utf8><meta name=viewport content="width=device-width,initial-scale=1"><style>[hidden]{display:none!important}</style></head><body style="height:100vh;margin:0">'+SRC+'</body></html>'
import os
SIMF='/tmp/claude-0/pt/sim_%d.html'%os.getpid()
open(SIMF,'w').write(HTML)
BOT=r'''(secs)=>{const X=window.__X,S=X.S,g=X.geo(),GT=X.GT();const line=g.squadY-X.sw()*.18,rc=(g.mid+g.roadX+g.roadW)/2,rm=g.mid+g.roadW/4;
 const log=window.__log=window.__log||{realms:{},events:[]};let acc=0;const dt=1/30;
 for(let st=0;st<secs*30;st++){
  if(S.won){log.clear=Math.round(S.t);return {dead:false,won:true,log}}
  if(X.S.deathOpen){log.deaths=(log.deaths||0)+1;log.dt=(log.dt||[]);log.dt.push(Math.round(X.S.t));const b=document.querySelector('#deathOpts button');if(b)b.click();}
  if(!X.running())return {dead:true,log};
  acc+=dt;
  log.dacc=(log.dacc||0)+dt;if(log.dacc>=.2){log.dacc=0;const d=X.dg();log.dn=(log.dn||0)+1;log.ds=(log.ds||0)+d;log.dm=Math.max(log.dm||0,d);const sg=X.S.surgeOn;log[sg?'sS':'sM']=(log[sg?'sS':'sM']||0)+d;log[sg?'nS':'nM']=(log[sg?'nS':'nM']||0)+1;(log.hist=log.hist||[]).push(+d.toFixed(2));if(log.hist.length>200)log.hist.shift()}
  if(acc>=.1){acc=0;
   const spd=S.objs.length?0:0, vv=g.H*.2*(1+Math.min(S.t,300)/750);
   const val=o=>{if(GT[o.g].lock&&o.lock>0&&o.g!=='jie'&&o.g!=='zou'){const arr=(line-o.y)/vv;if(o.lock>window.__dps()*arr*.6)return S.count}if(o.g==='art'||o.g==='fb'||o.g==='fu')return S.count*1.25;return X.gr(o)};
   let rows={};for(const o of S.objs){if(o.k==='gate'&&o.rid&&!o.dead&&o.y<line)(rows[o.rid]=rows[o.rid]||[]).push(o)}
   let best=null,minY=-1e9;for(const id in rows){const r=rows[id];const y=Math.max(...r.map(o=>o.y));if(y>minY){minY=y;best=r}}
   const zs=S.objs.filter(o=>o.k==='z'&&!o.dead);
   // fight target: column with the most threat
   let c0=0,c1=0;for(const z of zs){const w=(z.boss?(z.cast?14:6):z.type==='elite'?4:z.type==='hex'?6:z.type==='guard'?5:1)*(z.y/line);if(z.x<rm)c0+=w;else c1+=w}
   let tx=c1>c0?(rm+g.roadX+g.roadW)/2:(g.mid+rm)/2;const bz=zs.find(z=>z.boss&&z.y>0),hz=zs.find(z=>(z.type==='hex'&&z.cast>1)||z.type==='guard');if(bz&&(bz.cast||!hz))tx=bz.x;else if(hz)tx=hz.x;
   if(best){const bv=best.reduce((a,o)=>val(o)>val(a)?o:a,best[0]);const gain=val(bv)>S.count*1.001;const leftOnly=best.every(o=>o.x0<g.mid);
     const near=zs.filter(z=>z.y>line*.55).length;
     if(line-minY<g.squadY*.3){if(gain||!leftOnly)tx=(bv.x0+bv.x1)/2}
     else if(line-minY<g.squadY*.75&&gain&&(near<3||!X.S.surgeOn))tx=(bv.x0+bv.x1)/2}
   if(tx>g.mid){for(const t of S.objs.filter(o=>o.trap&&!o.rid&&!o.dead&&o.y<line&&o.y>line*.45)){if(tx>=t.x0-12&&tx<=t.x1+12)tx=(t.x0+t.x1)/2>rc?t.x0-22:t.x1+22}}
   if(window.__left){let lb=null;if(best){for(const o of best)if(o.x1<=g.mid+2&&(!lb||val(o)>val(lb)))lb=o}tx=lb&&val(lb)>=S.count?(lb.x0+lb.x1)/2:(g.roadX+g.mid)/2}
   S.x=tx;
   // skills
   const boss=zs.find(z=>z.boss),bossNear=boss&&boss.y>line*.62,eliteNear=zs.some(z=>z.type==='elite'&&z.y>line*.6);
   const crowd=zs.filter(z=>z.y>line*.45).length;
   if(!window.__nosk){
   if((bossNear||(eliteNear&&X.press()>1))&&S.shieldCd<=0)X.shield();
   if(S.shieldT<=0&&((crowd>=7)||(eliteNear&&X.press()>.8)||bossNear)&&S.freezeCd<=0)X.freeze();
   if(!window.__nocast&&S.boltCd<=0&&(crowd>=4||eliteNear))X.bolt();if(window.__path==='fa'&&!window.__nofa&&!window.__nocast&&(!window.__occ||bossNear||eliteNear||crowd>=8)){const mp=S.mp||0;if(crowd>=7)X.ice();if(crowd>=5||eliteNear||bossNear)X.sword();if(crowd>=4||eliteNear)X.bolt();if(zs.length&&(mp>60||crowd>=3))X.fire();}
   if(S.bombs>0&&S.shieldT<=0&&S.freezeT<=0&&((crowd>=10)||(bossNear&&boss.y>line*.8)||(eliteNear&&crowd>=5&&S.bombs>=2)))X.bomb();}
  }
  if(window.__pkt=(window.__pkt||0)+dt,window.__pkt>.5){window.__pkt=0;X.pk(!window.__rnd)}
  X.update(dt);log.mh=Math.min(log.mh==null?1:log.mh,S.hpF);
  const r=X.realm(),k=X.rname(r);const big=X.REALMS()[r.r];if(!(big in log.realms))log.realms[big]=Math.round(S.t);
 }
 return {dead:false,log};}'''
async def main():
  async with async_playwright() as p:
    b=await p.chromium.launch(args=['--no-sandbox'])
    for run in range(RUNS):
      pg=await b.new_page(viewport={'width':400,'height':820})
      errs=[];pg.on('pageerror',lambda e:errs.append(str(e)))
      await pg.goto('file://'+SIMF);await pg.wait_for_timeout(300)
      await pg.click('#new_1');
      await pg.evaluate("()=>{const s=window.__X.slot();s.noTips=true;s.tutDone=true;s.life=LIFE}".replace("LIFE",str(LIFE)))
      import os
      if os.environ.get('FAST'):await pg.evaluate('f=>{window.__fast=f}',float(os.environ['FAST']))
      await pg.click('#bFight');await pg.wait_for_timeout(200)
      if NOSK: await pg.evaluate('()=>{window.__nosk=1}')
      if RND: await pg.evaluate('()=>{window.__rnd=1}')
      if FB: await pg.evaluate('()=>{window.__fb=1}')
      if os.environ.get('PATH_'):await pg.evaluate('p=>{window.__path=p}',os.environ['PATH_'])
      if os.environ.get('NOFA'):await pg.evaluate('()=>{window.__nofa=1}')
      if os.environ.get('NOCAST'):await pg.evaluate('()=>{window.__nocast=1}')
      if os.environ.get('OCC'):await pg.evaluate('()=>{window.__occ=1}')
      if os.environ.get('LEFT'):await pg.evaluate('()=>{window.__left=1}')
      if os.environ.get('JUMP'):
        print('jump',await pg.evaluate('a=>window.__X.jump(a[0],a[1])',[int(os.environ['JUMP']),os.environ.get('PATH_','fa')]),flush=True)
      if TMP: await pg.evaluate('()=>{window.__tmp=1}')
      t=0;res=None;line=[]
      while t<TMAX:
        res=await pg.evaluate(BOT,60);t+=60
        st=await pg.evaluate("(()=>{const X=window.__X,S=X.S,l=window.__log||{};const r=[Math.round(S.t),X.rname(X.realm()),'M',(S.M||1).toFixed(2),'b/e',X.bm().toFixed(2),'mow',((l.sM||0)/Math.max(1,l.nM||1)).toFixed(2),'surge',((l.sS||0)/Math.max(1,l.nS||1)).toFixed(2),'sb',(S.sb||1).toFixed(2),'max',(l.dm||0).toFixed(2),'hp',(S.hpF||0).toFixed(2),'minhp',(l.mh==null?1:l.mh).toFixed(2),'bombs',S.bombs,'path',S.path||'-','D',(l.deaths||0),'rw',+(S.rwF||1).toFixed(2),'yq',+(S.yqM||0).toFixed(1),'hp0',Math.round((S.objs.filter(o=>o.k==='z'&&o.type==='n').map(o=>o.hp0)[0]||0)/Math.max(1e-9,window.__dps())*100)/100,'sh',X.share(),'mp',Math.round(S.mp||0),'jie',(S.jieWin||0)+'/'+(S.jieFail||0),S.maxWave];l.mh=1;l.ds=0;l.dn=0;l.dm=0;l.sM=0;l.nM=0;l.sS=0;l.nS=0;return r})()")
        line.append(st)
        if res['dead'] or res.get('won'):break
      for l in line:print(' ',l)
      print('  last40s',(await pg.evaluate('()=>window.__log.hist'))[-200::10])
      loss=await pg.evaluate("()=>document.getElementById('rLoss')?document.getElementById('rLoss').textContent:''")
      print('RUN',run,'WON' if res.get('won') else 'dead' if res['dead'] else 'alive','t',line[-1][0],'peak',line[-1][1],'coins',await pg.evaluate('()=>Math.round(window.__X.S.coins)'),'wave',line[-1][-1],loss)
      print('  realms',json.dumps(res['log']['realms'],ensure_ascii=False))
      print('  errs',errs[:3]);await pg.close()
    await b.close()
asyncio.run(main())

import asyncio,json,sys
from playwright.async_api import async_playwright
INJ="(()=>{\nwindow.__X={get S(){return S},update:dt=>update(dt),slot:()=>slot(),RS:()=>[RBASE,RSTART],clr:()=>{pop=null;coach=null},up:(g,k,n)=>{for(let i=0;i<n;i++)upLv(g,k)},sk:k=>({bolt:useBolt,shield:useShield,freeze:useFreeze,bomb:useBomb,fire:typeof useFire!=='undefined'?useFire:null,ice:typeof useIce!=='undefined'?useIce:null,sword:typeof useSword!=='undefined'?useSword:null})[k]&&({bolt:useBolt,shield:useShield,freeze:useFreeze,bomb:useBomb,fire:useFire,ice:useIce,sword:useSword})[k](),ci:()=>closeIntel(),mid:()=>mid,rx:()=>[roadX,roadW],petLv:n=>{const s=slot();s.pets=s.pets||{};}};\nconst $="
HOOK="""(()=>{const P=CanvasRenderingContext2D.prototype;window.__cnt={};window.__img={};const fn=()=>{const st=new Error().stack.split('\\n');for(let i=3;i<st.length;i++){const m=st[i].match(/at (?:Object\\.)?([\\w$.]+) /);if(m&&!/^(HTMLCanvas|CanvasRendering|eval|Array|anonymous|Function)/.test(m[1]))return m[1]}return '?'};
for(const k of ['fill','stroke','fillRect','strokeRect']){const o=P[k];P[k]=function(...a){if(window.__rec){const f=fn();window.__cnt[f]=(window.__cnt[f]||0)+1}return o.apply(this,a)}}
const di=P.drawImage;P.drawImage=function(...a){if(window.__rec){const f=fn();window.__img[f]=(window.__img[f]||0)+1}return di.apply(this,a)}})();"""
async def run(src,tag,path):
  s=open(src).read().replace("(()=>{\nconst $=",INJ,1)
  open('/tmp/claude-0/pt/tscan_%s.html'%tag,'w').write('<!doctype html><meta charset=utf8><meta name=viewport content="width=device-width,initial-scale=1"><body style="height:100vh;margin:0"><script>'+HOOK+'</script>'+s)
  async with async_playwright() as p:
    b=await p.chromium.launch(args=['--no-sandbox']);pg=await b.new_page(viewport={'width':390,'height':800})
    errs=[];pg.on('pageerror',lambda e:errs.append(str(e)))
    await pg.goto('http://127.0.0.1:8765/tscan_%s.html'%tag);await pg.wait_for_timeout(700)
    await pg.click('#new_1');await pg.evaluate("()=>{const s=window.__X.slot();s.noTips=true;s.tutDone=true;s.noIntel=true;s.noCut=true;s.cos={own:{},tr:'peach',au:'rune'};s.petLine='beast';s.petLv=12}");await pg.click('#bFight');await pg.wait_for_timeout(400)
    await pg.evaluate("""(path)=>{const X=window.__X,S=X.S,[RB,RS]=X.RS();S.maxR=9;S.rR=9;S.peakR=9;S.count=RB*Math.pow(2,RS[9]+1);S.path=path;S.lvR={};S.t=PRE_T;S.mp=999;S.bombs=3;
      S.lv.dmg=8;S.lv.spread=2;S.lv.rate=6;S.lv.pierce=2;S.fb={gourd:0,mirror:0,bell:0};for(const k of ['gourd','mirror','bell'])X.up('fb',k,10);
      for(const k of (path==='fa'?['crow','orb','cloud','fire','ice','sword','bolt']:['gang','zhan','jj']))X.up(path,k,15)}""".replace('PRE_T','15+60*20+42'),path)
    await pg.evaluate("()=>{window.__rec=1}")
    for i in range(8):
      await pg.evaluate("()=>{const X=window.__X;X.ci();X.clr();X.S.hpF=1;X.S.mp=999;for(const k of ['bolt','shield','freeze','bomb','fire','ice','sword'])try{X.sk(k)}catch(e){}}")
      await pg.wait_for_timeout(700)
    await pg.screenshot(path='/tmp/claude-0/pt/rd/scan_%s.png'%tag)
    c=await pg.evaluate("()=>[window.__cnt,window.__img]")
    print(tag,'CODE',json.dumps(sorted(c[0].items(),key=lambda x:-x[1])),'\n  IMG',json.dumps(sorted(c[1].items(),key=lambda x:-x[1])),errs[:2])
    await b.close()
async def main():
  for f,t in [('index.html','x'),('girl.html','g')]:
    for path in ['ti','fa']:await run('/home/claude/numgate/'+f,t+path,path)
if __name__=="__main__":asyncio.run(main())

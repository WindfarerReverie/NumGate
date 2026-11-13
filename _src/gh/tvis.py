import asyncio,sys
from playwright.async_api import async_playwright
sys.path.insert(0,'/tmp/claude-0/pt')
from tscan import INJ
async def run(src,tag,path,setup,clip):
  s=open(src).read().replace("(()=>{\nconst $=",INJ,1)
  open('/tmp/claude-0/pt/tvis_%s.html'%tag,'w').write('<!doctype html><meta charset=utf8><meta name=viewport content="width=device-width,initial-scale=1"><body style="height:100vh;margin:0">'+s)
  async with async_playwright() as p:
    b=await p.chromium.launch(args=['--no-sandbox']);pg=await b.new_page(viewport={'width':390,'height':800},device_scale_factor=2)
    errs=[];pg.on('pageerror',lambda e:errs.append(str(e)))
    await pg.goto('http://127.0.0.1:8765/tvis_%s.html'%tag);await pg.wait_for_timeout(700)
    await pg.click('#new_1');await pg.evaluate("()=>{const s=window.__X.slot();s.noTips=true;s.tutDone=true;s.noIntel=true;s.noCut=true}");await pg.click('#bFight');await pg.wait_for_timeout(400)
    await pg.evaluate("(path)=>{const X=window.__X,S=X.S,[RB,RS]=X.RS();S.maxR=9;S.rR=9;S.peakR=9;S.count=RB*Math.pow(2,RS[9]+1);S.path=path;S.lv.rate=6;S.lv.dmg=8}",path)
    await pg.evaluate(setup)
    await pg.wait_for_timeout(1500)
    await pg.evaluate("()=>{const X=window.__X;X.ci();X.clr()}")
    await pg.wait_for_timeout(300)
    await pg.screenshot(path='/tmp/claude-0/pt/rd/vis_%s.png'%tag,clip=clip)
    print(tag,errs[:2])
    await b.close()
if __name__=='__main__':
  src,tag,path,setup=sys.argv[1:5];clip=eval(sys.argv[5]) if len(sys.argv)>5 else {'x':0,'y':0,'width':390,'height':800}
  asyncio.run(run(src,tag,path,setup,clip))

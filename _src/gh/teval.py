import asyncio,sys
from playwright.async_api import async_playwright
from tscan import INJ
async def run(src,path,setup,expr):
  s=open(src).read().replace("(()=>{\nconst $=",INJ+"window.__E=(c)=>eval(c);\n",1) if False else open(src).read().replace("(()=>{\nconst $=",INJ,1)
  s=s.replace("window.__X={","window.__EV=c=>eval(c);window.__X={",1)
  open('/tmp/claude-0/pt/teval.html','w').write('<!doctype html><meta charset=utf8><body style="height:100vh;margin:0">'+s)
  async with async_playwright() as p:
    b=await p.chromium.launch(args=['--no-sandbox']);pg=await b.new_page(viewport={'width':390,'height':800})
    errs=[];pg.on('pageerror',lambda e:errs.append(str(e)))
    await pg.goto('http://127.0.0.1:8765/teval.html');await pg.wait_for_timeout(700)
    await pg.click('#new_1');await pg.evaluate("()=>{const s=window.__X.slot();s.noTips=true;s.tutDone=true;s.noIntel=true;s.noCut=true}");await pg.click('#bFight');await pg.wait_for_timeout(400)
    await pg.evaluate("(path)=>{const X=window.__X,S=X.S,[RB,RS]=X.RS();S.maxR=9;S.rR=9;S.peakR=9;S.count=RB*Math.pow(2,RS[9]+1);S.path=path;}",path)
    await pg.evaluate(setup);await pg.wait_for_timeout(1200)
    print(await pg.evaluate("(e)=>window.__EV(e)",expr),errs[:2])
    await b.close()
asyncio.run(run(*sys.argv[1:5]))

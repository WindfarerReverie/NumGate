import asyncio,sys
from playwright.async_api import async_playwright
from tscan import INJ
async def run(src,tag):
  s=open(src).read().replace("(()=>{\nconst $=",INJ,1).replace("window.__X={","window.__EV=c=>eval(c);window.__X={",1)
  open('/tmp/claude-0/pt/tbgm_%s.html'%tag,'w').write('<!doctype html><meta charset=utf8><body style="height:100vh;margin:0">'+s)
  async with async_playwright() as p:
    b=await p.chromium.launch(args=['--no-sandbox','--autoplay-policy=no-user-gesture-required']);pg=await b.new_page(viewport={'width':390,'height':800})
    errs=[];pg.on('pageerror',lambda e:errs.append(str(e)))
    await pg.goto('http://127.0.0.1:8765/tbgm_%s.html'%tag);await pg.wait_for_timeout(600)
    await pg.click('#new_1');await pg.evaluate("()=>{const s=window.__X.slot();s.noTips=true;s.tutDone=true;s.noIntel=true}");await pg.wait_for_timeout(2500)
    E=lambda c:pg.evaluate("c=>window.__EV(c)",c)
    print(tag,'menu',await E("JSON.stringify([!!SND.bgmG,Object.keys(BGM.buf),BGM.cur,actx&&actx.state])"))
    await pg.click('#bVolHub');await pg.wait_for_timeout(200)
    print(' panel',await E("JSON.stringify([!$('volPanel').hidden,$('volBgm').value,$('volSfx').value,$('volVo').value,$('bVolMute').textContent])"))
    await pg.evaluate("()=>{const e=document.getElementById('volBgm');e.value=30;e.dispatchEvent(new Event('input'))}");await pg.click('#bVolMute');await pg.wait_for_timeout(300)
    print(' after',await E("JSON.stringify([AV,localStorage.getItem('ngAudio'),+SND.out.gain.value.toFixed(2),+SND.bgmG.gain.value.toFixed(2),sound,$('bSnd').textContent])"))
    await pg.click('#bVolMute');await pg.click('#bVolX');await pg.wait_for_timeout(200)
    await pg.click('#bFight');await pg.wait_for_timeout(800)
    await E("S.t=PRE+5;window.__X.ci&&window.__X.ci();0");await pg.wait_for_timeout(2500)
    print(' mow',await E("JSON.stringify([BGM.cur,inSurge(),+SND.bgmG.gain.value.toFixed(2)])"))
    await E("S.t=PRE+MOW+2;0");await pg.wait_for_timeout(2500)
    print(' surge',await E("JSON.stringify([BGM.cur,inSurge(),BGM.tr.n])"))
    await pg.click('#bSnd');await pg.wait_for_timeout(200)
    print(' hud open',await E("JSON.stringify([!$('volPanel').hidden,paused])"));await pg.click('#bVolX');await pg.wait_for_timeout(200)
    print(' closed',await E("JSON.stringify([$('volPanel').hidden,paused])"))
    await pg.click('#bPause');await pg.wait_for_timeout(200);await pg.click('#bVolOpen');await pg.wait_for_timeout(200)
    print(' pause open',await E("JSON.stringify([!$('volPanel').hidden,paused])"));await pg.click('#bVolX');await pg.wait_for_timeout(200)
    print(' pause closed',await E("JSON.stringify([$('volPanel').hidden,paused,!$('ovPause').hidden])"))
    await pg.screenshot(path='/tmp/claude-0/pt/rd/bgm_%s.png'%tag)
    print(' errs',errs[:3]);await b.close()
async def main():
  for f,t in [('index.html','x'),('girl.html','g')]:await run('/home/claude/numgate/'+f,t)
asyncio.run(main())

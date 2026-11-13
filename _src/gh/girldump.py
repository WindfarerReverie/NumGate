import asyncio,json
from playwright.async_api import async_playwright
SRC=open('/home/claude/numgate/girl.html').read().replace("(()=>{\nconst $=","(()=>{\nwindow.__D=()=>{const o={};const g=(k,f)=>{try{o[k]=f()}catch(e){o[k]='ERR '+e}};g('REALMS',()=>REALMS);g('TEMPS',()=>TEMPS);g('PNAME',()=>PNAME);g('FA_SP',()=>FA_SP);g('FA_EVO',()=>FA_EVO);g('FA_PS',()=>Object.fromEntries(Object.entries(FA_PS).map(([k,v])=>[k,[v.n,v.d(1),v.d(5)]])));g('TI_PS',()=>Object.fromEntries(Object.entries(TI_PS).map(([k,v])=>[k,[v.n,v.d(1),v.d(5)]])));g('TI_UPD',()=>Object.fromEntries(Object.entries(TI_UPD).map(([k,v])=>[k,v(1)])));g('FA_UPD',()=>Object.fromEntries(Object.entries(FA_UPD).map(([k,v])=>[k,v(1)])));g('TI_EVO',()=>typeof TI_EVO!=='undefined'?TI_EVO:null);g('SHOP',()=>SHOP.map(s=>[s.name,s.eff(1)]));g('TIPS',()=>TIPS);g('BOSSES',()=>BOSSES.map(b=>b.n));g('PETS',()=>PETS.map(p=>p.n));g('INTEL',()=>INTEL);g('MON_V',()=>MON_V);g('PLACES',()=>PLACES);g('GT',()=>Object.fromEntries(Object.entries(GT).map(([k,v])=>[k,v.n])));g('FABAO',()=>FABAO);g('FBROAD',()=>FBROAD);g('TRAITS',()=>TRAITS);g('COACH',()=>COACH);g('MON_UP',()=>Object.fromEntries(Object.keys(MON_UP).map(k=>[k,MON_UP[k](4)])));g('FA_CTR',()=>FA_CTR);g('UPG',()=>typeof UPG!=='undefined'?UPG:null);g('XPETS',()=>XPETS.map(p=>p.n));g('BOSS_LORE',()=>BOSS_LORE);return o};\nconst $=",1)
open('/tmp/claude-0/pt/girldump.html','w').write('<!doctype html><meta charset=utf8><body style="height:100vh;margin:0">'+SRC)
async def main():
  async with async_playwright() as p:
    b=await p.chromium.launch(args=['--no-sandbox']);pg=await b.new_page(viewport={'width':390,'height':844})
    errs=[];pg.on('pageerror',lambda e:errs.append(str(e)))
    await pg.goto('http://127.0.0.1:8765/girldump.html');await pg.wait_for_timeout(800)
    d=await pg.evaluate("()=>JSON.stringify(window.__D(),(k,v)=>typeof v==='function'?undefined:v)")
    open('/tmp/claude-0/pt/girldump.json','w').write(d)
    html=await pg.evaluate("()=>document.body.innerText")
    open('/tmp/claude-0/pt/girl_dom.txt','w').write(html)
    print(errs[:3],len(d))
    await b.close()
asyncio.run(main())

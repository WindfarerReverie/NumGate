import asyncio,sys
from playwright.async_api import async_playwright
async def main():
  async with async_playwright() as p:
    b=await p.chromium.launch(args=['--no-sandbox'])
    pg=await b.new_page(viewport={'width':390,'height':844})
    errs=[];pg.on('pageerror',lambda e:errs.append(str(e)))
    await pg.goto('http://127.0.0.1:8765/'+sys.argv[1]);await pg.wait_for_timeout(1500)
    print(errs[:3], await pg.evaluate("()=>!!document.getElementById('new_1')"))
asyncio.run(main())

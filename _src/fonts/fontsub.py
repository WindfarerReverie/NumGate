# 自托管书法字体：按游戏里实际用到的字做子集，内嵌进 HTML（国内打不开 Google Fonts 也能显示）。字体均为 SIL OFL 开源授权。
import base64,re,subprocess,os
D='/home/claude/numgate'
M0,M1='/*BRUSHFONT*/','/*BRUSHFONT_END*/'
EXTRA='0123456789×+-%·：，。！？「」…—（）/ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz'
def face(ttf,text):
  open('/tmp/_fs.txt','w').write(text)
  subprocess.run(['pyftsubset',ttf,'--text-file=/tmp/_fs.txt','--flavor=woff2','--output-file=/tmp/_fs.woff2'],check=True)
  b=base64.b64encode(open('/tmp/_fs.woff2','rb').read()).decode()
  return M0+"@font-face{font-family:'NGBrush';src:url(data:font/woff2;base64,"+b+") format('woff2');font-display:swap}"+M1
def chars(t):t=re.sub(re.escape(M0)+'.*?'+re.escape(M1),'',t,flags=re.S);return ''.join(sorted(set(c for c in t if ord(c)>0x2e80)))+EXTRA
src=open(D+'/index.html').read()
blk=face(D+'/fonts/MaShanZheng-Regular.ttf',chars(src))
src=re.sub(re.escape(M0)+'.*?'+re.escape(M1),lambda m:blk,src,flags=re.S) if M0 in src else src.replace('<style>','<style>\n'+blk+'\n',1)
open(D+'/index.html','w').write(src)
subprocess.run(['python3',D+'/girl/build_girl.py','/tmp/_girl_probe.html'],check=True,capture_output=True)
g=open('/tmp/_girl_probe.html').read()
open(D+'/girl/font_girl.css','w').write(face(D+'/fonts/ZCOOLKuaiLe-Regular.ttf',chars(g)))
print('fonts ok',len(blk),os.path.getsize(D+'/girl/font_girl.css'))

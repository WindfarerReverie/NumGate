import json,re,sys,subprocess
out=subprocess.run(['python3','/tmp/claude-0/pt/mkcal.py']+sys.argv[1:],capture_output=True,text=True).stdout.splitlines()[0]
d=json.loads(out)
p='/home/claude/numgate/index.html';s=open(p,encoding='utf-8').read()
# smooth monotone: C,D,L,G,K non-decreasing
for k in 'CDKLG':
  a=d[k]
  for i in range(1,len(a)):a[i]=max(a[i],a[i-1])
blk='/*WCAL*/const WCAL='+json.dumps(d,separators=(',',':'))+';/*WCAL_END*/'
s2,n=re.subn(r'/\*WCAL\*/.*?/\*WCAL_END\*/',lambda m:blk,s,flags=re.S)
assert n==1
open(p,'w',encoding='utf-8').write(s2);print(blk[:300],'... pts',len(d['w']))

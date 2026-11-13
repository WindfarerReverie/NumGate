import sys,json
for f in sys.argv[1:]:
  rows=[json.loads(l[2:]) for l in open(f) if l.startswith('L ')]
  if not rows:print(f,'no data');continue
  out=[]
  for st in rows:
    i=st.index('CAL');t=st[0]
    if t%1800<60 or st is rows[-1]:out.append('%dm %s 最远第%d波 重修%d 最低血%s'%(t//60,st[1],st[i-1],st[i+10],st[st.index('minhp')+1]))
  print(f);[print('  ',x) for x in out]
  for l in open(f):
    if l.startswith('RUN') or 'errs' in l:print('  ',l.strip()[:150])

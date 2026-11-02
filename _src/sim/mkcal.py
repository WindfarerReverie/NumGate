import json,math,sys
REALMS=18
def lf(r):return math.log2(1.5+.5*max(1,r))
RSTART=[0,0];c=0
for r in range(1,REALMS):RSTART.append(c);c+=9*lf(r)
RSTART.append(c)
def realmOf(n):
  if n<100:return 0,0,n/100
  L=math.log2(n/100);r=1
  while r<REALMS-1 and L>=RSTART[r+1]:r+=1
  w=lf(r);into=L-RSTART[r];layer=min(9,int(into//w)+1);return r,layer,min(1,max(0,(into-(layer-1)*w)/w))
def layersOf(n):
  if n<100:return math.log2(max(1e-9,n)/100)
  r=realmOf(n)[0];return 9*(r-1)+(math.log2(n/100)-RSTART[r])/lf(r)
def load(f):
  rows=[]
  for line in open(f):
    if not line.startswith('L '):continue
    st=json.loads(line[2:]);i=st.index('CAL');Dref,M,yq,rw,cnt,coins,rR,maxR=st[i+1:i+9]
    t=st[0];w=max(0,(t-15)/60);r,lay,fr=realmOf(cnt);k=min(45,2.4*(max(1,maxR)-1)+2.4*(fr if r>=maxR else 0))
    rows.append(dict(w=w,C=math.log(Dref*M*yq*rw),D=math.log(Dref),K=k,L=layersOf(cnt),G=math.log(max(1,coins)),deaths=st[st.index('D')+1],realm=st[1]))
  return rows
runs=[load(f) for f in sys.argv[1:]]
n=min(len(r) for r in runs)
pts=[0,1,2,3,4,6,8,10,13,17,22,28,35,45,57,72,90,115,145,180,225,280,350,440,550]
mx=max(r[-1]['w'] for r in runs)
pts=[p for p in pts if p<=mx-2]+[round(mx-2)]
out={k:[] for k in 'wCDKLG'}
for p in pts:
  vals={k:[] for k in 'CDKLG'}
  for r in runs:
    if r[-1]['w']<p+2:continue
    win=[x for x in r if abs(x['w']-p)<=max(1,p*.12)]
    for k in vals:
      xs=sorted(x[k] for x in win);vals[k].append(xs[len(xs)//2])
  if not vals['C']:continue
  out['w'].append(p)
  for k in vals:out[k].append(round(sum(vals[k])/len(vals[k]),4))
print(json.dumps(out))
for i,p in enumerate(out['w']):
  print(p,'C',round(math.exp(out['C'][i]),1),'D',round(math.exp(out['D'][i]),1),'press',round(math.exp(out['C'][i]-out['D'][i]),2),'K',out['K'][i],'L',out['L'][i],'G',round(math.exp(out['G'][i])))
for r,f in zip(runs,sys.argv[1:]):print(f,'end w',round(r[-1]['w']),r[-1]['realm'],'deaths',r[-1]['deaths'])

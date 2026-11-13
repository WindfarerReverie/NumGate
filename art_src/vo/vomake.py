import wave,numpy as np,subprocess,json,os
exec(open('/tmp/claude-0/pt/vocut.py').read().split('for f in sys.argv')[0])
D='/tmp/claude-0/pt/vo2'
KEYS=['bomb','bolt','bolt2','shield','freeze','fire','fire2','ice','ice2','sword','sword2']
WS={'m_b':[0,3.88,7.66,12.50,15.64,19.18,22.22,26.24,29.18,32.10,35.28],
    'g_b':[0,1.66,3.54,6.32,9.00,10.76,12.86,14.74,16.96,18.74,20.16]}
def rawiv(f,th=-38):
    db,dur=env(f);pk=np.percentile(db,99);on=db>pk+th;iv=[];i=0
    while i<len(on):
        if on[i]:
            j=i
            while j<len(on) and on[j]:j+=1
            if j-i>4: iv.append([i*.01,j*.01])
            i=j
        else:i+=1
    return iv
def cuts(name):
    f=f'{D}/{name}.wav'
    if name in WS:
        ws=WS[name];iv=rawiv(f);g=[[] for _ in ws]
        for a,b in iv:
            k=max(i for i,t in enumerate(ws) if t<=a+0.7);g[k].append([a,b])
        return [[x[0][0],x[-1][1]] for x in g]
    return segs(f)[0]
def load(mp3):
    a=subprocess.run(['ffmpeg','-v','error','-i',mp3,'-ac','1','-ar','44100','-f','s16le','-'],capture_output=True).stdout
    return np.frombuffer(a,dtype=np.int16).astype(float)/32768
out={}
for name,pre in [('m_a','vo_'),('g_a','g_vo_'),('m_b','bk_vo_'),('g_b','bk_g_vo_')]:
    cs=cuts(name);a=load(f'{D}/{name}.mp3');sr=44100;assert len(cs)==11,(name,len(cs))
    out[name]=[[round(x,2),round(y,2),round(y-x,2)] for x,y in cs]
    for k,(s,e) in zip(KEYS,cs):
        x=a[int(max(0,s-.06)*sr):int(min(len(a)/sr,e+.18)*sr)].copy()
        fo=int(.1*sr);x[-fo:]*=np.linspace(1,0,fo);fi=int(.01*sr);x[:fi]*=np.linspace(0,1,fi)
        # RMS on voiced frames -> target -17 dBFS, cap peak -1 dB
        fr=x[:len(x)//441*441].reshape(-1,441);r=np.sqrt((fr**2).mean(1));v=r[r>r.max()*.1]
        g=10**(-17/20)/np.sqrt((v**2).mean());g=min(g,10**(-1/20)/np.abs(x).max());x*=g
        p=f'{D}/out/{pre}{k}.mp3';os.makedirs(f'{D}/out',exist_ok=True)
        subprocess.run(['ffmpeg','-v','error','-y','-f','s16le','-ar','44100','-ac','1','-i','-','-b:a','64k',p],input=(x*32767).astype(np.int16).tobytes())
print(json.dumps(out,ensure_ascii=False,indent=0))

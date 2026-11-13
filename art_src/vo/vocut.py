import wave,numpy as np,sys,json
def env(f):
    w=wave.open(f);a=np.frombuffer(w.readframes(w.getnframes()),dtype=np.int16).astype(float)/32768
    hop=160;n=len(a)//hop;r=np.sqrt((a[:n*hop].reshape(n,hop)**2).mean(1)+1e-12);return 20*np.log10(r),len(a)/16000
def segs(f,th=-38,N=11):
    db,dur=env(f);pk=np.percentile(db,99);on=db>pk+th
    iv=[];i=0
    while i<len(on):
        if on[i]:
            j=i
            while j<len(on) and on[j]:j+=1
            iv.append([i*.01,j*.01]);i=j
        else:i+=1
    iv=[v for v in iv if v[1]-v[0]>0.04]
    while len(iv)>N:
        g=[iv[k+1][0]-iv[k][1] for k in range(len(iv)-1)];k=int(np.argmin(g))
        iv[k]=[iv[k][0],iv[k+1][1]];del iv[k+1]
    gaps=[round(iv[k+1][0]-iv[k][1],2) for k in range(len(iv)-1)]
    return iv,gaps,dur
for f in sys.argv[1:]:
    iv,g,d=segs(f)
    print(f,len(iv),"min inter-gap",min(g));print("  ",[[round(a,2),round(b,2)] for a,b in iv]);print("   gaps",g)

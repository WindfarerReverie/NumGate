import sys
from PIL import Image
import numpy as np
from scipy import ndimage
NAMES=['tap','drag','lr','up','num','right','nocross','hourglass','target','refresh','break','scroll']
src,pre=sys.argv[1],sys.argv[2]   # pre: VI or GVI
im=Image.open(src).convert('RGBA');a=np.array(im)[:,:,3]
H,W=a.shape;mask=a>30
lab,n=ndimage.label(ndimage.binary_dilation(mask,iterations=6))
objs=ndimage.find_objects(lab)
cells={}
for i,sl in enumerate(objs):
  ys,xs=sl;area=(lab[sl]==i+1).sum()
  if area<400:continue
  cy=(ys.start+ys.stop)/2;cx=(xs.start+xs.stop)/2
  c=min(3,int(cx/(W/4)));r=min(2,int(cy/(H/3)))
  cells.setdefault(r*4+c,[]).append(sl)
out=[]
for idx in range(12):
  if idx not in cells:print('MISSING',idx,NAMES[idx]);continue
  y0=min(s[0].start for s in cells[idx]);y1=max(s[0].stop for s in cells[idx]);x0=min(s[1].start for s in cells[idx]);x1=max(s[1].stop for s in cells[idx])
  crop=im.crop((max(0,x0-4),max(0,y0-4),min(W,x1+4),min(H,y1+4)))
  fn='/mnt/user-data/uploads/Downloads/numgate_%s_%s.png'%(pre,NAMES[idx]);crop.save(fn);out.append((NAMES[idx],crop.size))
print(out)

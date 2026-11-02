import sys,json
for f in sys.argv[1:]:
  rows=[json.loads(l[2:]) for l in open(f) if l.startswith('L ')]
  print('==',f)
  for s in rows:
    if s[0]%900<60 or s is rows[-1]:
      i=s.index('CAL');g=lambda k:s[s.index(k)+1]
      print(' %3dm %-6s 波%-3s 血%s 最低%s 割草压%s 妖潮压%s 倒%s | %s'%(s[0]//60,s[1],s[i-1],g('hp'),g('minhp'),g('mow'),g('surge'),g('D'),g('sh')))

import os
ls=0
screen=[]
while 1:
 nls=int(os.popen('ls -l key.a').read().split()[4])
 z=open('key.a')
 z.read(ls)
 fs+=z.read(nls-ls)
 z.close()
 ls=nls

 for w in screen:
  print('\x1b['+str(w[0])+','+str(w[1])+'H\x1b'+','.join(w[2:])+'m\u2580\x1b[0m')

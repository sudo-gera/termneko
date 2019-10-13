from time import time,sleep
from sys import argv
from os import get_terminal_size as gt,system as sh
def enable(q):
 a=open(q)
 map1=a.read()
 a.close()
 map1=map1.split('\n')
 map1=[list(w) for w in map1]
 return map1
def place(x,y,q,nmap):
 for w in range(len(q)):
  for e in range(len(q[w])):
   maps[nmap][x+w][y+e]=q[w][e]
def entity(x,y,e=0):
  global emap
  if y%2:
   emap[y//2][x]='▄'
  else:
   emap[y//2][x]='▀'
def button():
 a=open('key.a')
 global ls
 a.read(ls)
 fs=a.read()
 ls+=len(fs)
 a.close()
 return fs
def draw():
 global wx,wy,px,pyy,emap
 wy=min(wy,py//2-4)
 wx=min(wx,px-8)
 wy=max(wy,py//2-gt()[1]+4)
 wx=max(wx,px-gt()[0]+8)
 tmp=emap[:]
 tmp=tmp[max(wy,0):max(wy+gt()[1],0)]
 tmp=[w[max(wx,0):max(wx+gt()[0],0)] for w in tmp]
 tmp=[''.join(w) for w in tmp]
 tmp=['\x1b['+str(1+w+max(0,-wy))+';'+str(max(0,-wx))+'H'+tmp[w] for w in range(len(tmp))]
 tmp=''.join(tmp)
 pr=tmp
 print(pr,end='\x1b[0;0H')
def free(x,y,p):
 global maps
 try:
  return maps[p][y//2][x]in' │'
 except:
  return 0
print('\n'*(gt()[1]-1),end='')
ls=0
maps=[enable('1.map'),enable('2.map')]
table=enable('table.map')
showcase=enable('showcase.map')
place(21,50,showcase,0)
for w in list(range(3))+list(range(4,8)):
 for e in range(3):
  place(5+w*8,5+e*16,table,0)
pmap=0
px=55
py=55
wx=0
wy=0
but=''
up=1
ti=time()
wi=0
inf=dict()
while 1:
 ww=''
 but+=button()
 if but:
  ww=but[0]
  but=but[1:]
 if ww == 'p':
  print('\x1b[0;0H',end='')
  print(' '*gt()[0]*gt()[1],end='')
  print('\x1b[0;0H',end='')
  exit()
 if ww == 'i':
  wi=1-wi
  print('\x1b[0;0H'+' '*gt()[0]*gt()[1]+'\x1b[0;0H',end='')
 if wi:
  pass
 else:
  if ww == 'd':
   if free(px+1,py,pmap):
    px+=1
  if ww == 'w':
   if free(px,py-1,pmap):
    py-=1
  if ww == 'a':
   if free(px-1,py,pmap):
    px-=1
  if ww == 's':
   if free(px,py+1,pmap):
    py+=1
  if px>66 and py>119:
   if up:
    pmap=1-pmap
    up=0
  else:
   up=1
  emap=[w[:] for w in maps[pmap]]
  entity(px,py)
  if time()>ti+0.03:
   draw()
   ti=time()

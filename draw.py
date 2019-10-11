import os
ls=0
def enable(q):
 a=open(q)
 map1=a.read()
 a.close()
 map1=map1.split('\n')
 map1=[list(w) for w in map1]
 return map1
maps=[enable('1.map'),enable('2.map')]
def place(x,y,q,nmap):
 global maps
 for w in range(len(q)):
  for e in range(len(q[w])):
   maps[nmap][x+w][y+e]=q[w][e]
table=enable('table')
for w in range(5):
 for e in range(2):
  place(10+w*15,10+e*15,table,0)
def button():
 nls=int(os.popen('ls -l key.a').read().split()[4])
 a=open('key.a')
 global ls
 a.read(ls)
 fs=a.read(nls-ls)
 a.close()
 ls=nls
 return fs
pmap=0
px=5
py=5
while 1:
 but=button()
 

a=open('2.map','w')
for w in range(9608//256*256,(9608+256)//256*256):
 print(w,chr(w))
a.write(chr(9556)+chr(9552)*64+chr(9574)+chr(9552)*64+chr(9559)+'\n')
for w in range(28):
 a.write(chr(9553)+' '*64+chr(9553)+' '*64+chr(9553)+'\n')
for w in range(4):
 a.write(chr(9553)+' '*64+' '+' '*64+chr(9553)+'\n')
a.write(chr(9568)+chr(9552)*64+chr(9571)+' '*64+chr(9553)+'\n')
for w in range(4):
 a.write(chr(9553)+' '*64+' '+' '*64+chr(9553)+'\n')
for w in range(20):
 a.write(chr(9553)+' '*64+chr(9553)+' '*64+chr(9553)+'\n')
a.write(chr(9553)+' '*64+chr(9568)+' '*8+chr(9552)*56+chr(9571)+'\n')
for w in range(7):
 a.write(chr(9553)+' '*64+chr(9553)+' '*64+chr(9553)+'\n')
a.write(chr(9562)+chr(9552)*64+chr(9577)+chr(9552)*64+chr(9565)+'\n')
a.close()
a=open('1.map','w')
a.write(chr(9556)+chr(9552)*64+chr(9574)+chr(9552)*64+chr(9559)+'\n')
for w in range(23):
 a.write(chr(9553)+' '*64+chr(9553)+' '*64+chr(9553)+'\n')
for w in range(4):
 a.write(chr(9553)+' '*64+' '+' '*64+chr(9553)+'\n')
for w in range(30):
 a.write(chr(9553)+' '*64+chr(9553)+' '*64+chr(9553)+'\n')
a.write(chr(9553)+' '*64+chr(9568)+' '*8+chr(9552)*56+chr(9571)+'\n')
for w in range(7):
 a.write(chr(9553)+' '*64+chr(9553)+' '*64+chr(9553)+'\n')
a.write(chr(9562)+chr(9552)*64+chr(9577)+chr(9552)*64+chr(9565)+'\n')
a.close()

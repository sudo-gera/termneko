for w in range((9608//256-6)*256,(9608//256-1)*256):
 print(chr(w)+str(w))
a=open('2.map','w')
a.write(' '*133+'\n')
a.write(' '*133+'\n')
a.write('  '+chr(9556)+chr(9552)*64+chr(9574)+chr(9552)*64+chr(9559)+'  \n')
for w in range(28):
 a.write('  '+chr(9553)+' '*64+chr(9553)+' '*64+chr(9553)+'  \n')
for w in range(4):
 a.write('  '+chr(9553)+' '*64+' '+' '*64+chr(9553)+'  \n')
a.write('  '+chr(9568)+chr(9552)*64+chr(9571)+' '*64+chr(9553)+'  \n')
for w in range(4):
 a.write('  '+chr(9553)+' '*64+' '+' '*64+chr(9553)+'  \n')
for w in range(20):
 a.write('  '+chr(9553)+' '*64+chr(9553)+' '*64+chr(9553)+'  \n')
a.write('  '+chr(9553)+' '*64+chr(9568)+chr(9552)*56+' '*8+chr(9571)+'  \n')
a.write('  '+chr(9553)+' '*64+chr(9553)+' '*64+chr(9553)+'  \n')
for w in range(5):
 a.write('  '+chr(9553)+' '*64+chr(9553)+' '+chr(9474)*62+' '+chr(9553)+'  \n')
a.write('  '+chr(9553)+' '*64+chr(9553)+' '*64+chr(9553)+'  \n')
a.write('  '+chr(9562)+chr(9552)*64+chr(9577)+chr(9552)*64+chr(9565)+'  \n')
a.write(' '*133+'\n')
a.close()
a=open('1.map','w')
a.write(' '*133+'\n')
a.write('  '+chr(9556)+chr(9552)*64+chr(9574)+chr(9552)*64+chr(9559)+'  \n')
for w in range(26):
 a.write('  '+chr(9553)+' '*64+chr(9553)+' '*64+chr(9553)+'  \n')
for w in range(5):
 a.write('  '+chr(8200)+' '*64+' '+' '*64+chr(9553)+'  \n')
for w in range(26):
 a.write('  '+chr(9553)+' '*64+chr(9553)+' '*64+chr(9553)+'  \n')
a.write('  '+chr(9553)+' '*64+chr(9568)+' '*0+chr(9552)*64+chr(9571)+'  \n')
a.write('  '+chr(9553)+' '*64+chr(9553)+' '*64+chr(9553)+'  \n')
for w in range(1):
 a.write('  '+chr(9553)+' '*64+chr(9553)+' '+chr(9474)*62+' '+chr(9553)+'  \n')
for w in range(3):
 a.write('  '+chr(9553)+' '*64+'  '+chr(9474)*62+' '+chr(9553)+'  \n')
for w in range(1):
 a.write('  '+chr(9553)+' '*64+chr(9553)+' '+chr(9474)*62+' '+chr(9553)+'  \n')
a.write('  '+chr(9553)+' '*64+chr(9553)+' '*64+chr(9553)+'  \n')
a.write('  '+chr(9562)+chr(9552)*64+chr(9577)+chr(9552)*64+chr(9565)+'  \n')
a.write(' '*133+'\n')
a.write(' '*133+'\n')
a.close()

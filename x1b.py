for w in range(30,40):
# print('\x1b['+str(w   )+'m#',end='')
 print('\x1b[0m',end='')
 print('\x1b['+str(w+10)+'m#',end='')
 print('\x1b[0m',end='')
# print('\x1b['+str(w+60)+'m#',end='')
 print('\x1b[0m',end='')
 print('\x1b['+str(w+70)+'m#',end='')
 print('\x1b[0m')

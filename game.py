import time,sys,tty,termios,os,sys

chd=sys.argv[0]
chd=chd.split('/')[:-1]
chd='/'.join(chd)
if chd=='':
 chd='.'
os.chdir(chd)
os.system('python3 draw.py &')
os.system('> key.a')
while 1:
	fd = sys.stdin.fileno()
	old_settings = termios.tcgetattr(fd)
	try:
	 tty.setraw(sys.stdin.fileno())
	 ch = sys.stdin.read(1)
	finally:
	 termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
	k=ch
	a=open('key.a','a')
	a.write(k)
	a.close()
	if k == 'p':
	 time.sleep(0.1)
	 exit()


from pwn import *


def recv(r):
	s = r.recvrepeat(1)
	print s
	
r = remote('54.175.183.202',12012)

recv(r)
r.send('user blankwall\n')
recv(r)
r.send('pass ' + '9aaaa[dbSx\x1b')
recv(r)
r.send('rdf\n')
recv(r)
r.interactive()

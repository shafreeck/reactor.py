#coding:utf8
import reactor
import time
def readmsg(net):
	time.sleep(1)
	print net.socket
	data = net.read(1024)
	if data == 'quit\r\n':
		net.close()
		return
	if data == 'pong\r\n':
		net.addreply('ping\r\n')
		print 'ping'
		print data,
if __name__ == '__main__':
	for i in xrange(5):
		r = reactor.Reactor()
		print 'created:',r.socket
		r.register_read_event(readmsg)
		r.connect('localhost',8804)
		r.addreply('ping\r\n')
	reactor.eventloop()

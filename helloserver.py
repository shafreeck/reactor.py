#coding:utf8
import reactor

def HelloServer(net):
	s = net.read(1024)
	net.addreply("Content-type: text/html\r\n\r\n")
	net.addreply("hello, world!\r\n")

def writeHandler(net):
	net.sendreply()
	net.close()


if __name__ == '__main__':
	r = reactor.Reactor()
	r.register_read_event(HelloServer)
	r.register_write_event(writeHandler)
	r.listenon('',8804)
	reactor.eventloop()

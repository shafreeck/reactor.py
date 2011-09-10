import reactor
def readmsg(net):
	data = net.read(1024)
	if data == 'quit\r\n':
		net.close()
		return
	if data == 'ping\r\n':
		net.addreply('pong\r\n')

if __name__ == '__main__':
	netevent = reactor.Reactor()
	netevent.register_read_event(readmsg)
	netevent.listenon('',8804)
	reactor.eventloop()


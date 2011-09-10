import reactor
def readmsg(net):
	data = net.read(1024)
	if data == 'quit\r\n':
		net.close()
		return
	net.addreply(data)

if __name__ == '__main__':
	netevent = reactor.Reactor('',8804)
	netevent.register_read_event(readmsg)
	netevent.eventloop()


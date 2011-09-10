#coding:utf8
'''
author:shafreeck
date:20110910
license:nothing,you can use it for free
'''
import asyncore,socket

class Reactor(asyncore.dispatcher):
	def __init__(self,host,port):
		asyncore.dispatcher.__init__(self)
		self.create_socket(socket.AF_INET, socket.SOCK_STREAM)
		self.set_reuse_addr()
		self.bind((host,port))
		self.listen(5)

		self.__rcallback = None
		self.__wcallback = None
		self.__tcallback = None
		self.__handler = None
	
	def handle_accept(self):
		pair = self.accept()
		if pair is None:
			pass #FIXME: handle this ,raise exception	
		else:
			sock,addr = pair
			self.__handler = IOdispatcher(sock)
			self.__handler.setrcallback(self.__rcallback)
			self.__handler.setwcallback(self.__wcallback)
		#	self.__handler.__tcallback = self.__tcallback

	
	def register_read_event(self,rcallback):
		self.__rcallback = rcallback
	def register_write_event(self,wcallback):
		self.__wcallback = wcallback
	def register_time_event(self,tcallback):
		self.__tcallback = tcallback
	def eventloop(self,timeout=30):
		asyncore.loop(timeout)

class IOdispatcher(asyncore.dispatcher_with_send):
	def __init__(self,sock):
		asyncore.dispatcher_with_send.__init__(self,sock)
		self.__rcallback = None
		self.__wcallback = None
		
	def read(self,num):
		return self.recv(num)
	def write(self,data):
		return self.send(data)

	def handle_read(self):
		if self.__rcallback:
			self.__rcallback(self)
	def handle_write(self):
		if self.__wcallback:
			self.__wcallback()
	def addreply(self,msg):
		self.send(msg)
	def setrcallback(self,call):
		self.__rcallback = call
	def setwcallback(self,call):
		self.__wcallback = call


'''
callback function format:
def readcallback(IOdispatcher)
def writecallback(IOdispatcher)
'''

__author__ = 'xzz'

from spyne import Application,rpc,ServiceBase,Iterable,Integer,Unicode
from spyne.protocol.soap import Soap11
from spyne.server.wsgi  import WsgiApplication

import logging
from wsgiref.simple_server import make_server

class HellWordService(ServiceBase):
	@rpc(Unicode,Integer,_returns=Iterable(Unicode))
	def say_hello(ctx,name,times):
		for i in range(times):
			yield u'Hello,%s'%name

application = Application([HellWordService],'spyne,examples.hello.soap',
							in_protocol=Soap11(validator='lxml'),
							out_protocol=Soap11())

wsgi_application = WsgiApplication(application)

if __name__ == '__main__':
	logging.basicConfig(level = logging.DEBUG)
	logging.getLogger('spyne.protocal.xml').setLevel(logging.DEBUG)

	logging.info("listening to http://172.16.41.202:8000")
	logging.info("wsdl is at:http://172.16.41.202:8000/?wsdl")

	server = make_server("172.16.41.202",8000,wsgi_application)
	server.serve_forever()

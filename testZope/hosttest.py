#encoding = utf-8
#coding = utf-8
from zope.interface import Interface
from zope.interface import implementer


class IHost(Interface):
	def goodmorning(self,guest):
		pass

		
class  Host(object):
	implementer(IHost)
	def goodmorning(self,guest):
		return ("Good morning,%s!" % guest)

if __name__ == '__main__':
	h = Host()
	hi = h.goodmorning('zhangsan')
	print (hi)


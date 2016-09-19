__author__ = 'xzz'

from suds.client import Client

url = "http://172.16.41.202:8000/?wsdl"
client = Client(url)

result = client.service.say_hello("xzz",3)
print(result)
__author__ = 'xzz'

from suds.client import Client
from suds.xsd.doctor import ImportDoctor,Import


#使用库  suds_jurko:https://bitbucket.org/jurko/suds
#web service 查询:http://www.webxml.com.cn/zh_cn/web_services.aspx

url = "http://www.webxml.com.cn/WebServices/WeatherWebService.asmx?wsdl"

imp = Import('http://www.w3.org/2001/XMLSchema',location='http://www.w3.org/2001/XMLSchema.xsd')
imp.filter.add('http://WebXml.com.cn/')
client = Client(url,plugins=[ImportDoctor(imp)])
result = client.service.getWeatherbyCityName('海口')

print(result)
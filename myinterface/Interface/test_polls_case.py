__author__='xzz'

import unittest
import requests
import os,sys
parentdir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

print ("test_polls_case: ",parentdir)
# parentdir = os.path.dirname((os.path.abspath("__file__"))
sys.path.insert(0,parentdir)
from db_fixture import test_polls_data
import myunit

class Test(myunit.MyTest):
	@classmethod
	def setUpClass(cls):
		test_polls_data.init_data()
	def test_get_all_polls(self):
		'''获取所有投票问题'''
		r = requests.get(self.base_url)
		self.code = r.status_code
		self.text = r.text
		self.assertEqual(self.code,200)
		self.assertIn("you buy pro6?",self.text)
	def test_get_polls_question(self):
		'''获取所有问题1的所有选项'''
		r = requests.get(self.base_url+'/1/')
		self.code= r.status_code
		self.text = r.text
		self.assertEqual(self.code,200)
		self.assertIn("buy",self.text)
		self.assertIn("not buy",self.text)

if __name__ == '__main__':
	unittest.main()		


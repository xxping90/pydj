__author__='xzz'

import unittest

#setting interface url
class MyTest(unittest.TestCase):
	def setUp(self):
		self.base_url = 'http://127.0.0.1:8000/polls'
	def tearDown(self):
		print(self.code,self.text)
		
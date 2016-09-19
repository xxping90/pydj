#coding = utf-8
#encoding = utf-8
import requests
import unittest
import json

# base_url = 'http://127.0.0.1:8000/polls'
# r = requests.get(base_url)
# code = r.status_code
# text = r.text
# print(code)
# print(text)

class PollsTest(unittest.TestCase):
	def setUp(self):
		self.base_url = 'http://127.0.0.1:8000/polls'

	def tearDown(self):
		pass

	def test_get_poll_index(self):
		'''测试投票系统首页'''
		r = requests.get(self.base_url)
		code = r.status_code
		text = r.text
		dicts = json.loads(text)
		self.assertEqual(code,200)
		self.assertEqual(dicts['message'],'success')
	def test_get_poll_question(self):
		'''获得问题一的所有选项'''
		r = requests.get(self.base_url+'/1/')
		code = r.status_code
		text = r.text
		dicts = json.loads(text)
		self.assertEqual(code,200)
		self.assertEqual(dicts['message'],'success')
	def test_get_poll_result(self):
		"""获取问题1的投票结果"""
		r = requests.get(self.base_url+'/2/results')
		code = r.status_code
		text = r.text
		dicts = json.loads(text)
		self.assertEqual(code,200)
		self.assertEqual(dicts['message'],'success')
	def test_post_poll_vote(self):
		'''对第一个问题的第2个选项投票'''
		r = requests.post(self.base_url+'/1/vote/',data={'choice':'2'})
		code = r.status_code
		text = r.text
		print(text)
		dicts = json.loads(text)
		self.assertEqual(code,200)
		self.assertEqual(dicts['message'],'success')

if __name__=="__main__":
	unittest.main()





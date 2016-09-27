from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from django.test import LiveServerTestCase
import unittest

class NewVistorTest(LiveServerTestCase):
	def setUp(self):
		self.browser = webdriver.Chrome()
		self.browser.implicitly_wait(3)
	def tearDown(self):
		self.browser.quit()
	def check_for_row_in_list_table(self,row_text):
		table = self.browser.find_element_by_id('id_list_table')
		rows = table.find_elements_by_tag_name("tr")
		self.assertIn(row_text,[row.text for row in rows])

	def test_can_start_a_list_and_rerieve_it_later(self):
		self.browser.get(self.live_server_url)

		self.assertIn('To-Do',self.browser.title)
		header_text = self.browser.find_element_by_tag_name('h1').text
		self.assertIn('To-Do',header_text)

		#应用邀请她输入一个待办事项
		inputbox = self.browser.find_element_by_id('id_new_item')
		self.assertEqual(
			inputbox.get_attribute('placeholder'),
			'Enter a to-do item'
			)
		inputbox.send_keys('Buy peacock feathers')
		inputbox.send_keys(Keys.ENTER)
		edith_list_url = self.browser.current_url

		self.assertRegex(edith_list_url,'/lists/.+')

		self.check_for_row_in_list_table('1:Buy peacock feathers')

		inputbox = self.browser.find_element_by_id('id_new_item')
		inputbox.send_keys('Use peacock feathers to make a fly')
		inputbox.send_keys(Keys.ENTER)

		self.check_for_row_in_list_table('1:Buy peacock feathers')
		self.check_for_row_in_list_table('2:Use peacock feathers to make a fly')

		# table = self.browser.find_element_by_id('id_list_table')
		# rows = table.find_elements_by_tag_name('tr')
		# self.assertIn('1:Buy peacock feathers',[row.text for row in rows])
		# self.fail('finish the test!')
		##使用新浏览器会话
		##确保伊迪丝的信息不回从cookie泄露出来
		self.browser.quit()
		self.browser = webdriver.Firefox()

		# 弗朗西斯访问首页，页面中将看不到伊迪丝的清单
		self.browser.get(self.live_server_url)
		page_text = self.browser.find_element_by_tag_name('body').text
		self.assertNotIn('Buy peacock feathers',page_text)
		self.assertNotIn('make a fly',page_text)

		#弗朗西斯输入一个新的待办事项，新建一个清单
		#他不像伊迪丝那样兴趣盎然
		inputbox = self.browser.find_element_by_id('id_new_item')
		inputbox.send_keys('Buy milk')
		inputbox.send_keys(Keys.ENTER)


		francis_list_url = self.browser.current_url
		self.assertRegex(francis_list_url,'/lists/.+')
		self.assertNotEqual(francis_list_url,edith_list_url)

		page_text = self.browser.find_element_by_tag_name('body').text
		self.assertNotIn('Buy peacock feathers',page_text)
		self.assertIn('Buy milk',page_text)


# if __name__=='__main__':
# 	unittest.main()
from django.test import TestCase
from blog.models import Author

# Create your tests here.

class AuthorTestCase(TestCase):
	"""docstring for AuthorTestCase"""
	def setUp(self):
		Author.objects.create(first_name="zhang",last_name='san',email="zhangsan@gmail.com")
		Author.objects.create(first_name="li",last_name='si',email="lisi@gmail.com")
	def test_add_author_email(self):
		""" test add author email"""
		zhang = Author.objects.get(first_name="zhang")
		li = Author.objects.get(first_name="li")
		self.assertEqual(zhang.email,"zhangsan@gmail.com")
		self.assertEqual(li.email,"lisi@gmail.com")
	def test_add_author_lastname(self):
		""" test add author last_name"""
		zhang = Author.objects.get(first_name="zhang")
		li = Author.objects.get(first_name="li")
		self.assertEqual(zhang.last_name,"san")
		self.assertEqual(li.last_name,"si")	

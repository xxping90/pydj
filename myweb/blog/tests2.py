from django.test import TestCase
from blog.models import Publisher

#Create your tests here.
class  PublisherTestCase(TestCase):
	def setUp(self):
		Publisher.objects.create(name="zhongxin",
								address='Xinyuan South Road,Chaoyang District,Beijing on the 6th',
								city='beijing',
								state_province='China',
								country='beijing',
								website='https://www.baidu.com/index.php?tn=monline_3_dg')
	def test_add_publisher_city(self):
		zhongxin = Publisher.objects.get(name="zhongxin")
		self.assertEqual(zhongxin.city,"beijing")

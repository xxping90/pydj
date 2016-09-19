__author__ = 'xzz'

import time,sys,os
sys.path.append('./Interface')
sys.path.append('./db_fixture')
import unittest
from HTMLTestRunner import HTMLTestRunner

#指定测试用例为当前文件夹下的interface目录
# test_dir = './Interface'
test_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), "Interface")
print (test_dir)
discover = unittest.defaultTestLoader.discover(test_dir,pattern='test_*.py',top_level_dir=None)

if __name__ == "__main__":
	testreport = os.path.join(os.path.dirname(os.path.abspath(__file__)), "report\\")
	now=time.strftime("%Y-%m-%d %H_%M_%S")
	filename = testreport + now + 'result.html'
	print (filename)
	fp = open(filename,'wb')
	runner = HTMLTestRunner(stream = fp,
							title='Polls System Interface Test Report',
							description='Implementation Example with:')
	runner.run(discover)
	fp.close()
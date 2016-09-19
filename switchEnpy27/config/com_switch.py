#coding=utf-8
#encoding=utf-8

__author__='xzz'

import os

def comSwitch(com_dir,num):


#测试环境切换
	if num == 1:
		with open(com_dir,"r") as f:
			d = f.read()
			d=d.replace("phpapi.99ducaijing.cn","testphp.99ducaijing.cn")
			f.close()
			print("test_com_environment_success")
		f = open(com_dir,"w")
		f.write(d)
		f.close()

#正式环境切换
	else:
		with open(com_dir,"r") as f:
			d = f.read()
			d=d.replace("testphp.99ducaijing.cn","phpapi.99ducaijing.cn")
			f.close()
			print("production_com__environment_success")
		f = open(com_dir,"w")
		f.write(d)
		f.close()

if __name__=="__main__":
	# parentdir = u"E:\\版本测试\\v1.4测试"
	parentdir = u"D:\\ProgramFiles\\99乐投"
	add_parentdir=parentdir+"\\Html\\js\\"
	com = "common.js"
	# oiparentdir =u
	com_dir = os.path.join(add_parentdir,com)
	print ("local.local_dir: ",com_dir)

	# comSwitch(com_dir,1)
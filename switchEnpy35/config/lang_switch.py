#coding=utf-8
#encoding=utf-8

__author__='xzz'

import os

def langSwitch(lang_dir,num):


#测试环境切换
	if num == 1:
		with open(lang_dir,"r",encoding="utf-16",errors="ignore") as f:
			d = f.read()
			d=d.replace("testlbs=false","testlbs=true")
			d=d.replace("phpapi.99ducaijing.cn","testphp.99ducaijing.cn")
			d=d.replace("www.99ducaijing.com","testphp.99ducaijing.cn")
			f.close()
			print("test_lang_environment_success")
		f = open(lang_dir,"w",encoding="utf-16")
		f.write(d)
		f.close()

#正式环境切换
	else:
		with open(lang_dir,"r",encoding="utf-16",errors="ignore") as f:
			d = f.read()
			d=d.replace("testlbs=true","testlbs=false")
			d=d.replace("testphp.99ducaijing.cn","phpapi.99ducaijing.cn")
			d=d.replace("testphp.99ducaijing.cn","www.99ducaijing.com")
			f.close()
			print("production_lang__environment_success")
		f = open(lang_dir,"w",encoding="utf-16")
		f.write(d)
		f.close()

if __name__=="__main__":
	parentdir = u"E:\\版本测试\\v1.4测试"
	lang = "languageCH.ini"
	# oiparentdir =u
	lang_dir = os.path.join(parentdir,lang)
	print ("local.local_dir: ",lang_dir)

	# langSwitch(lang_dir,2)
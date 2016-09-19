#coding=utf-8
#encoding=utf-8

__author__='xzz'

import os,sys,time
# from config import com_switch.comSwitch,lang_switch.langswitch,local_Switch.localSwitch
from config import com_switch,lang_switch,local_switch



if __name__=="__main__":
	# parentdir = u"E:\\版本测试\\v1.4测试"
	print("#############python3.5运行环境###############")
	parentdir = u"D:\\ProgramFiles\\99乐投"
	add_parentdir=parentdir+"\\Html\\js\\"
	local = "local.config"
	lang = "languageCH.ini"
	com = "common.js"

	

	local_dir = os.path.join(parentdir,local)
	lang_dir = os.path.join(parentdir,lang)
	com_dir = os.path.join(add_parentdir,com)

	print ("local.local_dir: ",local_dir)
	print ("local.local_dir: ",lang_dir)
	print ("local.local_dir: ",com_dir)

#state=2为测试环境
	state=2
	if os.path.exists(parentdir) == False:
		print ("安装目录不存在！请检查switch.py中变量parentdir之后再执行！！！")
	else:
		local_switch.localSwitch(local_dir,state)
		lang_switch.langSwitch(lang_dir,state)
		com_switch.comSwitch(com_dir,state)
		print ("切换到正式环境！")
	time.sleep(5)

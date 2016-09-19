#coding=utf-8
#encoding=utf-8

__author__='xzz'

import os

def localSwitch(local_dir,num):
	f = open(local_dir,"r",encoding="utf-8")
	lines = f.readlines()
	flen=len(lines)
	for i in range(flen):
		if lines[i].find("loginip=login") >=0  or lines[i].find("lobbyip=lobbyip") >=0 or \
		lines[i].find("lbsip=lbs") >=0 or lines[i].find("lbsip=testlbs") >=0:
			lines[i]=lines[i].replace("#","")
		else:
			pass
	f.close()
	f = open(local_dir,"w",encoding="utf-8")
	f.writelines(lines)
	f.close()
#测试环境切换
	if num == 1:
		with open(local_dir,"r",encoding="utf-8") as f:
			d = f.read()
			d=d.replace("loginip=login","#loginip=login")
			d=d.replace("lobbyip=lobbyip","#lobbyip=lobbyip")
			d=d.replace("lbsip=lbs","#lbsip=lbs")
			d=d.replace("phpapi.99ducaijing.cn","testphp.99ducaijing.cn")
			d=d.replace("www.99ducaijing.com","testphp.99ducaijing.cn")
			print("test_local_environment_success")
		f.close()
		f = open(local_dir,"w",encoding="utf-8")
		f.write(d)
		f.close()

#正式环境切换
	else:
		with open(local_dir,"r",encoding="utf-8") as f:
			d = f.read()
			d=d.replace("lbsip=testlbs","#lbsip=testlbs")
			d=d.replace("testphp.99ducaijing.cn","phpapi.99ducaijing.cn")
			d=d.replace("testphp.99ducaijing.cn","www.99ducaijing.com")
			print("production_loacal__environment_success")
		f.close()
		f = open(local_dir,"w",encoding="utf-8")
		f.write(d)
		f.close()
#QQ、微信等第三方登录
	with open(local_dir,"r",encoding="utf-8") as f:
		d = f.read()
		d=d.replace("qqloginurl=http://testphp.99ducaijing.cn","qqloginurl=http://www.99ducaijing.com")
		d=d.replace("weibologinurl=http://testphp.99ducaijing.cn","weibologinurl=http://www.99ducaijing.com")
		d=d.replace("wechatloginurl=http://testphp.99ducaijing.cn","wechatloginurl=http://www.99ducaijing.com")
		print("QQ/weixin/weibo")
	f.close()
	f = open(local_dir,"w",encoding="utf-8")
	f.write(d)
	f.close()

if __name__=="__main__":
	parentdir = u"E:\\版本测试\\v1.4测试"
	local = "local.config"
	# oiparentdir =u
	local_dir = os.path.join(parentdir,local)
	print ("local.local_dir: ",local_dir)

	localSwitch(local_dir,2)
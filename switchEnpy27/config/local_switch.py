#coding=utf-8
#encoding=utf-8

__author__='xzz'

import os

def localSwitch(local_dir,num):

	f = open(local_dir,"r")
	lines = f.readlines()
	flen=len(lines)
	for i in range(flen):
		if lines[i].find("loginip=login") >=0  or lines[i].find("lobbyip=lobbyip") >=0 or \
		lines[i].find("lbsip=lbs") >=0 or lines[i].find("lbsip=testlbs") >=0:
			lines[i]=lines[i].replace("#","")
		else:
			pass
	f.close()
	f = open(local_dir,"w")
	f.writelines(lines)
	f.close()
#测试环境切换
	if num == 1:
		with open(local_dir,"r") as f:
			d = f.read()
			d=d.replace("loginip=login","#loginip=login")
			d=d.replace("lobbyip=lobbyip","#lobbyip=lobbyip")
			d=d.replace("lbsip=lbs","#lbsip=lbs")
			d=d.replace("phpapi.99ducaijing.cn","testphp.99ducaijing.cn")
			d=d.replace("www.99ducaijing.com","testphp.99ducaijing.cn")
			print("test_local_environment_success")
		f.close()
		f = open(local_dir,"w")
		f.write(d)
		f.close()


#正式环境切换
	else:
		with open(local_dir,"r") as f:
			d = f.read()
			d=d.replace("lbsip=testlbs","#lbsip=testlbs")
			d=d.replace("testphp.99ducaijing.cn","phpapi.99ducaijing.cn")
			d=d.replace("testphp.99ducaijing.cn","www.99ducaijing.com")
			print("production_loacal__environment_success")
		f.close()
		f = open(local_dir,"w")
		f.write(d)
		f.close()
#QQ、微信等第三方登录
	with open(local_dir,"r") as f:
		d = f.read()
		d=d.replace("qqloginurl=http://testphp.99ducaijing.cn","qqloginurl=http://www.99ducaijing.com")
		d=d.replace("weibologinurl=http://testphp.99ducaijing.cn","weibologinurl=http://www.99ducaijing.com")
		d=d.replace("wechatloginurl=http://testphp.99ducaijing.cn","wechatloginurl=http://www.99ducaijing.com")
		print("QQ/weixin/weibo")
	f.close()
	f = open(local_dir,"w")
	f.write(d)
	f.close()

if __name__=="__main__":
	parentdir = u"E:\\版本测试\\v1.4测试"
	local = "local.config"
	# oiparentdir =u
	local_dir = os.path.join(parentdir,local)
	print ("local.local_dir: ",local_dir)

	localSwitch(local_dir,2)











# #coding=utf-8
# #encoding=utf-8

# __author__='xzz'

# import os

# def localSwitch(local_dir,num):
# 	# local_dir = os.path.join(parentdir,local)
# 	# print ("local.config_dir: ",local_dir)

# #测试环境切换
# 	if num == 1:
# 		with open(local_dir,"r") as f:
# 			lines = f.readlines()
# 			flen=len(lines)
# 			for i in range(flen):
# 				if lines[i][0]=="#" and lines[i][0:14]!="#lbsip=testlbs":
# 					# print("$#%5&&&&&")
# 					pass
# 				else:
# 					lines[i]=lines[i].replace("loginip=login","#loginip=login")
# 					lines[i]=lines[i].replace("lobbyip=lobbyip","#lobbyip=lobbyip")
# 					lines[i]=lines[i].replace("lbsip=lbs","#lbsip=lbs")
# 					lines[i]=lines[i].replace("#lbsip=testlbs","lbsip=testlbs")
# 					# print ("@@@@@@@")
# 				lines[i]=lines[i].replace("phpapi.99ducaijing.cn","testphp.99ducaijing.cn")
					
# 			print("test_local_environment_success")
# 		f.close()
# 		f = open(local_dir,"w")
# 		f.writelines(lines)
# 		f.close()

# 		# 	d = f.read()
# 		# 	d=d.replace("loginip=login","#loginip=login")
# 		# 	d=d.replace("lobbyip=lobbyip","#lobbyip=lobbyip")
# 		# 	d=d.replace("lbsip=lbs","#lbsip=lbs")
# 		# 	d=d.replace("#lbsip=testlbs","lbsip=testlbs")
# 		# 	d=d.replace("phpapi.99ducaijing.cn","testphp.99ducaijing.cn")
# 		# 	f.close()
# 		# 	print("test_local_environment_success")
# 		# f = open(local_dir,"w",encoding="utf-8")
# 		# f.write(d)
# 		# f.close()


# #正式环境切换
# 	else:
# 		with open(local_dir,"r") as f:
# 			lines = f.readlines()
# 			flen=len(lines)
# 			for i in range(flen):
# 				if lines[i][0]=="#" and lines[i][0:14]=="#lbsip=testlbs":
# 					# print("$#%5&&&&&")
# 					pass
# 				else:
# 					lines[i]=lines[i].replace("#loginip=login","loginip=login")
# 					lines[i]=lines[i].replace("#lobbyip=lobbyip","lobbyip=lobbyip")
# 					lines[i]=lines[i].replace("#lbsip=lbs","lbsip=lbs")
# 					lines[i]=lines[i].replace("lbsip=testlbs","#lbsip=testlbs")
# 					# print ("@@@@@@@")
# 				lines[i]=lines[i].replace("testphp.99ducaijing.cn","phpapi.99ducaijing.cn")
					
# 			print("production_local_environment_success")
# 		f.close()
# 		f = open(local_dir,"w")
# 		f.writelines(lines)
# 		f.close()

# 		# with open(local_dir,"r",encoding="utf-8") as f:
# 		# 	d = f.read()
# 		# 	d=d.replace("#loginip=login","loginip=login")
# 		# 	d=d.replace("#lobbyip=lobbyip","lobbyip=lobbyip")
# 		# 	d=d.replace("#lbsip=lbs","lbsip=lbs")
# 		# 	d=d.replace("lbsip=testlbs","#lbsip=testlbs")
# 		# 	d=d.replace("testphp.99ducaijing.cn","phpapi.99ducaijing.cn")
# 		# 	f.close()
# 		# 	print("production_loacal__environment_success")
# 		# f = open(local_dir,"w",encoding="utf-8")
# 		# f.write(d)
# 		# f.close()

# if __name__=="__main__":
# 	parentdir = u"E:\\版本测试\\v1.4测试"
# 	local = "local.config"
# 	# oiparentdir =u
# 	local_dir = os.path.join(parentdir,local)
# 	print ("local.local_dir: ",local_dir)

# 	localSwitch(local_dir,1)
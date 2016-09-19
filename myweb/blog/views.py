#coding=UTF-8
from blog.models import Blog,Book,File
from django.shortcuts import render_to_response
from django.http import HttpResponse,HttpResponseRedirect
from django.contrib import auth
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator,EmptyPage,PageNotAnInteger
from django.core.urlresolvers import reverse

from django.views.decorators.csrf import csrf_exempt
# Create your views here.

def index(request):
	blog_list = Blog.objects.all()
	return render_to_response('index.html',{'blogs':blog_list})
#登录
@csrf_exempt
def login(request):
	blog_list = Blog.objects.all()
	username=request.POST.get('username','')
	password=request.POST.get('password','')
	#if username == 'xzz10000' and password == '123456':
	#	return HttpResponse('login success!')
	#elif username == '' or password =='':
	#	return render_to_response('index.html',{'error':'username or password null!'})


	# if username !='' and password !='':
	# 	response = HttpResponseRedirect('/login_ok/')
	# 	#response.set_cookie('username',username,3600) #用户名cookie
	# 	request.session['username'] = username #将session信息写到服务器
	# 	return response

	users_ = [username]
	user = auth.authenticate(username=username,password=password)

	if user is not None:
		auth.login(request,user) #验证登录
		#response = HttpResponseRedirect('/login_ok/')
		response = HttpResponseRedirect(reverse('blog:login_ok'))
		request.session['username']=users_
		return response
	else:
		return render_to_response('index.html',{'error':'username or password error!','blogs':blog_list})
	

#登录成功
@login_required
def login_ok(request):
	blog_list=Blog.objects.all()
	#username = request.COOKIES.get('username','')
	username = request.session.get('username','') #读取用户session
	
	#return render_to_response('login_ok.html',{'user':username,'blog_list':blog_list})
	user = username[0]
	return render_to_response('login_ok.html',{'user':user,'blog_list':blog_list})
#退出登录
@login_required
def logout(request):
	# response = HttpResponseRedirect('/index/') #返回首页
	response = HttpResponseRedirect(reverse('blog:index'))
	#response.delete_cookie('username') #清理cookie里面保存的username
	del request.session['username']  #清理用户session
	return response

#学生表
def student(request):
	books =Book.objects.all()
	student = {
		'jack':[22,'boy','Programmer'],
		'alen':[27,'boy','Designer'],
		'una':[23,'girl','Tester'],
		'Brant':[23,'girl','Tester'],
		'David':[23,'boy','Tester']
	}
	return render_to_response('student.html',{'student_list':student,'book_list':books})

def page(request):
	file_list = Book.objects.all()
	paginator = Paginator(file_list,2)
	page = request.GET.get('page')
	try:
		contacts =paginator.page(page)
	except PageNotAnInteger:
		#if page is not an integer,deliver first page
		contacts = paginator.page(1)
	except EmptyPage:
		contacts = paginator.page(paginator.num_pages)
	return render_to_response('book.html',{'pages':contacts})

#上传文件页面

def upload(request):
	files = File.objects.all()
	reverse('blog:upload', current_app=request.resolver_match.namespace)
	return render_to_response('upload.html',{'file_list':files})

#执行文件上传
@csrf_exempt
def upload_save(request):
	files = File.objects.all()
	filename = request.POST.get('filename','') #获取表单文件说明
	fileing = request.FILES.get('fileing','') #获得文件
	response = HttpResponseRedirect(reverse('blog:login_ok'))
	if filename == '' or fileing == '':
		error = '文件与文件描述不能为空'
		return response,render_to_response('upload.html',{'error':error,'file_list':files})
	else:
		upload = File()  #将文件名和文件路径存放到File表中
		upload.filename = filename
		upload.fileway = fileing
		upload.save()
		return response,render_to_response('upload.html',{'upload_success':'文件上传成功','file_list':files})

# def page_not_found(request):
# 	return render_to_response('Error/404.html')


def hello(request):
	name = request.GET.get('name','')
	return HttpResponse("Hello,%s!" %name)
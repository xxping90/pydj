from django.shortcuts import render,get_object_or_404
from django.http import HttpResponseRedirect,HttpResponse
from django.core.urlresolvers import reverse
from .models import Question,Choice

from django.views.decorators.csrf import csrf_exempt
import json

# Create your views here.
#首页展示所有问题
# def index(request):

# 	latest_question_list = Question.objects.all()
# 	context = {'latest_question_list':latest_question_list}
# 	return render(request,'polls/index.html',context)

# #查看单个问题选项
# def detail(request,question_id):
# 	question = get_object_or_404(Question,pk=question_id)
# 	return render(request,'polls/detail.html',{'question':question})

# #查看投票结果
# def results(request,question_id):
# 	question = get_object_or_404(Question,pk=question_id)
# 	return render(request,'polls/results.html',{'question':question})

# #选择投票
# def vote(request,question_id):
# 	p = get_object_or_404(Question,pk=question_id)
# 	try:
# 		selected_choice = p.choice_set.get(pk=request.POST['choice'])
# 	except(KeyError,Choice.DoesNotExist):
# 		return render(request,'polls/detail.html',{
# 			'question':p,
# 			'error_message':"You didn't select a choice",
# 			})
# 	else:
# 		selected_choice.votes +=1
# 		selected_choice.save()

# 		return HttpResponseRedirect(reverse('polls:results',args=(p.id,)))




# # 只提供接口，不返回数据
# # 首页展示所有问题
def index(request):
	question_list = Question.objects.all()
	response_data = {}
	datas_list = []
	datas ={}
	if  question_list:
		# for question in question_list:
		# 	datas_list.append(question.question_text )
		# print(datas_list)
		# for i in range(0,len(datas_list)):
		# 	datas[i+1] = datas_list[i]
		# print (datas)
		for question in question_list:
			datas[question.id] = question.question_text
		response_data['status'] = '200'
		response_data['message'] = 'success'
		response_data['data'] = datas
		result = json.dumps(response_data)
		return HttpResponse(result)
	else:
		response_data['status'] = '10021'
		response_data['message'] = 'null'
		response_data['data'] =datas
		result = json.dumps(response_data)
		return HttpResponse(result)

#查看所有问题
def detail(request,question_id):
	choices = Choice.objects.filter(question_id=question_id)
	datas = {}
	response_data = {}
	if choices:
		for choice in choices:
			datas[choice.id] = choice.choice_text
		response_data['status'] = '200'
		response_data['message'] = 'success'
		response_data['data']  = datas
		result = json.dumps(response_data)
		return HttpResponse(result)
	else:
		response_data['status'] = '10021'
		response_data['message'] = 'null'
		response_data['data'] = datas
		result = json.dumps(response_data)
		return HttpResponse(result)

#查看投票结果
def results(request,question_id):
	results = Choice.objects.filter(question_id=question_id)
	datas = {}
	response_data = {}
	if results:
		for r in results:
			datas[r.choice_text] = r.votes
		response_data['status'] = '200'
		response_data['message'] = 'success'
		response_data['data'] = datas
		result = json.dumps(response_data)
		return HttpResponse(result)
	else:
		response_data['status'] = '10021'
		response_data['message'] = 'null'
		response_data['data'] = datas
		result = json.dumps(response_data)
		return HttpResponse(result)

#选择投票
@csrf_exempt
def vote(request,question_id):
	p = get_object_or_404(Question,pk=question_id)
	choice_id = request.POST.get('choice','')
	response_data = {}
	if choice_id == '':
		response_data['status'] = '10021'
		response_data['message'] = 'null'
		result = json.dumps(response_data)
		return HttpResponse(result)
	try:
		selected_choice = p.choice_set.get(pk=request.POST['choice'])
	except(KeyError,Choice.DoesNotExist):
		response_data['status'] = '10022'
		response_data['message'] = 'The problem is not the choice id'
		result = json.dumps(response_data)
		return HttpResponse(result)
	else:
		selected_choice.votes += 1
		selected_choice.save()
		response_data['status'] = '200'
		response_data['message'] = 'success'
		result = json.dumps(response_data)
		return HttpResponse(result)

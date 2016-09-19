from django.conf.urls import url,patterns
from . import views

app_name='polls'
urlpatterns = [
	#ex "/polls/"
	url(r'^$',views.index,name='index'),
	url(r'^(?P<question_id>[0-9]+)/$',views.detail,name='detail'),
	url(r'^(?P<question_id>[0-9]+)/results/$',views.results,name='results'),
	url(r'^(?P<question_id>[0-9]+)/vote/$',views.vote,name='vote'),
]


# urlpatterns = [
# 	#ex "/polls/"
# 	url(r'^(?P<question_id>[0-9]+)/$',views.index,name='index'),
# 	url(r'^(?P<question_id>[0-9]+)/$',views.detail,name='detail'),
# 	url(r'^(?P<question_id>[0-9]+)/results/$',views.results,name='results'),
# 	url(r'^(?P<question_id>[0-9]+)/vote/$',views.vote,name='vote'),
# ]
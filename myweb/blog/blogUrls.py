from django.conf.urls import url,patterns
from . import views

# app_name = 'blog'
# urlpatterns = patterns('',
#     url(r'^$',views.index,name='index'),
#     url(r'^login/$',views.login,name='login'),
#     url(r'^login_ok/$',views.login_ok,name='login_ok'),
#     url(r'^logout/$',views.logout,name='logout'),
#     url(r'^accounts/login/$',views.index,name='index'),
#     url(r'^student/$',views.student,name='student'),
#     url(r'^book/$',views.page,name='page'),
#     url(r'^upfile/$',views.upload,name='upload'),
#     url(r'^upload_s/$',views.upload_save,name='upload_save'),

# )


app_name = 'blog'
urlpatterns = [
    url(r'^$',views.index,name='index'),
    url(r'^login/$',views.login,name='login'),
    url(r'^login_ok/$',views.login_ok,name='login_ok'),
    url(r'^logout/$',views.logout,name='logout'),
    url(r'^accounts/login/$',views.index,name='index'),
    url(r'^student/$',views.student,name='student'),
    url(r'^book/$',views.page,name='page'),
    url(r'^upfile/$',views.upload,name='upload'),
    url(r'^upload_s/$',views.upload_save,name='upload_save'),
    url(r'^hello/$',views.hello,name='hello'),
    # url(r'^404/$',views.page_not_found,name='page_not_found'),

]
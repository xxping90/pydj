"""myweb URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
# from django.conf.urls import url
# from django.contrib import admin
# from blog.views import index,login,login_ok,logout,student,page,upload,upload_save

# urlpatterns = [
#     url(r'^admin/', admin.site.urls),
#     url(r'^index/$',index),
#     url(r'^login/$',login),
#     url(r'^login_ok/$',login_ok),
#     url(r'^logout/$',logout),
#     url(r'^accounts/login/$',index),
#     url(r'^student/$',student),
#     url(r'^book/$',page),
#     url(r'^upfile/$',upload),
#     url(r'^upload_s/$',upload_save),

# ]

from django.conf.urls import url, include,patterns
from django.contrib import admin
from blog import blogUrls
#from polls import pollsUrls


urlpatterns =[
	url(r'^admin/',admin.site.urls),
	url(r'^blog/',include(blogUrls)),
	url(r'^polls/',include('polls.pollsUrls',namespace='polls')),

]
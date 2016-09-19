#coding=UTF-8

from __future__ import unicode_literals

from django.db import models
from django.contrib import admin

# Create your models here.
class Blog(models.Model):
	title = models.CharField(max_length=150)
	body = models.TextField()
	timestamp = models.DateTimeField()

class BlogAdmin(admin.ModelAdmin):
	list_display = ('title','timestamp')



#Create your models here
#作者
class  Author(models.Model):
	first_name = models.CharField(max_length=30)
	last_name = models.CharField(max_length=40)
	email = models.EmailField()

	def __str__(self):
		return self.first_name

#出版社
class Publisher(models.Model):
	name = models.CharField(max_length=30)
	address = models.CharField(max_length=50)
	city = models.CharField(max_length=60)
	state_province = models.CharField(max_length=30)
	country = models.CharField(max_length=50)
	website = models.URLField()

	def __str__(self):
		return self.name

#书
class Book(models.Model):
	title = models.CharField(max_length=100)
	author = models.ManyToManyField(Author)
	publisher = models.ForeignKey(Publisher)
	publication_date = models.DateField()

	def __str__(self):
		return self.title

#file upload
class File(models.Model):
	filename = models.CharField(max_length=30)
	fileway = models.FileField(upload_to='./upload/')

	def __str__(self):
		return self.filename

admin.site.register(Blog,BlogAdmin)
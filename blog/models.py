from django.db import models
from django import forms
from django.utils import timezone

class Post(models.Model) :
	author = models.ForeignKey('auth.User')
	title = models.CharField(max_length=200)
	text = models.TextField()
	created_date = models.DateTimeField(default = timezone.now)
	published_date = models.DateTimeField(blank = True, null = True)

	def publish(self) :
		self.published_date = timezone.now()
		self.save()

	def __str__(self) :
		return self.title

class EmailForm(forms.Form) :
	user_id = forms.CharField(max_length=255)
	password = forms.CharField(max_length=32, widget = forms.PasswordInput)
	email_to = forms.CharField(max_length=255)
	subject = forms.CharField(max_length=255)
	message = forms.CharField()

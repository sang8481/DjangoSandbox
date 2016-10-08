from django import forms

from .models import Post

class PostForm(forms.ModelForm) :
	class Meta :
		model = Post
		fields = ('title', 'text',)

class EmailForm(forms.Form) :
	user_id = forms.CharField()
	user_pw = forms.CharField()
	mail_from = forms.CharField()
	mail_to = forms.CharField()
	subject = forms.CharField()
	body = forms.CharField()

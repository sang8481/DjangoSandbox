from django.conf.urls import patterns, url, include
from django.conf import settings
from django.views.generic.base import TemplateView
from . import views

urlpatterns = [
	url(r'^$', views.post_list, name='post_list'),
	url(r'^post/(?P<pk>[0-9]+)/$', views.post_detail, name='post_detail'),
	url(r'^post/new/$', views.post_new, name='post_new'),
	url(r'^email/send/$', views.sendmail),
    url(r'^email/thankyou/$', TemplateView.as_view(template_name='blog/thankyou.html'), name='thankyou'),
    url(r'^email/$', TemplateView.as_view(template_name='blog/email.html'), name='email'),

]

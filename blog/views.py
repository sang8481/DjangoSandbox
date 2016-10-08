from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic.base import TemplateView
from django.http import HttpResponseRedirect
from django.utils import timezone
from .forms import PostForm
from .models import Post
from .models import EmailForm
import getpass
import telnetlib
import socket
import base64
import sys

def post_list(request) :
	posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
	return render(request, 'blog/post_list.html', {'posts':posts})

def post_detail(request, pk) :
	post = get_object_or_404(Post, pk = pk)
	return render(request, 'blog/post_detail.html', {'post':post})

def post_new(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('blog.views.post_detail', pk=post.pk)
    else:
        form = PostForm()
    return render(request, 'blog/post_edit.html', {'form': form})

def sendmail(request):
	if request.method == 'POST':
		form = EmailForm(request.POST)
	if form.is_valid():
		user_id = form.cleaned_data['user_id']
		password = form.cleaned_data['password']
		email_to = form.cleaned_data['email_to']
		subject = form.cleaned_data['subject']
		message = form.cleaned_data['message']
	else :
		print("exit.")
		exit()


	HOST = socket.gethostbyname('cuvic.cnu.ac.kr')

	try:
		tn = telnetlib.Telnet(HOST, 25)
	except IOError :
		print("Telnet connection failed")
		sys.exit()

	host_name = "cnu.ac.kr"
	mail_from = user_id + "@" + host_name

	tn.write(b"EHLO " + mail_from.encode() + b"\r\n")
	tn.write(b"AUTH LOGIN\r\n")

	tn.write(base64.b64encode(user_id.encode()) + b"\r\n")
	tn.write(base64.b64encode(password.encode()) + b"\r\n")

	tn.write(b"MAIL FROM: " + mail_from.encode() + b"\r\n")
	tn.write(b"RCPT TO:"+ email_to.encode() + b"\r\n")
	tn.write(b"DATA\r\n")

	tn.write(b"SUBJECT: " + subject.encode() + b"\r\n")
	tn.write(b"FROM: " + mail_from.encode() + b"\r\n")
	tn.write(b"TO: " + mail_to.encode() + b"\r\n")

	tn.write(message.encode() + b"\r\n")
	tn.write(b".\r\n")
	tn.write(b"QUIT\r\n")

	print (tn.read_all())

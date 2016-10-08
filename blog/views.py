from django.shortcuts import render, redirect, get_object_or_404
from django.utils import timezone
from .forms import PostForm, EmailForm
from .models import Post
import socket
import base64

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

def email(request) :
	form_class = EmailForm
	if request.method == 'POST' :
		form = form_class(data=request.POST)
		username = request.POST.get('user_id', '')
		password = request.POST.get('user_pw', '')
		mail_from = request.POST.get('mail_from', '')
		mail_to = request.POST.get('mail_to', '')
		subject = request.POST.get('subject', '')
		body = request.POST.get('body', '')


		sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		server_host_name = 'cuvic.cnu.ac.kr'
		host_name = 'cnu.ac.kr'

		sock.connect((server_host_name, 25))
		print("socket connect")
		message = sock.recv(1024)
		print(message)

		sock.send(b"EHLO " + host_name.encode() + b"\r\n")
		print("send EHLO")
		message = sock.recv(1024)
		print(message)

		message = sock.recv(1024)
		print(message)

		sock.send(b"AUTH LOGIN\r\n")
		print("send AUTH LOGIN")
		message = sock.recv(1024)
		print(message)

		sock.send(base64.b64encode(username.encode()) + b"\r\n")
		print("send userid")
		message = sock.recv(1024)
		print(message)
		sock.send(base64.b64encode(password.encode()) + b"\r\n")
		print("send pw")
		message = sock.recv(1024)
		print(message)

		sock.send(b"MAIL FROM: " + mail_from.encode() + b"\r\n")
		message = sock.recv(1024)
		print(message)

		sock.send(b"RCPT TO: "+ mail_to.encode() + b"\r\n")
		message = sock.recv(1024)
		print(message)

		sock.send(b"DATA\r\n")
		message = sock.recv(1024)
		print(message)

		sock.send(b"SUBJECT: " + subject.encode() + b"\r\n")
		sock.send(b"FROM: " + mail_from.encode() + b"\r\n")
		sock.send(b"TO: "+ mail_to.encode() + b"\r\n\n")
		sock.send(body.encode() + b"\r\n")
		sock.send(b".\r\n")
		message = sock.recv(1024)
		print(message)
		sock.send(b"QUIT\r\n")
		message = sock.recv(1024)
		print(message)

		#print (user_id + user_pw + mail_from + mail_to + subject + body)


		return render(request, 'blog/email.html', {'form':form_class})

	return render(request, 'blog/email.html', {'form':form_class})

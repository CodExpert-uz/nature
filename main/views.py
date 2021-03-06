from django.shortcuts import render
from .models import *
from django.contrib import messages
from .forms import 	JoinUsForm
#Search views
from django.db.models import Q
# Create your views here.
import telebot 


me = 668618297
TOKEN = '1133552059:AAH_ZpM-cZHniQoheUqmTNc-wHRE8Enow1c'
bot = telebot.TeleBot(TOKEN)


def search(request):
	query = request.GET.get('search')
	posts = Post.objects.filter(
		Q(title__icontains=query) & Q(body__icontains=query)
		)
	context = {
		'results':posts
	}
	return render(request, 'results.html', context)


def index(request):
	if request.method == 'POST':
		form = JoinUsForm(request.POST)
		if form.is_valid():
			form.save()
			print('*'*50)
		else:
			print('#'*50)
	else:
		form = JoinUsForm()
	posts = Post.objects.all().order_by('-published')[:3]
	most_read = Post.objects.filter(most_read=True)

	context = {
	'posts':posts, 
	'most_read':most_read,
	'form':form
	}

	return render(request, 'home.html',context)


def contact(request):
	if request.method == 'POST':
		n = request.POST['name']
		e = request.POST['email']
		m = request.POST['message']
		Contact.objects.create(name=n, email=e, message=m)
		bot.send_message(me, 'Saytdan xabar bor \n Ismi : {0}'.format(n))
		print('*'*50)
	else:
		print('#'*50)

	return render(request, 'contacts.html')


def blog(request):
	posts = Post.objects.all()
	print(type(posts))
	return render(request, 'blog.html', {'posts':posts})

def blog_detail(request,post_slug):
	post = Post.objects.get(slug=post_slug)
	if request.method == 'POST':
		name = request.POST['name']
		email = request.POST['email']
		subject = request.POST['subject']
		message = request.POST['message']
	
		comment = Comment.objects.create(
				name=name,
				email=email,
				subject=subject,
				message=message
				)
		comment.post = post
		comment.save()
	

		messages.add_message(request, messages.SUCCESS, 'Muhokama qabul qilindi !')
	else:
		messages.add_message(request, messages.WARNING, 'Muhokama qabul qilinmadi !!!')


	context = {
		'post':post,
	}
		
	return render(request, 'post.html',context)	

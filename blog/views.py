from django.shortcuts import render,redirect
from django.http import HttpResponse
from blog.models import BlogPost

# Create your views here.

# def home(request):
# 	return HttpResponse("Hi there! Welcome to Django")

def home (request):
	return render(request,'base.html')

# def greet(request,name):
# 	return HttpResponse(f"Hi {name}! How you doing!")

def post_page(request,post_id):
	print(post_id)	
	post = BlogPost.objects.get(pk=post_id)
	return render(request,'post.html',{'currentpost':post})

def all_post(request):
	allpost = BlogPost.objects.all()
	return render(request,'allpost.html',{'allpostdict':allpost})

def create_post(request):

	if request.method == "POST":
		print(request)
		title = request.POST["title"]
		content = request.POST["content"]
		new_post = BlogPost.objects.create(title=title,content=content)
		return redirect("/allpost/")

	return render(request,'createpost.html')
	#allpost = BlogPost.objects.all()

def delete_post(request,post_id):
	post = BlogPost.objects.get(pk=post_id)
	post.delete()
	return redirect('/allpost/')
	#allpost = BlogPost.objects.all()

# GO to the post page
# Get a form prefilled with post data
# Edit the post and save back to the same post

def edit_post(request,post_id):
	post = BlogPost.objects.get(pk=post_id)
	if request.method == 'POST':
		title = request.POST["title"]
		content = request.POST["content"]

		post.title = title
		post.content = content
		post.save()
		
		return redirect(f'/post/{post_id}')
	return render(request,'editpost.html',{'post':post})

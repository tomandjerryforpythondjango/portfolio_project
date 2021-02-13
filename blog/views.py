from django.shortcuts import render,get_object_or_404
from blog.models import Blog

def allblogs(request):
	blogs = Blog.objects.all()
	return render(request, 'blog/allblogs.html', {'blogs': blogs})

def detail(request, blog_id):
	detail_blog = get_object_or_404(Blog, pk=blog_id)
	return render(request, 'blog/detail.html', {'detail_blog': detail_blog})
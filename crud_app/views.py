from django.shortcuts import render, get_object_or_404, redirect
from .models import Blog


def index(request):
    return render(request, 'base.html')

def all_blogs(request):
    blogs = Blog.objects.all().order_by('-created_at')
    return render(request, 'all-blogs.html', {'blogs': blogs})

def blog_detail(request):
    return render(request, 'blog-detail.html')

def add_blog(request):
    return render(request, 'all-blogs.html')

def update_blog(request):
    return render(request, 'update-blog.html')

def delete_blog(request):
    return render(request, 'delete-blog.html')



from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from .models import Blog


def index(request):
    return render(request, 'base.html')

def all_blogs(request):
    blogs = Blog.objects.all().order_by('-created_at')
    return render(request, 'all-blogs.html', {'blogs': blogs})

def blog_detail(request, id):
    blog = get_object_or_404(Blog, id=id)
    context={'blog': blog}
    return render(request, 'blog-details.html', context)

def add_blog(request):
    if request.method == 'POST':
        try:
            title = request.POST.get('title')
            content = request.POST.get('content')
            image = request.FILES.get('image')
            author = request.POST.get('author')

            Blog.objects.create(
                title=title,
                content=content,
                image=image,
                author=author
            )
            messages.success(request, 'Blog added successfully!')
            return redirect('/')
        except Exception as e:
            messages.error(request, f'Oops! An error occured while adding the blog. Try again later.')
    return render(request, 'add-blog.html')

def update_blog(request, id):
    blog = get_object_or_404(Blog, id=id)
    
    if request.method == 'POST':
        try:
            blog.title = request.POST.get('title')
            blog.content = request.POST.get('content')
            if 'image' in request.FILES:
                blog.image = request.FILES.get('image')
            blog.author = request.POST.get('author')
            blog.save()
            messages.success(request, 'Blog added successfully!')
        except Exception as e:
            messages.error(request, f'Oops! An error occured while updating the blog. Try again later.')
        return redirect('/')
    
    context={'blog': blog}
    return render(request, 'update-blog.html', context)

def delete_blog(request, id):
    blog = get_object_or_404(Blog, id=id)
    if request.method == 'POST':
        try:
            blog.delete()
            messages.success(request, 'Blog deleted successfully!')
            return redirect('/')
        except Exception as e:
            messages.error(request, f'Oops! The blog could not be deleted. Try again later.')
    
    context={'blog': blog}
    return render(request, 'delete-blog.html', context)



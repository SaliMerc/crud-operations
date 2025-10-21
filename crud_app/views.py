from django.shortcuts import render, get_object_or_404, redirect
from .models import Blog


def index(request):
    return render(request, 'base.html')

def all_blogs(request):
    blogs = Blog.objects.all().order_by('-created_at')
    return render(request, 'all-blogs.html', {'blogs': blogs})

def blog_detail(request, id):
    blog = get_object_or_404(Blog, id=id)
    context={'blog': blog}
    return render(request, 'blog-detail.html', context)

def add_blog(request):
    if request.method == 'POST':
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
        return redirect('/')
    return render(request, 'add-blog.html')

def update_blog(request):
    blog = get_object_or_404(Blog, id=id)
    context={'blog': blog}
    return render(request, 'update-blog.html')

def delete_blog(request):
    blog = get_object_or_404(Blog, id=id)
    context={'blog': blog}
    return render(request, 'delete-blog.html')



from django.urls import path
from crud_app.views import *

urlpatterns = [
    path('', all_blogs, name='all-blogs'),
    
    path('add-blog/', add_blog, name='add-blog'),
    path('update-blog/', add_blog, name='update-blog'),
    path('delete-blog/', add_blog, name='delete-blog'),
    
    path('blog-detail/', add_blog, name='blog-detail'),
]
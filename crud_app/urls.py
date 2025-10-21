from django.urls import path
from crud_app.views import *

urlpatterns = [
    path('', all_blogs, name='all-blogs'),
]
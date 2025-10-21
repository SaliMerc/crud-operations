from django.shortcuts import render, get_object_or_404, redirect
from .models import Blog


def index(request):
    return render(request, 'base.html')

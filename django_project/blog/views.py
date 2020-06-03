from django.shortcuts import render
from .models import Post


def home(request):
    context = { 'posts': Post.objects.all() }
    return render(request, 'blog/home.htm', context)

def about(request):
    return render(request, 'blog/about.htm')

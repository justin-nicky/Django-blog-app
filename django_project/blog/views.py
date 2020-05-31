from django.shortcuts import render
from django.http import HttpResponse

posts = [
    {
        'author':'justin',
        'title':'blog post 1',
        'content':'writing my first post',
        'date_posted':'may 31, 2020'
    },
    {
        'author':'justin',
        'title':'blog post 2',
        'content':'writing my second post',
        'date_posted':'may 31, 2020'
    }
]

def home(request):
    context = { 'posts': posts,}
    return render(request, 'blog/home.htm', context)

def about(request):
    return render(request, 'blog/about.htm')

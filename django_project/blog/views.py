from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return HttpResponse('<h1>Blog home</h1>')

def about(request):
    return HttpResponse('<h1>Blog-about</h1>')

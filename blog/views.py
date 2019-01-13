from django.shortcuts import render
from .models import Blog
# Create your views here.

def allblogs(request):
    blogitems = Blog.objects
    return render(request, 'blog/blogsAll.html',{'bItems':blogitems})
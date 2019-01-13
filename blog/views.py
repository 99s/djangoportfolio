from django.shortcuts import render, get_object_or_404
from .models import Blog
# Create your views here.

def allblogs(request):
    blogitems = Blog.objects
    return render(request, 'blog/blogsAll.html',{'bItems':blogitems})

def details(request, blog_id):
    detaildblog = get_object_or_404(Blog, pk=blog_id)
    return render(request, 'blog/blogdetails.html', {'bdetail':detaildblog})


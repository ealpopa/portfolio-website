from django.shortcuts import render
from django.shortcuts import get_object_or_404  # this is to get blog model by id
from .models import Blog


def all_blogs(req):
    blogs = Blog.objects
    return render(req, 'blog/all_blogs.html', {'blogs': blogs})


def details(req, blog_id):
    blog_details = get_object_or_404(Blog, pk=blog_id)
    return render(req, 'blog/details.html', {'blog': blog_details})

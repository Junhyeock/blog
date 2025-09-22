from django.shortcuts import render, get_object_or_404
from .models import Blog


def blog_list(request):
    blogs = Blog.objects.all()

    context = {
        'blogs': blogs
    }
    return render(request, 'blog_list.html', context)
# Create your views here.


def blog_detail(request, pk):
    blog = get_object_or_404(Blog, pk=pk)
    context = {
        'blog': blog
    }
    return render(request, 'blog_detail.html', context)

# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render, get_object_or_404

# Create your views here.
from blog.models import Blog


def all_blog(request):
    blog_count = Blog.objects.count()
    blog_list = Blog.objects.order_by('-publish_date')[:3]
    return render(request, 'all_blogs.html', {'blog_list': blog_list,
                                              'blog_count': blog_count})


def detail(request, blog_id):
    blog = get_object_or_404(Blog, id=blog_id)
    return render(request, 'blog_detail.html', {'blog': blog})

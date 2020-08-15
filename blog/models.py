# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib import admin
from django.db import models


# Create your models here.
class Blog(models.Model):
    title = models.CharField(max_length=100)
    desc = models.TextField()
    publish_date = models.DateField()
    blog_image = models.ImageField(upload_to='blog/image')

    def __str__(self):
        return self.title


class BlogAdmin(admin.ModelAdmin):
    search_fields = ('title', 'desc')


# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render

# Create your views here.
from portfolio.models import Project


def home(request):
    projects = Project.objects.all()
    return render(request, 'home.html', {'projects': projects})

# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

from .models import ConclusionPage
from .utils.populate_conclusionPages import populate
import json

def index(request):
    return render(request, 'digestif/index.html') # show just plain index page

def explore(request):
    populate()
    conclusion_pages = ConclusionPage.objects.all()
    context = {'conclusion_pages' : conclusion_pages}
    return render(request, 'digestif/explore.html', context)


def create(request):
    return render(request, 'digestif/create.html')

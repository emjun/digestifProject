# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

from .models import ConclusionPage
from .utils.populate_cp_blocks import populate # populate the DB with full conclusion pages and blocks
# from .utils.populate_favorites import getFavorites
import json

def index(request):
    return render(request, 'digestif/index.html') # show just plain index page

def explore(request):
    # TODO: Need to come up with a way to only allow populating the Blocks and
        # Conclusion Pages DB only once
    # populate()
    conclusion_pages = ConclusionPage.objects.order_by('platform') # get ConclusionPages ordered by platform name
    platforms = ConclusionPage.objects.order_by('platform').values('platform').distinct() # get unique set of platforms
    context = {'conclusion_pages' : conclusion_pages, 'platforms' : platforms}
    return render(request, 'digestif/explore.html', context)
    # return render(request, 'digestif/explore.html')

def cp_detail(request, id):
    conclusion_page = ConclusionPage.objects.get(cp_id=id)
    context = {'conclusion_page': conclusion_page}
    return render(request, 'digestif/cp_detail.html', context);

def block_detail(request, id):
    block = Block.objects.get(block_id=id)
    conclusion_page = ConclusionPage.objects.get(blocks__contains=block);
    context = {'block': block, 'conclusion_page': conclusion_page}
    return render(request, 'digestif/block_detail.html', context);

def create(request):
    # favorites = getFavorites()
    # context = {'favorites' : favorites}

    # Maybe instead of doing it in the views, I can do this directly with create.js...
    # return render(request, 'digestif/create.html', favorites)
    return render(request, 'digestif/create.html')

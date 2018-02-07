# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

from .models import ConclusionPage
from .models import Block
from .utils.populate_cp_blocks import populate # populate the DB with full conclusion pages and blocks
# from .utils.populate_favorites import getFavorites
import json

# global variable so that database is populated only once (to avoid duplicates)
# already_populated = 0;

def index(request):
    return render(request, 'digestif/index.html') # show just plain index page

def explore(request):
    #populate()
    conclusion_pages = ConclusionPage.objects.order_by('platform') # get ConclusionPages ordered by platform name
    platforms = ConclusionPage.objects.order_by('platform').values('platform').distinct() # get unique set of platforms
    acknowledgements = Block.objects.filter(block_type='acknowledgements')
    community_building = Block.objects.filter(block_type='community_building')
    experimental_design = Block.objects.filter(block_type='experimental_design')
    feedback = Block.objects.filter(block_type='feedback')
    other_studies = Block.objects.filter(block_type='other_studies')
    personalized_results = Block.objects.filter(block_type='personalized_results')
    previous_research = Block.objects.filter(block_type='previous_research')
    research_goals = Block.objects.filter(block_type='research_goals')
    research_motivations = Block.objects.filter(block_type='research_motivations')
    share = Block.objects.filter(block_type='share')
    context = {'conclusion_pages' : conclusion_pages, 'platforms' : platforms,
                'acknowledgements' : acknowledgements, 'community_building' : community_building,
                'experimental_design' : experimental_design, 'feedback' : feedback,
                'other_studies' : other_studies, 'personalized_results' : personalized_results,
                'previous_research' : previous_research, 'research_goals' : research_goals,
                'research_motivations' : research_motivations, 'share' : share
                }
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

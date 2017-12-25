# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

from .models import ConclusionPage
from .models import Block
from .utils.populate_cp_blocks import populate # populate the DB with full conclusion pages and blocks
# from .utils.populate_favorites import getFavorites
import json

def index(request):
    return render(request, 'digestif/index.html') # show just plain index page

def explore(request):
    # TODO: Need to come up with a way to only allow populating the Block and
        # Conclusion Pages DB only once
    # populate()
    conclusion_pages = ConclusionPage.objects.order_by('platform') # get ConclusionPages ordered by platform name
    platforms = ConclusionPage.objects.order_by('platform').values('platform').distinct() # get unique set of platforms
    acknowledgements = Block.objects.filter(block_type='acknowledgements')
    research_purpose = Block.objects.filter(block_type='research_purpose')
    study_summary = Block.objects.filter(block_type='study_summary')
    score_interpretation = Block.objects.filter(block_type='score_interpretation')
    personalized_results = Block.objects.filter(block_type='personalized_results')
    social_comparison = Block.objects.filter(block_type='social_comparison')
    share = Block.objects.filter(block_type='share')
    feedback = Block.objects.filter(block_type='feedback')
    other_studies = Block.objects.filter(block_type='other_studies')
    additional_resources = Block.objects.filter(block_type='additional_resources')
    context = {'conclusion_pages' : conclusion_pages, 'platforms' : platforms,
                'acknowledgements' : acknowledgements, 'research_purpose' : research_purpose,
                'study_summary' : study_summary, 'score_interpretation' : score_interpretation,
                'personalized_results' : personalized_results, 'social_comparison' : social_comparison,
                'share' : share, 'feedback' : feedback, 'other_studies' : other_studies, 'additional_resources' : additional_resources}
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

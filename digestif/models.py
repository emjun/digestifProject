# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from jsonfield import JSONField
from django.utils.encoding import python_2_unicode_compatible

# Includes all the meta-data for a conclusion page
# Also stores the file name to the static image associated with the full conclusion page
# Also stores references to the Blocks that store more detailed information and comprise the conclusion page
@python_2_unicode_compatible
class Block(models.Model):
    # block_id = models.CharField(max_length=255, primary_key=True)
    block_type = models.CharField(max_length=100)
    path_name = models.CharField(max_length=200)
    # block_layout = models.CharField(max_length=50)
    content = models.TextField()
    # benefits = models.CharField(max_length=500)
    cp = models.ForeignKey('ConclusionPage')
    """
    block_type refers to the kind of block that it is (e.g., Acknowledgements, Research Goals, etc.)
    path_name refers to the image of the particular block
    content is the HTML describing this block
    cp refers to the ConclusionPage object to which this Block points (Conclusion page it is associated with)
    """

    def __str__(self):
        return "%s" % self.block_type

    def __repr__(self):
        return "%s" % self.block_type



class ConclusionPage(models.Model):
    cp_id = models.CharField(max_length=200, primary_key=True) # used as a primary key
    platform = models.CharField(max_length=200)
    study = models.CharField(max_length=500)

    # let's try not grouping the blocks together in a JSON for now...
    full_page = models.CharField(max_length=200)
    # acknowledgements = models.ForeignKey('Block', on_delete=models.CASCADE,)
    # research_purpose = models.ForeignKey('Block', on_delete=models.CASCADE,)
    # study_summary = models.ForeignKey('Block', on_delete=models.CASCADE,)
    # score_interpretation = models.ForeignKey('Block', on_delete=models.CASCADE,)
    # personalized_results = models.ForeignKey('Block', on_delete=models.CASCADE,)
    # social_comparison = models.ForeignKey('Block', on_delete=models.CASCADE,)
    # share = models.ForeignKey('Block', on_delete=models.CASCADE,)
    # feedback = models.ForeignKey('Block', on_delete=models.CASCADE,)
    # other_studies = models.ForeignKey('Block', on_delete=models.CASCADE,)
    # additional_resources = models.ForeignKey('Block', on_delete=models.CASCADE,)
    content = models.TextField()

    """
    cp_id refers to the primary key id used for this conclusion page instance
    platform refers to the name of the online experimentation platform the conclusion page comes from
    study refers to the study on the "platform" this conclusion page comes from
    full_page is a string to the path name of the full conclusion page image file
    ALL OTHERS are references to the Block models that encapsulate information about the
        individual blocks comprising a full conclusion page (see Block model below)
    """

    blocks = models.ManyToManyField(Block)

    """
    blocks encapsulates all the ForeignKey Blocks that could be part of a Conclusion Page.
    blocks includes
        acknowledgements
        research_purpose
        study_summary
        score_interpretation
        personalized_results
        social_comparison
        share
        feedback
        other_studies
        additional_resources
    """

    def __str__(self):
        # return ",".join(b.block_type for b in self.blocks.all())
        return "%s" % self.cp_id

    def __repr__(self):
        # return "," .join(b.block_type for b in self.blocks.all())
        return "%s" % self.cp_id

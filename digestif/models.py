# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from jsonfield import JSONField
from django.utils.encoding import python_2_unicode_compatible

# Includes all the meta-data for a conclusion page
# Also stores the file name to the static image associated with the full conclusion page
# Also stores references to the Blocks that store more detailed information and comprise the conclusion page
@python_2_unicode_compatible
class ConclusionPage(models.Model):
    cp_id = models.CharField(max_length=200, primary_key=True) # used as a primary key
    platform = models.CharField(max_length=200)
    study = models.CharField(max_length=500)

    # let's try not grouping the blocks together in a JSON for now...
    full_page = models.CharField(max_length=200)
    acknowledgements = models.ForeignKey('Block', on_delete=models.CASCADE,)
    research_purpose = models.ForeignKey('Block', on_delete=models.CASCADE,)
    study_summary = models.ForeignKey('Block', on_delete=models.CASCADE,)
    score_interpretation = models.ForeignKey('Block', on_delete=models.CASCADE,)
    personalized_results = models.ForeignKey('Block', on_delete=models.CASCADE,)
    social_comparison = models.ForeignKey('Block', on_delete=models.CASCADE,)
    share = models.ForeignKey('Block', on_delete=models.CASCADE,)
    feedback = models.ForeignKey('Block', on_delete=models.CASCADE,)
    other_studies = models.ForeignKey('Block', on_delete=models.CASCADE,)
    additional_resources = models.ForeignKey('Block', on_delete=models.CASCADE,)

    """
    cp_id refers to the primary key id used for this conclusion page instance
    platform refers to the name of the online experimentation platform the conclusion page comes from
    study refers to the study on the "platform" this conclusion page comes from
    full_page is a string to the path name of the full conclusion page image file
    ALL OTHERS are references to the Block models that encapsulate information about the
        individual blocks comprising a full conclusion page (see Block model below)
    """

    # path_names = JSONField(default="NULL")
    # """
    #     path_names JSON object should have the following fields:
    #
    #     full
    #     acknowledgements
    #     research_purpose
    #     study_summary
    #     score_interpretation
    #     personalized_results
    #     social_comparison
    #     share
    #     feedback
    #     other_studies
    #     additional_resources
    #
    #     Each of these fields' values will be the file name of the static image
    #     file that corresponds to each full page or block
    # """

    def __str__(self):
        return self.cp_id
    def __repr__(self):
        return self.cp_id


class Block(models.Model):
    path_name = models.CharField(max_length=200)
    block_layout = models.CharField(max_length=50)
    content = JSONField(default="NULL")
    block_type = models.CharField(max_length=100)
    benefits = models.CharField(max_length=500)

    """
    block_layout refers to the basic layout of the block (used to populate a drag/drop elt, default block, etc.)
    content JSON object has the following fields:
        heading
        body
        footnote
    block_type refers to the kind of block that it is (e.g., Acknowledgements, Research Purpose, etc.)
    benefits refers to the benefits that including this block gives researchers and participants (e.g., marketing, outreach, etc.)
    """

    def __str__(self):
        return "".join(self.path_name).join(block_type)

    def __repr__(self):
        return "".join(self.path_name).join(block_type)


"""
block_layout could be "default", type1, type2,...

"""

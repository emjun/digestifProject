# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from jsonfield import JSONField
from django.utils.encoding import python_2_unicode_compatible

# Includes all the meta-data for a conclusion page
# Also stores the file names to the static images associated with the conclusion page
@python_2_unicode_compatible
class ConclusionPage(models.Model):
    cp_id = models.CharField(max_length=200) # used as a primary key
    # image =
    platform = models.CharField(max_length=200)
    study = models.CharField(max_length=500)
    path_names = JSONField(default="NULL")
    """
        path_names JSON object should have the following fields:

        full
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

        Each of these fields' values will be the file name of the static image
        file that corresponds to each full page or block
    """

    def __str__(self):
        return self.cp_id
    def __repr__(self):
        return self.cp_id

# TODO: Look at existing Django packages, etc.
# social media stuff --  should this be a JSON, too?
# Should we just use local storage, too?

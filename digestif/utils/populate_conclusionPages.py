# Run this script to import all the conclusion pages into our database

import os
import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "digestif.settings.local")
django.setup()

from digestif.models import ConclusionPage

# TODO:
# 1. Upload all images we have of the different conclusion pages
#   We may need to crop all the images to their blocks. Save these blocks as
#   separate images.
# 2. Upload all the block images.
# 3. Create new ConclusionPage objects for each study that we have, replacing
#   None with the image file names for the path_names (full and blocks)
# NOTE: There might be a more intelligent/less brute force way to do this.
def populate():
    print ("In populate!")
    ConclusionPage.objects.create(
        cp_id="ct_personality", # abbreviation for platform + study abbreviation
        platform="Cat Tracker",
        study="Personality Survey",
        path_names = {
            'full' : 'cattracker_personality_full.png',
            'acknowledgements' : None,
            'research_purpose' : None,
            'study_summary' : None,
            'score_interpretation' : None,
            'personalized_results' : None,
            'social_comparison' : None,
            'share' : None,
            'feedback' : None,
            'other_studies' : None,
            'additional_resources' : None

        })
    ConclusionPage.objects.create(
        cp_id="dmp_movies",
        platform="DiscoverMyProfile",
        study="Movie Recommendation Study", # get full name of study from platform website
        path_names = {
            'full' : 'dmp_movies_full.png',
            'acknowledgements' : None,
            'research_purpose' : None,
            'study_summary' : None,
            'score_interpretation' : None,
            'personalized_results' : None,
            'social_comparison' : None,
            'share' : None,
            'feedback' : None,
            'other_studies' : None,
            'additional_resources' : None
        })

    cp_set = ConclusionPage.objects.all()
    for cp in cp_set:
        print cp.path_names['full']

if __name__ == '__main__':
    populate()

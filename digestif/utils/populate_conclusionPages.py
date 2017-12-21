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
    ConclusionPage.objects.create(
        cp_id="ct_personality", # abbreviation for platform + study abbreviation
        platform="Cat Tracker",
        study="Personality Survey",
        path_names = {
            'full' : 'full/cattracker_personality.png',
            'acknowledgements' : 'acknowledgements/cattracker_personality.png',
            'research_purpose' : 'research_purpose/cattracker_personality.png',
            'study_summary' : None,
            'score_interpretation' : None,
            'personalized_results' : 'personalized_results/cattracker_personality.png',
            'social_comparison' : None,
            'share' : None,
            'feedback' : None,
            'other_studies' : None,
            'additional_resources' : None
        })
    ConclusionPage.objects.create(
        cp_id="dmp_movies",
        platform="Discover My Profile",
        study="Movie Recommendation Study", # get full name of study from platform website
        path_names = {
            'full' : 'full/dmp_movies.png',
            'acknowledgements' : None,
            'research_purpose' : None,
            'study_summary' : None,
            'score_interpretation' : None,
            'personalized_results' : 'personalized_results/dmp_movies.png',
            'social_comparison' : None,
            'share' : None,
            'feedback' : None,
            'other_studies' : None,
            'additional_resources' : None
        })
    ConclusionPage.objects.create(
        cp_id="dmp_personality",
        platform="Discover My Profile",
        study="Short Personality Test",
        path_names = {
            'full' : 'full/dmp_personality.png',
            'acknowledgements' : 'acknowledgements/dmp_personality.png',
            'research_purpose' : None,
            'study_summary' : None,
            'score_interpretation' : None,
            'personalized_results' : 'personalized_results/dmp_personality.png',
            'social_comparison' : None,
            'share' : 'share/dmp_personality.png',
            'feedback' : None,
            'other_studies' : 'other_studies/dmp_personality.png',
            'additional_resources' : None
        })
    ConclusionPage.objects.create(
        cp_id="gww_whichEnglish",
        platform="Games With Words",
        study="Which English",
        path_names = {
            'full' : 'full/gww_whichEnglish.png',
            'acknowledgements' : None,
            'research_purpose' : None,
            'study_summary' : None,
            'score_interpretation' : None,
            'personalized_results' : 'personalized_results/gww_whichEnglish.png',
            'social_comparison' : None,
            'share' : 'personalized_results/gww_whichEnglish.png',
            'feedback' : None,
            'other_studies' : 'other_studies/gww_whichEnglish.png',
            'additional_resources' : 'additional_resources/gww_whichEnglish.png'
        })
    ConclusionPage.objects.create(
        cp_id="msb_emotion",
        platform="My Social Brain",
        study="Predict Emotion Durations",
        path_names = {
            'full' : 'full/msb_emotion.png',
            'acknowledgements' : 'acknowledgements/msb_emotion.png',
            'research_purpose' : 'research_purpose/msb_emotion.png',
            'study_summary' : 'study_summary/msb_emotion.png',
            'score_interpretation' : 'score_interpretation/msb_emotion.png',
            'personalized_results' : 'personalized_results/msb_emotion.png',
            'social_comparison' : 'social_comparison/msb_emotion.png',
            'share' : 'share/msb_emotion.png',
            'feedback' : 'feedback/msb_emotion.png',
            'other_studies' : 'other_studies/msb_emotion.png',
            'additional_resources' : 'additional_resources/msb_emotion.png'
        })
    ConclusionPage.objects.create(
        cp_id="msb_writing",
        platform="My Social Brain",
        study="Who Do You Write Like?",
        path_names = {
            'full' : 'full/msb_writing.png',
            'acknowledgements' : 'acknowledgements/msb_writing.png',
            'research_purpose' : 'research_purpose/msb_writing.png',
            'study_summary' : 'study_summary/msb_writing.png',
            'score_interpretation' : 'score_interpretation/msb_writing.png',
            'personalized_results' : 'personalized_results/msb_writing.png',
            'social_comparison' : None,
            'share' : 'share/msb_writing.png',
            'feedback' : 'feedback/msb_writing.png',
            'other_studies' : 'other_studies/msb_writing.png',
            'additional_resources' : 'additional_resources/msb_writing.png'
        })
    ConclusionPage.objects.create(
        cp_id="mu_brainType",
        platform="The Musical Universe",
        study="Your Brain Type",
        path_names = {
            'full' : 'full/mu_brainType.png',
            'acknowledgements' : None,
            'research_purpose' : 'research_purpose/mu_brainType.png',
            'study_summary' : None,
            'score_interpretation' : 'score_interpretation/mu_brainType.png',
            'personalized_results' : 'personalized_results/mu_brainType.png',
            'social_comparison' : 'social_comparison/mu_brainType.png',
            'share' : None,
            'feedback' : 'feedback/mu_brainType.png',
            'other_studies' : None,
            'additional_resources' : None
        })
    ConclusionPage.objects.create(
        cp_id="mu_eyes",
        platform="The Musical Universe",
        study="Empathy and Listening Quiz",
        path_names = {
            'full' : 'full/mu_eyes.png',
            'acknowledgements' : None,
            'research_purpose' : 'research_purpose/mu_eyes.png',
            'study_summary' : 'study_summary/mu_eyes.png',
            'score_interpretation' : None,
            'personalized_results' : 'personalized_results/mu_eyes.png',
            'social_comparison' : 'social_comparison/mu_eyes.png',
            'share' : None,
            'feedback' : 'feedback/mu_eyes.png',
            'other_studies' : None,
            'additional_resources' : 'additional_resources/mu_eyes.png'
        })
    ConclusionPage.objects.create(
        cp_id="perfectPitch_thePerfectPitchStudy",
        platform="Perfect Pitch",
        study="The Perfect Pitch Study",
        path_names = {
            'full' : 'full/perfectPitch_thePerfectPitchStudy.png',
            'acknowledgements' : 'acknowledgements/perfectPitch_thePerfectPitchStudy.png',
            'research_purpose' : None,
            'study_summary' : 'study_summary/perfectPitch_thePerfectPitchStudy.png',
            'score_interpretation' : 'score_interpretation/perfectPitch_thePerfectPitchStudy.png',
            'personalized_results' : 'personalized_results/perfectPitch_thePerfectPitchStudy.png',
            'social_comparison' : None,
            'share' : None,
            'feedback' : None,
            'other_studies' : None,
            'additional_resources' : None
        })
    ConclusionPage.objects.create(
        cp_id="pi_genderCareer",
        platform="Project Implicit",
        study="Gender-Career Implicit Attitude Test",
        path_names = {
            'full' : 'full/pi_genderCareer.png',
            'acknowledgements' : None,
            'research_purpose' : None,
            'study_summary' : None,
            'score_interpretation' : 'score_interpretation/pi_genderCareer.png',
            'personalized_results' : 'personalized_results/pi_genderCareer.png',
            'social_comparison' : 'social_comparison/pi_genderCareer.png',
            'share' : 'share/pi_genderCareer.png',
            'feedback' : 'feedback/pi_genderCareer.png',
            'other_studies' : 'other_studies/pi_genderCareer.png',
            'additional_resources' : None
        })
    ConclusionPage.objects.create(
        cp_id="ps_rating",
        platform="Project Soothe",
        study="Survey",
        path_names = {
            'full' : 'full/ps_rating.png',
            'acknowledgements' : 'acknowledgements/ps_rating.png',
            'research_purpose' : 'research_purpose/ps_rating.png',
            'study_summary' : None,
            'score_interpretation' : None,
            'personalized_results' : 'personalized_results/ps_rating.png',
            'social_comparison' : None,
            'share' : None,
            'feedback' : 'feedback/ps_rating.png',
            'other_studies' : 'other_studies/ps_rating.png',
            'additional_resources' : 'additional_resources/ps_rating.png'
        })
    ConclusionPage.objects.create(
        cp_id="tmb_cognitiveSpeed",
        platform="Test My Brain",
        study="Cognitive Speed",
        path_names = {
            'full' : 'full/tmb_cognitiveSpeed.png',
            'acknowledgements' : None,
            'research_purpose' : None,
            'study_summary' : 'study_summary/tmb_cognitiveSpeed.png',
            'score_interpretation' : 'score_interpretation/tmb_cognitiveSpeed.png',
            'personalized_results' : 'personalized_results/tmb_cognitiveSpeed.png',
            'social_comparison' : 'social_comparison/tmb_cognitiveSpeed.png',
            'share' : 'share/tmb_cognitiveSpeed.png',
            'feedback' : 'feedback/tmb_cognitiveSpeed.png',
            'other_studies' : None,
            'additional_resources' : 'additional_resources/tmb_cognitiveSpeed.png'
        })
    ConclusionPage.objects.create(
        cp_id="tmb_famousFaces",
        platform="Test My Brain",
        study="Famous Faces",
        path_names = {
            'full' : 'full/tmb_famousFaces.png',
            'acknowledgements' : None,
            'research_purpose' : None,
            'study_summary' : 'study_summary/tmb_famousFaces.png',
            'score_interpretation' : 'score_interpretation/tmb_famousFaces.png',
            'personalized_results' : 'personalized_results/tmb_famousFaces.png',
            'social_comparison' : 'social_comparison/tmb_famousFaces.png',
            'share' : 'share/tmb_famousFaces.png',
            'feedback' : 'feedback/tmb_famousFaces.png',
            'other_studies' : None,
            'additional_resources' : 'additional_resources/tmb_famousFaces.png'
        })
    ConclusionPage.objects.create(
        cp_id="vs_band",
        platform="Volunteer Science",
        study="Which Band Member are You?",
        path_names = {
            'full' : 'full/vs_band.png',
            'acknowledgements' : None,
            'research_purpose' : None,
            'study_summary' : None,
            'score_interpretation' : None,
            'personalized_results' : 'personalized_results/vs_band.png',
            'social_comparison' : None,
            'share' : None,
            'feedback' : None,
            'other_studies' : None,
            'additional_resources' : None
        })
    ConclusionPage.objects.create(
        cp_id="vs_big5",
        platform="Volunteer Science",
        study="Big Five Personality",
        path_names = {
            'full' : 'full/vs_big5.png',
            'acknowledgements' : 'acknowledgements/vs_big5.png',
            'research_purpose' : None,
            'study_summary' : None,
            'score_interpretation' : None,
            'personalized_results' : 'personalized_results/vs_big5.png',
            'social_comparison' : None,
            'share' : 'share/vs_big5.png',
            'feedback' : 'feedback/vs_big5.png',
            'other_studies' : 'other_studies/vs_big5.png',
            'additional_resources' : 'additional_resources/vs_big5.png'
        })
    ConclusionPage.objects.create(
        cp_id="vs_cows",
        platform="Volunteer Science",
        study="Three Cows",
        path_names = {
            'full' : 'full/vs_cows.png',
            'acknowledgements' : 'acknowledgements/vs_cows.png',
            'research_purpose' : None,
            'study_summary' : None,
            'score_interpretation' : None,
            'personalized_results' : 'personalized_results/vs_cows.png',
            'social_comparison' : None,
            'share' : 'share/vs_cows.png',
            'feedback' : 'feedback/vs_cows.png',
            'other_studies' : 'other_studies/vs_cows.png',
            'additional_resources' : None
        })
    ConclusionPage.objects.create(
        cp_id="vs_individualism",
        platform="Volunteer Science",
        study="Collectivism-Individualism",
        path_names = {
            'full' : 'full/vs_individualism.png',
            'acknowledgements' : None,
            'research_purpose' : None,
            'study_summary' : None,
            'score_interpretation' : None,
            'personalized_results' : 'personalized_results/vs_individualism.png',
            'social_comparison' : None,
            'share' : 'share/vs_individualism.png',
            'feedback' : None,
            'other_studies' : None,
            'additional_resources' : 'additional_resources/vs_individualism.png'
        })
    ConclusionPage.objects.create(
        cp_id="vs_traveling",
        platform="Volunteer Science",
        study="Traveling Salesperson",
        path_names = {
            'full' : 'full/vs_traveling.png',
            'acknowledgements' : 'acknowledgements/vs_traveling.png',
            'research_purpose' : None,
            'study_summary' : None,
            'score_interpretation' : None,
            'personalized_results' : 'personalized_results/vs_traveling.png',
            'social_comparison' : 'social_comparison/vs_traveling.png',
            'share' : 'share/vs_traveling.png',
            'feedback' : 'feedback/vs_traveling.png',
            'other_studies' : 'other_studies/vs_traveling.png',
            'additional_resources' : None
        })
    ConclusionPage.objects.create(
        cp_id="litw_thinkingStyle-pr+other",
        platform="Lab in the Wild",
        study="What is Your Thinking Style?",
        path_names = {
            'full' : 'full/litw_thinkingStyle-pr+other.png',
            'acknowledgements' : 'acknowledgements/litw-acknowledgements.png',
            'research_purpose' : None,
            'study_summary' : None,
            'score_interpretation' : 'score_interpretation/litw_thinkingStyle-pr+other.png',
            'personalized_results' : 'personalized_results/litw_thinkingStyle-pr+other.png',
            'social_comparison' : None,
            'share' : 'share/litw_thinkingStyle-pr+other.png',
            'feedback' : 'feedback/litw_feedback.png',
            'other_studies' : 'other_studies/litw_thinkingStyle-pr+other.png',
            'additional_resources' : None
        })
    ConclusionPage.objects.create(
        cp_id="litw_mealtime",
        platform="Lab in the Wild",
        study="Where in the World Should You Have a Meal?",
        path_names = {
            'full' : 'full/litw-mealtime.png',
            'acknowledgements' : 'acknowledgements/litw-acknowledgements.png',
            'research_purpose' : None,
            'study_summary' : None,
            'score_interpretation' : None,
            'personalized_results' : 'personalized_results/litw-mealtime.png',
            'social_comparison' : None,
            'share' : 'share/litw_share.png',
            'feedback' : 'feedback/litw_feedback.png',
            'other_studies' : 'other_studies/litw-mealtime.png',
            'additional_resources' : None
        })
    ConclusionPage.objects.create(
        cp_id="litw_geometric-pr+other",
        platform="Lab in the Wild",
        study="???",
        path_names = {
            'full' : 'full/litw_geometric-pr+other.png',
            'acknowledgements' : 'acknowledgements/litw-acknowledgements.png',
            'research_purpose' : None,
            'study_summary' : None,
            'score_interpretation' : 'score_interpretation/litw_geometric-pr+other.png',
            'personalized_results' : 'personalized_results/litw_geometric-pr+other.png',
            'social_comparison' : 'social_comparison/litw_geometric-pr+other.png',
            'share' : 'share/litw_geometric-pr+other.png',
            'feedback' : 'feedback/litw_feedback.png',
            'other_studies' : 'other_studies/litw_geometric-pr+other.png',
            'additional_resources' : None
        })
    ConclusionPage.objects.create(
        cp_id="litw_nutrition",
        platform="Lab in the Wild",
        study="How Good is Your Nutrition Knowledge?",
        path_names = {
            'full' : 'full/litw_nutrition.png',
            'acknowledgements' : 'acknowledgements/litw-acknowledgements.png',
            'research_purpose' : None,
            'study_summary' : None,
            'score_interpretation' : None,
            'personalized_results' : 'personalized_results/litw_nutrition.png',
            'social_comparison' : 'social_comparison/litw_nutrition.png',
            'share' : 'share/litw_share.png',
            'feedback' : 'feedback/litw_feedback.png',
            'other_studies' : 'other_studies/litw_nutrition.png',
            'additional_resources' : None
        })
    ConclusionPage.objects.create(
        cp_id="litw_nutrition",
        platform="Lab in the Wild",
        study="How Good is Your Nutrition Knowledge?",
        path_names = {
            'full' : 'full/litw_nutrition.png',
            'acknowledgements' : 'acknowledgements/litw-acknowledgements.png',
            'research_purpose' : None,
            'study_summary' : None,
            'score_interpretation' : None,
            'personalized_results' : 'personalized_results/litw_nutrition.png',
            'social_comparison' : 'social_comparison/litw_nutrition.png',
            'share' : 'share/litw_share.png',
            'feedback' : 'feedback/litw_feedback.png',
            'other_studies' : 'other_studies/litw_nutrition.png',
            'additional_resources' : None
        })

if __name__ == '__main__':
    populate()

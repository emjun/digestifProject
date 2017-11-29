from django.conf.urls import url
from . import views
# from .utils.populate_conclusionPages import populate

# populate() # populate the explore page

app_name = 'digestif'
urlpatterns = [
    # /digestif/
    url(r'^$', views.index, name='index'),
    #/digestif/explore/page_id/
    url(r'^explore/(?P<id>[a-z]*_[a-z]*)/$', views.detail, name='detail'),
    # /digestif/explore/
    url(r'explore/$', views.explore, name='explore'),
    # /digestif/create/
    url(r'create/$', views.create, name='create'),
]

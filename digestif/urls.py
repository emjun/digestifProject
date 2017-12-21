from django.conf.urls import url
from . import views
# from .utils.populate_conclusionPages import populate

# populate() # populate the explore page

app_name = 'digestif'
urlpatterns = [
    # /digestif/
    url(r'^$', views.index, name='index'),
    #/digestif/explore/cp_id/
    url(r'^explore/(?P<id>cp_[a-z]*_[a-z]*)/$', views.cp_detail, name='cp_detail'),
    #/digestif/explore/block_id/
    url(r'^explore/(?P<id>block_[a-z]*_[a-z]*)/$', views.block_detail, name='block_detail'),
    # /digestif/explore/
    url(r'explore/$', views.explore, name='explore'),
    # /digestif/create/
    url(r'create/$', views.create, name='create'),
]

from django.conf.urls import patterns, url, include
from django.conf.urls.static import static
from django.conf import settings

from tiles.views import ProfileImageIndexView,ProfileImageView, ProfileDetailView
from tiles import views

urlpatterns = patterns('',
    url(r'^uploaded/(?P<slug>[-\w]+),(?P<pk>\d+)/$', ProfileDetailView.as_view(),name='profile_image'),
    url(r'^(?P<pk>\d+)/results/$', views.ResultsView.as_view(), name='results'),
    url(r'^(?P<pk>\d+)/$', views.DetailView.as_view(), name='detail'),
) 


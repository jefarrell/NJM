from django.conf.urls import patterns, include, url
from django.contrib import admin

from tiles.views import ProfileImageIndexView
from tiles.views import ProfileImageView, ProfileDetailView
from django.conf import settings

urlpatterns = patterns('',
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', ProfileImageIndexView.as_view(), name='home'),
    url(r'^upload/', ProfileImageView.as_view(), name='profile_image_upload'),
    url(r'^tiles/', include('tiles.urls', namespace="tiles")),url(r'^email-sent/', 'auth.app.views.validation_sent'),
    url(r'^login/$', 'auth.app.views.home'),
    url(r'^logout/$', 'auth.app.views.logout'),
    url(r'^done/$', 'auth.app.views.done', name='done'),
    url(r'^ajax-auth/(?P<backend>[^/]+)/$', 'auth.app.views.ajax_auth',
        name='ajax-auth'),
    url(r'^email/$', 'auth.app.views.require_email', name='require_email'),
    url(r'', include('social.apps.django_app.urls', namespace='social'))
)

if settings.DEBUG:
    urlpatterns += patterns('',
        url(r'^media/(?P<path>.*)$', 'django.views.static.serve', {
            'document_root': settings.MEDIA_ROOT,
        }),
   )


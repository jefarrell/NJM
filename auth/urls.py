from django.conf.urls import patterns, include, url
from django.contrib import admin


admin.autodiscover()

urlpatterns = patterns('',
    url(r'^email-sent/', 'auth.app.views.validation_sent'),
    url(r'^login/$', 'auth.app.views.home'),
    url(r'^logout/$', 'auth.app.views.logout'),
    url(r'^done/$', 'auth.app.views.done', name='done'),
    url(r'^ajax-auth/(?P<backend>[^/]+)/$', 'auth.app.views.ajax_auth',
        name='ajax-auth'),
    url(r'^email/$', 'auth.app.views.require_email', name='require_email'),
    url(r'', include('social.apps.django_app.urls', namespace='social'))
)

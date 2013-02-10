from django.conf.urls import patterns, include, url
from django.http import HttpResponse
from webapp.views import FilterByMuse

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('webapp.views',
    url(r'', include('singly.urls')),
    url(r'^$', 'index', name='index'),
    ('^results$', FilterByMuse),
)

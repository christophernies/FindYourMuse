from django.conf.urls import patterns, include, url
from django.http import HttpResponse
from webapp.views import FilterByMuse

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('webapp.views',
    url(r'', include('singly.urls')),
    url(r'^$', 'index', name='index'),
<<<<<<< HEAD
    url(r'^billbox$', 'billbox2.views.index'),
=======
    ('^results$', FilterByMuse),
>>>>>>> 03c5bbccd64c51c72852c044dbee4816e3e01c48
)


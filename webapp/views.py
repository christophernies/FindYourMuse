from login_credentials import *
from django.shortcuts import render_to_response
from django.template.context import RequestContext
from django.http import HttpResponse
import urllib, httplib2, os, sys, csv, time
from httplib import BadStatusLine
from hearst_apis import *

try:
	import json
except ImportError:
	import simplejson as json

####SETTINGS####
cloudmine_url_base = 'https://api.cloudmine.me/v1/app'
hearst_url_base = 'http://hearst.api.mashery.com/'
gilt_url_base = 'https://api.gilt.com/v1'

def index(request, template='index.html'):
    services = [
        'Facebook',
        'foursquare',
        'Instagram',
        'Tumblr',
        'Twitter',
        'LinkedIn',
        'FitBit',
        'Email'
    ]
    if request.user.is_authenticated():
        user_profile = request.user.get_profile()
        profiles = user_profile.profiles
    response = render_to_response(
            template, locals(), context_instance=RequestContext(request)
        )
    return response

def FilterByMuse(request):
	if 'q' in request.GET:
		search_term = request.GET['q']
		return render_to_response('index.html',{"search_term": search_term})
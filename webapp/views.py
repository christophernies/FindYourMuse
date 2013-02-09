from django.shortcuts import render_to_response
from django.template.context import RequestContext
from django.http import HttpResponse
import urllib, httplib2, os, sys, csv, time
from httplib import BadStatusLine
try:
	import json
except ImportError:
	import simplejson as json
	
####SETTINGS####
http = httplib2.Http()
cloudmine_url_base = 'https://api.cloudmine.me/v1/app'
singly_app = ''
singly_api_key = ''

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
from login_credentials import *
from django.shortcuts import render_to_response
from django.template.context import RequestContext
from django.http import HttpResponse
import urllib, httplib2, os, sys, csv, time
from httplib import BadStatusLine
from hearst_apis import *
from login_credentials import *

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
	array_results = []
	style_dict = {}
	if 'q' in request.GET:
		search_term = request.GET['q']
		search_term = search_term.replace(' ','%20')
		limit = 100
		API_results = ArticleSearch(search_term, limit, hearst_api_key)
		API_JSON = json.loads(API_results)['items']

#Getting rid of articles without images
		good_articles = [];
		for x in API_JSON:
			if str(x).find('IMAGE_1_default_url') != -1:
				if str(x).find('blog_element') != -1:
					if str(x['body'][0]['blog_element']).find(search_term) != -1:
						good_articles.append(x)

		images = []
		description_keywords = json.loads(ArticleImageSearch('', search_term, search_term, limit, hearst_api_key))['items']
		for x in description_keywords:
			images.append(x['default_url'])
		caption_keywords = json.loads(ArticleImageSearch(search_term, '', search_term, limit, hearst_api_key))['items']
		for x in caption_keywords:
			images.append(x['default_url'])
		caption_description = json.loads(ArticleImageSearch(search_term, search_term, '', limit, hearst_api_key))['items']
		for x in caption_description:
			images.append(x['default_url'])
		
		for x in images[:]:
			if x.find('handbag') != -1:
				images.remove(x)

		for x in images:
			print str(x) + '\n'


		
		API_JSON = good_articles

		# return render_to_response('index.html')

		for x in range(len(API_JSON)):
			style_dict['image'] = API_JSON[x]['IMAGE_1_default_url']
			style_dict['url'] = API_JSON[x]['canonical_url']
			style_dict['title'] = API_JSON[x]['title']
			style_dict['text'] = API_JSON[x]['body'][0]['blog_element'][0]['paragraph']
			array_results.append(style_dict)
			style_dict = {}
		link_to_profile = ''
		return render_to_response('index.html',{"search_term": array_results, "link_to_profile":link_to_profile})
			
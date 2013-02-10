import urllib, httplib2, os, sys, csv, time
from login_credentials import *
from httplib import BadStatusLine
try:
	import json
except ImportError:
	import simplejson as json

http = httplib2.Http()

gilt_url_base = 'https://api.gilt.com/v1'

def GiltUpcomingSales(store):
	if store != '':
		url = '/sales/' + store + '/upcoming.json?apikey=' + gilt_api_key
	else:
		url = '/sales/upcoming.json&apikey=' + gilt_api_key
	print url
	headers = {}
	body = ""
	response, content = http.request(gilt_url_base+url, 'GET', headers=headers, body=body)
	return content

def GiltSaleDetail(store, sale_key):
	if store != '':
		url = '/sales/' + store + '/' + sale_key + 'detail.json?apikey=' + gilt_api_key
	print url
	headers = {}
	body = ""
	response, content = http.request(gilt_url_base+url, 'GET', headers=headers, body=body)
	return content
	
def GiltProductDetail(product_id, store):
	if store != '':
		url = '/products/' + product_id + '/detail.json?apikey=' + gilt_api_key
	print url
	headers = {}
	body = ""
	response, content = http.request(gilt_url_base+url, 'GET', headers=headers, body=body)
	return content
	
def GiltProductDetail(store):
	if store != '':
		url = '/products/categories.json?apikey=' + gilt_api_key
	print url
	headers = {}
	body = ""
	response, content = http.request(gilt_url_base+url, 'GET', headers=headers, body=body)
	return content

def GiltActiveSales(store):
	if store != '':
		url = '/sales/' + store + '/active.json?apikey=' + gilt_api_key
	else:
		url = '/sales/active.json&apikey=' + gilt_api_key
	print url
	headers = {}
	body = ""
	response, content = http.request(gilt_url_base+url, 'GET', headers=headers, body=body)
	return content

def GiltLookup(url):
    url = url + '?apikey=' + gilt_api_key
    print "now url is " + url
    response, content = http.request(url, 'GET', headers={}, body="")
    return content
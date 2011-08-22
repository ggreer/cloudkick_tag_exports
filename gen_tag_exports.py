#!/usr/bin/env python

import urllib, urllib2
import re
try:
    import simplejson as json
except ImportError:
    import json

# TODO: grab these from cloudkick.conf or prompt for them
key = 'xxxxxxxx'
secret = 'yyyyyyyyy'

base_url = 'https://api.cloudkick.com/'

req_url = base_url + 'oauth/token'
post_data = { 'client_id': key,
              'client_secret': secret,
              'grant_type': 'client_credentials',
            }

# Get token
oauth_token_req = urllib2.urlopen(url=req_url, data=urllib.urlencode(post_data))
oauth_token_resp = oauth_token_req.read()
oauth_token = json.loads(oauth_token_resp)
oauth_token = oauth_token.get('access_token')

# Get list of nodes
req_url = base_url + ('2.0/nodes?oauth_token=%s' % oauth_token)
node_list_req = urllib2.urlopen(url=req_url)

node_list_resp = node_list_req.read()
node_list = json.loads(node_list_resp)
tag_list = {}

# Grab IPs and tag names
for node in node_list['items']:
    ip = node.get('public_ips')[0]
    for tag in node.get('tags'):
        tag_name = tag['name']
        if tag_list.get(tag_name):
            tag_list[tag_name].append(ip)
        else:
            tag_list[tag_name] = [ip]

# Print it in a useful format
for tag_name,ips in tag_list.items():
    tag_name = tag_name.upper()
    tag_name = re.sub(' ', '_', tag_name)
    ip_str = ''
    for ip in ips:
        ip_str += ip + ' '
    ip_str = ip_str.rstrip()
    print 'export TAG_%s="%s"' % (tag_name, ip_str)

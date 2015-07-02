from __future__ import absolute_import

import json
import argparse
import logging

import requests_oauthlib
import oauthlib

logging.basicConfig(level=logging.DEBUG)

parser = argparse.ArgumentParser(description="REST client")
parser.add_argument('configfile', help='Json file with config values.',
                    type=argparse.FileType('r'))

parsed = parser.parse_args()

config = parsed.configfile
js = json.load(config)

baseurl = js['baseurl']
username = js['username']
password = js['password']
clientid = js['clientid']
clientsecret = js['clientsecret']
redirecturi = js['redirecturi']

tokenurl = baseurl + '/o/token/'
print(tokenurl)

client = oauthlib.oauth2.LegacyApplicationClient(clientid)
session = requests_oauthlib.OAuth2Session(clientid, client=client,
                                          redirect_uri=redirecturi)
token = session.fetch_token(tokenurl, username=username, password=password,
                            client_id=clientid, client_secret=clientsecret,
                            verify=False, method='POST')

r = session.get(baseurl + '/api/users/').json()
userfound = False
for userdict in r:
    if userdict['username'] == username:
        userfound = True
        print("Found user %s" % username)
assert userfound, "Could not find user %s in users" % username

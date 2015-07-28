from __future__ import absolute_import

import argparse
import json
import logging

import oauthlib
import requests_oauthlib

import clusterlogger

logging.basicConfig(level=logging.INFO)


def setup_logger(name, host, port):
    log = logging.getLogger(name)
    handler = clusterlogger.GELFTCPHandler(host, port)
    log.addHandler(handler)
    log.addFilter(clusterlogger.HazelHenFilter())
    return log


def create_parser():
    parser = argparse.ArgumentParser(description="REST client")
    parser.add_argument('configfile', help='Json file with config values.',
                        type=argparse.FileType('r'))
    return parser


def check_result(result):
    userfound = False
    for userdict in r:
        if userdict['username'] == username:
            userfound = True
            log.info('Found User %s', username)
            break
    else:
        log.error('Could not find user %s in users', username)
        assert userfound, "Could not find user %s in users" % username


parser = create_parser()
parsed = parser.parse_args()

config = parsed.configfile
js = json.load(config)

host = js['host']
logport = js['logport']
username = js['username']
password = js['password']
clientid = js['clientid']
clientsecret = js['clientsecret']
redirecturi = js['redirecturi']

log = setup_logger('clusterclient', host, logport)

baseurl = 'https://' + host
tokenurl = baseurl + '/o/token/'

log.info('User: %s', username)
log.info('ClientID: %s', clientid)
log.info('Tokenurl: %s', tokenurl)

client = oauthlib.oauth2.LegacyApplicationClient(clientid)
session = requests_oauthlib.OAuth2Session(clientid, client=client,
                                          redirect_uri=redirecturi)
log.info('Requesting token')
token = session.fetch_token(tokenurl, username=username, password=password,
                            client_id=clientid, client_secret=clientsecret,
                            verify=False, method='POST')
log.info('Token received')
log.info('Requesting users')
r = session.get(baseurl + '/api/users/').json()
log.info('Received: %s', r)
check_result(r)

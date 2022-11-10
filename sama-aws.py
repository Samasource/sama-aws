#!/usr/bin/env python3
import argparse
import configparser
import json
from pathlib import Path
import os
import time
import urllib.request


def get_temp_credentials(project_id):

    f = open(os.path.join(Path.home(), '.sama.json'), "r")
    sama_config = json.load(f)

    # open a connection to a URL using urllib
    resp = urllib.request.urlopen(
        "https://api.sama.com/v2/projects/%s/credentials.json?access_key=%s" % (project_id, sama_config['apiKey']))
    return json.load(resp)


def refresh_credentials(profile, project_id):
    print('refreshing %s credentials' % (profile))

    credentials_file = os.path.join(Path.home(), '.aws/credentials')
    config = configparser.ConfigParser()
    config.read(credentials_file)

    temp_creds = get_temp_credentials(project_id)

    config[profile]['aws_access_key_id'] = temp_creds['access_key_id']
    config[profile]['aws_secret_access_key'] = temp_creds['secret_access_key']
    config[profile]['aws_session_token'] = temp_creds['session_token']

    with open(credentials_file, 'w') as configfile:
        config.write(configfile)


parser = argparse.ArgumentParser(
    prog='sama-aws',
    description='Get Sama temporary credentials')

parser.add_argument('action', choices=[
                    'configure', 'print', 'update-credentials-file'])

parser.add_argument('-i', '--project-id', type=int,
                    required=True, help="The Sama project id")
parser.add_argument(
    '-p', '--profile',
    help="The AWS CLI profile to refresh in ~/.aws/credentials (default: %(default)s)",
    default="sama-cyberduck")

args = parser.parse_args()

if (args.action == 'print'):
    temp_creds = get_temp_credentials(args.project_id)

    output = {
        "Version": 1,
        "AccessKeyId": temp_creds['access_key_id'],
        "SecretAccessKey": temp_creds['secret_access_key'],
        "SessionToken": temp_creds['session_token'],
        "Expiration": temp_creds['expiration'],
    }
    print(json.dumps(output))

if (args.action == 'update-credentials-file'):

    while (True):
        refresh_credentials(args.profile, args.project_id)
        print('Sleeping for 45 minutes...')
        time.sleep(2700)

#!/usr/bin/env python3
import argparse
import configparser
import json
from pathlib import Path
import os
import time
import urllib.request


def get_sama_aws_config():
    f = open(os.path.join(Path.home(), '.sama-aws.json'), "r")
    return json.load(f)


def get_project_info(project_id):

    sama_config = get_sama_aws_config()

    # open a connection to a URL using urllib
    resp = urllib.request.urlopen(
        "https://api.sama.com/v2/projects/%s.json?access_key=%s" % (project_id, sama_config['apiKey']))

    return json.load(resp)


def get_temp_credentials(project_id):

    sama_config = get_sama_aws_config()
    project_id = project_id if project_id else sama_config['projectID']

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

    try: 
        config[profile]
    except:
        config[profile] = {}

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
                    help="The Sama project id")
parser.add_argument(
    '-p', '--profile',
    help="The AWS CLI profile to refresh in ~/.aws/credentials (default: %(default)s)",
    default="sama-cyberduck")

args = parser.parse_args()


if (args.action == 'configure'):

    try:
        config = get_sama_aws_config()
    except:
        config = {
            "apiKey": "",
            "projectID": "",
        }

    api_key = input("API Key: (%s) " % (config['apiKey']))
    if (api_key != ""):
        config['apiKey'] = api_key

    project_id = input("Project ID: (%s) " % (config['projectID']))
    if (project_id != ""):
        config['projectID'] = project_id

    with open(os.path.join(Path.home(), '.sama-aws.json'), 'w') as configfile:
        configfile.write(json.dumps(config))

    info = get_project_info(config['projectID'])

    print('')
    print('Success!')
    print("Assets S3 URL: %s" % (info['asset_s3_url']))


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

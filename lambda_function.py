import os

import boto3
from botocore.exceptions import ClientError
import tweepy

BUCKET_NAME = os.environ['BUCKET_NAME']
KEY = 'jobs.txt'

s3 = boto3.resource('s3')
ssm = boto3.client('ssm')

def get_params(name):
    response = ssm.get_params(Name=name, WithDecryption=True)
    credentials = response['Parameter']['Value']
    return credentials

def get_job_desc():
    filename = '/tmp/' + KEY
    try:
        s3.Bucket(BUCKET_NAME).download_file(KEY, filename)
    except ClientError as e:
        if e.response['Error']['Code'] == '404':
            print(f'The object {KEY} does not exist in bucket {BUCKET_NAME}')
        else:
            raise
    
    with open(filename) as f:
        lines = f.readlines()
        return lines[-2]
        # seeing the latest entry to the txt update
        # the write skips a line in the file so it may need -2

def lambda_handler(event, context):
    #SSM Parameters
    CONSUMER_KEY = get_params('/Techjobstxbot/consumer_key')
    CONSUMER_SECRET = get_params('/Techjobstxbot/consumer_secret')
    ACCESS_TOKEN = get_params('/Techjobstxbot/access_token')
    ACCESS_TOKEN_SECRET = get_params('/Techjobstxbot/access_token_secret')

    #authenticate using tweepy
    auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
    auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
    api = tweepy.API(auth)

    #sending tweet
    tweet = get_job_desc()
    print(tweet)
    api.update_status(tweet)

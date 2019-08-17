#!/usr/bin/env python
# -*- coding: UTF-8
'''
    Simple Constants File
'''
__author__ = 'Jose Epifanio'
__licence__ = 'MIT'
__version__ = '0.0.1'
__email__ = 'jose.epifanio90@gmail.com'
__status__ = 'Development'


class Constants:
    ENV_FILE_NOT_FOUND = '[ERR] Hey! You\'re missing the .env' \
        'file with your API_KEY and API_SECRET_KEY'
    ENV_MISSING_KEYS = '[ERR] Yo! I need API_KEY, API_SECRET_KEY, ' \
        'ACCESS_TKN, ACCESS_TKN_SECRET defined in your .env file'
    INVALID_AUTH = '[ERR] It seems your credentials are off... Check them out!'
    FAILED_USER_SEARCH = '[ERR] Failed to retrieve the specified user'
    FAILED_REPORT_SEARCH = '[ERR] Failed to retrieve the specified report'
    FAILED_REPORT = '[ERR] Failed to create the report for the specified user'
    FAILED_RETRIEVENG_TWEETS = '[ERR] Failed to retrieve the user tweets'
    FAILED_RETRIEVENG_RETWEETS = '[ERR] Failed to retrieve the tweet replies'
    FAILED_PUBLISH = '[ERR] Failed to publis the report to twitter'

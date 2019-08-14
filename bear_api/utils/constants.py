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
    # Logger Actions
    AUTH_CREDENTIALS = 'Trying to validate the api keys'
    # Error Messages
    RETRIEVENG_USER = '[ERR] Failed to retrieve the specified user'
    UPDATING_STATUS = '[ERR] Posting Results'
    ANALYSING_TWEETS = '[ERR] Analysing tweets'
    RETRIEVING_TWEETS = '[ERR] Retrieving tweets'
    WRONG_TYPE_USR = '[ERR] User Input Menu'
    ENV_FILE_NOT_FOUND = '[ERR] Hey! You\'re missing the .env' \
        'file with your API_KEY and API_SECRET_KEY'
    ENV_MISSING_KEYS = '[ERR] Yo! I need API_KEY, API_SECRET_KEY, ' \
        'ACCESS_TKN, ACCESS_TKN_SECRET defined in your .env file'
    INVALID_AUTH = '[ERR] It seems your credentials are off... Check them out!'

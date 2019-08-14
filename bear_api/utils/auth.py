#!/usr/bin/env python
# -*- coding: UTF-8
import os

from dotenv import load_dotenv
import tweepy

from bear_api.utils.constants import Constants
'''
    Auth Class that checks for api keys in your env file
'''
__author__ = 'Jose Epifanio'
__licence__ = 'MIT'
__version__ = '0.0.1'
__email__ = 'jose.epifanio90@gmail.com'
__status__ = 'Development'


class Auth:
    def __init__(self):
        self.keys = dict()
        self.__fetch_api_keys()

    def get_auth_connection(self) -> object:
        api = tweepy.API(self.__get_auth_handler())
        try:
            api.verify_credentials()
            return api
        except Exception as e:
            self.logger.log(str(e), Constants.AUTH_CREDENTIALS)
            print(Constants.INVALID_AUTH)

    def __get_auth_handler(self) -> object:
        auth = tweepy.OAuthHandler(
            self.keys['API_KEY'],
            self.keys['API_SECRET_KEY']
        )
        auth.set_access_token(
            self.keys['ACCESS_TKN'],
            self.keys['ACCESS_TKN_SECRET']
        )

        return auth

    def __fetch_api_keys(self) -> None:
        self.__check_file()
        load_dotenv()
        self.__check_keys()

    def __check_file(self) -> None:
        if not os.path.exists('.env'):
            raise Exception(Constants.ENV_FILE_NOT_FOUND)

    def __check_keys(self) -> None:
        keys = ['API_KEY', 'API_SECRET_KEY', 'ACCESS_TKN', 'ACCESS_TKN_SECRET']

        for key in keys:
            if os.getenv(key) is None:
                raise Exception(Constants.ENV_MISSING_KEYS)
            else:
                self.keys[key] = os.getenv(key)

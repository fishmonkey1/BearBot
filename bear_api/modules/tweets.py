#!/usr/bin/env python
# -*- coding: UTF-8
import re

import tweepy
from textblob import TextBlob

from bear_api.utils.logger import Logger
from bear_api.utils.constants import Constants
'''
    Tweets Manager: Create, Update, Retrieve, Delete and more...
'''
__author__ = 'Jose Epifanio'
__licence__ = 'MIT'
__version__ = '0.0.1'
__email__ = 'jose.epifanio90@gmail.com'
__status__ = 'Development'


class TweetsModule:
    def __init__(self, api: tweepy.API, logger: Logger):
        self.api = api
        self.logger = logger

    def find(self, user: str, count: int, page: int):
        if user[0] != '@':
            user = '@' + user
        users = list()
        for user in self.api.search_users(user, count=count, page=page):
            users.append({
                'name': user.name,
                'screenName': user.screen_name,
                'url': user.url,
                'img': user.profile_image_url_https,
                'description': user.description,
                'tweets': user.statuses_count,
                'verified': user.verified,
                'followers': user.followers_count,
                'following': user.friends_count
            })
        return users

    def generate_analysis(self, user: str, tweet_count: int):
        try:
            tweets = self.__get_tweets(user, tweet_count)
            pos_tweets = [tw for tw in tweets if tw['sentiment'] == 'positive']
            neg_tweets = [tw for tw in tweets if tw['sentiment'] == 'negative']
            neutral_tweets = 100 * (len(tweets) - len(neg_tweets) - len(pos_tweets)) / len(tweets)  # nopep8
            results = {
                'positive': round(100 * len(pos_tweets) / len(tweets)),
                'negative': round(100 * len(neg_tweets) / len(tweets)),
                'neutral': round(100 * (len(tweets) - len(neg_tweets) - len(pos_tweets)) / len(tweets))  # nopep8
            }

            self.publish(results, user, tweet_count)

            return results
        except Exception as e:
            self.logger.log(str(e), Constants.ANALYSING_TWEETS)
            print('Failed to generate the sentiment analysis!')

    def publish(self, results, usr: str, tweets_count: int):
            try:
                tweet = f'Tweet Analysis Complete! \nUser @{usr} - ' \
                    f'{tweets_count} Tweets Were Used - Results: \n'

                for key in results:
                    tweet += f'{key.capitalize()} Tweets: {results[key]}% \n'

                self.api.update_status(tweet)
            except Exception as e:
                self.logger.log(str(e), Constants.UPDATING_STATUS)

    def __get_tweets(self, user: str, tweet_count: int):
        if user[0] != '@':
            user = '@' + user
        tweets = list()
        try:
            for tweet in self.api.user_timeline(user, count=tweet_count):
                parsed_tweet = dict(
                    text=tweet.text,
                    sentiment=self.__get_sentiment(tweet.text)
                )
                if tweet.retweet_count > 0:
                    if parsed_tweet not in tweets:
                        tweets.append(parsed_tweet)
                else:
                    tweets.append(parsed_tweet)

            return tweets
        except Exception as e:
            self.logger.log(str(e), Constants.RETRIEVING_TWEETS)
            print(str(e))

    def __get_sentiment(self, tweet: object):
        analysis = TextBlob(self.__clean(tweet))
        sentiment_type = ''
        if analysis.sentiment.polarity > 0:
            sentiment_type = 'positive'
        elif analysis.sentiment.polarity == 0:
            sentiment_type = 'neutral'
        else:
            sentiment_type = 'negative'

        return sentiment_type

    def __clean(self, tweet: str):
        return ' '.join(
            re.sub(
                "(@[A-Za-z0-9]+)|([^0-9A-Za-z \t])|(\w+:\/\/\S+)",
                " ",
                tweet
            ).split()
        )

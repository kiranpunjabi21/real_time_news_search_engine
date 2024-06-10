from newsapi import NewsApiCLient
from newsdataapi import NewsDataApiClient
from pydantic import ValidationError

from settings import settings
from models import NewsAPIModel, NewsDataIOModel

import logging
import datetime
import functools


class NewsFetcher():
    '''Class for fetching news from various API'''
    newsapi = NewsApiCLient(api_key = settings.NEWSAPI_KEY)
    newsdataapi = NewsDataApiClient(api_key = settings.NEWSDATAIO_KEY)
    time_window = 24 #Fetch news once in a day


    def fetch_from_newsapi():
        response = newsapi.get_everything(q=settings.NEWS_TOPIC)
        return [NewsAPIModel(**article).to_common() for article in response.get('articles',[])]
    
    def fetch_from_newsdataapi():
        response = newsdataapi.get_everything(q=settings.NEWS_TOPIC)
        return [NewsDataIOModel(**article).to_common() for article in response.get('articles',[])]
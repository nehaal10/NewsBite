'''extracts article data'''

import os
import sys
import requests
from bs4 import BeautifulSoup as bsoup
from src.logger import logging
from src.exception import CustomException
from config.webCrawlerConfig import WebCrawlerConfig

class article:
    def __init__(self) -> None:
        self.article_data = WebCrawlerConfig.article_data

    def article_information(self,url):
        logging.info("scrapping articles news")
        try:
            article=[]
            res=requests.get(url).text
            content=bsoup(res,'html.parser')
            data=content.find('div',class_='body-copy')
            article_data= data.find_all(['p','li','h4','h3','h2','h1'])
            for i in article_data:
                article.append(i.get_text())

            logging.info("scrapped succesfully")

            return ' '.join(article)
        except Exception as e:
            logging.info("exception raised")
            raise CustomException(e,sys)

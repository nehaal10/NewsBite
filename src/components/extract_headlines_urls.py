'''Extracts all the headlines of different news articles and and those article links respectivly'''

from src.exception import CustomException
from src.logger import logging
from config.webCrawlerConfig import WebCrawlerConfig
import sys
import requests
from bs4 import BeautifulSoup as bsoup
from dataclasses import dataclass

class extract_urls_headlines:
    def __init__(self):
        self.final = WebCrawlerConfig.final
        self.date  = '22'  #need to changed
        self.dates = WebCrawlerConfig.dates
        self.dict_store_values = WebCrawlerConfig.dict_store_values

    def extract(self,url):
        logging.info('started extracting headlines and urls')
        try:
            response = requests.get(url)
            content=bsoup(response.text,'html.parser') 
            all_data=content.find_all(['h3','h2','div'],class_=['entry-title','entry-title','entry-meta'])

            for i in range(len(all_data)):
        
                if all_data[i].name == 'h3':
                    if all_data[i].find('span').get('class')[-1]=='metered':
                        link=all_data[i].find_all('a')[-1].get('href')
                        link_date = link.split('.com')[-1].split('/')[3]
                        self.dates.append(link_date)
                        self.dict_store_values[all_data[i].find('span').get_text().strip()]=[link,link_date]

                else:
                    if all_data[i].name == 'h2':
                        if all_data[i].find('span').get('class')[-1]=='metered':
                            self.dates.append(all_data[i+1].find('time').get_text().split()[1].split(',')[0])
                            self.dict_store_values[all_data[i].find('span').get_text().strip()] = [all_data[i].find_all('a')[-1].get('href'),
                                                                            all_data[i+1].find('time').get_text().split()[1].split(',')[0]]
                            
            for i in list(self.dict_store_values.keys()):
                if self.dict_store_values[i][-1] == self.date:
                    self.final[i] = self.dict_store_values[i][0]

            if self.dates[-1] ==  self.date:
            #do load more 
                url_next_page=content.find('a',class_='load-more').get('href')
                self.extract(url_next_page)

            headlines = list(self.final.keys())
            urls = list(self.final.values())
            return headlines,urls
        
        except Exception as e:
            logging.info("exception occured")
            raise CustomException(e,sys)

'''to get date'''

import os
import sys
from config.webCrawlerConfig import WebCrawlerConfig
from src.exception import CustomException
from bs4 import BeautifulSoup as bsoup
from src.logger import logging
import requests
import calendar

class USA_date:
    def __init__(self) -> None:
        self.website = WebCrawlerConfig.website

    def date(self):
        logging.info("getting USA date")
        try:
            response = requests.get('https://www.siliconvalley.com')
            content=bsoup(response.text,'html.parser')
            date=content.find('div',class_='date').get_text().strip().split('\n')[0].strip()
            date_month_year=date.split(',')[-1].strip().split()
            month_name_to_num={month: index for index, month in enumerate(calendar.month_abbr) if month}
            month_num=month_name_to_num[date_month_year[0]]
            if month_num < 10:
                month_num = '0'+str(month_num)
            date='' .join((z for z in date_month_year[1] if  z.isdigit()))
            year=date_month_year[-1]

            return (
                date,
                month_num,
                year
            )
        except Exception as e:
            logging.info("exception raised")
            raise CustomException(e,sys)

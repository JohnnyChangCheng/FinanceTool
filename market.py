from selenium import webdriver
from collections import namedtuple
from bs4 import BeautifulSoup
import time
import requests
from io import StringIO
import pandas as pd
import numpy as np

class Market():
    def index( self ):
        self.driverpath = "./geckodriver"
        self.driver = webdriver.Firefox(executable_path=self.driverpath)
        self.finance_url = "https://finance.yahoo.com/"
        self.driver.get(self.finance_url)
        self.naming = ["S&P500", "DowJones", "NASDAQ", "Oil Crude"]
        self.index = []
        self.index_css_selector = [
                                  "#marketsummary-itm-\^GSPC > h3:nth-child(1) > span:nth-child(3)",
                                  "#marketsummary-itm-\^DJI > h3:nth-child(1) > span:nth-child(3)",
                                  "#marketsummary-itm-\^IXIC > h3:nth-child(1) > span:nth-child(3)",
                                  "#marketsummary-itm-CL\=F > h3:nth-child(1) > span:nth-child(3)"
                                  ]
        self.rate = []
        self.rate_css_selector = [
                                 "#marketsummary-itm-\^GSPC > h3:nth-child(1) > div:nth-child(4) > span:nth-child(2)",
                                 "#marketsummary-itm-\^DJI > h3:nth-child(1) > div:nth-child(4) > span:nth-child(2)",
                                 "#marketsummary-itm-\^IXIC > h3:nth-child(1) > div:nth-child(4) > span:nth-child(2)",
                                 "#marketsummary-itm-CL\=F > h3:nth-child(1) > div:nth-child(4) > span:nth-child(2)"
                                 ]
        self.incremental = []
        self.incremental_css_selector = [
                                        "#marketsummary-itm-\^GSPC > h3:nth-child(1) > div:nth-child(4) > span:nth-child(1)",
                                        "#marketsummary-itm-\^DJI > h3:nth-child(1) > div:nth-child(4) > span:nth-child(1)",
                                        "#marketsummary-itm-\^IXIC > h3:nth-child(1) > div:nth-child(4) > span:nth-child(1)",
                                        "#marketsummary-itm-CL\=F > h3:nth-child(1) > div:nth-child(4) > span:nth-child(1)"
                                        ]
        for css in self.index_css_selector :
            value = self.driver.find_element_by_css_selector(css)
            self.index.append(value.text)
        
        for css in self.incremental_css_selector :
            value = self.driver.find_element_by_css_selector(css)
            self.rate.append(value.text)
        
        for css in self.rate_css_selector :
            value = self.driver.find_element_by_css_selector(css)
            self.incremental.append(value.text)       

        print(self.naming)
        print(self.index)
        print(self.rate)
        print(self.incremental)
        self.driver.close()
    
    def twse( self ):
        self.TWSE_TABLE_LIST = ["價格指數(臺灣證券交易所)", 
                          "大盤統計資訊",
                          "漲跌證券數合計",
                          "每日收盤行情(全部(不含權證、牛熊證))"]
        self.twse_table = []
        datestr = '20200131'
        r = requests.post('https://www.twse.com.tw/exchangeReport/MI_INDEX?response=html&date=' + datestr + '&type=ALLBUT0999')   
        soup = BeautifulSoup(r.text, 'html.parser')
        
        self.twse_table.append( soup.find_all('table')[0] )    
        self.twse_table.append( soup.find_all('table')[6] )    
        self.twse_table.append( soup.find_all('table')[7] )
        self.twse_table.append( soup.find_all('table')[8] )        
        
        print(  self.twse_table[2] )
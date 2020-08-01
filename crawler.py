from selenium import webdriver
from collections import namedtuple
import time
    
class Crawler():
    def __init__( self ):
        self.driverpath = "/home/johnny/finance/geckodriver"
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
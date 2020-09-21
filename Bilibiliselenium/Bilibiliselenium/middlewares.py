from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from scrapy.http import HtmlResponse
from logging import getLogger
import random

class BilibiliseleniumMiddleware():
    def __init__(self, timeout = None):
        self.logger = getLogger(__name__)
        self.timeout = timeout
        self.browser = webdriver.Chrome()
        self.browser.set_window_size(1400, 700)
        self.browser.set_page_load_timeout(self.timeout)
        self.wait = WebDriverWait(self.browser, self.timeout)

    def __del__(self):
        self.browser.close()

    def process_request(self, request, spider):
        self.logger.debug('Chrome is starting')
        try:
            self.browser.get(request.url)
            self.wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, 'li.article-item')))
            return HtmlResponse(url = request.url, body = self.browser.page_source, request = request, encoding = 'utf-8', status = 200)
        except TimeoutException:
            return HtmlResponse(url = request.url, status = 500, request = request)
        
    
    @classmethod
    def from_crawler(cls, crawler):
        return cls(timeout = crawler.settings.get('SELENIUM_TIMEOUT'))


class UserAgentMiddleware():
    def __init__(self):
        self.user_agents = [
            'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/535.1 (KHTML, like Gecko) Chrome/14.0.835.163 Safari/535.1',
            'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:6.0) Gecko/20100101 Firefox/6.0',
            'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/534.50 (KHTML, like Gecko) Version/5.1 Safari/534.50'
        ]
     
    def process_request(self, request, spider):
        request.headers['User-Agent'] = random.choice(self.user_agents)


#class ProxyMiddleware():
#   def __init__(self, proxy_url):
#        self.logger = getLogger(__name__)
#        self.proxy_url = proxy_url

#    def process_request(self, request, spider):
        
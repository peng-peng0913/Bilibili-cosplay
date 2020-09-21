import scrapy
from urllib.parse import quote
from Bilibiliselenium.items import BilibiliseleniumItem
from scrapy import Request, Spider


class BilibiliSpider(scrapy.Spider):
    name = 'bilibili'
    allowed_domains = ['www.bilibili.com']
    base_url = 'https://search.bilibili.com/article?keyword='

    KEYWORDS = ['cosplay']

    def start_requests(self):
        for keyword in self.KEYWORDS:
            for page in range(1, self.settings.get('MAX_PAGE') + 1):
                url = self.base_url + quote(keyword) + '&page=' + quote(str(page))
                yield Request(url = url, callback = self.parse, meta = {'page' : page}, dont_filter = True)

    def parse(self, response):
        items = response.css('.article-item')
        for item in items:
            data = BilibiliseleniumItem()
            data['id1'] = item.css('a.title::attr(href)').extract_first().replace('//www.bilibili.com/read/', '').replace('//www.bilibili.com/read/', '').replace('?from=search', '')
            data['title'] = item.css('a.title::attr(title)').extract_first()
            data['image'] = item.css('a.poster img::attr(src)').extract_first()
            data['url'] = item.css('a.title::attr(href)').extract_first()
            data['view1'] = item.css('span[title="阅读"]::text').extract_first().strip()
            data['like1'] = item.css('span[title="喜欢"]::text').extract_first().strip()
            data['reply'] = item.css('span[title="global.common"]::text').extract_first().strip()
            yield data
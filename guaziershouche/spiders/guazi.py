# -*- coding: utf-8 -*-
import scrapy
import re
import time
import execjs
# from scrapy.linkextractors import LinkExtractor
# from scrapy.spiders import CrawlSpider, Rule
from guaziershouche.items import GuaziershoucheItem


class GuaziSpider(scrapy.Spider):
    name = 'guazi'
    allowed_domains = ['guazi.com']
    start_urls = ['https://www.guazi.com/su/dazhong/#bread']
    url='https://www.guazi.com/su/dazhong/#bread'
    # rules = (
    #     Rule(LinkExtractor(allow=r'guazi.com/[a-z]/[a-z]/#bread'), callback='start_requests', follow=True),
    # )

    def start_requests(self):
        yield scrapy.Request(url=self.url, dont_filter=True, callback=self.get_cookie)

    def get_cookie(self,response):
        pattern = re.compile('var value=anti\(\'(.*?)\',\'(.*?)\'\);')
        value = re.search(pattern, response.text).groups()

        with open('antipas.js', 'r', encoding='utf-8') as f:
            source = f.read()
            phantom = execjs.get('PhantomJS')
            getpass = phantom.compile(source)
            antipas = getpass.call('get_antipas', value[0], value[1])
            print(antipas)

        cookies = {
            'antipas': antipas
        }
        yield scrapy.Request(url=self.url, cookies=cookies, dont_filter=True, callback=self.parse_city,meta={'usercookie':cookies})

    def parse_city(self, response):
        # print(response.text)
        cookies=response.meta['usercookie']
        city_urls=response.xpath('//div[@class="city-box-left"]/dl/dd/a/@href').extract()
        for city_url in city_urls:
            yield scrapy.Request(url='https://www.guazi.com'+city_url, cookies=cookies,dont_filter=True, callback=self.parse)

    num=0
    def parse(self, response):
        print(response.status)
        self.num += 1
        print(self.num)
        if self.num == 17:
            time.sleep(60)
            self.num=0

        item=GuaziershoucheItem()
        base_url='https://www.guazi.com'
        contents=response.xpath('//ul[@class="carlist clearfix js-top"]/li')
        for content in contents:
            item['car_brand'] = content.xpath('a/h2[@class="t"]/text()').extract_first()
            car_url = content.xpath('a/@href').extract_first()
            item['car_url']=base_url+car_url
            year_mile= content.xpath('a/div[@class="t-i"]//text()').extract()
            item['buy_year'] = year_mile[0]
            item['mile'] = year_mile[2]
            item['sale_price'] = content.xpath('a/div[@class="t-price"]/p//text()').extract_first()
            item['original_price'] = content.xpath('a/div[@class="t-price"]/em//text()').extract_first()
            yield item

        next_url=response.xpath('//ul[@class="pageLink clearfix"]/li[last()]/a/@href').extract_first()
        if next_url:
            yield scrapy.Request(url=base_url+next_url,callback=self.parse)

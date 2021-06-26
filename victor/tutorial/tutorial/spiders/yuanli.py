#!/usr/bin/env python3
import scrapy
from scrapy.selector import Selector
from scrapy.linkextractors import LinkExtractor
from ..items import TutorialItem, BookItem
from w3lib import html
from lxml import etree
import re


class PageSpider(scrapy.Spider):
    name = 'page'
    allowed_domain = ['rumen8.com']
    link_extract = LinkExtractor(allow=r'.+/+\d+.+')
    urls = ['http://rumen8.com/gupiaoshuji/zhuanyetoujiyuanli/']
    page_link = []

    def start_requests(self):
        for url in self.urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response, **kwargs):
        item = TutorialItem()
        links = self.link_extract.extract_links(response)
        for i in links:
            item['link'] = i.url
            yield scrapy.Request(url=i.url, callback=self.detail_parse)
        return item

    def detail_parse(self, response, **kwargs):
        item = BookItem()
        title_doc = response.xpath('/html/body/div[2]/div[1]/div[3]/div[1]/h2').extract()
        # css 选着器 使用 css 的方法定位元素 #(id) .(class) 只收选择标签 两个冒号后面添加的为要提取的内容
        content_doc = response.xpath('/html/body/div[2]/div[1]/div[3]/div[2]').extract()
        try:
            title = html.remove_tags(title_doc[0])
            title_res = re.sub(r'\s+', '', title)
            item['title'] = title_res
            content = html.remove_tags(content_doc[0])
            content_res = re.sub(r'\s+', '', content)
            item['content'] = content_res
        except Exception as e:
            pass
        yield item

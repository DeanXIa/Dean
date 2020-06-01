# -*- coding: utf-8 -*-
import scrapy
import requests
from lxml import etree
from ..items import FirstpaItem

class TestSpider(scrapy.Spider):
    name = 'Test'
    allowed_domains = ['read.qidian.com']
    start_urls = ['https://read.qidian.com/chapter/5YAQ3XblbtNqqtWmhQLkJA2/DJ0272ECn7hp4rPq4Fd4KQ2']

    def parse(self, response):
        titles=response.xpath("//h3/span[contains(text(),\"第\")]/text()").extract()
        contents=response.xpath("//div/p/text()").extract()
        next_url = response.xpath("//a[contains(text(),\"下一章\")]/@href").extract()

        item = FirstpaItem()
        item["title"] = titles
        item["content"] = contents
        yield item

        if next_url:
            next_url = "https:" + str(next_url[0])
            yield scrapy.Request(url=next_url, callback=self.parse)


# def get(url):
#     content=requests.get(url).content
#     page_tree=etree.HTML(content)
#     titles=page_tree.xpath("//h3/span[contains(text(),\"第\")]/text()")
#     contents=page_tree.xpath("//div/p/text()")
#     next_url=page_tree.xpath("//a[contains(text(),\"下一章\")]/@href")
#     if next_url:
#         next_url="https:"+next_url[0]
#     print(content.decode("utf-8"))
#     print(next_url)
    # get(next_url)

# url='https://read.qidian.com/chapter/5YAQ3XblbtNqqtWmhQLkJA2/DJ0272ECn7hp4rPq4Fd4KQ2'
# get(url)
# data_nurl="https://vipreader.qidian.com/chapter/1018389161/529680155"
# data_info={"data-info":"1|529528411|529680155|0|1"}
# r=requests.post(data_nurl,data=data_info).text
# print(r)
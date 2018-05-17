# -*- coding: utf-8 -*-
import scrapy


class ParserSpider(scrapy.Spider):
    name = 'parser'
    start_urls = ['file:///D:/Takeout/YouTube/history/watch-history.html']

    def parse(self, response):
        for video in response.xpath('//a[starts-with(@href,"https://www.youtube.com/watch?v=")]'):
            yield {
                'name': video.xpath('text()').extract(),
                'url': video.xpath('@href').extract(),
            }

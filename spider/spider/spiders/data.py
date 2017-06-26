# -*- coding: utf-8 -*-
import scrapy
from scrapy.loader import ItemLoader
from spider.items import SpiderItem
import re
class dataSpider(scrapy.Spider):
    name = "data"
    allowed_domains = ['tmall.com']
    start_urls = [
        'https://list.tmall.com/search_product.htm?spm=a220m.1000858.0.0.53z7lb&cat=50474006&q=%B9%CC%CC%AC%D3%B2%C5%CC&sort=s&style=g&from=mallfp..pc_1_searchbutton&active=2&industryCatId=50474006&type=pc'
    ]
    def start_requests(self):
        for u in self.start_urls:
            yield scrapy.Request(u, callback=self.allpage,
                                    errback=self.errback,
                                    dont_filter=True)
    def allpage(self, response):
        num = int(response.xpath('//*[@id="J_Filter"]/p/b[1]').extract()[0].split("/")[1].split("<")[0])
    #   url=["https://list.tmall.com/search_product.htm?spm=a220m.1000858.0.0.n81v3g&cat=50474006&q=%B9%CC%CC%AC%D3%B2%C5%CC&sort=s&style=g&from=mallfp..pc_1_searchbutton&active=2&industryCatId=50474006&type=pc"]
        for i in range(1,num+1):
            s=str((i-1)*60)
            newurl="https://list.tmall.com/search_product.htm?spm=a220m.1000858.0.0.n81v3g&cat=50474006&" +"s=%s" % "s" +"&q=%B9%CC%CC%AC%D3%B2%C5%CC&sort=s&style=g&from=mallfp..pc_1_searchbutton&active=2&industryCatId=50474006&type=pc"
            yield scrapy.Request(newurl,callback=self.geturl,
                                 errback=self.errback)
    def parse(self, response):
        pass
    def geturl(self,response):
    #   div=response.xpath('//div[@class="product  "]').extract()
        url= response.css('a::attr(href)').extract()
        for i in range(0,len(url)+1):
            if "detail" in url[i]:
                yield scrapy.Request(url[i], callback=self.parse,
                                            errback=self.errback)

    def parse_item(self,response):
        dt = ItemLoader(item=SpiderItem(),response=response)
    def errback(self,failure):
        pass
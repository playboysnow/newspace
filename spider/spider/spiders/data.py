# -*- coding: utf-8 -*-
import scrapy,os,sys,time
from scrapy.loader import ItemLoader
from spider.items import SpiderItem
from selenium import webdriver
from bs4 import BeautifulSoup as BS
import re
class dataSpider(scrapy.Spider):
    name = "data"
    allowed_domains = ['tmall.com']
    start_urls = [
        'https://list.tmall.com/search_product.htm?q=%B9%CC%CC%AC%D3%B2%C5%CC&type=p&vmarket=&spm=875.7931836%2FB.a2227oh.d100&from=mallfp..pc_1_searchbutton'
    ]
    def errback(self, failure):

        pass

    def webpage(self, url):
        try:
            driver = webdriver.PhantomJS()
            driver.get(url)
            # print driver.page_source
            #        html = BS(driver.page_source,'lxml')

            name=driver.find_element_by_xpath('//*[@id="J_AttrUL"]/li[1]').text

            parse=driver.find_element_by_xpath('//*[@id="J_AttrUL"]/li[3]').text
            price=driver.find_element_by_xpath('//*[@id="J_StrPriceModBox"]/dd/span').text
            salecount = driver.find_element_by_xpath('//*[@id="J_DetailMeta"]/div/div[1]/div/ul/li[1]/div/span[2]').text
            with open('data2.json', 'a') as f:
                f.write('name:' + name.encode("utf-8") + '    ' + 'parse:' + parse.encode(
                    "utf-8") + '    ' + 'price:' + price.encode("utf-8") + '      ' + 'salecount:' + salecount.encode(
                    "utf-8"))
                f.write('\n')
                f.close()
        except:
            pass

        driver.quit()
        time.sleep(3)

    def start_requests(self):
        for u in self.start_urls:
            yield scrapy.Request(u, callback=self.allpage,
                                 errback=self.errback,
                                 dont_filter=True)
    def allpage(self, response):
        num = int(response.xpath('//*[@id="J_Filter"]/p/b[1]').extract()[0].split("/")[1].split("<")[0])
        #   url=["https://list.tmall.com/search_product.htm?spm=a220m.1000858.0.0.n81v3g&cat=50474006&q=%B9%CC%CC%AC%D3%B2%C5%CC&sort=s&style=g&from=mallfp..pc_1_searchbutton&active=2&industryCatId=50474006&type=pc"]
        headers={
            "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
            "Accept-Language": "zh-CN,zh;q=0.8,en-US;q=0.5,en;q=0.3",
            "Accept-Encoding": "gzip, deflate",
            "USER_AGENT" :"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.143 Safari/537.37",
            "Connection": "keep-alive"
        }
        for i in range(1,num+1):
            s=str((i-1)*60)
            newurl="https://list.tmall.com/search_product.htm?spm=a220m.1000858.0.0.n81v3g&cat=50474006&" +"s=%s" %  s +"&q=%B9%CC%CC%AC%D3%B2%C5%CC&sort=s&style=g&from=mallfp..pc_1_searchbutton&active=2&industryCatId=50474006&type=pc"
            yield scrapy.Request(newurl,callback=self.geturl,headers=headers,
                                 errback=self.errback)
            #   def parse(self, response):
            #       yield  self.parse_item(response)

    def geturl(self, response):
    #   div=response.xpath('//div[@class="product  "]').extract()
        url = response.css('a::attr(href)').extract()
        for i in range(0, len(url)):
            if "detail" in url[i]:
            #                yield scrapy.Request('https:'+url[i], callback=self.parse,
            #                                    errback=self.errback)
                yield  self.webpage('https:' + url[i])
            #                htmlres=self.webpage('https:' + url[i])
            #                yield self.parse_item(htmlres)
            #   def parse_item(self, response):
            #    res=self.geturl(response)

'''        dt = ItemLoader(item=SpiderItem(), response=response)
        dt.add_xpath('name', '//*[@id="J_AttrUL"]/li[1]')
        dt.add_xpath('parse', '//*[@id="J_AttrUL"]/li[3]')
        #   dt.add_xpath('price','//*[@id="J_StrPriceModBox"]/dd/span')
        dt.add_xpath('price', '//*[@id="J_StrPriceModBox"]/dd/span')
        return dt.load_item()

  def geturl(self,response):
       #   div=response.xpath('//div[@class="product  "]').extract()
       url= response.css('a::attr(href)').extract()
       for i in range(0,len(url)+1):
           if "detail" in url[i]:
#                yield scrapy.Request('https:'+url[i], callback=self.parse,
#                                    errback=self.errback)
               yield self.webpage('https:'+url[i])
'''

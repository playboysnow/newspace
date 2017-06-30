# -*- coding: utf-8 -*-
from selenium import webdriver
from bs4 import BeautifulSoup as BS
url="https://detail.tmall.com/item.htm?spm=a220m.1000858.1000725.5.kiaYU2&id=534255234480&skuId=3333324765627&areaId=110100&standard=1&user_id=704392951&cat_id=50474006&is_b=1&rn=c6dfc13a27ead1d22bc21372348a0f25"
driver=webdriver.PhantomJS()
driver.get(url)
#print driver.page_source
html=BS(driver.page_source,"lxml")
price=html.find_all("span",class_="tm-price")
a=driver.find_element_by_xpath('//*[@id="J_StrPriceModBox"]/dd/span').text
name=driver.find_element_by_xpath('//*[@id="J_AttrUL"]/li[1]').text
parse=driver.find_element_by_xpath('//*[@id="J_AttrUL"]/li[3]').text
print a.encode("utf-8")
print name.encode("utf-8")
print parse

#a=driver.find_element_by_xpath('//*[@id="J_StrPriceModBox"]/dd/span')
#a=driver.page_source.find("tm-price")
#print a
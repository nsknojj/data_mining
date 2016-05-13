# -*- coding: utf-8 -*-
# a wiki news crawler based on Scrapy framework : http://scrapy.org/
import re
import scrapy
import unicodedata
from wikicrawl.items import WikicrawlItem

class Count(object):
    def __init__(self):
        self.ct = 0
    def name(self):
        self.ct = self.ct + 1
        return str(self.ct)

number = Count()

class WikiSpider(scrapy.Spider):
    name = "wiki"
    allowed_domains = ["en.wikinews.org"]
    cat_list = (
        'Crime and law',
        'Culture and entertainment',
        'Disasters and accidents',
        'Science and technology',
        'Health'
    )
    start_urls = (
        'https://en.wikinews.org/wiki/Category:Crime_and_law',
        'https://en.wikinews.org/wiki/Category:Culture_and_entertainment',
        'https://en.wikinews.org/wiki/Category:Disasters_and_accidents',
        'https://en.wikinews.org/wiki/Category:Science_and_technology',
        'https://en.wikinews.org/wiki/Category:Health'
    )
    # parse the main page of each category
    def parse(self, response):
        for subpage in response.xpath('//body//div[@id="mw-pages"]//div[@class="mw-category-group"]//ul//li//a/@href').extract():
            print('\n'+response.urljoin(subpage)+'\n')
            yield scrapy.Request(response.urljoin(subpage),callback=self.parseSub)
            # break;  # for debug

        m=re.search(r'previous page(.*)<a href="(.*?)"',response.body)
        if m:
            nextpage=re.sub(r'&amp;','&',m.group(2));
            nextpage=response.urljoin(nextpage);
            print('/n'+nextpage+'\n')
            yield scrapy.Request(nextpage,callback=self.parse)
    # parse each article
    def parseSub(self, response):
        item=WikicrawlItem()
        print("\nScanning Article...\n")
        tmp=response.xpath('//body//h2/preceding-sibling::p//text()').extract()
        cat=self.getCat(response)
        # filter the article that has more than 1 category
        if (len(tmp)>2) and (len(cat)==1):
            filename='mirror/'+number.name()+'.txt'
            with open(filename,'wb') as f:
                f.write(response.xpath("//body//h1/text()").extract()[0])
                f.write('\n')
                for i in range(2,len(tmp)):
                    # deal with unicode
                    tmp[i]=unicodedata.normalize('NFKD',tmp[i]).encode('ascii','ignore')
                    f.write(tmp[i])
                f.write('\n')
                f.write(cat[0])
                # f.write(response.body)
        yield item

    def getCat(self,response):
        cat=response.xpath('//div[@id="mw-normal-catlinks" and @class="mw-normal-catlinks"]//ul//li//text()').extract()
        ret=[]
        for e in cat:
            e=unicodedata.normalize('NFKD',e).encode('ascii','ignore')
            if e in self.cat_list:
                ret.append(e)
        return ret

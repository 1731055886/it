
#coding=utf-8
import sys
import scrapy
from it.items import ItItem
reload(sys)
sys.setdefaultencoding('utf8')

class MySpider(scrapy.Spider):
    name = "qian"
    allowed_domain = ["imooc.com"]
    start_urls = ["http://www.imooc.com/course/list"]





    def parse(self,response):
        item = ItItem()
        res = response.xpath('//div[@class="course-card-container"]')
        for one in res:
            item['title'] = one.xpath('a[@target="_blank"]/div[@class="course-card-content"]/h3/text()').extract()[0].encode('utf-8')
            item['url'] = 'http://www.imooc.com' + one.xpath('.//a[@target="_blank"]/@href').extract()[0]
            item['img_url'] = 'http:' + one.xpath('.//div[@class="course-card-top"]/img/@src').extract()[0]
            item['introduction'] = one.xpath('.//p[@class="course-card-desc"]/text()').extract()[0].encode('utf-8')
            item['student'] = one.xpath('.//div[@class="course-card-info"]/span[2]/text()').extract()[0]
            yield item
        nextPage = response.xpath('//div[@class="page"]/a[8]/@href').extract()
        if nextPage:
            nextPage = nextPage[0]
            nextPage = 'http://www.imooc.com' + nextPage
            yield scrapy.Request(url=nextPage,callback=self.parse)
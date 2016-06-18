import scrapy
from scrapy.spiders import Spider
from scrapy.selector import Selector
from RA.items import RaItem

class RaSpider(Spider):
      name = "RA"
      allowed_domains = ["rakuten.com"]
      def start_requests(self):
          for i in range(208512673, 209500000):
              yield self.make_requests_from_url("http://www.rakuten.com/prod/%d.html" % i)
          #start_urls = ["http://www.rakuten.com/prod/200090868.html"]


      def parse(self, response):
          sel = Selector(response)
          sites = sel.xpath('//*[@id="product-tabs"]')
          items = []

          for response in sites:
            item = RaItem()
            item['start_url'] = response.xpath('/html/head/link[1]').extract()
            item['title'] = response.xpath('//*[@id="product-title-heading"]/text()').extract()
            item['category'] = response.xpath('//*[@id="product-content"]/div[2]/ul/li/a/text()').extract()
            item['manufaturer'] = response.xpath('//*[@id="specifications"]/table[1]/tr[1]//text()').extract()
            item['image_url'] = response.xpath('//*[@id="productmain"]/@src').extract()
            item['mfr_part'] = response.xpath('//*[@id="specifications"]/table[1]/tr[2]//text()').extract()
            item['sku'] = response.xpath('//*[@id="specifications"]/table[1]/tr[3]//text()').extract()
            item['upc'] = response.xpath('//*[@id="specifications"]/table[1]/tr[4]//text()').extract()
            item['upc14'] = response.xpath('//*[@id="specifications"]/table[1]/tr[5]//text()').extract()
            items.append(item)
            return items
# -*- coding: utf-8 -*-
import scrapy


class GlassesSpider(scrapy.Spider):
    name = 'glasses'
    allowed_domains = ['www.glassesshop.com']
    start_urls = ['https://www.glassesshop.com/bestsellers/']

    def parse(self, response):
        for item in response.xpath('//div[@class="col-12 pb-5 mb-lg-3 col-lg-4 product-list-row text-center product-list-item"]'):
            # product url
            url = item.xpath('./div[@class="product-img-outer"]/a[1]/@href').get()
            # product image link
            image_link = item.xpath('./div[@class="product-img-outer"]/a/img/@data-src').get()
            # product name
            name = item.xpath('./div[@class="product-img-outer"]/a[1]/@title').get()
            # product price
            price = item.xpath('.//div[@class="p-price"]/div/span/text()').get()

            yield {
                'url': url,
                'image_link': image_link,
                'name': name,
                'price': price
            }

        next_page = response.xpath('//a[@rel="next"]/@href').get()

        if next_page:
            yield scrapy.Request(url=next_page, callback=self.parse, dont_filter=True) 

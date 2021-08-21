# -*- coding: utf-8 -*-
import scrapy
from share_floor_sheet.items import ShareFloorSheetItem


class FloorsheetSpiderSpider(scrapy.Spider):
    name = 'floorsheet_spider'
    allowed_domains = ['www.nepalstock.com.np','merolagani.com']
    start_urls = ['https://merolagani.com/Floorsheet.aspx']

    def parse(self, response):
        # print(response.body)
        item = ShareFloorSheetItem()
        table_rows = response.xpath('//tr')
        for table_row in table_rows:
            transact_no = table_row.xpath('//td[2]/text()')
            symbol = table_row.xpath('//td[3]/a/text()')
            buyer = table_row.xpath('//td[4]/a/text()')
            seller = table_row.xpath('//td[5]/a/text()')
            quantity = table_row.xpath('//td[6]/text()')
            rate = table_row.xpath('//td[7]/text()')
            amount = table_row.xpath('//td[8]/text()')
            for datum in zip(transact_no,symbol,buyer,seller,quantity,rate,amount):
                item['transact_no'] = datum[0].extract()
                item['symbol'] = datum[1].extract()
                item['buyer'] = datum[2].extract()
                item['seller'] = datum[3].extract()
                item['quantity'] = datum[4].extract()
                item['rate'] = datum[5].extract()
                item['amount'] = datum[6].extract()
                yield item

        # next_page_urls = response.xpath('//*[@class="page-link"]/@href').extract()
        # for next_page_url in next_page_urls:
        #     yield Request(url=next_page_url, callback=self.parse, dont_filter=True
        #                   )

import scrapy


class ShopeeExtractSpider(scrapy.Spider):
    name = "shopee-extract"

    start_urls = [
        'https://shopee.co.id/aldmond22'
    ]

    def parse(self, response):
        for quote in response.css('div.quote'):
            yield {
                'text': quote.css('span.text::text').get(),
                'author': quote.css('small.author::text').get(),
                'tags': quote.css('div.tags a.tag::text').getall(),
            }
import scrapy


class ShopeeSpider(scrapy.Spider):
    name = "shopee"

    def start_requests(self):
        urls = [
            'http://shopee.co.id/aldmond22/'
        ]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        page = response.url.split("/")[-2]
        filename = f'shopee-{page}.html'
        with open(filename, 'wb') as f:
            f.write(response.body)
        self.log(f'Saved file {filename}')
import scrapy
from scrapy.core.engine import Response

class MainSpider(scrapy.Spider):
    name = "main"
    allowed_domains = ["pharmaclick.uz"]
    start_urls = ["https://pharmaclick.uz/ru/"]

    def start_requests(self):
        return super().start_requests()
    
    def parse(self, response: Response):
        for k in response.xpath('//ul/li/a[contains(@class, "icons_fa") and not (contains(@class, "parent"))]/@href'):
            yield scrapy.Request(url=response.urljoin(k.get()), callback=self.get_info_from_page)
            break
            
    def get_info_from_page(self, response):
        print(2)
        for farm in response.xpath("//div[has-class('item_info')]/div/a/span/text()"):
            print(3)
            print(farm.get())
            
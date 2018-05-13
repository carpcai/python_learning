import scrapy

class VochinaSpider(scrapy.Spider):
    name = "vochina"
    allowed_domains = ["vochina.com"]
    start_urls = [
        "https://vochina.com/"
    ]

    def parse(self, response):
        # filename = response.url.split("/")[-2]
        # with open(filename, 'wb') as f:
        #     f.write(response.body)
        data = response.xpath('//body/div/header')
        print(data)

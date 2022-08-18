import scrapy

class spider(scrapy.Spider):
    name = 'generic'
    with open ("urls.txt", "r") as f:
        start_urls = f.readlines()

    def parse(self, response):
        page = response.url.split("/")[-1]
        filename = 'data-%s.html' % page
        with open(filename, 'wb') as f:
            f.write(response.body)
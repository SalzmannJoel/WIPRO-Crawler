import scrapy
from scrapy.crawler import CrawlerProcess


class BlickSpider(scrapy.Spider):
    name = "blick"

    def start_requests(self):
        urls = [
            'https://www.blick.ch/life/horoskop/'
        ]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        horoskops = response.css("div#content_outer>div.contentwrapper>div#container>div.grid_6")
        for horoskop in horoskops:
            sign = horoskop.css("div.grid_6>div.articleHeader>h3::text").extract_first()
            horoskoptext = horoskop.css("div.grid_6>div.article-entry>p:nth-child(2)::text").extract_first()
            with open("blickHoroskops.txt", "a", encoding="utf-8") as horoskopfile:
                horoskopfile.write(sign)
                horoskopfile.write(":")
                horoskopfile.write(horoskoptext)
                horoskopfile.write("\n")

process = CrawlerProcess({
    'USER_AGENT': 'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1)'
})

process.crawl(BlickSpider)
process.start()
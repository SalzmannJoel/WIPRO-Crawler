import scrapy
from scrapy.crawler import CrawlerProcess


class SchweizerillustrierteSpider(scrapy.Spider):
    name = "schweizerillustrierte"

    def start_requests(self):
        urls = [
            'https://www.schweizer-illustrierte.ch/horoskop/'
        ]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        horoskops = response.css("div.horoscope-grid>article.horoscope")
        for horoskop in horoskops:
            sign = horoskop.css("article.horoscope h2::text").extract_first()
            horoskopdecades = horoskop.css("article.horoscope>div.horoscope__decade")
            for decade in horoskopdecades:
                horoskoptext = decade.css("div.horoscope__decade>p.horoscope__decade__content::text").extract_first()
                with open("schweizerillustrierteHoroskops.txt", "a", encoding="utf-8") as horoskopfile:
                    horoskopfile.write(sign)
                    horoskopfile.write(":")
                    horoskopfile.write(horoskoptext)
                    horoskopfile.write("\n")

process = CrawlerProcess({
    'USER_AGENT': 'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1)'
})

process.crawl(SchweizerillustrierteSpider)
process.start()
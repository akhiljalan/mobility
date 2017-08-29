import scrapy


class QuotesSpider(scrapy.Spider):
    name = "quotes" # each spider name must be UQ in a project
    # the crawl command is scrapy crawl quotes

    # returns an iterable of requests
    # def start_requests(self):
    #     urls = [
    #         'http://quotes.toscrape.com/page/1/',
    #         'http://quotes.toscrape.com/page/2/',
    #     ]
    #     for url in urls:
    #         yield scrapy.Request(url=url, callback=self.parse)
    start_urls = [
        'http://quotes.toscrape.com/page/1/',
        'http://quotes.toscrape.com/page/2/',
    ]

    #
    def parse(self, response):
        for quote in response.css("div.quote"):
            yield {
                'text': quote.css('span.text::text').extract_first(),
                'author': quote.css('small.author::text').extract_first(),
                'tags': quote.css('div.tags a.tag::text').extract(),
            }
        page = response.url.split("/")[-2]
        filename = 'quotes-%s.html' % page
        with open(filename, 'wb') as f:
            f.write(response.body)
        self.log('Saved file %s' % filename)
#key syntax
# the -o 'filename.txt' tag saves the results of the scraper
# the 'yield{}' command in the callback is what returns things
# launch the shell with scrapy shell <url>


#http_begin = 'http://www.equality-of-opportunity.org'
#links2 = response.css("#data_absolute a::attr(href)").extract()

#work smarter, not harder! first wave of download links. we don't need any of the .dta files
college_links = ['http://www.equality-of-opportunity.org/data/college/mrc_table1.dta',
 'http://www.equality-of-opportunity.org/data/college/mrc_table1.csv',
 'http://www.equality-of-opportunity.org/data/college/Codebook MRC Table 1.pdf',
 'http://www.equality-of-opportunity.org/data/college/mrc_table2.dta',
 'http://www.equality-of-opportunity.org/data/college/mrc_table2.csv',
 'http://www.equality-of-opportunity.org/data/college/Codebook MRC Table 2.pdf',
 'http://www.equality-of-opportunity.org/data/college/mrc_table3.dta',
 'http://www.equality-of-opportunity.org/data/college/mrc_table3.csv',
 'http://www.equality-of-opportunity.org/data/college/Codebook MRC Table 3.pdf',
 'http://www.equality-of-opportunity.org/data/college/mrc_table4.dta',
 'http://www.equality-of-opportunity.org/data/college/mrc_table4.csv',
 'http://www.equality-of-opportunity.org/data/college/Codebook MRC Table 4.pdf',
 'http://www.equality-of-opportunity.org/data/college/mrc_table5.dta',
 'http://www.equality-of-opportunity.org/data/college/mrc_table5.csv',
 'http://www.equality-of-opportunity.org/data/college/Codebook MRC Table 5.pdf',
 'http://www.equality-of-opportunity.org/data/college/mrc_table6.dta',
 'http://www.equality-of-opportunity.org/data/college/mrc_table6.csv',
 'http://www.equality-of-opportunity.org/data/college/Codebook MRC Table 6.pdf',
 'http://www.equality-of-opportunity.org/data/college/mrc_table7.dta',
 'http://www.equality-of-opportunity.org/data/college/mrc_table7.csv',
 'http://www.equality-of-opportunity.org/data/college/Codebook MRC Table 7.pdf',
 'http://www.equality-of-opportunity.org/data/college/mrc_table8.dta',
 'http://www.equality-of-opportunity.org/data/college/mrc_table8.csv',
 'http://www.equality-of-opportunity.org/data/college/Codebook MRC Table 8.pdf',
 'http://www.equality-of-opportunity.org/data/college/mrc_table9.dta',
 'http://www.equality-of-opportunity.org/data/college/mrc_table9.csv',
 'http://www.equality-of-opportunity.org/data/college/Codebook MRC Table 9.pdf',
 'http://www.equality-of-opportunity.org/data/college/mrc_table10.dta',
 'http://www.equality-of-opportunity.org/data/college/mrc_table10.csv',
 'http://www.equality-of-opportunity.org/data/college/Codebook MRC Table 10.pdf',
 'http://www.equality-of-opportunity.org/data/college/mrc_table11.dta',
 'http://www.equality-of-opportunity.org/data/college/mrc_table11.csv',
 'http://www.equality-of-opportunity.org/data/college/Codebook MRC Table 11.pdf',
 'http://www.equality-of-opportunity.org/data/college/replicate.zip']
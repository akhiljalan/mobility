import scrapy

css_selectors = [
        "#data_college a::attr(href)",
        "#data_absolute a::attr(href)",
        "#data_movers a::attr(href)",
        "#data_genders a::attr(href)",
        "#data_health a::attr(href)",
        "#data_trends a::attr(href)",
        "#data_ige a::attr(href)",
    ]
http_begin = 'http://www.equality-of-opportunity.org'

#takes the CSS selector for a certain class of links and extracts the category name
#example: "#data_college a::attr(href)" --> "college"
def get_category(str):
    arr = str.split()
    first_part = arr[0]
    return first_part[6:]

class MobilitySpider(scrapy.Spider):
    name = "mobility" # each spider name must be UQ in a project
    # the crawl command is scrapy crawl mobility

    start_urls = [
        'http://www.equality-of-opportunity.org/data'
    ]

    def parse(self, response):
        links_to_save = []
        for selector in css_selectors:
            cat = get_category(selector)
            URL_list = response.css(selector).extract()
            for URL in URL_list:
                links_to_save.append(dict(url=(http_begin + URL), category=cat))
                yield {
                    'url' : http_begin + URL,
                    'category' : cat,
                }
        # for link_json in links_to_save:
        #     yield {
        #         link_json
        #     }
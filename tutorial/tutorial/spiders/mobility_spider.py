import scrapy
import os
import errno

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

#Credit to this stackoverflow thread:
#https://stackoverflow.com/questions/273192/how-can-i-create-a-directory-if-it-does-not-exist
def make_dir(dir_name):
    #this is the filepath I want to save to on my local machine.
    path = os.path.expanduser("~/anaconda/mobility/data/")
    path += dir_name
    try:
        os.makedirs(path)
    except OSError as exception:
        if exception.errno != errno.EEXIST:
            raise

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
            #Makes a directory named after the data grouping
            #(If such a directory already exists, nothing happens)
            make_dir(cat)
            #Extract the URLs of all linked files which have the specified CSS selector
            URL_list = response.css(selector).extract()
            file_types = ('.xlsx', '.csv', '.pdf')
            for URL in URL_list:
                if (URL.endswith(file_types)):
                    if 'http' in URL:
                        links_to_save.append(dict(url=(URL), category=cat))
                        yield {
                            'url': URL,
                            'category': cat,
                        }
                    else:
                        links_to_save.append(dict(url=(URL), category=cat))
                        yield {
                            'url' : http_begin + URL,
                            'category': cat,
                        }
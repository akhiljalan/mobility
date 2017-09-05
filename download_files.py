import os
import urllib.request
import json
#req.urlretrieve(filename, file_name_test)

url_request = urllib.request.FancyURLopener({})

#URLs all have the structure of
#"http://www.equality-of-opportunity.org/data/college/mrc_table1.csv"
#we want the filename "mrc_table1.csv", so we split by "/" and take the last
#element of the resulting array
def get_filename(file_url):
    split_arr = file_url.split('/')
    return split_arr[-1]

json_filepath = os.path.expanduser('~/anaconda/mobility/tutorial/cleaned_download_links.json')
links_dicts = json.loads(open(json_filepath).read())
for dict in links_dicts:
    file_url = dict['url']
    filepath = os.path.expanduser('~/anaconda/mobility/data/')
    filepath += dict['category'] + '/' + get_filename(file_url)
    try:
        urllib.request.urlretrieve(file_url, filepath)
    except urllib.request.HTTPError as err:
        print(filepath, ' failed')
        # print(err.code)
        # print(err.read())



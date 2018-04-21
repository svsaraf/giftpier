from amazon.api import AmazonAPI
from secrets import ACCESS_KEY, SECRET_KEY, ASSOC_ID
from azsearch.models import Gift
import time

def process_list():
    file = open('listtosearch.txt', 'r')
    amazon = AmazonAPI(ACCESS_KEY, SECRET_KEY, ASSOC_ID)
    for line in file:
        print("Processing: " + line)
        process_file(line, amazon)
        time.sleep(60)


def process_file(line, amazon):
    products = amazon.search_n(30, Keywords=line, SearchIndex='All')
    for product in products:
        if product.title and product.offer_url and product.large_image_url and product.formatted_price and product.price_and_currency[0]:
            gift = Gift(name=product.title, link=product.offer_url, image_link=product.large_image_url, price_desc=product.formatted_price, price=product.price_and_currency[0])
            gift.save()

process_list()
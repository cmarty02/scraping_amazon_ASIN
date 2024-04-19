import scrapy
import csv
import time
import random
from datetime import datetime
from scrapy.crawler import CrawlerProcess

class AmazonReviewsSpider(scrapy.Spider):
    name = "amazon_reviews"

    def start_requests(self):
        csv_file_path = 'ASIN_Bewertungen.csv'

        with open(csv_file_path, 'r', newline='', encoding='utf-8') as csvfile:
            reader = csv.reader(csvfile)
            asin_list = [row[0] for row in reader]

        for asin in asin_list:
            amazon_reviews_url = f'https://www.amazon.de/product-reviews/{asin}/'
            yield scrapy.Request(url=amazon_reviews_url, callback=self.parse_reviews, meta={'asin': asin})

    def parse_reviews(self, response):
        asin = response.meta['asin']
        time.sleep(random.uniform(1, 3))

        current_datetime = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

        review_elements = response.css("#cm_cr-review_list div.review")
        total_reviews = 0
        total_stars = 0

        for review_element in review_elements:
            total_reviews += 1
            stars_text = review_element.css("*[data-hook*=review-star-rating] ::text").re_first(r"(\d+\.*\d*) out")
            if stars_text:
                total_stars += float(stars_text)

        total_ratings = response.xpath('/html/body/div[1]/div[1]/div[1]/div/div[1]/div[1]/div/div[1]/div[3]/span/text()').get()
        global_stars = response.xpath('/html/body/div[1]/div[1]/div[1]/div/div[1]/div[1]/div/div[1]/div[2]/div/div/div[2]/div/span/text()').get()

        data = {
            "asin": asin,
            "total_ratings": int(total_ratings.replace(' globale Bewertungen', '').split(' ')[0]) if total_ratings else None,
            "global_stars": float(global_stars.replace(',', '.').split(' ')[0]) if global_stars else None,
            "datetime": current_datetime
        }

        csv_file = 'amazon_reviews.csv'
        with open(csv_file, 'a', newline='', encoding='utf-8') as file:
            writer = csv.DictWriter(file, fieldnames=data.keys())
            if file.tell() == 0:
                writer.writeheader()
            writer.writerow(data)

# Configurar y ejecutar el proceso de Scrapy
process = CrawlerProcess({
    'USER_AGENT': 'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1)',
    'FEED_FORMAT': 'csv',
    'FEED_URI': 'amazon_reviews.csv'
})

process.crawl(AmazonReviewsSpider)
process.start()

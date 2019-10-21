# Importing Scrapy Library
import scrapy

# Creating a new class to implement Spide
class AmazonReviewsSpider(scrapy.Spider):
    
    # Spider name
    name = 'amazon_reviews'
    
    # Domain names to scrape
    allowed_domains = ['amazon.in']
    
    # Base URL for the MacBook air reviews
    myBaseUrl = "https://www.amazon.in/Acer-AN515-52-15-6-inch-i5-8300H-Graphics/dp/B07W6H2YCV/ref=sr_1_1?pf_rd_i=7198569031&pf_rd_m=A1K21FY43GMZF8&pf_rd_p=32e110dd-1981-4749-a665-dcc2dc3a954b&pf_rd_r=3K8FKPXA3XAM896NEWQS&pf_rd_s=merchandised-search-4&pf_rd_t=101&qid=1571632030&smid=A14CZOWI0VEHLG&sr=8-1&pageNumber="
    start_urls = []
   
    # Creating list of urls to be scraped by appending page number a the end of base url
    for i in range(1,10):
        start_urls.append(myBaseUrl+str(i))

    # Defining a Scrapy parser
    def parse(self, response):
            data = response.css('#cm_cr-review_list')
            
            # Collecting product star ratings
            star_rating = data.css('.review-rating')
            
            # Collecting user reviews
            comments = data.css('.review-text')
            count = 0
            
            # Combining the results
            for review in star_rating:
                yield{'stars': ''.join(review.xpath('.//text()').extract()),
                      'comment': ''.join(comments[count].xpath(".//text()").extract())
                     }
                count=count+1
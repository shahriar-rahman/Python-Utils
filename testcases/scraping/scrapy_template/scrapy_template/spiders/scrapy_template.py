# To run scrapy, 1."cd scraping" 2."cd scrapy_template" 3."scrapy crawl scr_template"
import scrapy
from .. import items
import python_utils.scraping_utils as su
import python_utils.common_utils as cu
# Objective: Scrape Quotes from page 1 to 3


class ScrapyTemplate(scrapy.Spider):
    name = 'scr_template'
    page_limit = 3
    all_quotes = []
    item = items.LyricsCrawlersItem()

    # DOM Selectors
    quote_xpath = '/html/body/div/div[2]/div[1]/div/span[1]'
    quote_css = 'div.quote > span:nth-child(1)'

    def start_requests(self):
        # Create a list of start URLs based on the page_limit
        start_urls = [f'https://quotes.toscrape.com/page/{i}/' for i in range(1, self.page_limit + 1)]

        # Loop through each URL in the start_urls list
        for url in start_urls:
            # Yield a Scrapy Request object for each URL
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response, **kwargs):
        # Create items object for temporary containers
        item = items.LyricsCrawlersItem()

        # Extract data from the current page
        get_text = True
        item['quotes'] = su.scrapy_scrape_elements(response, 'xpath', self.quote_xpath, get_text)

        # Append the extracted data to a list
        if hasattr(self, 'all_quotes'):
            self.all_quotes.extend(item['quotes'])
        else:
            self.all_quotes = item['quotes']

    def closed(self, reason):
        # After all pages are scraped, store the data in a DataFrame
        df = cu.create_df(({'quotes': self.all_quotes}))
        cu.save_df(df, "../datasets/scraped_data.csv")
        cu.display_df(df, 10)


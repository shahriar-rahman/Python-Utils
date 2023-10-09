# To run scrapy, 1."cd scraping" 2."cd scrapy_template" 3."scrapy crawl scr_template"
import scrapy
from .. import items
import python_utils.scraping_utils as su
import python_utils.common_utils as cu
import python_utils.db_utils as du
from sqlite3 import IntegrityError
# Objective: Scrape Quotes from page 1 to 3


class ScrapyTemplate(scrapy.Spider):
    name = 'scr_template'
    page_limit = 3
    all_quotes = []
    item = items.LyricsCrawlersItem()

    # Storage directories
    db_path = "../databases/scraped_data.db"
    data_path = "../datasets/scraped_data.csv"

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
        df = cu.create_df(({'quotes': self.all_quotes}), 'pl')
        cu.save_df(df, 'csv', self.data_path)
        cu.display_df(df, 10)

        # Create a SQLite connection using the provided database path.
        with du.SQLiteConnection(self.db_path) as db:
            # Create a 'quotes' table if it doesn't already exist.
            db.execute("""
                CREATE TABLE IF NOT EXISTS quotes(
                    quote_id INTEGER PRIMARY KEY AUTOINCREMENT,
                    quotes TEXT NOT NULL,
                    created_at DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP,
                    UNIQUE(quotes)
                )""")
            # Print information about the 'quotes' table.
            print("Quotes: ", *db.execute("PRAGMA table_info(quotes)"), sep="\n")

        # Iterate through each quote in the 'all_quotes' list.
        for quote in self.all_quotes:
            # Create a new SQLite connection for each quote.
            with du.SQLiteConnection(self.db_path) as db:
                # Insert the current quote into the 'quotes' table if not exists.
                try:
                    db.execute("INSERT INTO quotes (quotes) VALUES (?)", (quote,))
                # Catch Exception if failed.
                except IntegrityError as e:
                    print(f"Data Insertion unsuccessful: {e}")



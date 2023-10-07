import python_utils.common_utils as cu
import python_utils.scraping_utils as su
# Objective: Scrape Quotes from page 1 to 3


class Bs4Template:
    def __init__(self):
        self.all_quotes = []
        pages = 3

        # DOM keywords
        self.quote_tag = 'span'
        self.quote_attr = {'class': 'text'}

        # Connection to bs4
        start_urls = [f'https://quotes.toscrape.com/page/{i}/' for i in range(1, pages+1)]
        self.soup = [su.bs4_request(url, 'lxml') for url in start_urls]

    def bs4_scraping(self):
        # Scrape quotes using list comprehension for each request
        for soup in self.soup:
            quotes = [quote.text for quote in su.bs4_scrape_elements(soup, 'findAll', self.quote_tag, self.quote_attr)]

            # Append the extracted data to a list
            if hasattr(self, 'all_quotes'):
                self.all_quotes.extend(quotes)
            else:
                self.all_quotes = quotes

        # After all pages are scraped, store the data in a DataFrame
        df = cu.create_df({'quotes': self.all_quotes})
        cu.save_df(df, "../datasets/scraped_data.csv")
        cu.display_df(df, 10)


if __name__ == "__main__":
    main = Bs4Template()
    main.bs4_scraping()

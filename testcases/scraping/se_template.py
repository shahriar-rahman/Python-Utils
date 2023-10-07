import python_utils.common_utils as cu
import python_utils.scraping_utils as su
# Objective: Scrape Quotes from page 1 to 3


class SeleniumTemplate:
    def __init__(self):
        pages = 3
        self.all_quotes = []

        # Generate URLs
        self.start_urls = [f'https://quotes.toscrape.com/page/{i}/' for i in range(1, pages+1)]

        # DOM Selectors
        self.quote_xpath = '/html/body/div/div[2]/div[1]/div/span[1]'
        self.quote_css = 'body > div > div:nth-child(2) > div.col-md-8 > div > span.text'

    def selenium_scraping(self):
        # Configure Chrome if needed
        su.selenium_configure_chrome()

        for url in self.start_urls:
            # Configure Chrome driver with headless option
            headless = True
            driver = su.selenium_configure_driver(headless)

            # Load url with implicit wait
            driver.get(url)
            driver.implicitly_wait(5)

            # Retrieve quotes from each page
            all_elements = True
            quotes = [quote.text for quote in su.selenium_scrape_elements(driver, 5, 'xpath',
                                                                               self.quote_xpath, all_elements)]

            # Append the extracted data to a list
            if hasattr(self, 'all_quotes'):
                self.all_quotes.extend(quotes)
            else:
                self.all_quotes = quotes

            driver.quit()

        # After all pages are scraped, store the data in a DataFrame
        df = cu.create_df({'quotes': self.all_quotes})
        cu.save_df(df, "../datasets/scraped_data.csv")
        cu.display_df(df, 10)


if __name__ == "__main__":
    main = SeleniumTemplate()
    main.selenium_scraping()
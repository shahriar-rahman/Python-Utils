import python_utils.common_utils as cu
import python_utils.scraping_utils as su
import python_utils.db_utils as du
from sqlite3 import IntegrityError
# Objective: Scrape Quotes from page 1 to 3


class Bs4Template:
    def __init__(self):
        self.all_quotes = []
        pages = 3

        # Storage directories
        self.db_path = "../databases/scraped_data.db"
        self.data_path = "../datasets/scraped_data.csv"

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


if __name__ == "__main__":
    main = Bs4Template()
    main.bs4_scraping()

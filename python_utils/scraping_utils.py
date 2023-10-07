import bs4
import requests
import scrapy
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver import Chrome
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


class ScrapingUtils:
    def __init__(self):
        pass

    @staticmethod
    def bs4_request(url, parse_format):
        try:
            # Send an HTTP GET request to the provided URL
            req = requests.get(url)

            # Raise an exception for bad HTTP status codes
            req.raise_for_status()

            # Parse the response content using BeautifulSoup with the specified parse format
            return BeautifulSoup(req.text, parse_format)

        except requests.exceptions.RequestException as e:
            # Handle any exceptions that occur during the request
            print(f"An error occurred while fetching {url}: {e}")
            return None  # Return None to indicate failure

    @staticmethod
    def bs4_scrape_elements(soup: bs4.BeautifulSoup, method_name: str, keyword: str, attrs: dict = None):
        # Map the method_name to BeautifulSoup method names for consistency
        method_map = {
            'find': 'find',
            'findAll': 'find_all',
            'find_all': 'find_all',
            'findNext': 'find_next',
            'find_next': 'find_next',
        }

        try:
            # Get the corresponding BeautifulSoup method from the map
            bs_method = method_map.get(method_name)

            if bs_method:
                # Check if attrs (attributes) are provided for searching
                if attrs:
                    # Use the BeautifulSoup method with keyword and attributes
                    data = getattr(soup, bs_method)(keyword, attrs=attrs)
                else:
                    # Use the BeautifulSoup method with just the keyword
                    data = getattr(soup, bs_method)(keyword)

                # Return the scraped data
                return data

        except AttributeError as exc:
            # Handle AttributeError and print an error message
            print(f"! AttributeError: {exc}")
        except Exception as exc:
            # Handle other exceptions and print an error message
            print(f"! Exception: {exc}")

        # Return None if an error occurs or no data is found
        return None

    @staticmethod
    def selenium_configure_chrome():
        try:
            # Configure options here if needed
            options = Options()
            options.add_argument("--headless=new")

            # Create a service object (if necessary)
            service = Service()

            # Create the WebDriver with the specified service and options
            driver = webdriver.Chrome(service=service, options=options)

            # You can add WebDriverWait here to wait for specific conditions if needed
            WebDriverWait(driver, 5)

            # Close the WebDriver when done
            driver.quit()

            print(">> Chrome Configuration successful.")

        except Exception as e:
            print("Exception: ", e)

    @staticmethod
    def selenium_configure_driver(headless: bool):
        # Create a Chrome WebDriver options object
        options = Options()
        options.add_experimental_option("detach", True)

        if headless:
            # If running in headless mode, add the headless argument
            options.add_argument("--headless=new")

        # Create a Chrome WebDriver with the configured options
        driver = Chrome(options=options)

        if not headless:
            # If not running in headless mode, maximize the browser window
            driver.maximize_window()

        # Return the configured driver
        return driver

    @staticmethod
    def selenium_scrape_elements(driver: WebDriver, wait_time: int, selector: str, path: str, all_elements: bool):
        # Determine the 'By' and 'expected_conditions' based on the selector type ('xpath' or 'css')
        by = By.XPATH if selector == 'xpath' else By.CSS_SELECTOR

        if all_elements:
            # Wait for all matching elements to be present on the page
            condition = EC.presence_of_all_elements_located((by, path))
        else:
            # Wait for a single matching element to be present on the page
            condition = EC.presence_of_element_located((by, path))

        # Use WebDriverWait to wait for the specified condition to be met
        data = WebDriverWait(driver, wait_time).until(condition)

        # Return the located elements
        return data

    @staticmethod
    def scrapy_scrape_elements(response: scrapy.http.response.html.HtmlResponse, selector: str, path: str, text: bool):
        # Check if the selector is 'xpath'
        if selector == 'xpath':
            # If 'text' is True, select the text nodes using '/text()' in the XPath expression
            # Otherwise, select elements without text nodes
            return response.xpath(path + '/text()').extract() if text else response.xpath(path).extract()

        # Check if the selector is 'css'
        elif selector == 'css':
            # If 'text' is True, select the text nodes using '::text' in the CSS expression
            # Otherwise, select elements without text nodes
            return response.css(path + '::text').extract() if text else response.css(path).extract()

        else:
            # Raise a ValueError for an invalid selector type
            raise ValueError("Invalid selector type")


if __name__ == "__main__":
    main = ScrapingUtils()

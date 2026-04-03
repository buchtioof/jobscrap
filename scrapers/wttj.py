from playwright.sync_api import sync_playwright
from bs4 import BeautifulSoup

class WttjScraper(ScraperStrategy):
    
    def can_handle(self, url: str) -> bool:
        return "welcometothejungle.com" in url.lower()

    def extract_data(self, url: str) -> dict:
        with sync_playwright() as p:
            browser = p.chromium.launch()
            page = browser.new_page()

            page.goto(url)
            html_content = page.content()

            output = html_content
            browser.close()
        
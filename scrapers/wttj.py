from contract import ScraperStrategy
from playwright.sync_api import sync_playwright
from bs4 import BeautifulSoup

class WttjScraper(ScraperStrategy):
    
    def can_handle(self, url: str) -> bool:
        return "welcometothejungle.com" in url.lower()

    def extract_data(self, url: str) -> dict:

        # With library Playwright, fetch all page source code
        with sync_playwright() as p:
            browser = p.chromium.launch()
            page = browser.new_page()

            page.goto(url)
            html_content = page.content()

            output = html_content
            browser.close()
        
        # Call Beatifulsoup lib
        soup = BeautifulSoup(html_content, 'html.parser')

        offer_title = soup.find('h2')
        offer = offer_title.text.strip() if offer_title else "No title found for this offer"

        company_name = soup.find('span', class_='sc-TezEC kuLxbv wui-text')
        company = company_name.text.strip() if company_name else "Company name not found"

        return {
            "title": offer,
            "company": company
        }
        
class WttjScraper(ScraperStrategy):
    
    def can_handle(self, url: str) -> bool:
        return "welcometothejungle.com" in url.lower()
        pass

    def extract_data(self, url: str) -> dict:
        from playwright.sync_api import sync_playwright

        with sync_playwright() as p:
            browser = p.chromium.launch()
            page = browser.new_page()

            page.goto(url)
            html_content = page.content()

            print(html_content)
            browser.close()
        pass
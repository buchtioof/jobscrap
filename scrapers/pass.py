from contract import ScraperStrategy
from playwright.sync_api import sync_playwright
from bs4 import BeautifulSoup

class WttjScraper(ScraperStrategy):
    
    def can_handle(self, url: str) -> bool:
        return "pass.fonction-publique.gouv.fr" in url.lower()

    def extract_data(self, url: str) -> dict:

        # With library Playwright, fetch all page source code
        with sync_playwright() as p:
            browser = p.chromium.launch()
            page = browser.new_page()

            page.goto(url)
            page.wait_for_load_state("networkidle")
            html_content = page.content()

            output = html_content
            browser.close()
        
        # Call Beatifulsoup lib
        soup = BeautifulSoup(html_content, 'html.parser')

        offer_title = soup.find('h1')
        offer = offer_title.text.strip() if offer_title else "Aucun titre n'a été trouvé"

        company_name = soup.find('span', class_='sc-TezEC kuLxbv wui-text')
        company = company_name.text.strip() if company_name else "Aucun nom d'entreprise n'a été trouvé"

        titles_h4 = soup.find_all('h4')
        for h4 in titles_h4:
            if "Qui sont-ils" in h4.text:
                corp_div = h4.find_next_sibling('div')
                
                if corp_div:
                    corp_detail = "\n".join(corp_div.stripped_strings)
                
                break

        desc_div = soup.find('div', attrs={'data-testid': 'job-section-description'})
        if desc_div:
            desc = "\n\n".join(desc_div.stripped_strings)

        profile_div = soup.find('div', attrs={'data-testid': 'job-section-experience'})
        if profile_div:
            profile = "\n\n".join(profile_div.stripped_strings)

        return {
            "title": offer,
            "company": company,
            "company_details": corp_detail,
            "description": desc,
            "profile": profile
        }
        
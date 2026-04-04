from contract import ScraperStrategy
from playwright.sync_api import sync_playwright
from bs4 import BeautifulSoup

class PassScraper(ScraperStrategy):
    
    def can_handle(self, url: str) -> bool:
        return "pass.fonction-publique.gouv.fr" in url.lower()

    def extract_data(self, url: str) -> dict:

        with sync_playwright() as p:
            browser = p.chromium.launch()
            page = browser.new_page()

            page.goto(url)
            page.wait_for_load_state("networkidle")
            html_content = page.content()

            browser.close()
        
        soup = BeautifulSoup(html_content, 'html.parser')

        offer = "Aucun titre n'a été trouvé"
        company = "Aucun nom d'entreprise n'a été trouvé"
        corp_detail = "Aucun détail sur l'entreprise n'a été trouvé"
        desc = "Aucune description n'a été trouvée"
        profile = "Aucun profil n'a été trouvé"

        offer_title = soup.find('h1')
        if offer_title:
            offer = offer_title.text.strip()

        corpname_li = soup.find('li', class_='field--name-field-entite')
        if corpname_li:
            corpname_p = corpname_li.find('p', class_='field__item')
            if corpname_p:
                company = corpname_p.text.strip()

        corp_div = soup.find('div', class_='field--name-field-description-de-l-employeur')
        if corp_div:
            corp_item = corp_div.find('div', class_='field__item')
            if corp_item:
                corp_detail = "\n\n".join(corp_item.stripped_strings)

        desc_div = soup.find('div', class_='field--name-field-description-du-poste')
        if desc_div:
            desc_item = desc_div.find('div', class_='field__item')
            if desc_item:
                desc = "\n\n".join(desc_item.stripped_strings)

        profile_div = soup.find('div', class_='field--name-field-descriptif-du-profil-reche')
        if profile_div:
            profile_item = profile_div.find('div', class_='field__item')
            if profile_item:
                profile = "\n\n".join(profile_item.stripped_strings)

        return {
            "title": offer,
            "company": company,
            "company_details": corp_detail,
            "description": desc,
            "profile": profile
        }
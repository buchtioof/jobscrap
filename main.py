import os
from contract import ScraperStrategy
from orchestrator import JobOrchestrator
from scrapers.wttj import WttjScraper
from scrapers.passfr import PassScraper

def main():
    # Create the object
    orchestrator = JobOrchestrator()
    
    # Add the scraper strategy in orchestrator list
    orchestrator.register_strategy(WttjScraper())
    orchestrator.register_strategy(PassScraper())
    
    # Give a URL
    url = input("Entrez l'url de l'offre : ")

    if url:
        print(f"\nFetch offer content: {url}")

        result = orchestrator.process_url(url)

        directory = "output"
        os.makedirs(directory, exist_ok=True)
        filename = f"offer.md"
        path = os.path.join(directory, filename)

        with open(path, "w", encoding="utf-8") as mdfile:
            mdfile.write(result)
                
        print(f"Offer have been saved successfully")

"""     with open("urls.txt", "r") as f:
        for index, line in enumerate(f):
            url = line.strip()
            
            if url:
                print(f"\nFetch offer content: {url}")

                result = orchestrator.process_url(url)

                directory = "output"
                os.makedirs(directory, exist_ok=True)
                filename = f"offer_{index + 1}.md"
                path = os.path.join(directory, filename)

                with open(path, "w", encoding="utf-8") as mdfile:
                    mdfile.write(result)
                
                print(f"Offer have been saved successfully") """

if __name__ == "__main__":
    main()
import os
from contract import ScraperStrategy
from orchestrator import JobOrchestrator
from scrapers.wttj import WttjScraper

def main():
    # Create the object
    orchestrator = JobOrchestrator()
    
    # Add the scraper strategy in orchestrator list
    orchestrator.register_strategy(WttjScraper())
    
    # Give a URL
    with open("urls.txt", "r") as f:
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
                
                print(f"Offers have been saved successfully")

if __name__ == "__main__":
    main()
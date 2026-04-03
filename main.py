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
        for line in f:
            url = line.strip()
            
            if url:
                print(f"\nFetch offer content: {url}")

                result = orchestrator.process_url(url)

                print(result)

if __name__ == "__main__":
    main()
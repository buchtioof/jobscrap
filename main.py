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
        url = f.read()
        
    result = orchestrator.process_url(url)
    
    print(result)

if __name__ == "__main__":
    main()
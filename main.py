from contract import ScraperStrategy
from orchestrator import JobOrchestrator
from strategies import HelloWorkScraper

def main():
    # Create the object
    orchestrator = JobOrchestrator()
    
    # Add the scraper strategy in orchestrator list
    orchestrator.register_strategy(HelloWorkScraper())
    
    # Give a URL
    url = "https://www.welcometothejungle.com/fr/companies/exemple/jobs/developpeur"
    
    result = orchestrator.process_url(url)
    
    print(result)

if __name__ == "__main__":
    main()
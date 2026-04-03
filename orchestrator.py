# Orchestrator.py - Manage all the strategies available

class JobOrchestrator:

    # List every strategies available
    def __init__(self):
        self.strategies = []
    
    # Add new strategies
    def register_strategy(self, strategy):
        self.strategies.append(strategy)

    # Use the good strategy then runs it
    def process_url(self, url: str) -> str:
        
        # Check which strategy is the good one
        for strategy in self.strategies:
            if strategy.can_handle(url):
                print(f"Finding the best scrap strategy...")
                
                # Run strategy extraction and save it here
                data_fetched = strategy.extract_data(url)
                
                # Markdown formatter
                return self._format_markdown(data_fetched)
        
        # Else, error
        return "ERROR: No scraper strategy found for this website."

    # Formatter for fetched data in Markdown
    def _format_markdown(self, data: dict) -> str:
        return f"## {data.get('title', 'Unknown title')} at {data.get('company', 'Unknown company')}\n..."
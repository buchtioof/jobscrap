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
        return f"# {data.get('title', 'Titre inconnu')} à {data.get('company', 'Entreprise inconnue')}\n\n## Détails de l'entreprise\n {data.get('company_details', 'Aucun détail trouvé')}\n\n## Description\n{data.get('description', 'Aucune description trouvée')}\n\n## Profil du candidat\n{data.get('profile', 'Aucune donnée trouvée')}"
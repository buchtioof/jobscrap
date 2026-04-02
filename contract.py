# Contract.py - Define the way Strategies works

# ABC (Abstract Base Classes) protect the "Orchestrator" from false Strategies (ones who doesn't respect this Contract) by being strict on the class
from abc import ABC, abstractmethod

class ScraperStrategy(ABC):

    # Check if the url given corresponds to this Strategy then return TRUE or FALSE 
    @abstractmethod
    def can_handle(self, url: str) -> bool:
        pass

    # Contains the scraping logic from the Strategy
    @abstractmethod
    def extract_data(self, url: str) -> dict:
        pass
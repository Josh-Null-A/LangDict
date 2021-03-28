from abc import ABCMeta, abstractmethod
import requests

class Backend(metaclass=ABCMeta):
    def __init__(self, language):
        self.language = language

    @abstractmethod
    def scrape_translations(self, english):
        pass

class CambridgeBackend(Backend):
    def __init__(self, *args):
        super().__init__(*args)

    def scrape_translations(self, english):
        pass

class GoogleBackend(Backend):
    def __init__(self, *args):
        super().__init__(*args)

    def scrape_translations(self, english):
        pass

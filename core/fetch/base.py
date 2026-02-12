# core/fetch/base.py

class BaseFetcher:

    def search(self, probe: str):
        raise NotImplementedError

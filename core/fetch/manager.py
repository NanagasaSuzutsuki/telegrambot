class FetchManager:

    def __init__(self, fetchers):

        self.fetchers = fetchers

    def search_all(self, probes):

        results = []

        for probe in probes:
            for f in self.fetchers:
                results.extend(f.search(probe))

        return results

import feedparser
from core.fetch.base import BaseFetcher
from core.models import Paper

from core.embed import embed


class ArxivFetcher(BaseFetcher):

    def search(self, probe):

        url = (
            "http://export.arxiv.org/api/query?"
            f"search_query=ti:\"{probe}\"+OR+abs:\"{probe}\""
            "&max_results=20"
        )

        feed = feedparser.parse(url)

        papers = []

        for entry in feed.entries:

            title = entry.title
            abstract = entry.summary

            emb = embed(title + " " + abstract)

            papers.append(
                Paper(
                    id=entry.id,
                    title=title,
                    abstract=abstract,
                    source="arxiv",
                    embedding=emb,
                )
            )

        return papers

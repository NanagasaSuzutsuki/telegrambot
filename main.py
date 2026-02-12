from bot.telegram import run_bot
from core.fetch.arxiv import ArxivFetcher
from core.fetch.manager import FetchManager

fetcher = ArxivFetcher()

manager = FetchManager([fetcher])

TOKEN = ""


if __name__ == "__main__":

    run_bot(TOKEN, manager)

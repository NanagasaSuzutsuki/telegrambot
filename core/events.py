import json
import os

LOG_FILE = "storage/events.jsonl"

def append_event(event):

    os.makedirs("storage", exist_ok=True)

    with open(LOG_FILE, "a") as f:
        f.write(json.dumps(event) + "\n")


def load_events():

    if not os.path.exists(LOG_FILE):
        return []

    with open(LOG_FILE) as f:
        return [json.loads(line) for line in f]

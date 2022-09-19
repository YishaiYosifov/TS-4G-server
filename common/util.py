import json
with open("config.json") as f: CONFIG = json.load(f)

def format_url(url : str) -> str:
    for remove in ["://", "www."]:
        if remove in url: url = "".join(url.split(remove)[1:])
    return url
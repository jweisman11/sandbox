"""
Provides some arithmetic functions
"""



import requests
import textwrap
import pandas as pd
import click
from . import __version__


API_URL = "https://en.wikipedia.org/api/rest_v1/page/random/summary"

# test
# test
####    test
@click.command()
def main():
    """The hypermodern Python project."""
    with requests.get(API_URL) as response:
        print(response)
        response.raise_for_status()
        data = response.json()
    title = data["title"]
    extract = data["extract"]
    click.secho(title, fg="green")
    click.echo(textwrap.fill(extract))


j = [1, 2, 3]

a = {
    "test": [
        {
            "w": "a",
            "w": "a",
            "w": "a",
            "w": "a",
            "w": "a",
            "w": "a",
            "w": "a",
            "w": "a",
            "w": "a",
            "w": "a",
        }
    ]
}

main()

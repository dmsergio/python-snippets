# request_get.py
import json

import requests


ENDPOINT = "https://api.github.com/events"


def get_random_repositories():
    """Make a simple request"""
    response = requests.get(url=ENDPOINT)
    # response.status_code -> code response
    # response.text -> json string... parse with json module to work with it
    # response.content -> good for image data
    # response.json() -> parsed with python structure data
    # json.loads(response.text) -> this is equivalent to response.json()

    print("\nList of GitHub repos:")
    for idx, data in enumerate(response.json(), 1):
        repo_name = data["repo"]["name"]
        print(f"\t{idx}.- {repo_name}")


def get_custom_repositories():
    """Make a request with params"""
    params = {
        "q": "requests+language:python",
        "per_page": "10"
    }
    response = requests.get(url=ENDPOINT, params=params)
    print("\nList of Django repos:")
    for idx, data in enumerate(response.json(), 1):
        repo_name = data["repo"]["name"]
        print(f"\t{idx}.- {repo_name}")


if __name__ == "__main__":
    get_random_repositories()
    get_custom_repositories()

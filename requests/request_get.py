# request_get.py
import requests

URL = "https://api.github.com/events"


def get_request():
    response = requests.get(URL)
    print(response.status_code)
    print(type(response.text))  # parse with json module to work with it
    print(type(response.content))  # good for image data
    print(type(response.json()))  # parsed with python structure data

    print("\nList of GitHub repos:")
    for idx, data in enumerate(response.json(), 1):
        repo_name = data["repo"]["name"]
        print(f"\t{idx}.- {repo_name}")


if __name__ == "__main__":
    get_request()

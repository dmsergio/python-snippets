# request_post.py

import requests


ENDPOINT = "https://httpbin.org/post"


def main():
    post_data = {
        "username": "Sergio",
        "password": "123456",
    }

    response = requests.post(url=ENDPOINT, data=post_data)
    if response.ok:
        data = response.json()
        origin_ip = data["origin"]
        username = data["form"]["username"]
        password = data["form"]["password"]
        print(f"Successful login from {origin_ip} IP!")
        print(f"User: {username}")
        print(f"Pass: {password}")


if __name__ == "__main__":
    main()

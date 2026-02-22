import requests


def get_devpost_hackathons():

    url = "https://devpost.com/api/hackathons"

    params = {
        "status[]": "open",
        "order_by": "deadline"
    }

    response = requests.get(url, params=params)

    data = response.json()

    links = []

    for hackathon in data["hackathons"]:
        links.append(hackathon["url"])

    return links
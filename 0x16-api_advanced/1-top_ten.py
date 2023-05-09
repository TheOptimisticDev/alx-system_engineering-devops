#!/usr/bin/python3
"""
Function that queries the Reddit API and prints the titles of the first 10 hot posts listed for a given subreddit.
"""

def top_ten(subreddit):
    """
    If not a valid subreddit, print None.
    """
    import json
    import requests
    url = "https://www.reddit.com/r/{}/hot/.json".format(subreddit)
    headers = {
        "User-Agent": "User Agent"
    }
    params = {
        "limit": 10
    }
    response = requests.get(url, headers=headers, params=params,
                            allow_redirects=False)
    if response.status_code == 404:
        print("None")
        return
    results = response.json().get("data")
    [print(top.get("data").get("title")) for top in results.get("children")]

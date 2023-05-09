#!/usr/bin/python3
"""
Function that queries the Reddit API and returns the number of subscribers (not active users, total subscribers) for a given subreddit. If an invalid subreddit is given, the function should return 0
"""

import requests

def number_of_subscribers(subreddit):
    """
    If not a valid subreddit, return 0.
    """
    url = 'https://www.reddit.com/r/{}/about.json'.format(subreddit)
    user_agent = 'User Agent'
    headers = {
        'User-Agent': user_agent
    }

    response = requests.get(url, headers=headers, allow_redirects=False)
    if response.status_code == 200:
        result = response.json().get('data')
        return result.get('subscribers')
    else:
        return 0

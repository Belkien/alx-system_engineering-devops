#!/usr/bin/python3
"""Function querying subscribers on a given Reddit API."""
import requests
import sys

def number_of_subscribers(subreddit):
    """  Args:
        subreddit: subreddit name
    Returns:
        number of subscribers to the subreddit,
        or 0 if subreddit requested NOT VALID"""
    headers = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) 9'}
    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    response = requests.get(url, headers=headers, allow_redirects=False)

    if response.status_code == 200:
        return (response.json().get("data").get("subscribers"))
    return (0)



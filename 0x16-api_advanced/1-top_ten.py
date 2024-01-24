import requests

def top_ten(subreddit):
    url = f'https://www.reddit.com/r/{subreddit}/hot.json?limit=10'
    headers = {'User-Agent': 'linux:0x16.api.advanced:v1.0.0 (by/Belkien)'}  # Set your own User-Agent header

    response = requests.get(url, headers=headers)

    """ Check if the request was successful """
    if response.status_code == 200:
        data = response.json()

        """Checking if the subreddit exists"""
        if 'error' in data:
            print(f"Error: {data['message']}")
            return

        """Extracts and print titles of the first 10 hot posts"""
        for i, post in enumerate(data['data']['children'][:10], start=1):
            print(f"{i}. {post['data']['title']}")

    else:
        print(f"Error: Unable to fetch data. Status code: {response.status_code}")



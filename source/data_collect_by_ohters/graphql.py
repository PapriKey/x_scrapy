import requests

proxyHost = ''
proxyPort = ''
proxies = {
    "http": f"http://{proxyHost}:{proxyPort}",
    "https": f"https://{proxyHost}:{proxyPort}",
    "socks": f"socks://{proxyHost}:{proxyPort}"
}

data = {
    "operationName": "UserByScreenName",
    "variables": {
        "screen_name": "elonmusk",
        "withHighlightedLabel": True,
        "withTweetQuoteCount": True,
        "includePromotedContent": True,
        "withTweetResult": False,
        "withReactions": False,
        "withUserResults": False,
        "withVoice": False,
        "withNonLegacyCard": True
    },
    "extensions": {
        "persistedQuery": {
            "version": 1,
            "sha256Hash": ""
        }
    }
}

headers = {
    "x-twitter-client-language": "en"
}

print("proxies:{}".format(proxies))

session = requests.Session()
url = "https://twitter.com/i/api/graphql/_/UserByScreenName"
response = session.post(url, headers=headers, data=data)
print(response.text)

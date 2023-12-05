import requests
import os
import json

# To set your enviornment variables in your terminal run the following line:
# export 'BEARER_TOKEN'='<your_bearer_token>'
bearer_token = os.environ.get("BEARER_TOKEN")


def create_url(usernames="usernames=TwitterDev,TwitterAPI", user_fields="user.fields=description,created_at"):
    # Specify the usernames that you want to lookup below
    # You can enter up to 100 comma-separated values.
    # usernames = "usernames=TwitterDev,TwitterAPI"
    # user_fields = "user.fields=description,created_at"
    # User fields are adjustable, options include:
    # created_at, description, entities, id, location, name,
    # pinned_tweet_id, profile_image_url, protected,
    # public_metrics, url, username, verified, and withheld
    url = "https://api.twitter.com/2/users/by?{}&{}".format(usernames, user_fields)
    return url


def bearer_oauth(r):
    """
    Method required by bearer token authentication.
    """

    r.headers["Authorization"] = f"Bearer {bearer_token}"
    r.headers["User-Agent"] = "v2UserLookupPython"
    return r


def connect_to_endpoint(url):
    response = requests.request("GET", url, auth=bearer_oauth,)
    print(response.status_code)
    if response.status_code != 200:
        raise Exception(
            "Request returned an error: {} {}".format(
                response.status_code, response.text
            )
        )
    return response.json()


def main():
    url = create_url()
    json_response = connect_to_endpoint(url)
    print(json.dumps(json_response, indent=4, sort_keys=True))


def get_user_by_names(usernames, user_fields="user.fields=description,created_at,id,location,name,pinned_tweet_id,"
                                             "profile_image_url,username,verified"):
    """

    :param usernames:
    :param user_fields:
    :return:
    {
      "data": [
        {
          "created_at": "2013-12-14T04:35:55.000Z",
          "username": "TwitterDev",
          "pinned_tweet_id": "1255542774432063488",
          "id": "2244994945",
          "name": "Twitter Dev"
        },
        {
          "created_at": "2007-02-20T14:35:54.000Z",
          "username": "Twitter",
          "pinned_tweet_id": "1274087687469715457",
          "id": "783214",
          "name": "Twitter"
        }
      ],
      "includes": {
        "tweets": [
          {
            "created_at": "2020-04-29T17:01:38.000Z",
            "text": "During these unprecedented times, what’s happening on Twitter can help the world better understand &amp; respond to the pandemic. nnWe're launching a free COVID-19 stream endpoint so qualified devs &amp; researchers can study the public conversation in real-time. https://t.co/BPqMcQzhId",
            "id": "1255542774432063488"
          },
          {
            "created_at": "2020-06-19T21:12:30.000Z",
            "text": "📍 Minneapolisn🗣️ @FredTJoseph https://t.co/lNTOkyguG1",
            "id": "1274087687469715457"
          }
        ]
      }
    }
    """
    url = create_url(usernames, user_fields)
    json_response = connect_to_endpoint(url)
    return json.dumps(json_response, indent=4, sort_keys=True)


if __name__ == "__main__":
    main()

"""
the data from 1201 is collected by third party,
using the hashtags, and don't collect the social network
"""
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

from collections import Counter


def user_properties_analysis(filename="../../data/US2020election_user.csv"):
    with open(filename, "rb") as f:
        data = pd.read_csv(f)
    tweet_count = data['tweets_count'].values
    liked_tweet_count = data['liked_tweets_count'].values
    follower_count = data['followers_count'].values
    following_count = data['followings_count'].values

    tweet_count.sort()
    a = tweet_count // 100
    a = Counter(a)
    x = [1000.]
    y = [0.]
    for xi, yi in a.items():
        if xi < 1000:
            x.append(xi)
            y.append(yi)
        else:
            y[0] += yi
    plt.plot(x, y)
    plt.show()


def user_related_tweets_analysis(filename="../../data/US2020election_tweet.csv"):
    with open(filename, "rb") as f:
        data = pd.read_csv(f)


if __name__ == "__main__":
    user_properties_analysis()

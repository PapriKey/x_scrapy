"""
the data from 1201 is collected by third party,
using the hashtags, and don't collect the social network
"""
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

from collections import Counter


def plot_by_percentage(array, base=100, **kwargs):
    array.sort()
    y = []
    for i in range(base+1):
        y.append(array[int(len(array) * (i / (base + 1)))])
    plt.plot(y)
    for i in range(10):
        i *= 10
        plt.text(i, y[i], y[i], ha='center', va='bottom', fontsize=10)
    plt.title(kwargs['title'])
    plt.ylabel(kwargs['ylabel'])
    plt.xlabel(kwargs['xlabel'])
    xi = int(base * 0.7)
    yi = int(y[-1] * 0.8)
    plt.text(xi, yi, 'mean: {}'.format(int(array.mean())), fontsize=10)
    yi = int(y[-1] * 0.7)
    plt.text(xi, yi, 'median: {}'.format(y[base//2]), fontsize=10)
    plt.savefig(kwargs['savefig_path'])
    # plt.show()
    plt.clf()
    plt.cla()


def user_properties_analysis(filename="../../data/US2020election_user.csv"):
    with open(filename, "rb") as f:
        data = pd.read_csv(f)
    tweet_count = data['tweets_count'].values
    liked_tweet_count = data['liked_tweets_count'].values
    follower_count = data['followers_count'].values
    following_count = data['followings_count'].values

    info = {
        'title': 'user tweets analysis',
        'ylabel': 'tweets count',
        'xlabel': 'percentage',
        'savefig_path': './data/user_tweets_analysis'
    }
    plot_by_percentage(tweet_count, **info)

    info['title'] = 'user_liked_tweet_analysis'
    info['savefig_path'] = './data/user_liked_tweet_analysis'
    plot_by_percentage(liked_tweet_count, **info)

    info['title'] = 'user_following_count_analysis'
    info['ylabel'] = 'following_count'
    info['savefig_path'] = './data/' + info['title']
    plot_by_percentage(following_count, **info)

    info['title'] = 'user_follower_count_analysis'
    info['ylabel'] = 'follower_count'
    info['savefig_path'] = './data/' + info['title']
    plot_by_percentage(follower_count, **info)


def user_related_tweets_analysis(filename="../../data/US2020election_user2tweet.csv"):
    with open(filename, "rb") as f:
        data = pd.read_csv(f)
    user_related_tweets_count = data['user_id'].value_counts().values
    counter = Counter(user_related_tweets_count)

    # 1~10
    x = list(range(1, 11))
    y = []
    for xi in x:
        if xi in counter:
            y.append(counter[xi])
        else:
            y.append(0)
    plt.title('user_related_tweets_count: 1~10')
    plt.ylabel('user_count')
    plt.xlabel('tweet_count')
    plt.bar(x=x, height=y, )
    for i in range(len(x)):
        plt.text(x[i], y[i], y[i], ha='center', va='bottom')
    plt.text(9, 13e3, 'user_total: {}'.format(sum(y)), ha='center', va='bottom')
    # plt.show()
    plt.savefig('./data/user_related_tweets_count_1~10')
    plt.clf()
    plt.cla()

    counter_interval = Counter(user_related_tweets_count // 5)
    counter_interval.pop(0)
    counter_interval.pop(1)

    plt.title('user_related_tweets_count: interval')
    plt.ylabel('user_count')
    plt.xlabel('tweet_count // 5')
    x = list(counter_interval.keys())
    y = list(counter_interval.values())
    plt.bar(x=x, height=y, )
    for i in range(len(x)):
        if x[i] > 25:
            continue
        plt.text(x[i], y[i], y[i], ha='center', va='bottom')
    plt.text(20, 350, 'user_total: {}'.format(sum(y)), ha='center', va='bottom')
    plt.xlim(1, 25)
    # plt.show()
    plt.savefig('./data/user_related_tweets_count_interval')
    plt.clf()
    plt.cla()


def tweet_properties_analysis(filename="../../data/US2020election_tweet.csv"):
    with open(filename, "rb") as f:
        data = pd.read_csv(f)
    # create_at = data['create_at'].values
    liked_count = data['liked_count'].values
    mention_count = data['mention_count'].values
    retweet_count = data['retweet_count'].values

    info = {
        'title': 'tweet_liked_user_count',
        'ylabel': 'user_count',
        'xlabel': 'percentage',
        'savefig_path': './data/tweets_liked_user_count'
    }
    plot_by_percentage(liked_count, **info)

    info['title'] = 'tweet_mention_count'
    info['savefig_path'] = './data/' + info['title']
    plot_by_percentage(mention_count, **info)

    info['title'] = 'tweet_retweet_count'
    info['savefig_path'] = './data/' + info['title']
    plot_by_percentage(retweet_count, **info)


if __name__ == "__main__":
    # user_properties_analysis()
    # user_related_tweets_analysis()
    # tweet_properties_analysis()

    with open('../../data/us_2020_election/degree_1.csv', 'r') as f:
        nodes_df = pd.read_csv(f)

    info = {
        'title': 'degree_count',
        'ylabel': 'degree',
        'xlabel': 'percentage',
        'savefig_path': './data/degree_count'
    }

    plot_by_percentage(nodes_df['degree'].values, **info)
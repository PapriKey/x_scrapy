"""
the data from 1201 is collected by third party,
using the hashtags, and don't collect the social network
"""
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from ast import literal_eval
from collections import Counter


def plot_by_percentage(array, base=100, **kwargs):
    plt.figure(figsize=(10, 6))  # 调整图表尺寸
    array = np.array(array)
    array.sort()
    y = [array[int(len(array) * (i / (base + 1)))] for i in range(base + 1)]
    plt.plot(y)
    for i in range(0, 101, 10):
        plt.text(i, y[i], str(y[i]), ha='center', va='bottom', fontsize=8)
    plt.title(kwargs['title'])
    plt.ylabel(kwargs['ylabel'])
    plt.xlabel(kwargs['xlabel'])
    xi = int(base * 0.7)
    yi = int(y[-1] * 0.8)
    plt.text(xi, yi, 'mean: {}'.format(int(array.mean())), fontsize=10)
    yi = int(y[-1] * 0.7)
    plt.text(xi, yi, 'median: {}'.format(int(np.median(array))), fontsize=10)
    plt.subplots_adjust(left=0.15, bottom=0.15)  # 调整边界
    plt.savefig(kwargs['savefig_path'])
    plt.clf()
    plt.cla()

def user_properties_analysis(filename="../../data/us_2020_election/user_1.csv"):
    with open(filename, "rb") as f:
        data = pd.read_csv(f)

    # 将字符串表示的字典转换为字典对象
    data['public_metrics'] = data['public_metrics'].apply(literal_eval)

    # 现在你可以像这样访问字典中的值
    tweet_count = data['public_metrics'].apply(lambda x: x['tweet_count']).values
    # liked_tweet_count = data['liked_tweets_count'].values
    follower_count = data['public_metrics'].apply(lambda x: x['followers_count']).values
    following_count = data['public_metrics'].apply(lambda x: x['following_count']).values

    info = {
        'title': 'user tweets',
        'ylabel': 'tweets count',
        'xlabel': 'percentage',
        'savefig_path': './data/user_tweets_analysis'
    }
    plot_by_percentage(tweet_count, **info)

    # info['title'] = 'user_liked_tweet_analysis'
    # info['savefig_path'] = './data/user_liked_tweet_analysis'
    # plot_by_percentage(liked_tweet_count, **info)

    info['title'] = 'user_following_count_analysis'
    info['ylabel'] = 'following_count'
    info['savefig_path'] = './data/' + info['title']
    plot_by_percentage(following_count, **info)

    info['title'] = 'user followers count'
    info['ylabel'] = 'followers count'
    info['savefig_path'] = './data/' + info['title']
    plot_by_percentage(follower_count, **info)

def user_related_tweets_analysis(filename="../../data/us_2020_election/key_tweet_1.csv"):
    with open(filename, "rb") as f:
        data = pd.read_csv(f)
    user_related_tweets_count = data['user_id'].value_counts().values
    counter = Counter(user_related_tweets_count)

    # 1~30
    x = list(range(1, 31))
    y = []
    for xi in x:
        y.append(counter.get(xi, 0))
    plt.title('User Related Tweets Count (1-30)')
    plt.ylabel('Users Count')
    plt.xlabel('Tweets Count')
    plt.bar(x=x, height=y)
    for i in range(len(x)):
        plt.text(x[i], y[i], str(y[i]), ha='center', va='bottom')
    plt.text(25, max(y) * 0.9, 'user_total: {}'.format(sum(y)), ha='center', va='bottom')

    # 设置x轴的刻度为整数，并间隔1个显示
    plt.xticks(x[::2])  # 修改这里来控制间隔显示，例如[::2]为每2个显示一个刻度

    plt.savefig('./data/user_related_tweets_count_1~30')
    plt.clf()
    plt.cla()

    # 对于区间，我们需要重新计算counter_interval
    # 为了使x轴范围为1到30，我们需要调整计数逻辑
    counter_interval = Counter((user_related_tweets_count - 1) // 5 + 1)
    # 移除不在1到30范围内的键
    keys_to_remove = [key for key in counter_interval.keys() if key < 1 or key > 30]
    for key in keys_to_remove:
        del counter_interval[key]

    plt.title('user_related_tweets_count: interval')
    plt.ylabel('user_count')
    plt.xlabel('tweet_count // 5')
    x = list(range(1, 31))  # 确保x轴范围为1到30
    y = [counter_interval.get(xi, 0) for xi in x]  # 获取每个区间的计数
    plt.bar(x=x, height=y)
    for i in range(len(x)):
        plt.text(x[i], y[i], y[i], ha='center', va='bottom')
    plt.text(25, 350, 'user_total: {}'.format(sum(y)), ha='center', va='bottom')
    plt.xlim(0.5, 30.5)  # 设置x轴的显示范围稍微宽一点，确保第一个和最后一个柱形完全显示
    plt.xticks(x)  # 设置x轴的刻度为整数
    plt.savefig('./data/user_related_tweets_count_interval')
    plt.clf()
    plt.cla()

def tweet_properties_analysis(filename="../../data/us_2020_election/key_tweet_1.csv"):
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
    user_properties_analysis()
    user_related_tweets_analysis()
    tweet_properties_analysis()

    # with open('../../data/us_2020_election/degree_1.csv', 'r') as f:
    #     nodes_df = pd.read_csv(f)
    #
    # info = {
    #     'title': 'degree_count',
    #     'ylabel': 'degree',
    #     'xlabel': 'percentage',
    #     'savefig_path': './data/degree_count'
    # }
    #
    # plot_by_percentage(nodes_df['degree'].values, **info)


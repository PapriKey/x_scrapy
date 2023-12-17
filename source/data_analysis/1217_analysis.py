import re

import numpy as np
import pandas as pd


def read_data_from_csv(filename):
    with open(filename, 'rb') as f:
        df = pd.read_csv(f)
    return df


def user_followers_sum():
    users = read_data_from_csv('../../data/US2020election_user.csv')
    # users['followers_count'] = users['followers_count'].apply(lambda x : int(x) if int(x) < 100 else 100)
    return users['followers_count'].sum()


drop_patten = r'[#@][_\w]+'


def drop_hashtag_a(obj):
    text = str(obj).strip()
    return ''.join(re.split(drop_patten, text))


def tweet_len_clean():
    tweets = read_data_from_csv('../../data/US2020election_tweet_new.csv')
    tweets['text'] = tweets['text'].apply(lambda x: drop_hashtag_a(x))
    tweets['text'] = tweets['text'].apply(lambda x:
                         0 if str(x).lower().find('rt') >= 0 or str(x).lower().find('retweet') >= 0
                         else len(str(x).strip().split()))
    tweets = tweets[tweets['text'] >= 10]
    tweets = tweets[tweets['text'] <= 128]
    user_related_tweets_count = tweets['user_id'].value_counts(ascending=True)
    user2tweet_a_clean = pd.DataFrame(
        np.concatenate(
            (user_related_tweets_count.index.values.reshape(-1, 1), user_related_tweets_count.values.reshape(-1, 1)),
            axis=1),
        columns=['user_id', 'tweet_count'])
    user2tweet_a_clean = user2tweet_a_clean[user2tweet_a_clean['tweet_count'] < 3]
    user2tweet_a_clean.to_csv('./data/user2tweet_a_clean.csv', index=False)
    return user2tweet_a_clean.shape[0]


def user_followers_sum_from_new():
    users = read_data_from_csv('../../data/US2020election_user.csv')
    users_new = read_data_from_csv('./data/user2tweet_a_clean.csv')
    useful_user = pd.merge(users_new, users, on='user_id', how='left')
    useful_user = useful_user[useful_user['followers_count'] < 200]  # 1128
    print(useful_user.shape[0])
    useful_user.to_csv('../../data/US2020election_need_osn_user.csv', index=False)
    return useful_user['followers_count'].sum()


if __name__ == '__main__':
    # print(user_followers_sum())
    # 293,194,306 no limit
    # 8,160,996 250
    # 3,354,137 100
    # user2tweet = read_data_from_csv('../../data/US2020election_user2tweet.csv')
    # tweets = read_data_from_csv('../../data/US2020election_tweet.csv')
    # new = pd.merge(tweets, user2tweet, on='tweet_id', how='left')
    # new.to_csv('../../data/US2020election_tweet_new.csv', index=False)
    # tweet_len_clean()
    print(user_followers_sum_from_new())  # 97,377,889, 104,195

import json
from collections import Counter

import networkx as nx
import pandas as pd
import matplotlib.pyplot as plt


def graph_degree():
    with open('../../data/us_2020_election/user_1.csv', 'r') as f:
        nodes_df = pd.read_csv(f)
    with open('../../data/us_2020_election/osn_1.csv', 'r') as f:
        edges_df = pd.read_csv(f)
    with open('../../data/us_2020_election/degree_1.csv', 'r') as f:
        degree_df = pd.read_csv(f)

    edge_types = edges_df['relation'].unique().tolist()
    max_degree = degree_df['degree'].idxmax()
    print(max_degree)
    # node_id = degree_df['id'].iloc[max_degree]
    node_id = 'u2591320394'
    print(node_id)

    # edge_type1_df = edges_df[edges_df['relation'] == edge_types[0]]
    ids = [node_id]
    ids += edges_df[edges_df['source_id'] == node_id][['target_id']].values.squeeze().tolist()
    ids += edges_df[edges_df['target_id'] == node_id][['source_id']].values.squeeze().tolist()

    edge_new = edges_df[edges_df['source_id'].isin(ids)]
    edge_new = edge_new[edge_new['target_id'].isin(ids)]
    g = nx.Graph()
    # g.add_nodes_from(edges_df[['source_id', 'target_id']].values)
    # g.add_edges_from(edges_df[['source_id', 'target_id']].values)
    g.add_edges_from(edge_new[['source_id', 'target_id']].values)
    print(g.degree)
    # degree_df = pd.DataFrame(g.degree, columns=['id', 'degree'])
    # print(degree_df)
    # degree_df.to_csv('../../data/us_2020_election/degree_1.csv', index=False)
    # pos = nx.spring_layout(g)
    # nx.draw_networkx(g, pos)
    # labels = nx.get_edge_attributes(g, 'weight')
    # nx.draw_networkx_edge_labels(g, pos)
    nx.draw(g, node_size=20, edge_color='g')
    plt.show()


def osn():
    edges_filename = '/home/majun/data/datasets/TwiBot-22/edge.csv'
    with open(edges_filename, 'r') as f:
        edges = pd.read_csv(f)
    with open('../../data/us_2020_election/user_1.csv', 'r') as f:
        users = pd.read_csv(f)
    user_ids = users['id'].unique().tolist()
    other_user_ids = edges[edges['source_id'].isin(user_ids)]['target_id'].values.squeeze().tolist()
    other_user_ids += edges[edges['target_id'].isin(user_ids)]['source_id'].values.squeeze().tolist()
    other_user_ids += user_ids
    other_user_ids = list(Counter(other_user_ids).keys())
    print(len(other_user_ids))  # 2442021
    with open('../../data/us_2020_election/id.txt', 'w') as f:
        for user_id in other_user_ids:
            f.write(user_id + '\n')
    # edges_all = edges[edges['source_id'].isin(other_user_ids)]
    # edges_all = edges_all[edges_all['target_id'].isin(other_user_ids)]
    # print(edges_all.shape[0])
    # edges_all.to_csv('../../data/us_2020_election/edge.csv', index=False)


def user():
    user_filename = '/home/majun/data/datasets/TwiBot-22/user.json'
    with open(user_filename, 'r') as f:
        users = json.load(f)
    users_df = pd.DataFrame(users)
    print(users_df.shape[0])  # 1000000
    with open('../../data/us_2020_election/id.txt', 'r') as f:
        ids = f.readlines()
    ids = [id.strip() for id in ids]
    print(len(ids))
    users_all = users_df[users_df['id'].isin(ids)]
    print(users_all.shape)  # (63999, 14)
    users_all.to_csv('../../data/us_2020_election/user.csv', index=False)


def tweet():
    user_filename = '/home/majun/data/datasets/TwiBot-22/'
    with open('../../data/us_2020_election/id.txt', 'r') as f:
        ids = f.readlines()
    ids = [id.replace('u', '').strip() for id in ids]
    tweet_id = []
    user_id = []
    for id in ids:
        if id[0] == 't':
            tweet_id.append(id)
        elif id[0] in '0123456789':
            user_id.append(int(id))

    print(len(tweet_id))  # 2369074
    print(len(user_id))  # 63999
    tweet_relation = None
    for i in range(9):
        with open(user_filename + ('tweet_%d.json' % i), 'r') as f:
            tweets = json.load(f)
        tweets_df = pd.DataFrame(tweets)
        # tweet_0 = tweets_df[tweets_df['id'].isin(tweet_id)]
        # print(tweet_0.shape[0])
        # if tweet_relation is None:
        #     tweet_relation = tweet_0
        # else:
        #     tweet_relation = pd.concat([tweet_relation, tweet_0], ignore_index=True)
        tweet_i = tweets_df[tweets_df['author_id'].isin(user_id)]
        print(tweet_i.shape)
        tweet_i.to_csv('../../data/us_2020_election/tweet_%d.csv' % i, index=False)
    # print(tweet_relation.shape)
    # if tweet_relation is not None:
    #     tweet_relation.to_csv('../../data/us_2020_election/tweet_relation.csv', index=False)
    """
    tweet_0 
    tweet relation
    195308
    565382
    188731
    192716
    224781
    203930
    237428
    238016
    322782
    (2369074, 17)
    """


if __name__ == '__main__':
    # with open('../../data/us_2020_election/edge.csv', 'r') as f:
    #     edge = pd.read_csv(f)
    # # print(edge['relation'].value_counts())
    # types = pd.DataFrame(edge['relation'].value_counts(), columns=['count'])
    # print(types)
    tweet()
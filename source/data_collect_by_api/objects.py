import json
import os.path
import csv

from abc import ABCMeta, abstractmethod
from source.twitter_api import get_users_with_bearer_token as user_properties
from source.twitter_api import user_tweets as user_timelines
from source.twitter_api import followers_lookup as user_followers
from source.twitter_api import following_lookup as user_followings
from source.twitter_api import user_mentions as user_mentions
from source.twitter_api import liked_tweets as user_likes


class NodeWithEdges(metaclass=ABCMeta):
    @abstractmethod
    def get_edge(self):
        raise NotImplementedError("method: get_edge must be implemented")

    @abstractmethod
    def get_node_properties(self):
        raise NotImplementedError("method: get_node_properties must be implemented")

    @abstractmethod
    def get_node_information(self):
        raise NotImplementedError("method: get_node_information must be implemented")

    @abstractmethod
    def get_relations2nodes(self):
        raise NotImplementedError("method: get_relations2nodes must be implemented")




class Tweet(object):
    def __init__(self):
        pass

    def get_post_from_remote(self):
        pass


class User(object, NodeWithEdges):

    def __init__(self, unique):
        self.unique = unique
        self.username = unique
        self.user_id = None
        self.properties = None
        self.liked_tweets = None
        self.mentions = None
        self.timelines = None
        self.followers = None
        self.followings = None

    def set_from_remote(self):
        # TODO fix format errors of user.properties
        # TODO modify the fields of twitter api
        self.properties = json.loads(user_properties.get_user_by_names(self.username))['data'][0]
        self.user_id = self.properties['id']
        self.timelines = user_timelines.get_tweets_by_userid(self.user_id)
        self.followings = json.loads(user_followings.get_followings_by_userid(self.user_id))['data']
        self.followers = json.loads(user_followers.get_followers_by_userid(self.user_id))['data']
        self.mentions = user_mentions.get_mentions_by_userid(self.user_id)
        self.liked_tweets = user_likes.get_user_liked_tweets_by_user_id(self.user_id)

    def get_user_properties(self):
        pass

    def get_user_social_network(self):
        return self.followers, self.followings

    def save_tweets_to_file(self, path):
        # TODO: save as csv file: user, tweets, mentions, followers, followings
        # save the user to US2020election/user.csv
        parent_path = 'US2020election'
        filename = os.path.join(path, parent_path, 'user.csv')
        with open(filename, 'a', newline='', ) as f:
            pass


    def get_edge(self):
        return [val['username'] for val in self.followers + self.followings]

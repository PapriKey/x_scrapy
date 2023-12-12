import json
import os.path
import csv

from abc import ABCMeta, abstractmethod
from source.data_collect_by_api.x_api import get_users_with_bearer_token as user_properties
from source.data_collect_by_api.x_api import user_tweets as user_timelines
from source.data_collect_by_api.x_api import followers_lookup as user_followers
from source.data_collect_by_api.x_api import following_lookup as user_followings
from source.data_collect_by_api.x_api import user_mentions as user_mentions
from source.data_collect_by_api.x_api import liked_tweets as user_likes


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
        self.is_update = False

    def set_from_remote(self):
        self.properties = json.loads(user_properties.get_user_by_names(self.username))['data'][0]
        self.user_id = self.properties['id']
        self.timelines = user_timelines.get_tweets_by_userid(self.user_id)
        self.followings = json.loads(user_followings.get_followings_by_userid(self.user_id))['data']
        self.followers = json.loads(user_followers.get_followers_by_userid(self.user_id))['data']
        self.mentions = user_mentions.get_mentions_by_userid(self.user_id)
        self.liked_tweets = user_likes.get_user_liked_tweets_by_user_id(self.user_id)

    def get_node_properties(self):
        return self.properties

    def get_node_information(self):
        return {'user_id': self.user_id,
                'liked_tweets': self.liked_tweets,
                'mentions': self.mentions,
                'timelines': self.timelines}

    def get_relations2nodes(self):
        return {
            'user_id': self.user_id,
            'followers': self.followers,
            'followings': self.followings
        }

    def get_edge(self):
        if not self.is_update:
            self.set_from_remote()
        return [val['username'] for val in self.followers + self.followings]

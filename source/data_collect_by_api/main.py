import os

from source.data_collect_by_api.bfs import breadth_first_search_collect
from source.data_collect_by_api.data_clean import write_to_file

if __name__ == '__main__':
    os.environ['BEARER_TOKEN'] = ''  # TODO:
    nodes = breadth_first_search_collect()
    filenames = {
        'nodes_data': 'user.csv',
        'nodes_other_data': 'user_tweets.csv',
        'relations_data': 'relations.csv'
    }
    write_to_file(nodes, filepath='../../data/US2020_election', filenames=filenames)

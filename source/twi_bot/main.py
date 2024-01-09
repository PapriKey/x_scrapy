import os

import pandas as pd

from source.data_collect_by_api.bfs import breadth_first_search_collect
from source.data_collect_by_api.objects import TwiBotUsers
from source.twi_bot.data_process import get_seed_users
from source.twi_bot.file_utils import read_data_from_file


if __name__ == '__main__':

    params = {
        'twi_bot_dir': ''
    }
    data_dir = '../../data/us_2020_election'
    os.makedirs(data_dir, exist_ok=True)
    TwiBotUsers.edges = read_data_from_file(os.path.join(params['twi_bot_dir'], 'edge.csv'))
    users = breadth_first_search_collect(get_seeds=get_seed_users, node_cls=TwiBotUsers, **params)
    id_list = [user.id for user in users]
    osn_list = [user.get_osn() for user in users]
    osn_df = pd.concat(osn_list, axis=0)
    osn_df.to_csv(os.path.join(data_dir, 'osn.csv'), index=False)

    users_in_tb = get_seed_users(related_us_2020_election=False, filename='')
    users_in_tb = pd.DataFrame(users_in_tb)
    user_df = users_in_tb[users_in_tb['id'].isin(id_list)]
    user_df.to_csv(os.path.join(data_dir, 'user.csv'), index=False)

    # 差一个tweet 日后再说
    print('差一个 tweet.csv')
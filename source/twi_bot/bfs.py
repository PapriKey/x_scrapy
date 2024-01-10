import os
import pandas as pd

from source.data_collect_by_api.bfs import breadth_first_search_collect
from source.data_collect_by_api.objects import TwiBotUsers
from source.twi_bot.data_process import get_seed_users
from source.twi_bot.file_utils import read_data_from_file


if __name__ == '__main__':

    params = {
        'twi_bot_dir': '/home/majun/datasets/TwiBot-22'
    }
    data_dir = '../../data/us_2020_election'
    os.makedirs(data_dir, exist_ok=True)
    edges = read_data_from_file(os.path.join(params['twi_bot_dir'], 'edge.csv'))
    user_id = get_seed_users()
    users_in_tb = get_seed_users(related_us_2020_election=False, filename='/home/majun/datasets/TwiBot-22/user.json')
    users_in_tb = pd.DataFrame(users_in_tb)

    data0 = edges[edges['source_id'].isin(user_id)]
    data1 = data0[data0['target_id'].isin(user_id)]
    data1.to_csv(os.path.join(data_dir, 'osn_1.csv'), index=False)
    users1 = users_in_tb[users_in_tb['id'].isin(user_id)]
    users1.to_csv(os.path.join(data_dir, 'user_1.csv'), index=False)

    # print(data1.shape[0])  # 17406
    # print(data1['source_id'].value_counts())  # 172

    data2 = data0[[not val for val in data0['target_id'].isin(user_id).values]]
    data3 = data2[data2['relation'].isin(['followers', 'following'])]
    user_id += data3['target_id'].values.tolist()
    print(len(user_id))  # 80671
    data4 = edges[edges['source_id'].isin(user_id)]
    data5 = data4[data4['target_id'].isin(user_id)]
    data1.to_csv(os.path.join(data_dir, 'osn_2.csv'), index=False)
    users2 = users_in_tb[users_in_tb['id'].isin(user_id)]
    users2.to_csv(os.path.join(data_dir, 'user_2.csv'), index=False)
    print(data5.shape[0])  # 266891
    print(data5['source_id'].value_counts())  # 1173


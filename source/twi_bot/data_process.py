import os

from source.twi_bot.file_utils import read_data_from_file


def get_users_from_twi_bot(**kwargs):
    data_dir = kwargs.get('data_dir', '../../data/')
    cache_filename = kwargs.get('cache_filename', 'related_users_in_twi_bot.csv')
    users_election_filename = kwargs.get('users_election_filename', 'US2020election_user.csv')
    twi_bot_dir = kwargs.get('twi_bot_dir', None)

    if os.path.exists(os.path.join(data_dir, cache_filename)):
        return read_data_from_file(os.path.join(data_dir, cache_filename), **kwargs)['id'].values.tolist()

    if twi_bot_dir is None:
        return None

    users = read_data_from_file(os.path.join(twi_bot_dir, 'users.json'), **kwargs)
    users_in_election = read_data_from_file(os.path.join(data_dir, users_election_filename), **kwargs)

    if users is None or users_in_election is None:
        return None

    usernames = users_in_election['username'].values.tolist()
    related_users_in_twi_bot = users[users['username'].isin(usernames)]
    related_users_in_twi_bot.to_csv(os.path.join(data_dir, cache_filename), index=False)
    return related_users_in_twi_bot['id'].values.tolist()


def get_seed_users(related_us_2020_election=True, filename='../../data/seed_users.csv', **kwargs):
    if related_us_2020_election:
        return get_users_from_twi_bot(**kwargs)
    return read_data_from_file(filename, **kwargs)


if __name__ == '__main__':
    seed_users = read_data_from_file('../../data/related_users_in_twi_bot.csv')
    print(seed_users)
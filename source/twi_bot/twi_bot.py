import json
import pandas as pd


filename = ''


def hashtag():
    with open(filename, "r") as f:
        data_lists = json.load(f)
    with open('../../data/filter_hashtag.txt', 'r') as f:
        filtered_data = f.readlines()
    count = {}
    filtered_data = [elem.strip().lower() for elem in filtered_data]
    for data in data_lists:
        for ht in filtered_data:
            if ht in data['tag_name'].lower():
                # print(data['tag_name'])
                if ht not in count:
                    count[ht] = 0
                count[ht] += 1
    print(count)
    """
    {'republican': 601, 'voteblue': 167, 'maga': 3209, 'election2020': 51, 'joebiden': 182, 'donaldtrump': 116, 'bidenharris2020': 9, 'democrats': 322, 'nevertrump': 14, 'dumptrump': 14, 'neverbiden': 8, 'americafirst': 28, 'trumpcrimefamily': 19, 'trumptrain': 11, 'berniesanders': 23, 'sanders': 212, 'keepamericagreat': 3, 'notmypresident': 21, 'bernie2020': 4, 'berniewon': 2, 'feelthebern': 7, 'notmeus': 4, 'trumpresign': 5, 'sleepyjoe': 7, 'bidencrimefamily': 9, 'bidenlied': 6, 'neverbernie': 2, 'trump2020landslide': 2, 'notmypresidentbiden': 2, 'sandersforpresident': 2, 'bidenforpresident': 1, 'joeandkamala': 1}
    """


def seed_user():
    with open(filename, "r") as f:
        data_lists = pd.DataFrame(json.load(f))
    with open('../../data/US2020election_user.csv', 'rb') as f:
        df = pd.read_csv(f)
    usernames = df['username'].values.tolist()
    usernames = [username.strip() for username in usernames]

    users_in_twi_bot = data_lists[data_lists['username'].isin(usernames)]
    print(len(users_in_twi_bot))  # 8570
    users_in_twi_bot.to_csv('../../data/related_users_in_twi_bot.csv', index=False)
    """
    ['KamalaHarris', 'IlhanMN', 'RealCandaceO', 'BarackObama', 'ladygaga', 'SarahKSilverman', 'MMFlint', 'SenWarren', 'AOC', 'MarkRuffalo', 'BernieSanders', 'MichelleObama', 'LindseyGrahamSC', 'charliekirk11', 'kayleighmcenany', 'SarahHuckabee', 'TuckerCarlson', 'seanhannity', 'johnlegend', 'DannyDeVito', 'KingJames', 'ninaturner']
    22
    """


def edge():
    # with open(filename, "rb") as f:
    #     data_lists = pd.read_csv(f)
    with open('../../data/US2020election_user.csv', 'rb') as f:
        users = pd.read_csv(f)
    usernames = users[users['username']=='HastaElFinaII']['username'].values
    print(type(usernames[0]))
    print(str(usernames))


if __name__ == "__main__":
    edge()

import pandas as pd
import matplotlib.pyplot as plt

# 读取.csv文件
df = pd.read_csv('../../data/us_2020_election/key_tweet_1.csv')


# 计算每个用户的发帖数
user_post_counts = df['user_id'].value_counts()

# 计算每个用户的发帖数在总发帖数中的百分比
user_post_percentages = user_post_counts / user_post_counts.sum() * 100

# 绘制柱状图
plt.figure(figsize=(12, 6))
plt.bar(range(len(user_post_percentages)), user_post_percentages.values, color='skyblue')
plt.xlabel('Users')
plt.ylabel('Percentage of Posts (%)')
plt.title('User Post Distribution')
plt.xticks(range(len(user_post_percentages)), user_post_percentages.index, rotation=45)
plt.show()
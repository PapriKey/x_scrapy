# 1201
## do
* 使用data_collect_1中的方法，从第三方手中获取到了6万多条数据（只使用了前12个关键字）
## problem
* 总结可以从哪些方面进行数据标注
* 如何获取到社交网络数据
* 方法2的中seed users不包含反对者

# 1205
## do
* 对获取到的数据进行了分析(x_scrapy/source/data_analysis/data)
## idea
* 使用BFS时，边最好使用followers。观察followers和followings统计图，
可以发现，用户间的followers数量差距远远小于followings数量差距
* 是否要使用{liked, mention, retweet} 作为边
* 到底该如何获取社交网络信息，第三方还是自己写爬虫
* 自己写爬虫的难度较高：
  1. 推特对每个账户做了限制。每天能过获取的推文数量有限
  2. 未认证的账户只能观察到一个用户的部分follower/following信息
  3. 认证的账户是否能观察到全部的follower/following信息，也还不清楚
* 如何定下非文本数据用于数据标注的尺度
* 没有数据，难以完善data_collect_by_api部分的代码

# 1206
## do
* 整理可以用于数据标注的特征
  1. user_timeline (recent tweets)
  2. retweeted (if not...support...)
  3. mention (...oppose...)
  4. liked (...support...)
  5. follower/following (...homo...)
  6. name, description, location(it may or may not work)

* online social network(OSN)
  1. follower
  2. following (too many)
  3. retweet
  4. liked
  5. mention

* 特征的用法
  1. 做成统计图，用于给标注者提供信息
  2. 用做后台打分
  3. 用作标注质量的检测

* 标注的尺度
  1. 等待更进一步的统计研究

* 尝试了reddit的API接口

## TODO
* 完善数据获取的代码
* 完善标注尺度
* 考虑该如何获取数据

## idea
* 目前遇到的主要问题，还是数据的获取方面，如果有足够的数据用作研究，那么上述问题可能会得到解决。
  1. 如标注的尺度、特征的用法，可以从足量的已标注数据的特征分布得出（这样与使用机器学习的方法有何不同？）
  2. 不能获取数据，就无法进一步的实践
  3. 现在获取到的数据进行标注的话，实际上，按照最好的情况进行估计，也不过是对P-Stance进行扩充

* 推特的API
  1. 对于获取的推文，做了时间上的限制（最近7天）
  2. 不提供获取用户关注、粉丝列表的权限
  3. 不提供过滤功能

* 第三方的爬虫
  1. 只能根据关键字进行推文搜索（可能无法获取完整的社交网络）
  2. osn只能获取follower/following

* 数据获取方面过于困难，感觉不能推进
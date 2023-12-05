# 1201
## do
* 使用data_collect_1中的方法，从第三方手中获取到了6万多条数据（只使用了前12个关键字）
## problem
* 总结可以从哪些方面进行数据标注
* 如何获取到社交网络数据
* 方法2的中seed users不包含反对者

# 1205
## do
* 对获取到的数据进行了分析
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
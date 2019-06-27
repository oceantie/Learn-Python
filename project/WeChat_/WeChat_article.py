from datetime import *
import wechatsogou


# 文章爬取
def get_articles(headline=True, original=True, timedel=1, add_account=None):


   accounts=['36氪','AI前线']
   ws_api = wechatsogou.WechatSogouAPI(captcha_break_time=3)
   articles = []
   for account in accounts:
       articles.extend(reformat(ws_api.get_gzh_article_by_history(account)))

   # 时间过滤，只选取规定天数以内的
   timestamp = int((datetime.now()-timedelta(days=timedel)).timestamp())
   articles = [article for article in articles if article['datetime'] > timestamp]
   print(articles)
   # 头条文章过滤，是否选取头条文章，默认是
   if headline:
       articles = [article for article in articles if article['main'] == 1]

   # 原创文章过滤，是否选取原创文章，默认是
   if original:
       articles = [article for article in articles if article['copyright_stat'] == 100]

   # return articles


# 为保存每篇文章的字典添加一个公众号来源
def reformat(data):
   atcs = data.get('article')
   if atcs is not None:
       wechat_name = data.get('gzh')['wechat_name']
       for article in atcs:
           article['wechat_name'] = wechat_name
       return atcs


get_articles()
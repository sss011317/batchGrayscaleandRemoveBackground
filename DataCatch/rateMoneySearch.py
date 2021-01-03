import requests
import pandas
# res = requests.get('https://rate.bot.com.tw/xrt?Lang=zh-TW')
# print(res)

dfs = pandas.read_html('https://rate.bot.com.tw/xrt?Lang=zh-TW')
currency = dfs[0]
currency = currency.iloc[:,0:5]
currency.columns =[u'幣別',u'現金匯率-本行買入匯率-本行買入',u'現金匯率-本行賣出',u'即期匯率-本行買入',u'即期匯率-本行賣出']
print(currency)

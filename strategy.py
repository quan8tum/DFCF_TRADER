#-*- coding:utf-8 -*-

import requests


STRATEGY_4_DAYS="http://www.iwencai.com/stockpick/load-data"
STRATEGY_URL='http://www.iwencai.com/traceback/strategy/submit'
TRANSACTION_URL='http://www.iwencai.com/traceback/strategy/transaction'
QUERY="非st; 收盘价在5元至30元之间; 总市值小于6000000000; 涨幅0%-6%; 15日区间涨跌幅<6%; 换手率<3.5%; 量比小于1.5; 市盈率(pe)<400;  boll突破中轨; dde大单净额流入; 一阳三线; a股市值(不含限售股)从小到大排列"

class Strategy(object):
    
    def __init__(self):
        self.s = requests.session()
        headers={
                "Host": "www.iwencai.com",
                "Connection": "keep-alive",
                "Accept": "application/json, text/javascript, */*; q=0.01",
                "X-Requested-With": "XMLHttpRequest",
                "User-Agent": "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.87 Safari/537.36",
                "Referer": "http://www.iwencai.com",
                "Accept-Encoding": "gzip, deflate, sdch",
                "Accept-Language": "zh-CN,zh;q=0.8"
                }
        self.s.headers.update(headers)
    def pickstock(self):
        params={
                "typed":"0",
                "preParams":"",
                "ts":"1",
                "f":"1",
                "qs":"result_original",
                "selfsectsn":"",
                "querytype":"",
                "searchfilter":"",
                "tid":"stockpick",
                "w":QUERY,
                "queryarea":"" 
               }
        r=self.s.get(STRATEGY_4_DAYS,params=params)
        #print r.json()["data"]["result"]["result"][0][1]
        print r.json()["data"]["result"]["result"][0][1]



    def traceback(self):
        url="http://www.iwencai.com/traceback/strategy/submit"
        params={
                "query":QUERY,
                "daysForSaleStrategy":"20,30,40,50,60",
                "startDate":"2014-01-01",
                "endDate":"2017-01-11",
                "fell":"0.001",
                "upperIncome":"40",
                "lowerIncome":"20",
                "fallIncome":"10",
                "stockHoldCount":"2"               
               }
        r=self.s.post(url,data=params)
        return r.json()
       
       
    def transaction(self):
        params_2={
                "stime":"2017-01-01",
                "etime":"2027-10-20",
                "hold_for":"4",
                "sort":"desc",
                "title":"bought_at",
                "stockHoldCount":"1",
                "fallIncome":"5",
                "lowerIncome":"8",
                "upperIncome":"20",
                "fell":"0.001",
                "endDate":" ",
                "startDate":" ",
                "daysForSaleStrategy":"4",
                "query":QUERY,
                "newType":"0"
                 }
        r=self.s.post(TRANSACTION_URL,data=params_2)
        print r.json()["data"][0]["stock_name"], \
              r.json()["data"][0]["bought_at"], \
              r.json()["data"][0]["sold_at"]
       
       
if __name__=="__main__":
    #pickstock=Strategy()
    #pickstock.pickstock()
    
    test=Strategy()
    print test.traceback()['data']['stockData']['list']['data'][0]['codeName']
    test.transaction()








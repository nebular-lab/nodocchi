import json
import requests
from bs4 import BeautifulSoup
import urllib.request as req


def lambda_handler(event, context):
    # url="https://stocks.finance.yahoo.co.jp/stocks/detail/?code=usdjpy"
    # res = req.urlopen(url)
    # soup = BeautifulSoup(res, 'html.parser');
    # d1 = soup.select_one("._3BGK5SVf").string #(1)
    # d1=round(float(d1),1)

    # return res
    if event['playerName'] != "":
        result = "取得した値は「" + event['playerName'] + "」です。"
    else:
        result = "値を取得できませんでした。"
    return {
        "result": result
    }

from selenium import webdriver
import automate
import os

# 環境変数HOMEを変更する。
os.environ['HOME'] = '/opt/'

def lambda_handler(event, context):
    name=event['playerName']
    
    selenium=automate.Selenium()
    url='https://nodocchi.moe/tenhoulog/#!&name='+name
    
    selenium.access(url)
    selenium.stop(7)
    
    rule = selenium.driver.find_element_by_id('f_sct__SCType_enabled')
    selenium.stop(1)
    rule.click()
    
    # ルールの設定
    # (span[5]なら鳳凰)
    tokujou = selenium.driver.find_element_by_xpath(
        '//*[@id="div_filter"]/div[2]/form/fieldset/div[3]/span[4]/label')
    selenium.stop(1)
    tokujou.click()
    
    # 四麻ボタン
    yonma = selenium.driver.find_element_by_xpath(
        '//*[@id="div_filter"]/div[2]/form/fieldset/div[2]/span[3]/label')
    selenium.stop(1)
    yonma.click()
    
    # 適用ボタン
    tekiyou = selenium.driver.find_element_by_xpath(
        '//*[@id="div_filter"]/div[2]/form/fieldset/legend/input[2]')
    selenium.stop(1)
    tekiyou.click()
    
    
    #一番下のindexを取得して、100戦分を指定するべき
    #レート
    xpath='//*[@id="tbl_list"]/tbody/tr[position()>1500]/td[6]'
    
    # xpath = '//*[@id="tbl_list"]/tbody/tr[position()>683]/td[5]/span/sub'

    selenium.stop(10)

    elems = selenium.driver.find_elements_by_xpath(xpath)

    scores = []
    for elem in elems:
        scores.append(int(elem.text.replace('R', '')))
    return {
        "result": scores
    }


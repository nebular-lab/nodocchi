from selenium import webdriver
import automate
import os


def lambda_handler(event, context):

    
    name=event['playerName']
    
    selenium=automate.Selenium()
    url='https://nodocchi.moe/tenhoulog/#!&name='+name
    
    selenium.access(url)
    selenium.stop(5)
    
    
    rule = selenium.driver.find_element_by_id('f_sct__SCType_enabled')
    selenium.stop(1)
    rule.click()
    
    # ルールの設定
    # (span[5]なら鳳凰)
    # 特上卓
    tokujou_button = selenium.driver.find_element_by_xpath(
        '//*[@id="div_filter"]/div[2]/form/fieldset/div[3]/span[4]/label')
    selenium.stop(1)
    tokujou_button.click()
    
    # 四麻ボタン
    yonma_button = selenium.driver.find_element_by_xpath(
        '//*[@id="div_filter"]/div[2]/form/fieldset/div[2]/span[3]/label')
    selenium.stop(1)
    yonma_button.click()
    
    # 適用ボタン
    tekiyou_button = selenium.driver.find_element_by_xpath(
        '//*[@id="div_filter"]/div[2]/form/fieldset/legend/input[2]')
    selenium.stop(1)
    tekiyou_button.click()
    
    #試合数の取得
    xpath_num_match='//*[@id="div_stable"]/div/span/span[1]/span[2]/span[2]'
    num_match_elem=selenium.driver.find_element_by_xpath(xpath_num_match)
    num_match=int(num_match_elem.text.replace(' games',''))
    
    #取得するデータ数
    data_num=50
    
    #レーティングポイントの取得
    xpath_rate='//*[@id="tbl_list"]/tbody/tr[position()>'+str(num_match-data_num)+']/td[6]'

    selenium.stop(9)

    rate_elems = selenium.driver.find_elements_by_xpath(xpath_rate)
    rate_data_set = []
    for rate_elem in rate_elems:
        rate_data_set.append(int(rate_elem.text.replace('R', '')))
    return {
        "result": rate_data_set
    }
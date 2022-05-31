from selenium import webdriver
import automate
#import boto3
import os

# 環境変数HOMEを変更する。
# もともとLambda自体、Linuxベースで動いている。 : https://docs.aws.amazon.com/ja_jp/lambda/latest/dg/lambda-runtimes.html
# 故に環境変数の扱いもLinuxを元にしていて、HOMEの環境変数は、「あなたのホームディレクトリのパス」を表す。
# ホームディレクトリとは? : https://wa3.i-3-i.info/word11160.html
# HOMEを/opt/に設定することでlambda_handler関数が実行される前に、/opt/以下のファイルを自動読みこみする。
# /opt/以下に、.fontsを設置することで、ファイルの自動読み込みを行い、文字化け現象を防ぐ。
# LambdaのLayerでアップロードしたコードは自動的に/opt/以下に配置される。
os.environ['HOME'] = '/opt/'

# s3のサービスを利用する。
#s3 = boto3.resource('s3')

# 撮影したいスクリーンショットURLを設定する。
#URL = "https://www.yahoo.co.jp/"

# スクリーンショットを一時的に格納するファイルパス名
# /tmp以下に置く理由として、/tmp以外では、ファイルの読み書きができないため。
#SCREEN_SHOT_PATH_NAME = "/tmp/screen_shot.png"

# Bucketの名前
#BUCKET_NAME = 'imglist'
# S3へ書き出すファイルパス名
#OUTPUT_FILE_NAME = 'screenshot.png'

# Lambdaにおけるメイン関数
# event : 最初の引数は イベントオブジェクト です。イベントは、処理する関数 Lambda のデータを含む JSON 形式のドキュメントです。 Lambda ランタイム は、イベントをオブジェクトに変換し、それを関数コードに渡します。
# context : 2番目の引数は コンテキストオブジェクト です。コンテキストオブジェクトは、ランタイムに Lambda によって関数に渡されます。このオブジェクトは、呼び出し、関数、およびランタイム環境に関する情報を示すメソッドおよびプロパティを提供します。
# https://docs.aws.amazon.com/ja_jp/lambda/latest/dg/python-handler.html


def lambda_handler(event, context):
    # Seleniumに関するInstance生成を行う。
    #selenium = automate.Selenium()

    # スクリーンショットしたいページへアクセス
    #selenium.access(URL)
    # ページ読み込みのために遅延させる。
    #selenium.stop(5)

    # スクリーンショットを実行して、一時的にファイル保存する。
    #selenium.saveScreenshot(SCREEN_SHOT_PATH_NAME)

    # スクリーンショットをS3にアップロードする。
    # s3.meta.client.upload_file(
    #     SCREEN_SHOT_PATH_NAME, BUCKET_NAME, OUTPUT_FILE_NAME)

    # Selenium処理終了
    #selenium.quit()
    
    
    selenium=automate.Selenium()
    url='https://nodocchi.moe/tenhoulog/#!&name=%E3%81%AD%E3%81%B6%E3%81%A4%E3%83%BC'
    
    selenium.access(url)
    selenium.stop(2)
    
    
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
    
    
    xpath = '//*[@id="tbl_list"]/tbody/tr[position()>683]/td[5]/span/sub'
    
    # スクロール
    count = 25
    for i in range(count):
        selenium.driver.execute_script(
            "window.scrollTo("+str(i*3000)+", "+str((i+1)*3000)+")")
        selenium.stop(1)
    elems = selenium.driver.find_elements_by_xpath(xpath)
    
    
    scores = []
    for elem in elems:
        scores.append(elem.text.replace('pt', ''))
    
    
    scores_int = []
    for score in scores:
        scores_int.append(int(score))
    
    selenium.quit()
    
    return scores_int


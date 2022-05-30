import time
from selenium import webdriver
import chromedriver_binary
import matplotlib as mpl
import matplotlib.pyplot as plt

driver = webdriver.Chrome()


driver.get(
    'https://nodocchi.moe/tenhoulog/#!&name=%E3%81%AD%E3%81%B6%E3%81%A4%E3%83%BC')
time.sleep(2)


rule = driver.find_element_by_id('f_sct__SCType_enabled')
time.sleep(1)
rule.click()

# ルールの設定
# (span[5]なら鳳凰)
tokujou = driver.find_element_by_xpath(
    '//*[@id="div_filter"]/div[2]/form/fieldset/div[3]/span[4]/label')
time.sleep(1)
tokujou.click()

# 四麻ボタン
yonma = driver.find_element_by_xpath(
    '//*[@id="div_filter"]/div[2]/form/fieldset/div[2]/span[3]/label')
time.sleep(1)
yonma.click()

# 適用ボタン
tekiyou = driver.find_element_by_xpath(
    '//*[@id="div_filter"]/div[2]/form/fieldset/legend/input[2]')
time.sleep(1)
tekiyou.click()


xpath = '//*[@id="tbl_list"]/tbody/tr[position()>683]/td[5]/span/sub'

# スクロール
count = 25
for i in range(count):
    driver.execute_script(
        "window.scrollTo("+str(i*3000)+", "+str((i+1)*3000)+")")
    time.sleep(1.5)
elems = driver.find_elements_by_xpath(xpath)


scores = []
for elem in elems:
    scores.append(elem.text.replace('pt', ''))


scores_int = []
for score in scores:
    scores_int.append(int(score))

driver.quit()


# グラフの描画
filename = input("Input Filename !\n")

ymin = 0
ymax = 2400

plt.plot(list(range(len(elems))), scores_int)

plt.hlines([ymax/2], 0, len(elems), "red")
plt.hlines([ymax/4], 0, len(elems), "green")
plt.hlines([ymax/4*3], 0, len(elems), "green")
#title=input('Input gragh title \n')
plt.title('Six Level Hill')

plt.xlim(0, len(elems))
plt.ylim(ymin, ymax)

plt.savefig(filename)

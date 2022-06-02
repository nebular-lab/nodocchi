import time
from selenium import webdriver


class Selenium:
    driver = None
    element = None

    def __init__(self):
        options = webdriver.ChromeOptions()
        options.add_argument("--headless")
        options.add_argument("--no-sandbox")
        options.add_argument("--single-process")
        options.add_argument("--disable-gpu")
        options.add_argument("--window-size=1000x100000")
        options.add_argument(
            "--user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.113 Safari/537.36")
        # ログ周り : https://qiita.com/grohiro/items/718239cdd36da42bd517#%E3%83%AD%E3%82%B0%E3%82%92%E5%87%BA%E3%81%99
        options.add_argument("--enable-logging")
        # ログ周り : https://qiita.com/grohiro/items/718239cdd36da42bd517#%E3%83%AD%E3%82%B0%E3%82%92%E5%87%BA%E3%81%99
        options.add_argument("--log-level=0")
        # ssh証明書周りのエラー回避
        options.add_argument("--ignore-certificate-errors")
        # https://daily.belltail.jp/?p=2691
        options.add_argument("--disable-dev-shm-usage")

        options.binary_location = "/opt/headless/python/bin/headless-chromium"

        self.driver = webdriver.Chrome(
            executable_path="/opt/headless/python/bin/chromedriver",
            chrome_options=options
        )

    def access(self, url):
        self.driver.get(url)

    def stop(self, num):
        time.sleep(num)

    def quit(self):
        self.driver.quit()

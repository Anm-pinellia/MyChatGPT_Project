from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from unicodedata import name
import time, json, os
from collections import namedtuple

class BingSearchScript:
    def __init__(self):
        options = Options()
        # options.add_argument('--headless')
        self.driver = webdriver.Chrome(options)
        self.setting = namedtuple('Setting', 'email password')(**json.loads(open(r'./setting.json', 'r').read()))
        self.cookies = self._load_cookies_json()

    def _load_cookies_json(self):
        if os.path.exists('bing_cookies.json'):
            return json.load(open('bing_cookies.json', 'r'))
        else:
            return None

    def _save_cookies_json(self, cookies):
        json.dump(cookies, open('bing_cookies.json', 'w'))
        return cookies

    def _find_element_wait(self, by_type, name):
        # WebDriverWait(self.driver, 10).until(EC.find_element(by_type, name))
        time.sleep(1)
        return self.driver.find_element(by_type, name)

    def _login_account(self):
        url = 'https://cn.bing.com/?homepage'
        self.driver.get(url)
        login_button = self._find_element_wait(By.ID, 'id_s')
        login_button.click()
        email_input_item = self._find_element_wait(By.NAME, 'loginfmt')
        email_input_item.send_keys(self.setting.email)
        sumit_button = self._find_element_wait(By.ID, 'idSIButton9')
        sumit_button.click()
        pwd_input_item = self._find_element_wait(By.NAME, 'passwd')
        pwd_input_item.send_keys(self.setting.password)
        login_button = self._find_element_wait(By.ID, 'idSIButton9')
        login_button.click()
        check_box = self._find_element_wait(By.ID, 'KmsiCheckboxField')
        check_box.click()
        check_button = self._find_element_wait(By.ID, 'idSIButton9')
        check_button.click()
        print('登录成功！')
        self.cookies = self._save_cookies_json(self.driver.get_cookies())

    def _search(self):
        url = 'https://cn.bing.com/search'
        self.driver.get(url)
        for cookie in self.cookies:
            self.driver.add_cookie(cookie)
        self.driver.refresh()
        search_strs = [name(chr(i), '') for i in range(48, 48+30)] * 3
        # inputs_search_item = self._find_element_wait(By.ID, 'sb_form_q')
        # search_button = self._find_element_wait(By.CSS_SELECTOR, '#search_icon > svg')
        # inputs_search_item.click()
        # inputs_search_item.send_keys(search_strs[0])
        # search_button.click()
        for i, search_str in enumerate(search_strs):
            inputs_search_item = self._find_element_wait(By.ID, 'sb_form_q')
            inputs_search_item.click()
            inputs_search_item.send_keys(search_str)
            inputs_search_item.send_keys(Keys.ENTER)
            time.sleep(1)
            print(f'第{i+1}次搜索完成，等待1s:\t{search_str}')
        print('搜索完毕，请查看积分！')


    def run(self):
        if self.cookies is None:
            self._login_account()
        self._search()
        time.sleep(10)
        self.driver.close()

if __name__ == '__main__':
    script = BingSearchScript()
    script.run()
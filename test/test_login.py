# 企业微信登录
"""
    登录问题：二维码登录，验证码
    1 复用已有浏览器 Chrome debug 登录
    2 cookie 免登陆
"""
import json
from time import sleep

import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By


class TestLogin:
    def setup(self):
        # chrome --remote-debugging-port=9222，打开前关闭所有的Google浏览器
        chrome_args = webdriver.ChromeOptions()
        # r 防止\转义
        # chrome_args.binary_location = r"C:\Program Files (x86)\Google\Chrome\Application\chrome.exe"
        chrome_args.debugger_address = "127.0.0.1:9222"
        # self.driver = webdriver.Chrome(options=chrome_args)
        self.driver = webdriver.Chrome()

    def teardown(self):
        self.driver.quit()
        pass

    @pytest.mark.skip
    def test_get_cookie(self):
        cookies = self.driver.get_cookies()
        with open("datafile/cookie.json", 'w') as f:
            json.dump(cookies, f)

    def test_login_cookie(self):
        # 告诉selenium向那个页面添加cookie
        self.driver.get("https://work.weixin.qq.com/")
        # 以文件流的形式打开cookie文件，向目标页面注入cookie
        with open("datafile/cookie.json") as f:
            cookies = json.load(f)
            # print(cookies)
            # 循环读取，一行一行往里加
        for cookie in cookies:
            self.driver.add_cookie(cookie)
        self.driver.get("https://work.weixin.qq.com/wework_admin/frame#index")
        sleep(3)
        self.driver.find_element(By.XPATH, '//*[@id="menu_customer"]/span').click()
        sleep(3)

    @pytest.mark.skip
    def test_login_reuse_browser(self):
        self.driver.get("https://work.weixin.qq.com/")
        sleep(3)
        self.driver.find_element_by_xpath('//*[@class="index_top_operation_loginBtn"]').click()
        sleep(3)
        # 没有定位到元素
        # self.driver.find_element_by_xpath('//*[@class="frame_nav_item_title"]').click()
        self.driver.find_element(By.XPATH, '//*[@id="menu_customer"]/span').click()

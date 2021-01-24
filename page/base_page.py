import json

from selenium import webdriver
from selenium.webdriver.remote.webdriver import WebDriver


class BasePage:
    def __init__(self, base_driver: WebDriver = None):
        if base_driver is None:
            self.driver = webdriver.Chrome()
            """
            driver为空的时候进行登录操作，登录的方法里会登录到首页
            如果driver不为空的时候说明已经登录了，在其他page进行实例化的时候又进行登录操作会跳转到首页，导致找不到元素报错
            """
            self._login_cookie()
        else:
            self.driver = base_driver
        self.driver.implicitly_wait(20)

    def _login_cookie(self):
        # 告诉selenium向哪个页面添加cookie
        self.driver.get("https://work.weixin.qq.com/")
        # 以文件流的形式打开cookie文件，向目标页面注入cookie
        with open("../test/datafile/cookie.json") as f:
            cookies = json.load(f)
        # print(cookies)
        # 循环读取，一行一行往里加（可能是因为格式化后不是一行了）
        for cookie in cookies:
            self.driver.add_cookie(cookie)
        self.driver.get("https://work.weixin.qq.com/wework_admin/frame#index")

    def find(self, by, value):
        return self.driver.find_element(by=by, value=value)

    def finds(self, by, value):
        return self.driver.find_elements(by=by, value=value)



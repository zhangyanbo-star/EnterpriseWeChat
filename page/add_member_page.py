from time import sleep
from typing import List

from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement

from page.base_page import BasePage
from page.contact_page import ContactPage


class AddMemberPage(BasePage):

    def add_member(self, username, acctid, phone):
        self.find(By.ID, 'username').send_keys(username)
        self.find(By.ID, 'memberAdd_acctid').send_keys(acctid)
        self.find(By.ID, 'memberAdd_phone').send_keys(phone)
        self.find(By.CSS_SELECTOR, '.js_btn_save').click()
        sleep(3)
        return ContactPage(self.driver)

    def add_member_fail(self, username, acctid, phone):
        self.find(By.ID, 'username').send_keys(username)
        self.find(By.ID, 'memberAdd_acctid').send_keys(acctid)
        self.find(By.ID, 'memberAdd_phone').send_keys(phone)
        self.find(By.CSS_SELECTOR, '.js_btn_save').click()
        return self
        # self.find(By.CSS_SELECTOR, '.js_btn_cancel').click()
        # sleep(3)
        # return ContactPage(self.driver)

    def get_input_with_tips(self):
        total_tips: List[WebElement] = self.finds(By.CSS_SELECTOR, ".ww_inputWithTips_tips")
        input_tips = []
        for tip in total_tips:
            if tip.text != "":
                input_tips.append(tip.text)
        print(input_tips)
        return len(input_tips)

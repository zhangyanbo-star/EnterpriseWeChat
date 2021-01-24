from selenium.webdriver.common.by import By

from page.add_member_page import AddMemberPage
from page.base_page import BasePage
from page.contact_page import ContactPage


class MainPage(BasePage):

    def goto_contact(self):
        self.driver.find_element(By.XPATH, '//*[@id="menu_contacts"]/span').click()
        return ContactPage(self.driver)

    def goto_add_member(self):
        self.driver.find_element(By.XPATH, '//*[@id="_hmt_click"]/div[1]/div[4]/div[2]/a[1]/div/span[2]').click()
        return AddMemberPage(self.driver)

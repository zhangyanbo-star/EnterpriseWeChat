from time import sleep

from selenium.webdriver.common.by import By

from page.base_page import BasePage


class ContactPage(BasePage):

    def goto_add_member(self):
        pass

    def add_department(self, partyname):
        self.find(By.CSS_SELECTOR, '.member_colLeft_top_addBtn').click()
        self.find(By.CSS_SELECTOR, '.js_create_party').click()
        self.find(By.CSS_SELECTOR, '[name=name]').send_keys(partyname)
        sleep(3)
        self.find(By.CSS_SELECTOR, '.js_toggle_party_list').click()
        sleep(3)
        # 选择最下面的一个下拉列表选项
        # self.driver.find_element(By.XPATH, '//*[@id="__dialog__MNDialog__"]/div/div[2]/div/form/div[3]/div').click()
        # 组合定位要用 CSS_SELECTOR，不能用 XPATH
        self.find(By.CSS_SELECTOR, '.member_tag_dialog [id="1688853347080537_anchor"]').click()
        sleep(3)
        self.find(By.XPATH, '//*[@id="__dialog__MNDialog__"]/div/div[3]/a[1]').click()
        return self

    def get_member_list(self):
        """
        返回通讯录页面的成员信息
        :return:
        """
        name_webelement_list = self.driver.find_elements(By.CSS_SELECTOR,
                                                         '.member_colRight_memberTable_td:nth-child(2)')
        name_list = []
        for webelement in name_webelement_list:
            name_list.append(webelement.text)
        return name_list

    def get_department_list(self):
        department_webelement_list = self.driver.find_elements(By.CSS_SELECTOR, '.jstree-anchor')
        department_list = []
        for webelement in department_webelement_list:
            department_list.append(webelement.text)
        return department_list

    def get_tips(self):
        tips = self.find(By.ID, "js_tips").text
        return tips

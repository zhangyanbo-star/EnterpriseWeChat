from typing import List

import pytest

from page.base_page import BasePage
from page.main_page import MainPage

"""
用例描述的是业务场景，不是描述具体的行为操作
"""


class TestAddMember:

    def setup(self):
        self.main = MainPage()

    def test_add_member(self):
        result = self.main.goto_add_member().add_member('Usopu', 'usopu@163.com', '15900000004').get_tips()
        assert "保存成功" == result

    def test_add_member_fail(self):
        """
        不能用username是否在列表里断言，username是可以重复的
        :return:
        """
        result = self.main.goto_add_member().add_member_fail('Nami', 'nami@163.com', '15900000003').get_input_with_tips()
        print(result)
        assert result > 0

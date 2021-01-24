from page.main_page import MainPage


class TestAddDepartment:
    def setup(self):
        self.main = MainPage()

    def test_add_department(self):
        result = self.main.goto_contact().add_department("第三开发部").get_tips()
        assert "新建部门成功" == result

import pytest

from app_wx.page.app import App


class TestAdd:
    def setup(self):
        self.app = App()
        self.main = self.app.start().goto_main()

    def teardown(self):
        self.app.stop()

    @pytest.mark.parametrize('name, gender, phone',
                             [('kaisaly', '男', '13400000097'), ('小明', '男', '13400000091'),
                              ('小华', '女', '13400000092')])
    def test_add_success(self, name, gender, phone):
        result = self.main.goto_address()\
            .add_men().add_by_menual()\
            .add_contact(name, gender, phone).get_toast()
        assert result == '添加成功'



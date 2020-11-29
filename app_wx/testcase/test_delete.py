import pytest

from app_wx.page.app import App


class TestDelete:

    def setup(self):
        self.app = App()
        self.main = self.app.start().goto_main()

    def teardown(self):
        self.app.stop()

    @pytest.mark.parametrize('name', ['marly'])
    def test_delete_success(self, name):
        result = self.main.goto_address()\
            .goto_search().search(name).goto_setting()\
            .goto_edit().delete_men().search_result(name)
        assert result is None

    @pytest.mark.parametrize('name', ['marlyly'])
    def test_delete_cancel(self, name):
        result = self.main.goto_address().goto_search()\
            .search(name).goto_setting().goto_edit().delete_cancel()
        assert result is None


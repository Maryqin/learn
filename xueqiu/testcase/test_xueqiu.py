from xueqiu.page.app import App


class TestXueqiu:

    def setup(self):
        self.app = App()
        self.main = self.app.start().goto_main()

    def teardown(self):
        self.app.stop()

    def test_stock(self):
        self.main.goto_stock().goto_stockdetail().detail_k()



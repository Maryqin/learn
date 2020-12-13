from xueqiu.page.base_page import BasePage
from xueqiu.page.stockdetailpage import StockDetail


class StockModule(BasePage):
    def goto_stockdetail(self):
        self.parse_yaml(r'D:\MyProject\xueqiu\data\stockdetail.yaml', 'goto_stockdetail')
        return StockDetail(self.driver)

from appium.webdriver.common.mobileby import MobileBy

from xueqiu.page.base_page import BasePage
from xueqiu.page.stockmodulepage import StockModule


class MainPage(BasePage):

    def goto_stock(self):
        self.parse_yaml(r'D:\MyProject\xueqiu\data\mainpage.yaml', 'goto_stock')
        return StockModule(self.driver)



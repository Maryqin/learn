from appium.webdriver.common.mobileby import MobileBy

from xueqiu.page.base_page import BasePage
from xueqiu.page.snowballwebviewpage import SnowballWebView


class StockDetail(BasePage):
    def detail_fs(self):
        self.parse_yaml(r'D:\MyProject\xueqiu\data\stockdetail.yaml', 'detail_rs')
        return SnowballWebView(self.driver)

    def detail_k(self):
        self.parse_yaml(r'D:\MyProject\xueqiu\data\stockdetailpage.yaml', 'detail_k')
        locator = (MobileBy.XPATH, '//*[contains(@text,"均")]')
        return self.wait(10, locator)


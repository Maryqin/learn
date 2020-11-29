from appium.webdriver.common.mobileby import MobileBy

from app_wx.page.base_page import BasePage
from app_wx.page.menberlist_page import Memberlist


class WwMainpage(BasePage):
    def goto_messege(self):
        pass

    def goto_address(self):
        self.find_click(MobileBy.XPATH, '//*[@text="通讯录"]')
        return Memberlist(self.driver)

    def goto_work(self):
        pass

    def goto_me(self):
        pass

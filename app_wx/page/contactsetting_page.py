from appium.webdriver.common.mobileby import MobileBy

from app_wx.page.base_page import BasePage
from app_wx.page.contactedit_page import ContactEdit


class ContactSetting(BasePage):

    def goto_edit(self):
        self.find_click(MobileBy.XPATH, '//*[@text="编辑成员"]')
        return ContactEdit(self.driver)

from appium.webdriver.common.mobileby import MobileBy

from app_wx.page.base_page import BasePage
from app_wx.page.contactsetting_page import ContactSetting


class ContactDetail(BasePage):

    def goto_setting(self):
        self.find_click(MobileBy.XPATH, '//*[@text="个人信息"]/../../../../..//android.widget.RelativeLayout')
        return ContactSetting(self.driver)

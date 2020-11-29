from appium.webdriver.common.mobileby import MobileBy
from selenium.webdriver.support.wait import WebDriverWait

from app_wx.page.base_page import BasePage


class ContactAdd(BasePage):

    def add_contact(self, name, gender, phone):
        self.find_send_keys(MobileBy.XPATH, '//*[contains(@text,"姓名")]/../..//android.widget.EditText', name)
        self.find_click(MobileBy.XPATH, '//*[contains(@text,"性别")]/..//android.widget.RelativeLayout/android.widget.LinearLayout')
        locator = (MobileBy.XPATH, '//*[@text="女"]')
        self.wait(10, locator)
        if gender == '男':
            self.find_click(MobileBy.XPATH, '//*[@text="男"]')
        else:
            self.find_click(MobileBy.XPATH, '//*[@text="女"]')

        self.find_send_keys(MobileBy.XPATH, '//*[contains(@text,"手机") and @clickable="true"]', phone)

        self.find_click(MobileBy.XPATH, '//*[@text="保存"]')

        from app_wx.page.invitemenu_page import MemberInviteMenu
        return MemberInviteMenu(self.driver)

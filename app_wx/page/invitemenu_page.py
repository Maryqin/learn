from appium.webdriver.common.mobileby import MobileBy

from app_wx.page.base_page import BasePage
# from app_wx.page.contactmen_page import ContactAdd


class MemberInviteMenu(BasePage):

    def add_by_weixim(self):
        pass

    def add_by_book(self):
        pass

    def add_by_menual(self):
        self.find(MobileBy.XPATH, '//*[@text="手动输入添加"]').click()
        from app_wx.page.contactmen_page import ContactAdd
        return ContactAdd(self.driver)

    def get_toast(self):
        result = self.find_toast_text()
        return result

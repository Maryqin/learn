from appium.webdriver.common.mobileby import MobileBy

from app_wx.page.base_page import BasePage
from app_wx.page.invitemenu_page import MemberInviteMenu
from app_wx.page.mensearch_page import DepartmentSearch


class Memberlist(BasePage):

    def add_men(self):
        self.find_scroll("添加成员")
        return MemberInviteMenu(self.driver)

    def goto_search(self):
        self.find_click(MobileBy.ID, 'com.tencent.wework:id/i6n')
        return DepartmentSearch(self.driver)






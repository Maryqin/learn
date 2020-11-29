from appium.webdriver.common.mobileby import MobileBy

from app_wx.page.base_page import BasePage


class ContactEdit(BasePage):

    def delete_men(self):
        # 滚动找到删除成员且点击
        self.find_scroll('删除成员')
        # 点击确定删除
        self.find_click(MobileBy.XPATH, '//*[@text="确定"]')

        from app_wx.page.mensearch_page import DepartmentSearch
        return DepartmentSearch(self.driver)

    def delete_cancel(self):
        self.find_scroll('删除成员')
        self.find_click(MobileBy.XPATH, '//*[@text="取消"]')
        return self.wait_source(10, '删除成员')


from appium.webdriver.common.mobileby import MobileBy

from app_wx.page.base_page import BasePage
from app_wx.page.contacdetail_page import ContactDetail


class DepartmentSearch(BasePage):

    def search(self, text):
        # 输入数据查询
        self.find_send_keys(MobileBy.XPATH, f'//*[@text="搜索"]', f'{text}')
        # 查询且点击
        self.find_click(MobileBy.XPATH, f'//*[@text="{text}" and @clickable="false"]')
        return ContactDetail(self.driver)

    # 查找不但元素
    def search_result(self, text):
        locator = (MobileBy.XPATH, f'//*[@text="{text}" and @clickable="false"]')
        return self.wait_not(10, locator)


from appium import webdriver
from appium.webdriver.common.mobileby import MobileBy
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class TestDaka:

    def setup(self):
        desire_caps = {}
        desire_caps['platformName'] = 'android'
        desire_caps['platformVersion'] = '6.0'
        # genymotion模拟器
        desire_caps['deviceName'] = '127.0.0.1:5555'
        desire_caps['appPackage'] = 'com.tencent.wework'
        desire_caps['appActivity'] = '.launch.LaunchSplashActivity'
        desire_caps['noReset'] = 'true'
        # 设置idle的时间
        # desire_caps['settings[waitForIdleTimeout]'] = 0
        desire_caps['unicodeheyBoard'] = 'true'
        desire_caps['reseKeyBoard'] = 'true'
        # 指定chromedriver的地址
        desire_caps['chromedriverExecutable'] = r'D:\Downloads\chromedriver\74.0.3729\chromedriver.exe'
        self.driver = webdriver.Remote('http://localhost:4723/wd/hub', desire_caps)
        self.driver.implicitly_wait(10)

    def teardown(self):
        self.driver.back()
        self.driver.back()
        self.driver.quit()

    def test_daka(self):
        self.driver.find_element(MobileBy.XPATH, '//*[@text="工作台"]').click()
        # 滚动查找打卡
        self.driver.find_element_by_android_uiautomator('new UiScrollable(new UiSelector().'
                                                        'scrollable(true).instance(0)).'
                                                        'scrollIntoView(new UiSelector().text("打卡").'
                                                        'instance(0));').click()
        # 设置idle的时间
        self.driver.update_settings({"waitForIdleTimeout": 0})
        locator = (MobileBy.ID, 'com.tencent.wework:id/auw')
        WebDriverWait(self.driver, 10).until(expected_conditions.element_to_be_clickable(locator))
        self.driver.find_element(*locator).click()
        # assert "正常" in self.driver.page_source
        WebDriverWait(self.driver, 10).until(lambda x: "正常" in x.page_source)

import allure
import pytest

# 整个模块的说明


@allure.feature('登入模块')
class TestLogin:
    # 标记级别
    @allure.severity(allure.severity_level.TRIVIAL)
    # 添加对测试方法的说明
    @allure.story('登入成功')
    @allure.title('登入测试')
    def test_login_success(self):
        # 添加测试步骤的说明
        with allure.step('步骤1：打开应用'):
            print('打开应用')
        with allure.step('步骤2：进入登入页面'):
            print('进入登入页面')
        with allure.step('步骤3：输入用户名和密码'):
            print('输入用户名和密码')
        print('这是登入：测试用例，登入成功！')
        pass

    @allure.story('登入失败')
    def test_login_failure(self):
        print('这是登入：测试用例，登入失败！')

    def test_login_failure_a(self):
        print('用户名缺失')
        pass

    @allure.story('密码缺失')
    def test_login_failure_b(self):
        with allure.step('点击用户名'):
            print('输入密码')
        with allure.step('点击密码'):
            print('输入密码')
        with allure.step('点击登入之后登入失败'):
            assert '1' == 1
            print('登入失败')

    def test_login_failure_c(self):
        print('这是登录：测试用例，登入失败')
        pass


if __name__ == '__main__':
    pytest.main()

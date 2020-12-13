import allure


def handle_black(func):
    def wrapper(*args, **kwargs):
        from xueqiu.page.base_page import BasePage
        try:
            instance: BasePage = args[0]
            result = func(*args, **kwargs)
            instance.error_num = 0
            return result
        except Exception as e:
            # 截图
            instance.driver.save_screenshot('tmp.png')
            # 上传截图到allure报告
            with open(r'D:\MyProject\xueqiu\testcase\tmp.png', 'rb') as f:
                content = f.read()
            allure.attach(content, attachment_type=allure.attachment_type.PNG)

            if instance.error_num > instance.max_num:
                raise e
            instance.error_num = instance.error_num + 1
            for black in instance.black_list:
                element = instance.driver.find_elements(*black)
                if len(element) > 0:
                    element[0].click()
                return wrapper(*args, **kwargs)
        raise e
    return wrapper

from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from Utils.Driver import DriverUtils


class BaseAction:

    def __init__(self):
        self.driver = DriverUtils.get_mis_driver()

    # 获取元素方法
    def get_element(self, feature):
        '''
        功能：调用当前方法，传入一个feature 元素的元素信息，返回目标元素或 None
        ：param feature ：元祖类型， 表示当前目标元素特征   By.ID   'ID值'
        ：return obj 如果元素存在obj未element，如果元素不存在，返回None
        '''
        wait = WebDriverWait(self.driver, 5, 1)
        try:
            obj = wait.until(lambda x: x.find_element(*feature))  # 使用显示等待配合find_element进行捕获
        except Exception:
            # 如果捕获到异常，则返回 None
            return None
        else:
            # 如果没有捕获到异常返回 obj
            return obj

    # 执行输入框输入操作
    def execute_input(self, obj, val):
        '''
        核心功能: 在obj输入框内写入val
        return: None
        '''
        obj.clear()
        obj.send_keys(val)

    # 执行元素点击操作
    def execute_click(self, obj):
        obj.click()

    # 获取多个元素方法
    def get_elements(self, feature):
        '''
        功能：调用当前方法，传入一个feature 元素的元素信息，返回目标元素或 None
        ：param feature ：元祖类型， 表示当前目标元素特征   By.ID   'ID值'
        ：return obj 如果元素存在obj未element，如果元素不存在，返回None
        '''
        wait = WebDriverWait(self.driver, 5, 1)
        try:
            obj = wait.until(lambda x: x.find_elements(*feature))  # 使用显示等待配合find_element进行捕获
        except Exception:
            # 如果捕获到异常，则返回 None
            return None
        else:
            # 如果没有捕获到异常返回 obj
            return obj

    # 工具方法 获取下拉菜单指定某个选项
    def get_select_channel(self, box_name, scroll_name, targer_name):

        # 定义一个变量用例存放元素
        targer_itme = None
        flag = False  # 人为定义一个开关,默认值是 False 表示目标元素不存在

        # 1 点击最外层下拉菜单
        channel_box_fea = box_name
        self.execute_click(self.get_element(channel_box_fea))

        # 2 获取下拉菜单中的所有下拉选项
        items_fea = scroll_name
        items_list = self.get_elements(items_fea)

        print(len(items_list))  # 调试函数

        # 3 从当前的下拉选项中找出目标 channel
        for itme in items_list:
            # print(itme, '---->', itme.text)
            if itme.text == '{}'.format(targer_name):
                # 找到目标元素,则返回
                targer_itme = itme
                flag = True  # 找到目标元素后将开关置位 True
                break
            else:
                # 如果没有找到,就需要不停的往下切
                ActionChains(self.driver).move_to_element(itme).send_keys(Keys.DOWN).perform()

        # 4 如果目标选项不存在下拉选项中,则返回 None
        if not flag:
            return None

        # 循环完成之后返回 targer_itme
        return targer_itme

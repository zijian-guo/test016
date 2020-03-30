# 将来可能把多个web系统+app+后台管理系统置于一个自动化框架
# 所以就会需要多个driver,因为我们选择一个类来管理不同的driver 获取
from selenium import webdriver


class DriverUtils:
    # 定义driver
    _pm_driver = None
    _mis_driver = None
    _app_driver = None

    # 获取自媒体driver
    @classmethod
    def get_pm_driver(cls):
        if cls._pm_driver is None:
            cls._pm_driver = webdriver.Chrome()
            cls._pm_driver.get('http://ttmp.research.itcast.cn/')
            cls._pm_driver.maximize_window()
        return cls._pm_driver

    @classmethod
    def close_pm_driver(cls):
        if cls._pm_driver is not None:
            cls._pm_driver.quit()
            cls._pm_driver = None

    # 获取后端管理系统 driver
    @classmethod
    def get_mis_driver(cls):
        if cls._mis_driver is None:
            cls._mis_driver = webdriver.Chrome()
            cls._mis_driver.get("http://ttmis.research.itcast.cn/")
            cls._mis_driver.maximize_window()
        return cls._mis_driver

    @classmethod
    def cloes_mis_driver(cls):
        if cls._mis_driver is not None:
            cls._mis_driver.quit()
            cls._mis_driver = None

from selenium.webdriver.common.by import By
import Base

class PageIndex(Base.BaseAction):

    infor_man_fea = By.XPATH, "//a[contains(text(),'信息管理')]"
    content_check_fea = By.XPATH, "//a[contains(text(),'内容审核')]"

    def get_infor_man_fea(self):
        return self.get_element(self.infor_man_fea)

    def get_content_check_fea(self):
        return self.get_element(self.content_check_fea)

from selenium.webdriver.common.by import By
import Base

class PageLogin(Base.BaseAction):

    user_fea = By.NAME, "username"
    pwd_fea = By.NAME, "password"
    btn_fea = By.ID, "inp1"
    logo_fea = By.CSS_SELECTOR, '.logo'

    def get_user_fea(self):
        return self.get_element(self.user_fea)

    def get_pwd_fea(self):
        return self.get_element(self.pwd_fea)

    def get_btn_fea(self):
        return self.get_element(self.btn_fea)

    def get_logo_fea(self):
        return self.get_element(self.logo_fea)



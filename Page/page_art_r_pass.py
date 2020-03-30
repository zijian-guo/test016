from selenium.webdriver.common.by import By
import Base

class PageleArticleReviewPass(Base.BaseAction):

    title_box_fea = By.XPATH, '//input[contains(@placeholder," 文章名称")]'
    status_bbox_fea = By.XPATH, '//input[contains(@placeholder,"请选择状态")]'
    select_fea = By.XPATH, "//li//span[text()='待审核']"
    query_fea = By.CSS_SELECTOR, ".find"
    pass_click__fea = By.XPATH, "//button//span[text()='通过']"
    sure_fea = By.XPATH, "//button//span[contains(text(),'确定')]"
    success_fea = By.XPATH, "//p[text()='修改成功']"

    def get_title_box_fea(self):
        return self.get_element(self.title_box_fea)

    def get_status_bbox_fea(self):
        return self.get_element(self.status_bbox_fea)

    def get_select_fea(self):
        return self.get_element(self.select_fea)

    def get_query_fea(self):
        return self.get_element(self.query_fea)

    def get_pass_click__fea(self):
        return self.get_element(self.pass_click__fea)

    def get_sure_fea(self):
        return self.get_element(self.sure_fea)

    def get_success_fea(self):
        return self.get_element(self.success_fea)


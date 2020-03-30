import Page

class HandleIndex(Page.PageIndex):

    def click_infor_man_fea(self):
        self.execute_click(self.get_infor_man_fea())

    def clcik_content_check_fea(self):
        self.execute_click(self.get_content_check_fea())
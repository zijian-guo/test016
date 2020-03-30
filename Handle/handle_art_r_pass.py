import Page


class HandleleArticleReviewPass(Page.PageleArticleReviewPass):

    def input_title_box_fea(self):
        self.execute_input(self.get_title_box_fea(), "2222")

    # def click_select_fea(self):
        # self.get_select_channel(self.status_bbox_fea, self.select_fea, '待审核')

    def click_status_bbox_fea(self):
        self.execute_click(self.get_status_bbox_fea())

    def click_select_fea(self):
        self.execute_click((self.get_select_fea()))

    def click_get_query_fea(self):
        self.execute_click(self.get_query_fea())

    def click_pass_click__fea(self):
        self.execute_click(self.get_pass_click__fea())

    def click_sure_fea(self):
        self.execute_click(self.get_sure_fea())

    def assert_success(self):
        msg = self.get_success_fea()
        assert True if msg else False

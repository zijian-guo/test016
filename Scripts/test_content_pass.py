import time

import Handle


class TestLogin:

    def setup(self):
        self.handle = Handle.HandleTotal()

    def teardown(self):
        pass

    def test_login(self):
        # [数据]

        # [业务: 账号 密码 登录]
        self.handle.init_login.input_user()
        self.handle.init_login.input_pwd()
        self.handle.init_login.click_login()
        self.handle.init_index.click_infor_man_fea()
        time.sleep(1)
        self.handle.init_index.clcik_content_check_fea()
        # time.sleep(1)
        # self.handle.init_art_r_pass.input_title_box_fea()
        time.sleep(1)
        self.handle.init_art_r_pass.click_status_bbox_fea()
        time.sleep(1)
        self.handle.init_art_r_pass.click_select_fea()
        time.sleep(1)
        self.handle.init_art_r_pass.click_get_query_fea()
        time.sleep(3)
        self.handle.init_art_r_pass.click_pass_click__fea()
        time.sleep(1)
        self.handle.init_art_r_pass.click_sure_fea()
        # [断言]
        # time.sleep(1)
        # self.handle.init_art_r_pass.assert_success()

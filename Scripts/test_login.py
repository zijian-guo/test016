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

        # [断言]
        self.handle.init_login.assert_logo()




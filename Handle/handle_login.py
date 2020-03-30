import Page


class HandleLogin(Page.PageLogin):

    def input_user(self):
        self.execute_input(self.get_user_fea(), 'testid')

    def input_pwd(self):
        self.execute_input(self.get_pwd_fea(), "testpwd123")

    def click_login(self):
        # 默认情况下当前元素具有一个 disabled 属性, 此时是不允许被点击
        # 因为我们需要在自动化测试脚本中想办法去除它身上的 disabled

        # JS
        # document 网页全部选中
        # 1 在做 wen ui 自动化测试的时候,一般看到的都是前端界面
        # 2 这些前端界面的本事就是一个个 html 文件 (标签 + 样式)
        # 3 这些 HTML 文件将来可能会用过 JS 来进行交互操作
        # 4 JS 和 HTML 分别是两种不同的语言,如果想让JS是控制或者操作HTML,
        # 那么在JS中必要有一个东西跟 HTML 做对应
        # 5 此时在 JS 中定义了一个叫 document 关键之来表示整个 HTML 页面

        # 1 将需要执行的 JS 代码定义
        js_code = "document.getElementById('inp1').removeAttribute('disabled')"

        # 2 使用 webdriver 当中的 API 来执行 JS 代码
        self.driver.execute_script(js_code)

        self.execute_click(self.get_btn_fea())

    def assert_logo(self):
        msg = self.get_logo_fea()
        assert (True if msg else False)




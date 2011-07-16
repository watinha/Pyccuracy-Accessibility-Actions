from pyccuracy.page import Page

class GooglePage(Page):
    url = 'http://www.google.com.br'

    def register(self):
        self.quick_register("google search input", "#lst-ib")
        self.quick_register("google submit button", "span.lsbb > input.lsb")

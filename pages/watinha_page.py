from pyccuracy.page import Page

class WatinhaPage(Page):
    url = 'http://watinha.com' 

    def register(self):
        self.quick_register("introduction link", "#introduction11")
        self.quick_register("body", "body")

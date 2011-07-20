from pyccuracy.actions import ActionBase

from accessibility_actions import JsCodeLoader

class FillFocusedElementAction(ActionBase):
    __builtin__ = True
    regex = r'^(And )?I type [\"](?P<text>.+)[\"]$'

    def execute(self, context, text):
        js_loader = JsCodeLoader()
        js_code = js_loader.load('get_active_element_xpath.js')
        active_element_xpath = context.browser_driver.exec_js(js_code)
        context.browser_driver.type_text(active_element_xpath, text)


class PressEnterAction(ActionBase):
    __builtin__ = True
    regex = r'^(And )?I press enter$'

    def execute(self, context, extra_argument):
        js_loader = JsCodeLoader()
        js_code = js_loader.load('get_active_element_xpath.js')
        active_element_xpath = context.browser_driver.exec_js(js_code)
        context.browser_driver.type_keys(active_element_xpath, '\13')

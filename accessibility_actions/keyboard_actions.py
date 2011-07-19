from pyccuracy.actions import ActionBase

from accessibility_actions import JsCodeLoader

class FillFocusedElementAction(ActionBase):
    __builtin__ = True
    regex = r'^(And )?I type [\"](?P<text>.+)[\"]$'

    def execute(self, context, text):
        js_loader = JsCodeLoader()
        active_element_xpath = js_loader.load('get_active_element_xpath.js')
        context.browser_driver.type_text(active_element_xpath, text)


class PressEnterAction(ActionBase):
    __builtin__ = True
    regex = r'^(And )?I press enter$'

    def execute(self, context, text):
        raise self.failed('no press enter yet...')

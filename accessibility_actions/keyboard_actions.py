from pyccuracy.actions import ActionBase

from accessibility_actions import JsCodeLoader

class FillFocusedElementAction(ActionBase):
    __builtin__ = True
    regex = r'^(And )?I type [\"](?P<text>.+)[\"]$'

    def execute(self, context, text):
        js_loader = JsCodeLoader()

        active_element_dom = js_loader.exec_js(context, 'get_active_element_dom.js')
        context.browser_driver.type_text(active_element_dom, text)
        active_element_value = js_loader.exec_js(context, 'verify_active_element_value.js')

        if (active_element_value != text):
            raise self.failed('Focused element does not support keyboard input')


class PressEnterAction(ActionBase):
    __builtin__ = True
    regex = r'^(And )?I press enter$'

    def execute(self, context, extra_argument):
        js_loader = JsCodeLoader()
        active_element_dom = js_loader.exec_js(context, 'get_active_element_dom.js')
        context.browser_driver.type_keys(active_element_dom, '\13')

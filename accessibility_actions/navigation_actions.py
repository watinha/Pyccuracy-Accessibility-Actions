from pyccuracy.actions import ActionBase
from accessibility_actions import JsCodeLoader

class TabNavigationAction(ActionBase):
    __builtin__ = True
    regex = r'^(And )?I tab navigate to [\"](?P<element_text>[^"]+)[\"] (?P<element_type><element selector>)$'
    NOT_FOUND_ELEMENT = 'element not found'
    MAX_TAB_PRESSES_EXCEEDED = 'exceed max number of tab keys pressed'

    def execute(self, context, element_type, element_text):
        js_loader = JsCodeLoader()
        js_code = js_loader.load('tab_navigation.js', element_text)

        result = context.browser_driver.exec_js(js_code)
        if (result == self.NOT_FOUND_ELEMENT):
            raise self.failed('"' + element_text + '" does not exists or is not focusable...')
        if (result == self.MAX_TAB_PRESSES_EXCEEDED):
            raise self.failed('"' + element_text + '" max number of tab key presses was exceeded...')


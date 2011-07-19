from pyccuracy.actions import ActionBase
from accessibility_actions import JsCodeLoader

class TabNavigationAction(ActionBase):
    __builtin__ = True
    regex = r'^(And )?I tab navigate to [\"](?P<element_text>[^"]+)[\"] (?P<element_type><element selector>)( with (?P<tab_number>\d+) key presses)?$'
    NOT_FOUND_ELEMENT = 'element not found'
    MAX_TAB_PRESSES_EXCEEDED = 'exceed max number of tab keys pressed'
    MAX_NUMBER_OF_TAB_KEYS = '30'

    def execute(self, context, element_type, element_text, tab_number):
        js_loader = JsCodeLoader()
        if (tab_number):
            js_code = js_loader.load('tab_navigation.js', element_text, tab_number)
        else:
            js_code = js_loader.load('tab_navigation.js', element_text, self.MAX_NUMBER_OF_TAB_KEYS)

        result = context.browser_driver.exec_js(js_code)
        if (result == self.NOT_FOUND_ELEMENT):
            raise self.failed('"' + element_text + '" does not exists or is not focusable...')
        if (result == self.MAX_TAB_PRESSES_EXCEEDED):
            raise self.failed('"' + element_text + '" max number of tab key presses was exceeded...')


from pyccuracy.actions import ActionBase

class TabNavigationAction(ActionBase):
    __builtin__ = True
    regex = r'^(And )?I tab navigate to [\"](?P<element_text>[^"]+)[\"] (?P<element_type><element selector>)$'

    def execute(self, context, element_type, element_text):
        raise self.failed('no tab navigation yet...')

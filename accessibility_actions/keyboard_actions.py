from pyccuracy.actions import ActionBase

class FillFocusedElementAction(ActionBase):
    __builtin__ = True
    regex = r'^(And )?I type [\"](?P<text>.+)[\"]$'

    def execute(self, context, text):
        raise self.failed('no type text yet...')


class PressEnterAction(ActionBase):
    __builtin__ = True
    regex = r'^(And )?I press enter$'

    def execute(self, context, text):
        raise self.failed('no press enter yet...')

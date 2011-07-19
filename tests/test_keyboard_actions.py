import unittest
from mock import Mock, patch

from pyccuracy.errors import ActionFailedError
from accessibility_actions.keyboard_actions import FillFocusedElementAction
from accessibility_actions import JsCodeLoader

class FillFocusedElementActionTest(unittest.TestCase):

    def test_fill_element_should_call_js_loader_and_type_action_in_browser_driver(self):
        context_mock = Mock()
        with patch.object(JsCodeLoader, 'load') as load_mock:
            load_mock.return_value = '//input[2]'
            fill_action = FillFocusedElementAction()
            fill_action.execute(context_mock, "watinha")

        self.assertTrue(load_mock.called)
        load_mock.assert_called_with('get_active_element_xpath.js')
        self.assertTrue(context_mock.browser_driver.type_text.called)
        context_mock.browser_driver.type_text.assert_called_with("//input[2]", "watinha")


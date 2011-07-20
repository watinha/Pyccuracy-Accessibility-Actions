import unittest
from mock import Mock, patch

from pyccuracy.errors import ActionFailedError
from accessibility_actions.keyboard_actions import FillFocusedElementAction, PressEnterAction
from accessibility_actions import JsCodeLoader

class FillFocusedElementActionTest(unittest.TestCase):

    def test_fill_element_should_call_js_loader_and_type_action_in_browser_driver(self):
        context_mock = Mock()
        js_code_dummy = 'function testing(){console.log(12);};result = testing();'

        context_mock.browser_driver.exec_js.return_value = '//input[2]'

        with patch.object(JsCodeLoader, 'load') as load_mock:
            load_mock.return_value = js_code_dummy
            fill_action = FillFocusedElementAction()
            fill_action.execute(context_mock, 'watinha')

        self.assertTrue(load_mock.called)
        load_mock.assert_called_with('get_active_element_xpath.js')
        self.assertTrue(context_mock.browser_driver.exec_js.called)
        context_mock.browser_driver.exec_js.assert_called_with(js_code_dummy)
        self.assertTrue(context_mock.browser_driver.type_text.called)
        context_mock.browser_driver.type_text.assert_called_with('//input[2]', 'watinha')

class PressEnterActionTest(unittest.TestCase):

    def test_press_enter_should_call_exec_js_and_load_from_js_loader(self):
        context_mock = Mock()
        js_code_dummy = 'function test_press_enter(){return 1;}test_press_enter();'

        context_mock.browser_driver.exec_js.return_value = '//button[1]'

        with patch.object(JsCodeLoader, 'load') as load_mock:
            load_mock.return_value = js_code_dummy
            enter_action = PressEnterAction()
            enter_action.execute(context_mock, None)

        self.assertTrue(load_mock.called)
        load_mock.assert_called_with('get_active_element_xpath.js')
        self.assertTrue(context_mock.browser_driver.exec_js.called)
        context_mock.browser_driver.exec_js.assert_called_with(js_code_dummy)
        self.assertTrue(context_mock.browser_driver.type_keys.called)
        context_mock.browser_driver.type_keys.assert_called_with('//button[1]', '\13')


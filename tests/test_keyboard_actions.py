import unittest
from mock import Mock, patch

from pyccuracy.errors import ActionFailedError
from accessibility_actions.keyboard_actions import FillFocusedElementAction, PressEnterAction
from accessibility_actions import JsCodeLoader

class FillFocusedElementActionTest(unittest.TestCase):

    def test_fill_element_should_call_js_loader_and_type_action_in_browser_driver(self):
        context_mock = Mock()
        js_code_dummy = 'function testing(){alert(12);};result = testing();'
        js_code_dummy_2 = 'function testing2(){};result = testing2();'
        js_load_return_values = [js_code_dummy, js_code_dummy_2]
        js_load_return_values.reverse()
        def jsload_return(*args):
            return js_load_return_values.pop()

        exec_js_return_values = ['document.getElementsByTagName("input")[2]', 'watinha']
        exec_js_return_values.reverse()
        def execjs_return(*args):
            return exec_js_return_values.pop()
        context_mock.browser_driver.exec_js.side_effect = execjs_return

        with patch.object(JsCodeLoader, 'load') as load_mock:
            load_mock.side_effect = jsload_return
            fill_action = FillFocusedElementAction()
            fill_action.execute(context_mock, 'watinha')

        self.assertEquals(2, load_mock.call_count)
        self.assertTrue('get_active_element_dom.js' in load_mock.mock_calls[0][1])
        self.assertTrue('verify_active_element_value.js' in load_mock.mock_calls[1][1])

        self.assertEquals(2, context_mock.browser_driver.exec_js.call_count)
        self.assertTrue(js_code_dummy in context_mock.browser_driver.exec_js.mock_calls[0][1])
        self.assertTrue(js_code_dummy_2 in context_mock.browser_driver.exec_js.mock_calls[1][1])

        self.assertTrue(context_mock.browser_driver.type_text.called)
        context_mock.browser_driver.type_text.assert_called_with('document.getElementsByTagName("input")[2]', 'watinha')

class PressEnterActionTest(unittest.TestCase):

    def test_press_enter_should_call_exec_js_and_load_from_js_loader(self):
        context_mock = Mock()
        js_code_dummy = 'function test_press_enter(){return 1;}test_press_enter();'

        context_mock.browser_driver.exec_js.return_value = 'document.getElements...[1]'

        with patch.object(JsCodeLoader, 'load') as load_mock:
            load_mock.return_value = js_code_dummy
            enter_action = PressEnterAction()
            enter_action.execute(context_mock, None)

        self.assertTrue(load_mock.called)
        load_mock.assert_called_with('get_active_element_dom.js')
        self.assertTrue(context_mock.browser_driver.exec_js.called)
        context_mock.browser_driver.exec_js.assert_called_with(js_code_dummy)
        self.assertTrue(context_mock.browser_driver.type_keys.called)
        context_mock.browser_driver.type_keys.assert_called_with('document.getElements...[1]', '\13')


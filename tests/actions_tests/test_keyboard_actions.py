import unittest
from mock import Mock, patch

from pyccuracy.errors import ActionFailedError
from accessibility_actions.keyboard_actions import FillFocusedElementAction, PressEnterAction
from accessibility_actions import JsCodeLoader

class FillFocusedElementActionTest(unittest.TestCase):

    def test_fill_focused_should_get_active_type_text_and_get_active_value(self):
        context_mock = Mock()
        fill_action = FillFocusedElementAction()

        exec_returns = ['document.getElement...', 'watinha']
        exec_returns.reverse()
        def exec_return(*args, **args2):
            return exec_returns.pop()

        with patch.object(JsCodeLoader, 'exec_js') as exec_mock:
            exec_mock.side_effect = exec_return
            fill_action.execute(context_mock, 'watinha')

        self.assertTrue(context_mock, exec_mock.mock_calls[0][1])
        self.assertTrue('get_active_element_dom.js', exec_mock.mock_calls[0][1])
        self.assertTrue(context_mock, exec_mock.mock_calls[1][1])
        self.assertTrue('verify_active_element_value.js', exec_mock.mock_calls[1][1])

        context_mock.browser_driver.type_text.assert_called_with('document.getElement...', 'watinha')

    def test_fill_non_input_element_should_throw_failure_exception(self):
        context_mock = Mock()
        fill_action = FillFocusedElementAction()

        exec_returns = ['document.getElement...', 'not found']
        exec_returns.reverse()
        def exec_return(*args, **args2):
            return exec_returns.pop()

        with patch.object(JsCodeLoader, 'exec_js') as exec_mock:
            exec_mock.side_effect = exec_return
            try:
                fill_action.execute(context_mock, 'watinha')
                self.assertTrue(False)
            except ActionFailedError:
                self.assertTrue(True)


class PressEnterActionTest(unittest.TestCase):

    def test_press_enter_should_call_exec_js_and_load_from_js_loader(self):
        context_mock = Mock()

        exec_returns = ['document.getElements...[1]', 'link activated']
        exec_returns.reverse()
        def exec_return(*args, **args2):
            return exec_returns.pop()
        with patch.object(JsCodeLoader, 'exec_js') as exec_js_mock:
            exec_js_mock.side_effect = exec_return
            enter_action = PressEnterAction()
            enter_action.execute(context_mock, None)

        self.assertEquals(2, exec_js_mock.call_count)
        self.assertTrue(context_mock in exec_js_mock.mock_calls[0][1])
        self.assertTrue('get_active_element_dom.js' in exec_js_mock.mock_calls[0][1])

        self.assertTrue(context_mock.browser_driver.type_keys.called)
        context_mock.browser_driver.type_keys.assert_called_with('document.getElements...[1]', '\13')

        exec_js_mock.assert_called_with(context_mock, 'activate_elements.js')


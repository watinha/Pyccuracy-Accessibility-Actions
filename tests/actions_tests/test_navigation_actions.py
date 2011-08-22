import unittest
from mock import Mock, patch

from pyccuracy.errors import ActionFailedError
from accessibility_actions.navigation_actions import TabNavigationAction, ArrowNavigationAction
from accessibility_actions import JsCodeLoader

class TabNavigationActionTest(unittest.TestCase):

    def test_execute_function_should_exec_js_and_return_searched_element(self):
        element_text_dummy = 'a link to look for'

        context_mock = Mock()

        with patch.object(JsCodeLoader, 'exec_js') as exec_js_mock:
            exec_js_mock.return_value = element_text_dummy
            tab_navigation = TabNavigationAction()
            tab_navigation.execute(context_mock, 'element', element_text_dummy, False)

        self.assertTrue(exec_js_mock.called)
        exec_js_mock.assert_called_with(context_mock, 'tab_navigation.js', element_text_dummy, '30')


    def test_execute_function_should_exec_js_and_return_searched_element_with_tab_limit_argument(self):
        element_text_dummy = 'a link to look for'

        context_mock = Mock()

        with patch.object(JsCodeLoader, 'exec_js') as exec_js_mock:
            exec_js_mock.return_value = element_text_dummy
            tab_navigation = TabNavigationAction()
            tab_navigation.execute(context_mock, 'element', element_text_dummy, '2')

        self.assertTrue(exec_js_mock.called)
        exec_js_mock.assert_called_with(context_mock, 'tab_navigation.js', element_text_dummy, '2')


    def test_execute_function_should_fail_with_not_found_element(self):
        element_text_dummy = 'a link to look for'

        context_mock = Mock()

        with patch.object(JsCodeLoader, 'exec_js') as exec_js_mock:
            exec_js_mock.return_value = 'element not found'
            tab_navigation = TabNavigationAction()
            try:
                tab_navigation.execute(context_mock, 'element', element_text_dummy, False)
                self.fail('if "element not found" received should raise a failed scenario exception')
            except ActionFailedError:
                self.assertTrue(True)


    def test_execute_function_should_fail_if_max_number_of_tab_presses_exceed(self):
        element_text_dummy = 'a link to look for'

        context_mock = Mock()

        with patch.object(JsCodeLoader, 'exec_js') as exec_js_mock:
            exec_js_mock.return_value = 'exceed max number of tab keys pressed'
            tab_navigation = TabNavigationAction()
            try:
                tab_navigation.execute(context_mock, 'element', element_text_dummy, False)
                self.fail('if "exceed max number of tab keys pressed" received should raise a failed scenario exception')
            except ActionFailedError:
                self.assertTrue(True)


class ArrowNavigationActionTest(unittest.TestCase):

    def test_arrow_navigation_execute_should_call_js_loader_exec_js(self):
        context_mock = Mock()

        with patch.object(JsCodeLoader, 'exec_js') as exec_js_mock:
            exec_js_mock.return_value = 'some_element'
            arrow_action = ArrowNavigationAction()
            arrow_action.execute(context_mock, 'element', 'some element', False)

        exec_js_mock.assert_called_once_with(context_mock, 'arrow_navigation.js', 'some element', '30')

    def test_execute_should_include_key_press_attribute_if_passed(self):
        context_mock = Mock()

        with patch.object(JsCodeLoader, 'exec_js') as exec_js_mock:
            exec_js_mock.return_value = 'some_element'
            arrow_action = ArrowNavigationAction()
            arrow_action.execute(context_mock, 'element', 'some element', '20')

        exec_js_mock.assert_called_once_with(context_mock, 'arrow_navigation.js', 'some element', '20')

    def test_execute_should_throw_action_failed_error_on_not_found_response(self):
        context_mock = Mock()

        with patch.object(JsCodeLoader, 'exec_js') as exec_js_mock:
            exec_js_mock.return_value = 'Not found...'
            arrow_action = ArrowNavigationAction()
            try:
                arrow_action.execute(context_mock, 'element', 'some element', '20')
                self.assertTrue(False)
            except ActionFailedError:
                self.assertTrue(True)

        exec_js_mock.assert_called_once_with(context_mock, 'arrow_navigation.js', 'some element', '20')

    def test_execute_should_throw_action_failed_error_on_max_key_presses_reached(self):
        context_mock = Mock()

        with patch.object(JsCodeLoader, 'exec_js') as exec_js_mock:
            exec_js_mock.return_value = 'Max number of key presses reached...'
            arrow_action = ArrowNavigationAction()
            try:
                arrow_action.execute(context_mock, 'element', 'some element', '20')
                self.assertTrue(False)
            except ActionFailedError:
                self.assertTrue(True)

        exec_js_mock.assert_called_once_with(context_mock, 'arrow_navigation.js', 'some element', '20')




import unittest
from mock import Mock, patch

from pyccuracy.errors import ActionFailedError
from accessibility_actions.navigation_actions import TabNavigationAction
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


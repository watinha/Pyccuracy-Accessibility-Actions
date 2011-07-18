import unittest
from mock import Mock, patch

from pyccuracy.errors import ActionFailedError
from accessibility_actions.navigation_actions import TabNavigationAction
from accessibility_actions import JsCodeLoader

class TabNavigationActionTest(unittest.TestCase):

    def test_execute_function_should_exec_js_and_return_searched_element(self):
        element_text_dummy = 'a link to look for'
        js_code_dummy = """
        function tab_navigation(text){
            console.log('unit_testing:' + text);
        }
        result = tab_navigation("a link to look for");
        """

        context_mock = Mock()
        context_mock.browser_driver.exec_js.return_value = element_text_dummy

        with patch.object(JsCodeLoader, 'load') as load_mock:
            load_mock.return_value = js_code_dummy
            tab_navigation = TabNavigationAction()
            tab_navigation.execute(context_mock, 'element', element_text_dummy)

        self.assertTrue(load_mock.called)
        load_mock.assert_called_with('tab_navigation.js', element_text_dummy)

        self.assertTrue(context_mock.browser_driver.exec_js.called)
        context_mock.browser_driver.exec_js.assert_called_with(js_code_dummy)

    def test_execute_function_should_fail_with_not_found_element(self):
        element_text_dummy = 'a link to look for'
        js_code_dummy = """
        function tab_navigation(text){
            console.log('unit_testing:' + text);
        }
        result tab_navigation("a link to look for");
        """

        context_mock = Mock()
        context_mock.browser_driver.exec_js.return_value = 'element not found'

        with patch.object(JsCodeLoader, 'load') as load_mock:
            load_mock.return_value = js_code_dummy
            tab_navigation = TabNavigationAction()
            try:
                tab_navigation.execute(context_mock, 'element', element_text_dummy)
                self.fail('if "element not found" received should raise a failed scenario exception')
            except ActionFailedError:
                self.assertTrue(True)


    def test_execute_function_should_fail_if_max_number_of_tab_presses_exceed(self):
        element_text_dummy = 'a link to look for'
        js_code_dummy = """
        function tab_navigation(text){
            console.log('unit_testing:' + text);
        }
        result tab_navigation("a link to look for");
        """

        context_mock = Mock()
        context_mock.browser_driver.exec_js.return_value = 'exceed max number of tab keys pressed'

        with patch.object(JsCodeLoader, 'load') as load_mock:
            load_mock.return_value = js_code_dummy
            tab_navigation = TabNavigationAction()
            try:
                tab_navigation.execute(context_mock, 'element', element_text_dummy)
                self.fail('if "exceed max number of tab keys pressed" received should raise a failed scenario exception')
            except ActionFailedError:
                self.assertTrue(True)


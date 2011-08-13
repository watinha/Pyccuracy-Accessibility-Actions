import unittest
from mock import Mock, patch

from accessibility_actions import JsCodeLoader

class JsCodeLoaderTest(unittest.TestCase):

    def test_load_should_load_javascript_files(self):
        js_code_dummy = """
        function tab_navigation(text){
            console.log('unit_testing:' + text);
        }"""
        dummy_argument = 'argument1'
        expected_js_code_dummy = """current_document = this.browserbot.getCurrentWindow().document; current_window = this.browserbot.getCurrentWindow();

        function tab_navigation(text){
            console.log('unit_testing:' + text);
        }
action = new tab_navigation();
result = action.execute("argument1");"""
        js_file_dummy = 'js_test.js'

        mocked_file = Mock()
        mocked_file.read.return_value = js_code_dummy

        mocked_open = Mock()
        mocked_open.return_value = mocked_file
        with patch.dict(__builtins__, {'open': mocked_open}):
            js_loader = JsCodeLoader()
            result = js_loader._load(js_file_dummy, ['argument1'])

            mocked_open.assert_called_with('js_codes/' + js_file_dummy, 'r')
            self.assertTrue(mocked_file.read.called)

        self.assertEquals(expected_js_code_dummy, result)

    def test_load_should_load_javascript_files_with_more_arguments(self):
        js_code_dummy = """
        function keyboard_action(text){
            console.log('other cool test');
        }"""
        dummy_argument = 'argument1'
        expected_js_code_dummy = """current_document = this.browserbot.getCurrentWindow().document; current_window = this.browserbot.getCurrentWindow();

        function keyboard_action(text){
            console.log('other cool test');
        }
action = new keyboard_action();
result = action.execute("argument1","argument2","argument3");"""
        js_file_dummy = 'js_test.js'

        mocked_file = Mock()
        mocked_file.read.return_value = js_code_dummy

        mocked_open = Mock()
        mocked_open.return_value = mocked_file
        with patch.dict(__builtins__, {'open': mocked_open}):
            js_loader = JsCodeLoader()
            result = js_loader._load(js_file_dummy, ['argument1', 'argument2', 'argument3'])

            mocked_open.assert_called_with('js_codes/' + js_file_dummy, 'r')
            self.assertTrue(mocked_file.read.called)

        self.assertEquals(expected_js_code_dummy, result)

    def test_load_should_load_javascript_files_with_no_arguments(self):

        js_code_dummy = """
        function other_cool_function(){
            console.log('other cool test');
        }"""
        dummy_argument = 'argument1'
        expected_js_code_dummy = """current_document = this.browserbot.getCurrentWindow().document; current_window = this.browserbot.getCurrentWindow();

        function other_cool_function(){
            console.log('other cool test');
        }
action = new other_cool_function();
result = action.execute();"""
        js_file_dummy = 'js_test.js'

        mocked_file = Mock()
        mocked_file.read.return_value = js_code_dummy

        mocked_open = Mock()
        mocked_open.return_value = mocked_file
        with patch.dict(__builtins__, {'open': mocked_open}):
            js_loader = JsCodeLoader()
            result = js_loader._load(js_file_dummy, [])

            mocked_open.assert_called_with('js_codes/' + js_file_dummy, 'r')
            self.assertTrue(mocked_file.read.called)

        self.assertEquals(expected_js_code_dummy, result)

    def test_exec_js_should_call_js_loader_and_browser_driver_exec_js(self):
        context_mock = Mock()
        context_mock.browser_driver.exec_js.return_value = 'document.getEle...'
        js_file_stub = 'some_js_file.js'

        jsloader = JsCodeLoader()
        jsloader._load = Mock()
        jsloader._load.return_value = 'function(){console.log();...'
        result = jsloader.exec_js(context_mock, js_file_stub)

        jsloader._load.assert_called_with('some_js_file.js', ())
        context_mock.browser_driver.exec_js.assert_called_with('function(){console.log();...')

        self.assertEquals('document.getEle...', result)

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
result = tab_navigation("argument1");"""
        js_file_dummy = 'js_test.js'
        
        mocked_file = Mock()
        mocked_file.read.return_value = js_code_dummy

        mocked_open = Mock()
        mocked_open.return_value = mocked_file
        with patch.dict(__builtins__, {'open': mocked_open}):
            js_loader = JsCodeLoader()
            result = js_loader.load(js_file_dummy, 'argument1')

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
result = keyboard_action("argument1","argument2","argument3");"""
        js_file_dummy = 'js_test.js'
        
        mocked_file = Mock()
        mocked_file.read.return_value = js_code_dummy

        mocked_open = Mock()
        mocked_open.return_value = mocked_file
        with patch.dict(__builtins__, {'open': mocked_open}):
            js_loader = JsCodeLoader()
            result = js_loader.load(js_file_dummy, 'argument1', 'argument2', 'argument3')

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
result = other_cool_function();"""
        js_file_dummy = 'js_test.js'
        
        mocked_file = Mock()
        mocked_file.read.return_value = js_code_dummy

        mocked_open = Mock()
        mocked_open.return_value = mocked_file
        with patch.dict(__builtins__, {'open': mocked_open}):
            js_loader = JsCodeLoader()
            result = js_loader.load(js_file_dummy)

            mocked_open.assert_called_with('js_codes/' + js_file_dummy, 'r')
            self.assertTrue(mocked_file.read.called)

        self.assertEquals(expected_js_code_dummy, result)

import re


class JsCodeLoader:

    JS_DIR = 'js_codes/'
    FUNCTION_REGEXP = "(function)\s+((.)+)\s*\((.)*\)\s*\{"

    def load(self, js_filename, *args):
        js_file = open(self.JS_DIR + js_filename, 'r')
        js_code = js_file.read()

        function_match = re.search(self.FUNCTION_REGEXP, js_code)
        function_name = function_match.group(2)

        function_arguments = ','.join(['"' + arg + '"' for arg in args])

        # returns the result of javascript code to pyccuracy interface with selenium through exec_js browser_driver method
        js_constructor_line = 'action = new ' + function_name + '();'
        js_result_line = 'result = action.execute(' + function_arguments + ');'

        # getting the DOM document element reference from within selenium
        js_header = "current_document = this.browserbot.getCurrentWindow().document; current_window = this.browserbot.getCurrentWindow();"
        return js_header + "\n" + js_code + "\n" + js_constructor_line + "\n" + js_result_line

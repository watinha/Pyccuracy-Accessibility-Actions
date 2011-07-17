import re


class JsCodeLoader:

    JS_DIR = '../js_codes/'
    FUNCTION_REGEXP = "(function)\s+((.)+)\s*\((.)*\)\s*\{"

    def load(self, js_filename, *args):
        js_file = open(self.JS_DIR + js_filename, 'r')
        js_code = js_file.read()

        function_match = re.search(self.FUNCTION_REGEXP, js_code)
        function_name = function_match.group(2)

        function_arguments = ','.join(['"' + arg + '"' for arg in args])
        js_result_line = 'result = ' + function_name + '(' + function_arguments + ');'

        return js_code + "\n" + js_result_line

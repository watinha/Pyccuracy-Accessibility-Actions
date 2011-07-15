from pyccuracy.actions import ActionBase
from pyccuracy.actions.core.element_actions import resolve_element_key
from accessibility_actions import teste

class ElementClickAction(ActionBase):
    __builtin__ = True
    regex = r'^(And )?I tab navigate to [\"](?P<element_name>[^"]+)[\"] (?P<element_type><element selector>)$'

    def execute(self, context, element_type, element_name):
        element_key = resolve_element_key(context, element_type, element_name, self.resolve_element_key)
        
        error_message = "basic error message :: " + element_key
        opa = ""
        self.assert_element_is_visible(context, element_key, error_message)
        text = context.browser_driver.exec_js('this.browserbot.getCurrentWindow().document.querySelectorAll("#introduction")[0].focus();')
        if (teste()):
            raise self.failed("opa pegou")
        find_xpath_current_js = """
           var current_element = this.browserbot.getCurrentWindow().document.activeElement; 
           var all_links = this.browserbot.getCurrentWindow().document.getElementsByTagName('a');
           for (var cont = 0; cont < all_links.length; cont++){
               if (all_links[cont] == current_element)
                   index = cont;
           }
           '//a[' + (index) + ']'; 
        """
        new_name = context.browser_driver.exec_js(find_xpath_current_js)
        #raise self.failed("opa :: " + element_key + " " + new_name)
        context.browser_driver.type_keys(new_name, '\9')


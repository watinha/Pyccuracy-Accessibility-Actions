function get_active_element_xpath(){
    this.constants = {
        NOT_FOUND_ELEMENT: "active element not found"
    };

    var active_element = current_document.activeElement,
        element_type = active_element.tagName,
        nodes = current_document.getElementsByTagName(element_type);

    for (var cont = 0; cont < nodes.length; cont++)
        if (active_element == nodes[cont])
            return "//" + (element_type + "[" + cont + "]").toLowerCase();
    
    return this.constants.NOT_FOUND_ELEMENT;
}

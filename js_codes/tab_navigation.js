function tab_navigation(element_text, tab_limit){
    this.constants = {
        ELEMENT_NOT_FOUND: 'element not found',
        TAB_LIMIT: 30,
        TAB_LIMIT_EXCEEDED: 'exceed max number of tab keys pressed'
    };

    if( ! tab_limit)
        tab_limit = this.constants.TAB_LIMIT;

    /*
     * Function to look into parent nodes styles to
     *  identify whether elements are visible or not
     */
    function is_visible(node) {
        var computed_style = current_window.getComputedStyle(node);
        if ( ! computed_style){
            return true;
        }
        if (computed_style.getPropertyValue("visibility") == "hidden")
            return false;
        if (computed_style.getPropertyValue("display") == "none")
            return false;
        return is_visible(node.parentNode);
    }

    var nodes = current_document.getElementsByTagName("*"),
        focusable_nodes = [];

    /*
     * retrieving focusable elements
     */
    for (var cont = 0; cont < nodes.length; cont++) {
        if (nodes[cont].tabIndex >= 0 && is_visible(nodes[cont])){
            /*
             * ordering accordingly to tabindex (NO OPTIMIZATION IMPLEMENTED SIMPLE INSERTION SORT)
             */
            var cont_focusable = 0;
            while (cont_focusable < focusable_nodes.length && (nodes[cont].tabIndex == 0 || nodes[cont].tabIndex >= focusable_nodes[cont_focusable].tabIndex))
                cont_focusable++;
            focusable_nodes.splice(cont_focusable, 0, nodes[cont]);
        }
    }

    /*
     * get the current activeElement in DOM
     */
    var current_index = 0;
    for (var cont in focusable_nodes)
        if (current_document.activeElement == focusable_nodes[cont])
            current_index = cont;

    /*
     * Setting focus for focusable_nodes in order looking for element_text within it
     */
    var cont;
    for (cont = (current_index); cont < focusable_nodes.length && (cont - current_index) < tab_limit; cont++){
        focusable_nodes[cont].focus();
        if (focusable_nodes[cont].innerHTML.search(element_text) >= 0)
            return element_text;
        if(focusable_nodes[cont].title && focusable_nodes[cont].title.search(element_text) >= 0)
            return element_text;
        if(focusable_nodes[cont].name && focusable_nodes[cont].name.search(element_text) >= 0)
            return element_text;
    }
    if((cont - current_index) == tab_limit)
        return this.constants.TAB_LIMIT_EXCEEDED;
    return this.constants.ELEMENT_NOT_FOUND;
}

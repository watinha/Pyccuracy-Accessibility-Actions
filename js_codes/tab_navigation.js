function TabNavigation() {
    this.constants = {
        ELEMENT_NOT_FOUND: 'element not found',
        TAB_LIMIT: 30,
        TAB_LIMIT_EXCEEDED: 'exceed max number of tab keys pressed'
    };
}
TabNavigation.prototype.execute = function(element_text, tab_limit) {
    var tab_nav = new TabNavigation();
    var focusable_nodes = tab_nav.get_focusable();
    var current_index = tab_nav.get_active_index();
    return tab_nav.search_for_focusable(element_text, tab_limit);
}
/*
 * Function to look into parent nodes styles to
 *  identify whether elements are visible or not
 */
TabNavigation.prototype.is_visible = function (node) {
    var computed_style = current_window.getComputedStyle(node);
    if ( ! computed_style){
        return true;
    }
    if (computed_style.getPropertyValue("visibility") == "hidden")
        return false;
    if (computed_style.getPropertyValue("display") == "none")
        return false;
    return this.is_visible(node.parentNode);
}
/*
 * retrieving focusable elements
 */
TabNavigation.prototype.get_focusable = function () {
    var nodes = current_document.getElementsByTagName("*"),
        focusable_nodes = [];

    for (var cont = 0; cont < nodes.length; cont++) {
        if (
            nodes[cont].tabIndex >= 0 &&
            this.is_visible(nodes[cont]) &&
            (nodes[cont].tagName != "A" || nodes[cont].href)
        ){
            /*
             * ordering accordingly to tabindex (NO OPTIMIZATION IMPLEMENTED SIMPLE INSERTION SORT)
             */
            var cont_focusable = 0;
            while (cont_focusable < focusable_nodes.length && (nodes[cont].tabIndex == 0 || nodes[cont].tabIndex >= focusable_nodes[cont_focusable].tabIndex))
                cont_focusable++;
            focusable_nodes.splice(cont_focusable, 0, nodes[cont]);
        }
    }
    this.focusable_nodes = focusable_nodes;
    return focusable_nodes;
}
/*
 * get the current activeElement in DOM
 */
TabNavigation.prototype.get_active_index = function () {
    var current_index = 0,
        focusable_nodes = this.focusable_nodes;
    for (var cont in focusable_nodes) {
        if (current_document.activeElement == focusable_nodes[cont]) {
            current_index = cont;
            break;
        }
    }
    this.current_index = current_index;
    return current_index;
}
/*
 * Setting focus for focusable_nodes in order looking for element_text within it
 */
TabNavigation.prototype.search_for_focusable = function (element_text, tab_limit) {
    if( ! tab_limit)
        tab_limit = this.constants.TAB_LIMIT;
    else
        tab_limit = parseInt(tab_limit);

    var cont,
        current_index = this.current_index,
        focusable_nodes = this.focusable_nodes;

    for (cont = (current_index); (cont - current_index) < focusable_nodes.length && (cont - current_index) <= tab_limit; cont++){
        var current_node = cont % focusable_nodes.length;
        focusable_nodes[current_node].focus();
        if (focusable_nodes[current_node].innerHTML.search(element_text) >= 0)
            return element_text;
        if(focusable_nodes[current_node].title && focusable_nodes[current_node].title.search(element_text) >= 0)
            return element_text;
        if(focusable_nodes[current_node].name && focusable_nodes[current_node].name.search(element_text) >= 0)
            return element_text;
        if(focusable_nodes[current_node].value && focusable_nodes[current_node].value.search(element_text) >= 0)
            return element_text;
    }
    if((cont - current_index) == (tab_limit + 1))
        return this.constants.TAB_LIMIT_EXCEEDED;
    return this.constants.ELEMENT_NOT_FOUND;
}

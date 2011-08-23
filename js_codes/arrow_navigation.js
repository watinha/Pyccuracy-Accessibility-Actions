function ArrowNavigation() {
}
ArrowNavigation.prototype.constants = {
    ELEMENT_NOT_FOUND: "Element not found",
    KEYPRESSES_LIMIT: "Max number of keypresses reached"
}
ArrowNavigation.prototype.execute = function (element_text, keypress_limit) {
    var active_element = current_document.activeElement,
        elements_array = this._build_array(current_document.body),
        cont = 0,
        active_index = 0,
        keypress_limit = parseInt(keypress_limit),
        text_nodes_count = 0;

    for (cont = 0; cont < elements_array.length; cont++) {
        if (elements_array[cont] == active_element)
            break;
    }
    active_index = cont;
    for (cont; cont < elements_array.length; cont++) {
        if (text_nodes_count >= keypress_limit)
            return this.constants.KEYPRESSES_LIMIT;
        if (elements_array[cont].nodeType == 3)
            text_nodes_count++;
        if (elements_array[cont].nodeType == 3 &&
            elements_array[cont].nodeValue.search(element_text) >= 0)
            return element_text;
    }
    return this.constants.ELEMENT_NOT_FOUND;
}
ArrowNavigation.prototype._build_array = function (element) {
    if ( ! element.childNodes)
        return [element];
    var childs = element.childNodes,
        array = [element];

    for (var cont = 0; cont < childs.length; cont++)
        array = array.concat(this._build_array(childs[cont]));

    return array;
}

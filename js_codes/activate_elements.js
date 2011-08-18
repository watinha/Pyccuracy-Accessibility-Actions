function ActivateElements() {
}
ActivateElements.prototype.constants = {
    FORM_ELEMENT_NOT_FOUND: "parent form not found"
};
ActivateElements.prototype.execute = function () {
    var active_element = current_document.activeElement;

    // Firefox handling for special characters event dispatching
    var keydown_event = current_document.createEvent("KeyboardEvent"),
        keypress_event = current_document.createEvent("KeyboardEvent"),
        keyup_event = current_document.createEvent("KeyboardEvent");

    if (keydown_event.initKeyEvent) {
        keydown_event.initKeyEvent("keydown", true, false, window, false, false, false, false, 13, 13);
        keypress_event.initKeyEvent("keypress", true, false, window, false, false, false, false, 13, 13);
        keyup_event.initKeyEvent("keyup", true, false, window, false, false, false, false, 13, 13);

        active_element.dispatchEvent(keydown_event);
        active_element.dispatchEvent(keypress_event);
        active_element.dispatchEvent(keyup_event);
        return true;
    }

    switch (active_element.tagName) {
        case "A":
            this._click_activation(active_element);
            break;
        case "BUTTON":
            this._click_activation(active_element);
            break;
        case "INPUT":
            this._activate_form(active_element);
            break;
    }
}
ActivateElements.prototype._activate_form = function (active_element) {
    var form_parent = this._search_form_parent(active_element);
    form_parent.submit();
}
ActivateElements.prototype._click_activation = function (active_element) {
    var click_event = current_document.createEvent("MouseEvent");
    click_event.initMouseEvent("click", true, true, current_window, 12, 12, 12, 12, 12, false, false, false, false, 0, null);
    active_element.dispatchEvent(click_event);
    return "link activated";

}
ActivateElements.prototype._search_form_parent = function (input_element) {
    if (input_element.parentNode.tagName == "FORM")
        return input_element.parentNode;
    if (input_element.parentNode.tagName == "BODY")
        return this.constants.FORM_ELEMENT_NOT_FOUND;
    return this._search_form_parent(input_element.parentNode);
}

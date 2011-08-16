function ActivateElements() {
}
ActivateElements.prototype.constants = {
    FORM_ELEMENT_NOT_FOUND: "parent form not found"
};
ActivateElements.prototype.execute = function () {
    var active_element = current_document.activeElement,
        click_event = current_document.createEvent("MouseEvent");

    if (active_element.tagName == "A") {
        click_event.initMouseEvent("click", true, true, current_window, 12, 12, 12, 12, 12, false, false, false, false, 0, null);
        current_document.activeElement.dispatchEvent(click_event);
        return "link activated";
    } else if (active_element.tagName == "INPUT") {
        var form_parent = this._search_form_parent(active_element);
        form_parent.submit();
    }
}
ActivateElements.prototype._search_form_parent = function (input_element) {
    if (input_element.parentNode.tagName == "FORM")
        return input_element.parentNode;
    if (input_element.parentNode.tagName == "BODY")
        return this.constants.FORM_ELEMENT_NOT_FOUND;
    return this._search_form_parent(input_element.parentNode);
}

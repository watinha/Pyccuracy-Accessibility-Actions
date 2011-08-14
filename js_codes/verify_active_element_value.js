function GetActiveValue(){
}
GetActiveValue.prototype.constants = {
    NOT_A_FORM_ELEMENT: "not a form element"
}
GetActiveValue.prototype.execute = function () {
    var activeElement = current_document.activeElement;

    if (activeElement.tagName != "INPUT" &&
        activeElement.tagName != "TEXTAREA")
        return this.constants.NOT_A_FORM_ELEMENT;

    return activeElement.value;
}

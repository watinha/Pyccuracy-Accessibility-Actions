function ActivateElements() {
}
ActivateElements.prototype.execute = function () {
    var click_event = current_document.createEvent("MouseEvent");
    click_event.initMouseEvent("click", true, true, current_window, 12, 12, 12, 12, 12, false, false, false, false, 0, null);
    current_document.activeElement.dispatchEvent(click_event);
    return "link activated";
}

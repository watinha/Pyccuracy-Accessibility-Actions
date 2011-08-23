function ArrowNavigationTest() {
}
ArrowNavigationTest.prototype.run_test = function () {

    current_document = document;
    current_window = window;

    module("arrow_navigation");

    test("execute should find and return second header in fixture", function () {
        var action = new ArrowNavigation(),
            element_text = "Second header",
            keypress_limit = "3",
            result;
        current_document.querySelectorAll("#qunit-fixture > h1")[0].focus();

        result = action.execute(element_text, keypress_limit);

        equal(result, "Second header");
    });

    test("execute should return not found", function () {
        var action = new ArrowNavigation(),
            element_text = "non existant",
            keypress_limit = "3000",
            result;
        current_document.querySelectorAll("#qunit-fixture > h1")[0].focus();

        result = action.execute(element_text, keypress_limit);
        equal(result, "Element not found");
    });

    test("execute should return max number of keypresses reached", function () {
        var action = new ArrowNavigation(),
            element_text = "some text inside a div",
            keypress_limit = "3",
            result;
        current_document.querySelectorAll("#qunit-fixture > h1")[0].focus();

        result = action.execute(element_text, keypress_limit);
        equal(result, "Max number of keypresses reached");
    });

    test("execute should not find element with the max number defined", function () {
        var action = new ArrowNavigation(),
            element_text = "non-link",
            keypress_limit = "3",
            result;
        current_document.querySelectorAll("#qunit-fixture > h1")[0].focus();

        result = action.execute(element_text, keypress_limit);
        equal(result, "Max number of keypresses reached");
    });
};

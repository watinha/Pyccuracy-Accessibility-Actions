function GetActiveValueTest () {
}
GetActiveValueTest.prototype.run_test = function () {
    current_document = document;
    current_window = window;

    module("get active element value");

    test("test get active element should return the value of the element", function() {
        document.querySelectorAll("form > input")[0].focus();
        document.querySelectorAll("form > input")[0].value = 'watinha';
        var action = new GetActiveValue(),
            result = action.execute();

        equal(result, 'watinha');

        document.querySelectorAll("form > input")[0].value = '';
    });

    test("test get active element value should return error message if not input ", function () {
        document.querySelectorAll("#link1")[0].focus();
        document.querySelectorAll("#link1")[0].value = 'watinha';
        var action = new GetActiveValue(),
            result = action.execute();

        equal(result, 'not a form element');

        document.querySelectorAll("#link1")[0].value = '';
    });
}

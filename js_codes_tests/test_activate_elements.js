function ActivateElementsTest() {
};
ActivateElementsTest.prototype.run_test = function () {
    current_document = document;
    current_window = window;

    module("test activate elements");

    test("test link activation should dispatch a click event", function () {
        // setting the click listener
        function click_event(ev) {
            ok(true, "link activated");
        }
        document.querySelectorAll("#link1")[0].addEventListener("click", click_event, true);
        document.querySelectorAll("#link1")[0].focus();

        var location_temp = window.location + "",
            hash_position = location_temp.search("#");

        // setting the query string in the location bar
        if (hash_position)
            window.location = location_temp.substring(0, hash_position) + "#";
        else
            window.location += "#";
        location_temp = window.location + "";

        var action = new ActivateElements();
        var result = action.execute();

        expect(3);
        equal(result, "link activated");
        equal(window.location + "", location_temp + "link1"); // should also change the location bar address

        // removing listener to avoid tests interference
        document.querySelectorAll("#link1")[0].removeEventListener("click", click_event);
    });

    test("test form activation should follow form action attribute", function () {
        var previous_submit = document.querySelectorAll("form")[0].submit;
        document.querySelectorAll("form")[0].submit = function () {
            ok(true, "form submitted ok");
        }
        document.querySelectorAll("form > input")[0].value = "watinha";
        document.querySelectorAll("form > input")[0].focus();

        var action = new ActivateElements();
        var result = action.execute();

        expect(1);

        // avoid tests interference
        document.querySelectorAll("form")[0].submit = previous_submit;
    });

    test("test _search_form_parent function gets the parent form element", function () {
        var fixture_input = document.createElement("input"),
            fixture_div = document.createElement("div"),
            fixture_span = document.createElement("span"),
            fixture_form = document.createElement("form");

        fixture_form.appendChild(fixture_div);
        fixture_div.appendChild(fixture_span);
        fixture_span.appendChild(fixture_input);

        var action = new ActivateElements(),
            parent_form = action._search_form_parent(fixture_input);

        equal(parent_form, fixture_form);
    });

}

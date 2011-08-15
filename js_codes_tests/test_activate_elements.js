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

}

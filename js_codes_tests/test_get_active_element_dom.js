document.addEventListener("load", function(e){
    current_document = document;
    current_window = window;

    module("get_active_element_dom");

    test("test get dom should generate dom for elements", function(){
        document.getElementById("link1").focus();
        var action = new GetActiveNode();
        var result = action.execute();
        /*
         * DOM order is not granted in Javascript
         */
        ok(result == "document.getElementsByTagName(\"a\")[1]" ||
           result == "document.getElementsByTagName(\"a\")[19]");

        document.getElementsByTagName("h1")[1].focus();
        var result = action.execute();
        equal(result, "document.getElementsByTagName(\"h1\")[1]");

        document.getElementsByTagName("a")[2].focus();
        var result = action.execute();
        equal(result, "document.getElementsByTagName(\"a\")[2]");

        document.getElementsByTagName("input")[2].focus();
        var result = action.execute();
        equal(result, "document.getElementsByTagName(\"input\")[2]");

        document.getElementsByTagName("button")[0].focus();
        var result = action.execute();
        equal(result, "document.getElementsByTagName(\"button\")[0]");
    });

}, true);

document.addEventListener("load", function(e){
    current_document = document;
    current_window = window;

    module("get_active_element_xpath");

    test("test get xpath should generate xpath for elements", function(){
        document.getElementById("link1").focus();
        var action = new GetActiveNode();
        var result = action.execute();
        equal(result, "document.getElementsByTagName(\"a\")[1]");

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

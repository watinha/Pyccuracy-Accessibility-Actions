document.addEventListener("load", function(e){
    current_document = document;
    current_window = window;

    module("get_active_element_xpath");
    
    test("test get xpath should generate xpath for elements", function(){
        document.getElementById("link1").focus();
        var result = get_active_element_xpath();
        equal(result, "//a[1]");

        document.getElementsByTagName("h1")[1].focus();
        var result = get_active_element_xpath();
        equal(result, "//h1[1]");

        document.getElementsByTagName("a")[2].focus();
        var result = get_active_element_xpath();
        equal(result, "//a[2]");

        document.getElementsByTagName("input")[2].focus();
        var result = get_active_element_xpath();
        equal(result, "//input[2]");

        document.getElementsByTagName("button")[0].focus();
        var result = get_active_element_xpath();
        equal(result, "//button[0]");
    });

}, true);

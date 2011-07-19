document.addEventListener("load", function(e){
    current_document = document;
    current_window = window;

    module("tab_navigation");

    test("tab_navigation should return the text inside the element it reaches and set the activeElement", function(){
        var result = tab_navigation("first button");
        equal(result, "first button");
        var button_element = document.getElementsByTagName("button")[0];
        equal(document.activeElement, button_element);
    });

    test("tab_navigation should return the text inside the element it reaches and set the activeElement for title and name", function(){
        var result = tab_navigation("textinput");
        equal(result, "textinput");
        equal(document.activeElement.name, "textinput");

        result = tab_navigation("textinput2");
        equal(result, "textinput2");
        equal(document.activeElement.title, "textinput2");
    });

    test("tab_navigation should return 'element not found' when the element been looked for is not focusable", function(){
        var result = tab_navigation("Fourth header");
        equal(result, "element not found");
    });

    test("tab_navigation should return 'exceed max number of tab keys pressed'", function(){
        document.getElementsByTagName("h1")[1].focus();
        var result = tab_navigation("interactive span", 5);
        equal(result, "exceed max number of tab keys pressed");
    });

    test("tab_navigation should ignore display:none and visibility:hidden elements", function() {
        var result = tab_navigation("invisible link1");
        equal(result, "element not found");

        result = tab_navigation("invisible link2");
        equal(result, "element not found");

        result = tab_navigation("invisible link3");
        equal(result, "element not found");
    });

    test("tab_navigation should get sequential elements with different number of tab limits", function(){
        var result = tab_navigation("First header");
        equal(result, "First header");
        var searched_element = document.getElementsByTagName("h1")[1];
        equal(document.activeElement, searched_element);

        result = tab_navigation("link 1", 2);
        equal(result, "link 1");
        searched_element = document.getElementById("link1");
        equal(document.activeElement, searched_element);

        result = tab_navigation("link 5", 5);
        equal(result, "link 5");
        equal(document.activeElement.innerHTML, "link 5");
    });
}, true);

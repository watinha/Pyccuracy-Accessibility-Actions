document.addEventListener("load", function(e){
    current_document = document;
    current_window = window;

    module("tab_navigation");

    test("tab_navigation should return the text inside the element it reaches and set the activeElement", function(){
        var action = new TabNavigation();
        var result = action.execute("first button");
        equal(result, "first button");
        var button_element = document.getElementsByTagName("button")[0];
        equal(document.activeElement, button_element);
    });

    test("tab_navigation should return the text inside the element it reaches and set the activeElement for title and name", function(){
        var action = new TabNavigation();
        var result = action.execute("textinput");
        equal(result, "textinput");
        equal(document.activeElement.name, "textinput");

        result = action.execute("textinput2");
        equal(result, "textinput2");
        equal(document.activeElement.title, "textinput2");
    });

    test("tab_navigation should return 'element not found' when the element been looked for is not focusable", function(){
        var action = new TabNavigation();
        var result = action.execute("Fourth header");
        equal(result, "element not found");
    });

    test("tab_navigation should return 'exceed max number of tab keys pressed'", function(){
        document.getElementsByTagName("h1")[1].focus();
        var action = new TabNavigation();
        var result = action.execute("interactive span", 5);
        equal(result, "exceed max number of tab keys pressed");
    });

    test("tab_navigation should ignore links with no href attribute", function(){
        document.getElementsByTagName("h1")[1].focus();
        var action = new TabNavigation();
        var result = action.execute("non-link");
        equals(result, "element not found");
    });

    test("tab_navigation should ignore display:none and visibility:hidden elements", function() {
        document.getElementsByTagName("h1")[1].focus();
        var action = new TabNavigation();
        var result = action.execute("invisible link1");
        equal(result, "element not found");

        result = action.execute("invisible link2");
        equal(result, "element not found");

        result = action.execute("invisible link3");
        equal(result, "element not found");
    });

    test("tab_navigation should get sequential elements with different number of tab limits", function(){
        document.getElementsByTagName("h1")[1].focus();
        var action = new TabNavigation();
        var result = action.execute("First header");
        equal(result, "First header");
        var searched_element = document.getElementsByTagName("h1")[1];
        equal(document.activeElement, searched_element);

        result = action.execute("link 1", 2);
        equal(result, "link 1");
        searched_element = document.getElementById("link1");
        equal(document.activeElement, searched_element);

        result = action.execute("link 5", 5);
        equal(result, "link 5");
        equal(document.activeElement.innerHTML, "link 5");
    });
}, true);

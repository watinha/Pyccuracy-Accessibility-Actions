Introduction
============
The main objective of this project is to implement accessibility actions for the pyccuracy, web acceptance testing application (http://pyccuracy.org). Pyccuracy makes use of natural language expressions to generate user stories and acceptance scenarios that are automatically run in the browser, evaluating the behaviour of all layers of a web application (server and client side-scripting). 

However pyccuracy still have not implemented actions that can be classified as accessible for disabled users like "tabbing navigation", focus possibility for interactive elements, landmarks and header navigation, among other actions.

Howto use
=========

--> on development stages, so if you want to try the new actions out, you will have to add them to pyccuracy\_console with the -A option.

--> as soon as the development evolves I will be putting new information on how to use accessibility actions, one-by-one. :)

Goal
====
The goal of implementing accessibility actions for pyccuracy is to be able to execute acceptance tests of web applications functionality, considering disabled users task completion with assistive technologies. These users do no rely on the same visual and interactive mechanisms such as mouse and link colors, for example. So pyccuracy actions must consider these characteristics to guarantee that the functionality of the web application is available for all users. 

From the development perspective, accessibility actions drive automatic accessibility evaluation tools into a Continuous Integration environment. Making it possible to include accessibility non-functional requirements into the development life-cycle of projects and assisting developers while coding solutions for them.

Current Status
==============
Still in the very beginning of the coding. Should try implement a few accessible actions for users.

Code architecture
=================
The code is organized in two folds:

- Pyccuracy actions implemented in python and tested with Python unit tests

- Javascript implementation of events to be run in the browser and tested with Qunit

In order to validate the integration of both codes (python and javascript) I am currently using a few pyccuracy base scenarios as acceptance testing for the complete application. If the pyccuracy scenarios are run successfully, them the applications is OK.

check it out as a ASCII model :)

                                                                    |
_____________         _____________           __________________    |
|           |         |           |           |                |    |
| Selenium  | <------ |  Python   | <-------- |   JavaScript   |    |
|  server   |         | Pyccuracy |           |     event      |    |      
|           |         |  actions  |           | implementation |    |
|___________|         |___________|           |________________|    |        _______________
                            |                          |            |        |             | 
                            |                          |            | -----> |  Pyccuracy  | 
                      _____________              _______________    |        |    Tests    |
                      |           |              |             |    |        |  Scenarios  |
                      |  Python   |              |  JavaScript |    |        | (Acceptance)|
                      |   unit    |              |    QUnit    |    |        |_____________|
                      |   test    |              |             |    |
                      |___________|              |_____________|    |
                                                                    |
--------------------------------------------------------------------|
                                                                    
Contact
=======
If you find these information useful or would like to contribute to this project, feel free to send me a message: talk@watinha.com.

WORK LOG
========

- work a javascript log to debug application

- implement remaining actions for the first established scenario 

- filter tab navigation links considering its visibility (window.getComputedStyle(document.querySelectorAll('div.introduction a')[1], null).getPropertyValue('visibility') TODO)

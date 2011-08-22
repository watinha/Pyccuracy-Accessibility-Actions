#! /usr/bin/make

PYTHON=/usr/bin/python
RM=/bin/rm

tests-actions:
	@./bin/run_actions_tests.py

tests-jsunit:
	@./bin/run_js_codes_test.sh

tests-pyccuracy:
	@./bin/run_pyccuracy.sh

help:
	@echo "****************************************************"
	@echo "***** \033[1;34mAccessibility Actions for Pyccuracy help\033[0;0m *****"
	@echo "****************************************************"
	@echo "    \033[32mtests-actions:\033[0m   unit test the python written action classes"
	@echo "    \033[0;32mtests-jsunit:\033[0m    unit test the javascript written action classes"
	@echo "    \033[0;32mtests-pyccuracy:\033[m acceptance test all actions implemented (js and python)"
	@echo "\n"

clean:
	@$(RM) -r accessibility_actions/*.pyc tests/*.pyc

.PHONY: tests-actions tests-jsunit tests-pyccuracy help clean

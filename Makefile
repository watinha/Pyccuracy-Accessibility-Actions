PYTHON=/usr/bin/python
RM=/bin/rm

tests-actions:
	@./bin/run_actions_tests.py

tests-jsunit:
	@./bin/run_js_codes_test.sh

tests-pyccuracy:
	@./bin/run_pyccuracy.sh

clean:
	@$(RM) -r accessibility_actions/*.pyc tests/*.pyc

.PHONY: tests-actions tests-jsunit tests-pyccuracy clean

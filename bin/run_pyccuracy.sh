#
#   Single script for running pyccuracy with pre-established pages and
#    stories for testing the general sanity of the system
#
pyccuracy_console -A accessibility_actions/ -P pages/ --browser=safari -d $1 -p *.acc

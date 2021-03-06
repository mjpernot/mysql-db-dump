#!/bin/bash
# Unit test code coverage for program module.
# This will run the Python code coverage module against all unit test modules.
# This will show the amount of code that was tested and which lines of code
#   that was skipped during the test.

coverage erase

echo ""
echo "Running unit test modules in conjunction with coverage"
coverage run -a --source=mysql_db_dump test/unit/mysql_db_dump/add_ssl.py
coverage run -a --source=mysql_db_dump test/unit/mysql_db_dump/add_tls.py
coverage run -a --source=mysql_db_dump test/unit/mysql_db_dump/crt_dump_cmd.py
coverage run -a --source=mysql_db_dump test/unit/mysql_db_dump/dump_db.py
coverage run -a --source=mysql_db_dump test/unit/mysql_db_dump/dump_run.py
coverage run -a --source=mysql_db_dump test/unit/mysql_db_dump/help_message.py
coverage run -a --source=mysql_db_dump test/unit/mysql_db_dump/main.py
coverage run -a --source=mysql_db_dump test/unit/mysql_db_dump/run_program.py
coverage run -a --source=mysql_db_dump test/unit/mysql_db_dump/set_db_list.py

echo ""
echo "Producing code coverage report"
coverage combine
coverage report -m

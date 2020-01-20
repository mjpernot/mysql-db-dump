#!/bin/bash
# Unit testing program for the program module.
# This will run all the units tests for this program.
# Will need to run this from the base directory where the module file
#   is located at.

echo ""
echo "Unit testing..."
test/unit/mysql_db_dump/crt_dump_cmd.py
test/unit/mysql_db_dump/dump_db.py
test/unit/mysql_db_dump/dump_run.py
test/unit/mysql_db_dump/help_message.py
test/unit/mysql_db_dump/set_db_list.py

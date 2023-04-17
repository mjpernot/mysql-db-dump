#!/bin/bash
# Unit testing program for the program module.
# This will run all the units tests for this program.
# Will need to run this from the base directory where the module file
#   is located at.

echo ""
echo "Unit testing..."
/usr/bin/python test/unit/mysql_db_dump/add_ssl.py
/usr/bin/python test/unit/mysql_db_dump/add_tls.py
/usr/bin/python test/unit/mysql_db_dump/crt_dump_cmd.py
/usr/bin/python test/unit/mysql_db_dump/dump_db.py
/usr/bin/python test/unit/mysql_db_dump/dump_run.py
/usr/bin/python test/unit/mysql_db_dump/help_message.py
/usr/bin/python test/unit/mysql_db_dump/main.py
/usr/bin/python test/unit/mysql_db_dump/run_program.py
/usr/bin/python test/unit/mysql_db_dump/set_db_list.py

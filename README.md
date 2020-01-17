# Python project for dumping a database in a MySQL database.
# Classification (U)

# Description:
  This program is used to dump a database in a MySQL database to include dumping single and multiple databases, dump multiple databases to individual files or a single all-encompassing file.


###  This README file is broken down into the following sections:
  * Features
  * Prerequisites
  * Installation
  * Configuration
  * Program Help Function
  * Testing
    - Unit


# Features:
  * Dump single, multiple, or all databases in a MySQL server.
  * Dump databases to individual files or a single file.
  * Dump the database as a single transaction.
  * Compress database dump file.
  * Remove GTID entries from the dump file.

# Prerequisites:

  * List of Linux packages that need to be installed on the server.
    - python-libs
    - python-devel
    - git
    - python-pip

  * Local class/library dependencies within the program structure.
    - lib/cmds_gen
    - lib/arg_parser
    - lib/gen_libs
    - lib/gen_class
    - mysql_lib/mysql_libs
    - mysql_lib/mysql_class


# Installation:

Install the project using git.

```
umask 022
cd {Python_Project}
git clone git@sc.appdev.proj.coe.ic.gov:JAC-DSXD/mysql-db-dump.git
```

Install/upgrade system modules.

```
cd mysql-db-dump
umask 022
pip install -r requirements.txt --upgrade --trusted-host pypi.appdev.proj.coe.ic.gov
exit
```

Install supporting classes and libraries.

```
pip install -r requirements-python-lib.txt --target lib --trusted-host pypi.appdev.proj.coe.ic.gov
pip install -r requirements-mysql-lib.txt --target mysql_lib --trusted-host pypi.appdev.proj.coe.ic.gov
pip install -r requirements-python-lib.txt --target mysql_lib/lib --trusted-host pypi.appdev.proj.coe.ic.gov
```

# Configuration:
  * Replace **{Python_Project}** with the baseline path of the python program.

Create MySQL configuration file.

```
cd config
cp mysql_cfg.py.TEMPLATE mysql_cfg.py
```

Make the appropriate change to the environment.
  * Change these entries in the MySQL setup:
    - passwd = "ROOT_PASSWORD"
    - host = "SERVER_IP"
    - name = "HOST_NAME"
    - sid = SERVER_ID
    - extra_def_file = "{Python_Project}/config/mysql.cfg"

```
vim mysql_cfg.py
chmod 600 mysql_cfg.py
```

Create MySQL definition file.

```
cp mysql.cfg.TEMPLATE mysql.cfg
```

Make the appropriate change to the environment.
  * Change these entries in the MySQL definition file:
    - password="ROOT_PASSWORD"
    - socket={BASE_DIR}/mysql/tmp/mysql.sock

```
vim mysql.cfg
chmod 600 mysql.cfg
```


# Program Help Function:

  The program has a -h (Help option) that will show display an usage message.  The help message will usually consist of a description, usage, arugments to the program, example, notes about the program, and any known bugs not yet fixed.  To run the help command:
  * Replace **{Python_Project}** with the baseline path of the python program.

```
{Python_Project}/mysql-db-dump/mysql_db_dump.py -h
```


# Testing:


# Unit Testing:

### Description: Testing consists of unit testing for the functions in the mysql_db_dump.py program.

### Installation:

Install the project using git.
  * Replace **{Python_Project}** with the baseline path of the python program.
  * Replace **{Branch_Name}** with the name of the Git branch being tested.  See Git Merge Request.

```
umask 022
cd {Python_Project}
git clone --branch {Branch_Name} git@sc.appdev.proj.coe.ic.gov:JAC-DSXD/mysql-db-dump.git
```

Install/upgrade system modules.

```
cd mysql-db-dump
sudo bash
umask 022
pip install -r requirements.txt --upgrade --trusted-host pypi.appdev.proj.coe.ic.gov
exit
```

Install supporting classes and libraries.

```
pip install -r requirements-python-lib.txt --target lib --trusted-host pypi.appdev.proj.coe.ic.gov
pip install -r requirements-mysql-lib.txt --target mysql_lib --trusted-host pypi.appdev.proj.coe.ic.gov
pip install -r requirements-python-lib.txt --target mysql_lib/lib --trusted-host pypi.appdev.proj.coe.ic.gov
```


# Unit test runs for mysql_db_dump.py:
  * Replace **{Python_Project}** with the baseline path of the python program.

### Unit testing:
```
cd {Python_Project}/mysql-db-dump
test/unit/mysql_db_dump/help_message.py
test/unit/mysql_db_dump/main.py
test/unit/mysql_db_dump/run_program.py
```

### All unit testing
```
test/unit/mysql_db_dump/unit_test_run.sh
```

### Code coverage program
```
test/unit/mysql_db_dump/code_coverage.sh
```


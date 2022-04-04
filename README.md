# Python project for dumping a database in a MySQL database.
# Classification (U)

# Description:
  Dump a database in a MySQL database to include dumping single and multiple databases, dump multiple databases to individual files or dump all databases to a single all-encompassing file.


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
  * Redirect standard out error to a file and email.

# Prerequisites:

  * List of Linux packages that need to be installed on the server.
    - git
    - python-pip

  * Local class/library dependencies within the program structure.
    - python-lib
    - mysql-lib


# Installation:

Install the project using git.
  * From here on out, any reference to {Python_Project} or PYTHON_PROJECT replace with the baseline path of the python program.

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
pip install -r requirements-mysql-python-lib.txt --target mysql_lib/lib --trusted-host pypi.appdev.proj.coe.ic.gov
```

# Configuration:

Create MySQL configuration file.
Make the appropriate change to the environment.
  * Change these entries in the MySQL setup:
  * Note:  May have to set host to "localhost" to use sockets properly when using SSL connections.
    - user = "USER"
    - japd = "PSWORD"
    - host = "SERVER_IP"
    - name = "HOST_NAME"
    - sid = SERVER_ID
    - extra_def_file = "PYTHON_PROJECT/config/mysql.cfg"
    - cfg_file = "MYSQL_DIRECTORY/mysqld.cnf"

  * Change these entries only if required:
    - serv_os = "Linux"
    - port = 3306

  * If SSL connections are being used, configure one or more of these entries:
    - ssl_client_ca = None
    - ssl_client_key = None
    - ssl_client_cert = None

  * Only changes these if necessary and have knowledge in MySQL SSL configuration setup:
    - ssl_client_flag = None
    - ssl_disabled = False
    - ssl_verify_id = False
    - ssl_verify_cert = False

```
cd config
cp mysql_cfg.py.TEMPLATE mysql_cfg.py
vim mysql_cfg.py
chmod 600 mysql_cfg.py
```

Create MySQL definition file.
Make the appropriate change to the environment.
  * Change these entries in the MySQL definition file:
  * Note:  socket use is only required to be set in certain conditions when connecting using localhost.
    - password="PASSWORD"
    - socket=DIRECTORY_PATH/mysql.sock

```
cp mysql.cfg.TEMPLATE mysql.cfg
vim mysql.cfg
chmod 600 mysql.cfg
```


# Program Help Function:

  The program has a -h (Help option) that will show display an usage message.  The help message will usually consist of a description, usage, arugments to the program, example, notes about the program, and any known bugs not yet fixed.  To run the help command:

```
{Python_Project}/mysql-db-dump/mysql_db_dump.py -h
```


# Testing:

# Unit Testing:

### Installation:

Install the project using the procedures in the Installation section.

### Testing:

```
cd {Python_Project}/mysql-db-dump
test/unit/mysql_db_dump/unit_test_run.sh
```

### Code coverage:
```
cd {Python_Project}/mysql-db-dump
test/unit/mysql_db_dump/code_coverage.sh
```


# Python project for dumping a database in a MySQL database.
# Classification (U)

# Description:
  This program is used to dump a database in a MySQL database to include dumping single and multiple databases, dump multiple databases to individual files or a single all-encompassing file.


###  This README file is broken down into the following sections:
  * Features
  * Prerequisites
  * Installation
  * Configuration
  * Program Description
  * Program Help Function
  * Help Message
  * Testing
    - Unit
    - Integration
    - Blackbox


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


# Program Descriptions:
### Program: mysql_db_dump.py
##### Description: Administration program for the MySQL binary log system.


# Program Help Function:

  The program has a -h (Help option) that will show display an usage message.  The help message will usually consist of a description, usage, arugments to the program, example, notes about the program, and any known bugs not yet fixed.  To run the help command:
  * Replace **{Python_Project}** with the baseline path of the python program.

```
{Python_Project}/mysql-db-dump/mysql_db_dump.py -h
```


# Help Message:
  Below is the help message for the program the program.  Run the program with the -h option get the latest help message for the program.

    Program:  mysql_db_dump.py

    Description:  The mysql_db_dump program runs the mysqldump program against a
        MySQL database and dumps one or more databases to files.

    Usage:
        mysql_db_dump.py -c file -d path {-B db_name [db_name ...] |
            -A | -D} [-o name | -p path | -s | -z | -r] [-v | -h] 

    Arguments:
        -B databases => Database names, space delimited.
        -A => Dump all databases to individual files.
        -D => Dump all databases to a single dump file.
        -c file => Server configuration file.  Required arg.
        -d dir path => Directory path to config file (-c). Required arg.
        -o dir path => Directory path to dump directory.
        -p dir path => Directory path to mysql programs.  Only required
            if the mysql binary programs do not run properly.  (i.e. not
            in the $PATH variable.)
        -s => Run dump as a single transaction.
        -r => Remove GTID entries from dump file.
        -z => Compress database dump files
        -v => Display version of this program.
        -h => Help and usage message.

        NOTE 1:  -v or -h overrides the other options.
        NOTE 2:  -A, -B, and -D are XOR arguments.

    Notes:
        Database configuration file format (mysql_{host}.py):
            # Configuration file for {Database Name/Server}
            user = "root"
            passwd = "ROOT_PASSWORD"
            host = "IP_ADDRESS"
            serv_os = "Linux" or "Solaris"
            name = "HOSTNAME"
            port = PORT_NUMBER (default of mysql is 3306)
            cfg_file = "DIRECTORY_PATH/my.cfg"
            sid = "SERVER_ID"
            extra_def_file = "DIRECTORY_PATH/myextra.cfg"

        NOTE:  Include the cfg_file even if running remotely as the file will
            be used in future releases.

        configuration modules -> name is runtime dependent as it can be
            used to connect to different databases with different names.

        Defaults Extra File format (filename.cfg):
            [client]
            password="ROOT_PASSWORD"
            socket="DIRECTORY_PATH/mysql.sock"

        NOTE:  The socket information can be obtained from the my.cnf
            file under ~/mysql directory.

    Example:
        mysql_db_dump.py -A -c mysql -d config -z -s


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

```
cd {Python_Project}/mysql-db-dump
```

### Unit:  help_message
```
test/unit/mysql_db_dump/help_message.py
```

### Unit:  
```
test/unit/mysql_db_dump/
```

### Unit:  
```
test/unit/mysql_db_dump/
```

### Unit:  run_program
```
test/unit/mysql_db_dump/run_program.py
```

### Unit:  main
```
test/unit/mysql_db_dump/main.py
```

### All unit testing
```
test/unit/mysql_db_dump/unit_test_run.sh
```

### Code coverage program
```
test/unit/mysql_db_dump/code_coverage.sh
```


# Integration Testing:

### Description: Testing consists of integration testing of functions in the mysql_db_dump.py program.

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

### Configuration:
  * Replace **{Python_Project}** with the baseline path of the python program.

Create MySQL configuration file.
```
cd test/integration/mysql_db_dump/config
cp ../../../../config/mysql_cfg.py.TEMPLATE mysql_cfg.py
```

Make the appropriate change to the environment.
  * Change these entries in the MySQL setup.
    - passwd = "ROOT_PASSWORD"
    - host = "HOST_IP"
    - name = "HOSTNAME"
    - sid = SERVER_ID
    - extra_def_file = '{Python_Project}/config/mysql.cfg'

```
vim mysql_cfg.py
chmod 600 mysql_cfg.py
```

Create MySQL definition file.

```
cp ../../../../config/mysql.cfg.TEMPLATE mysql.cfg
```

Make the appropriate change to the MySQL definition setup.
  * Change these entries in the MySQL configuration file:
    - password="ROOT_PASSWORD"
    - socket={BASE_DIR}/mysql/tmp/mysql.sock

```
vim mysql.cfg
chmod 600 mysql.cfg
```


# Integration test runs for mysql_db_dump.py:
  * Replace **{Python_Project}** with the baseline path of the python program.

```
cd {Python_Project}/mysql-binlog
```

### Integration:  
```
test/integration/mysql_db_dump/
```

### All integration testing
```
test/integration/mysql_db_dump/integration_test_run.sh
```

### Code coverage program
```
test/integration/mysql_db_dump/code_coverage.sh
```


# Blackbox Testing:

### Description: Testing consists of blackbox testing of the mysql_db_dump.py program.

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

### Configuration:

Create MySQL configuration file.
  * Replace **{Python_Project}** with the baseline path of the python program.

```
cd test/blackbox/mysql_db_dump/config
cp ../../../../config/mysql_cfg.py.TEMPLATE mysql_cfg.py
```

Make the appropriate change to the environment.
  * Change these entries in the MySQL setup:
    - passwd = "ROOT_PASSWORD"
    - host = "HOST_IP"
    - name = "HOSTNAME"
    - sid = SERVER_ID
    - extra_def_file = '{Python_Project}/config/mysql.cfg'

```
vim mysql_cfg.py
chmod 600 mysql_cfg.py
```

Create MySQL definition file.

```
cp ../../../../config/mysql.cfg.TEMPLATE mysql.cfg
```

Make the appropriate change to the MySQL definition setup.
  * Change these entries in the MySQL configuration file:
    - password="ROOT_PASSWORD"
    - socket={BASE_DIR}/mysql/tmp/mysql.sock

```
vim mysql.cfg
chmod 600 mysql.cfg
```

# Blackbox test run for mysql_db_dump.py:
  * Replace **{Python_Project}** with the baseline path of the python program.

```
cd {Python_Project}/mysql-db-dump
```


### Blackbox:  
```
test/blackbox/mysql_db_dump/blackbox_test.sh
```


# Changelog
All notable changes to this project will be documented in this file.

The format is based on "Keep a Changelog".  This project adheres to Semantic Versioning.


## [4.0.1] - 2025-05-30
- Updated python-lib to v4.0.1
- Updated mysql-lib to v5.5.1
- Removed support for MySQL 5.6/5.7

### Changed
- Documentation changes.


## [4.0.0] - 2025-02-14
Breaking Changes

- Removed support for Python 2.7.
- Updated mysql-lib v5.4.0
- Updated python-lib v4.0.0

### Changed
- Documentation changes.

### Deprecated
- Support for MySQL 5.6/5.7


## [3.5.5] - 2024-11-18
- Updated python-lib to v3.0.8
- Updated mysql-lib to v5.3.9

### Fixed
- Set chardet==3.0.4 for Python 3.

### Deprecated
- Support for Python 2.7


## [3.5.4] - 2024-11-07
- Updated chardet==4.0.0 for Python 3
- Updated distro==1.9.0 for Python 3
- Updated mysql-connector-python==8.0.28 for Python 3
- Updated protobuf==3.19.6 for Python 3
- Updated python-lib to v3.0.7
- Updated mysql-lib to v5.3.8


## [3.5.3] - 2024-09-27
- Updated simplejson==3.13.2 for Python 3
- Updated python-lib to v3.0.5
- Updated mysql-lib to v5.3.7


## [3.5.2] - 2024-09-09

### Changed
- config/mysql_cfg.py.TEMPLATE:  Changed cfg_file default value.
- main: Removed parsing from gen_class.ArgParser call and called arg_parse2 as part of "if" statement.


## [3.5.1] - 2024-02-29
- Updated to work in Red Hat 8
- Updated python-lib to v3.0.3
- Updated mysql-lib to v5.3.4

### Changed
- main, dump_run: Removed gen_libs.get_inst call.
- Set simplejson to 3.12.0 for Python 3.
- Set chardet to 3.0.4 for Python 2.
- Documentation updates.


## [3.5.0] - 2023-03-15
- Replaced the use of arg_parser with gen_class.ArgParser class
- Upgraded python-lib to v2.10.1

### Changed
- Multiple functions: Replaced the use of arg_parser (args_array) with gen_class.ArgParser class (args).


## [3.4.4] - 2022-12-15
- Updated to work in Python 3 too
- Upgraded python-lib to v2.9.4
- Upgraded mysql-lib to v5.3.2
 
### Changed
- Converted imports to use Python 2.7 or Python 3.
- add_ssl: Converted dict keys() call to a list.
- dump_run: Changed open() to io.open().
 

## [3.4.3] - 2022-05-24
- Updated mysql-connector-python to v8.0.22
- Updated mysql-libs to v5.3.1

### Added
- add_tls: Add TLS option to the dump command line, if available.

### Changed
- run_program: Added call to add_tls function to add TLS versions to the dump command line.
- config/mysql_cfg.py.TEMPLATE: Added tls-version entry to allow for setting of TLS versions.
- Documentation updates.


## [3.4.2] - 2022-04-04
### Fixed
- Timestamps on files are not using 24-hour clock.  Updated gen_libs to v2.8.6.

### Changed
- crt_dump_cmd, dump_db: Replaced cmds_gen module with gen_libs module.

### Removed
- cmds_gen module


## [3.4.1] - 2021-06-22
### Fixed
- config/mysql_cfg.py.TEMPLATE:  Fixed ssl_mode entry format.


## [3.4.0] - 2021-06-15
- Updated to work in a SSL environment.
- Updated to use the mysql_libs v5.2.0 library.

### Added
- add_ssl:  Add SSL options to the dump command line.
- Added -l option to allow for the use of SSL connections.

### Changed
- run_program:  Call add_ssl to process SSL options if detected and added check not to run database dump command if SSL configuration is not setup correctly.
- config/mysql_cfg.py.TEMPLATE:  Added SSL options.


## [3.3.2] - 2021-05-04
- Updated to work in MySQL 8.0 environment.
- Updated to use the mysql_libs v5.1.0 library.
- Validated against MySQL 5.7 database.

### Changed
- run_program:  Capture and process status from connect method call.
- Removed \*\*kwargs from functions not using keyword arguments.
- config/mysql_cfg.py.TEMPLATE:  Updated to standard format.
- Documentation updates.


## [3.3.1] - 2021-04-27
### Added
- Added -u option to override postfix and use mailx command.

### Changed
- dump_db:  Set the use_mailx argument in the mail.send_mail command.
- main:  Added -u option to allow for mailx use.
- run_program:  Added use_mailx keyword argument to dump_db call.
- run_program:  Replaced cmds_gen.disconnect with mysql_libs.disconnect call.


## [3.3.0] - 2020-11-06
- Updated to use the mysql_libs v5.0.0 library.

### Fixed
- config/mysql.cfg.TEMPLATE:  Point to correct socket file.
- run_program:  Remove "-r" from command line if database not GTID enabled.

### Changed
- set_db_list:  Replace multiple returns with single return.
- run_program:  Changed default value of dmp_path to None.
- main:  Made "-o" a required argument for "-A", "-B", and "-D" options.
- config/mysql_cfg.py.TEMPLATE:  Changed entry name.
- Documentation updates.


## [3.2.0] - 2020-07-06
### Fixed
- main: Fixed handling command line arguments from SonarQube scan finding.

### Added
- Added email capability for error output.
- Added standard error out redirection -w option.

### Changed
- dump_db:  Add email capability for dumps error file.
- run_program:  Setup and configured email.
- main:  Added -e and -t options to parsing for email capability.
- dump_db, set_db_list:  Changed variable to standard naming convention.
- main:  Remove non-used argument in run_program call.
- dump_run:  Setup subprocess.Popen with stderr option and pass error file to the option.
- dump_db:  Set up and open error file if error suppression is passed.
- run_program: Parse the -w option.
- run_program: Refactored check on -z option in args_array.
- config/mysql.cfg.TEMPLATE:  Changed format of file.
- dump_run:  Replaced cmds_gen.run_prog with "with open" and "subprocess.Popen" code.
- Documentation updates.


## [3.1.0] - 2020-01-17
### Fixed
- dump_run, dump_db, set_db_list, run_program, crt_dump_cmd:  Fixed problem with mutable default arguments issue.

### Changed
- main:  Added program lock functionality to program.
- main:  Added new option -y to the program.
- set_db_list, run_program, crt_dump_cmd:  Changed variable name to standard convention.
- main:  Refactored and streamlined "if" statements.
- Added \*\*kwargs to those function parameter lists without the keyword argument capability.
- Documentation updates.


## [3.0.1] - 2018-12-06
### Changed
- Documentation updates.


## [3.0.0] - 2018-05-23
Breaking Change

### Changed
- Updated "mysql_libs", "cmds_gen", "gen_libs", and "arg_parser" calls to new naming schema.
- Changed function names from uppercase to lowercase.
- Setup single-source version control.


## [2.7.0] - 2018-05-11
### Changed
- Changed "server" to "mysql_class" module reference.
- Changed "commands" to "mysql_libs" module reference.

### Added
- Added single-source version control.


## [2.6.0] - 2017-08-18
### Changed
- Convert program to use local libraries from ./lib directory.
- Change single quotes to double quotes.
- Help_Message:  Replace docstring with printing the programs \_\_doc\_\_.


## [2.5.0] - 2016-12-19
### Changed
- Set_Db_List:  Modified -B section to handle multiple databases.  Replaced sys.exit() with empty list.
- Dump_DB:  Added elif to check for all-databases run and modified else to assume empty database list and there is nothing to dump or missing -D option.
- Run_Program:  Removed if statement and call Set_Db_List function regardlessly, also added \*\*kwargs to argument list to Set_Db_List call.
- main:  Added opt_multi_list variable.
- Added option for -B option to have multiple database names and also corrected an error if no option selected the program crashed trying to access the database name under -B option.


## [2.4.0] - 2016-10-19
### Changed
- Crt_Dump_Cmd:  Replaced prog_gen.Is_Add_Cmd with cmds_gen.Is_Add_Cmd and Replaced prog_gen.Add_Cmd with cmds_gen.Add_Cmd.
- Run_Program:  Determine if database list creation required.  Set the Servers class GTID mode.  Remove --set-gtid-purged for databases not GTID enabled.
- Dump_Db:  If database list is empty, then run dump command without database names.  Replaced prog_gen.Add_Cmd with cmds_gen.Add_Cmd.
- main:  Replaced Arg_Req_Xor with Arg_Xor_Dict and added -D option arguments to opt_dump_list variable.
- MySQL 5.6 (GTID Enabled) gives warning if a database is dumped with GTID entries.  Added two new options (-D and -r) to purge the GTID entries from the dump file and/or dump all of the databases to a single dump file and this will drop the warning message.

### Added
- Dump_Cmd function.


## [2.3.0] - 2016-10-18
### Changed
- main:  Changed -b to -B and -a to -A.
- Set_Db_List:  Changed -b to -B.
- Bring the main argument options in-line with the other programs.


## [2.2.0] - 2016-10-12
### Changed
- Run_Program:  Replaced Crt_Srv_Inst with Create_Instance to allow for --defaults-extra-file option.
- MySQL 5.6 now gives warning if password is passed on the command line.  To suppress this warning, will require the use of the --defaults-extra-file option.  This will require the use of updated commands library and server class files.  See in documentation above for exact version required for MySQL 5.6.


## [2.1.0] - 2016-09-13
### Changed
- Dump_Db:  Replaced my_prog.Append_Cmd with prog_gen.Add_Cmd.  Replaced my_prog.Run_Prog_2_File with prog_gen.Run_Prog.
- Crt_Dump_Cmd:  Replaced my_prog.Crt_Cmd with commands.Crt_Cmd.  Replaced my_prog.Append_Cmd with prog_gen.Add_Cmd.  Replaced my_prog.Is_Add_Cmd with prog_gen.Is_Add_Cmd.
- main:  Replaced Arg_Parse with Arg_Parse2, reorganized the main 'if' statements, and streamlined the check process.
- Set_Db_List:  Added connect and disconect commands to the database.


## [2.0.0] - 2015-12-04
### Changed
- Extensive updates to the program to modularize and streamline the program and also replace the current database connection mechanism with a class based database connection mechanism.


## [1.0.0] - 2015-10-08
- Initial creation.


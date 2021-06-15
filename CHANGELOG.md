# Changelog
All notable changes to this project will be documented in this file.

The format is based on "Keep a Changelog".  This project adheres to Semantic Versioning.


## [3.4.0] - 2021-06-15
- Updated to work in a SSL environment.
- Updated to use the mysql_libs v5.2.0 library.


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


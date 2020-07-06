#!/usr/bin/python
# Classification (U)

"""Program:  mysql_db_dump.py

    Description:  The mysql_db_dump program runs the mysqldump program against
        a MySQL database and dumps one or more databases to files.

    Usage:
        mysql_db_dump.py -c file -d path {-B db_name [db_name ...] |
            -A | -D} [-o name | -p path | -s | -z | -r] [-y flavor_id]
            [-v | -h]

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
        -z => Compress database dump files.
        -y value => A flavor id for the program lock.  To create unique lock.
        -v => Display version of this program.
        -h => Help and usage message.

        NOTE 1:  -v or -h overrides the other options.
        NOTE 2:  -A, -B, and -D are XOR arguments.

    Notes:
        Database configuration file format (mysql_cfg.py.TEMPLATE):
            # Configuration file for Database
            user = "root"
            passwd = "ROOT_PASSWORD"
            host = "IP_ADDRESS"
            serv_os = "Linux" or "Solaris"
            name = "HOSTNAME"
            port = PORT_NUMBER (default of mysql is 3306)
            cfg_file = "DIRECTORY_PATH/my.cfg"
            sid = "SERVER_ID"
            extra_def_file = "DIRECTORY_PATH/myextra.cfg"

        NOTE 1:  Include the cfg_file even if running remotely as the file will
            be used in future releases.

        NOTE 2:  In MySQL 5.6 - it now gives warning if password is passed on
            the command line.  To suppress this warning, will require the use
            of the --defaults-extra-file option (i.e. extra_def_file) in the
            database configuration file.  See below for the defaults-extra-file
            format.

        configuration modules -> name is runtime dependent as it can be
            used to connect to different databases with different names.

        Defaults Extra File format (mysql.cfg.TEMPLATE):
            [client]
            password="ROOT_PASSWORD"
            socket="DIRECTORY_PATH/mysql.sock"

        NOTE:  The socket information can be obtained from the my.cnf
            file under ~/mysql directory.

    Example:
        mysql_db_dump.py -A -c mysql -d config -z -s

"""

# Libraries and Global Variables

# Standard
import sys
import subprocess

# Local
import lib.arg_parser as arg_parser
import lib.gen_libs as gen_libs
import lib.gen_class as gen_class
import lib.cmds_gen as cmds_gen
import mysql_lib.mysql_class as mysql_class
import mysql_lib.mysql_libs as mysql_libs
import version

__version__ = version.__version__


def help_message():

    """Function:  help_message

    Description:  Displays the program's docstring which is the help and usage
        message when -h option is selected.

    Arguments:

    """

    print(__doc__)


def crt_dump_cmd(server, args_array, opt_arg_list, opt_dump_list, **kwargs):

    """Function:  crt_dump_cmd

    Description:  Create the database dump command line.

    Arguments:
        (input) server -> Database server instance.
        (input) args_array -> Array of command line options and values.
        (input) opt_arg_list -> List of commands to add to cmd line.
        (input) opt_dump_list -> Dictionary of additional options.
        (output) -> Database dump command line.

    """

    args_array = dict(args_array)
    opt_dump_list = dict(opt_dump_list)
    opt_arg_list = list(opt_arg_list)
    dump_args = mysql_libs.crt_cmd(
        server, arg_parser.arg_set_path(args_array, "-p") + "mysqldump")

    # Add arguments to dump command.
    for arg in opt_arg_list:
        dump_args = cmds_gen.add_cmd(dump_args, arg=arg)

    # Append additional options to command.
    return cmds_gen.is_add_cmd(args_array, dump_args, opt_dump_list)


def dump_run(dump_cmd, dmp_file, compress, **kwargs):

    """Function:  dump_run

    Description:  Run the database dump command, save to file, and compress.

    Arguments:
        (input) dump_cmd -> Database dump command line.
        (input) compress -> Compression flag.
        (input) dmp_file -> Dump file and path name.

    """

    dump_cmd = list(dump_cmd)

    with open(dmp_file, "wb") as f_name:
        proc1 = subprocess.Popen(dump_cmd, stdout=f_name, stderr=None)
        proc1.wait()

    if compress:
        gen_libs.compress(dmp_file)


def dump_db(dump_cmd, db_list, compress, dmp_path, **kwargs):

    """Function:  dump_db

    Description:  Runs the database dump command against one or more databases
        in the database list.  Will create a dump file for each database.

    Arguments:
        (input) dump_cmd -> Database dump command line.
        (input) db_list -> Array of database names.
        (input) compress -> Compression flag.
        (input) dmp_path -> Database dump output directory path.

    """

    dump_cmd = list(dump_cmd)
    db_list = list(db_list)

    if db_list:
        for db in db_list:
            dump_cmd = cmds_gen.add_cmd(dump_cmd, arg=db)
            dmp_file = gen_libs.crt_file_time(db, dmp_path, ".sql")
            dump_run(dump_cmd, dmp_file, compress)

            # Remove database name from command.
            dump_cmd.pop(len(dump_cmd) - 1)

    elif "--all-databases" in dump_cmd:
        dmp_file = gen_libs.crt_file_time("All_Databases", dmp_path, ".sql")
        dump_run(dump_cmd, dmp_file, compress)

    else:
        print("WARNING:  No databases to dump or missing -D option.")


def set_db_list(server, args_array, **kwargs):

    """Function:  set_db_list

    Description:  Get the database list and check if all databases or a single
        database is being selected.

    Arguments:
        (input) server -> Database server instance.
        (input) args_array -> Array of command line options and values.
        (output) -> Database list.

    """

    args_array = dict(args_array)
    db_list = gen_libs.dict_2_list(mysql_libs.fetch_db_dict(server),
                                   "Database")

    # Specified databases.
    if "-B" in args_array:

        # Difference of -B databases to database list.
        for db in set(args_array["-B"]) - set(db_list):
            print("Warning: Database(%s) does not exist." % (db))

        # Intersect of -B databases to database list.
        return list(set(args_array["-B"]) & set(db_list))

    # All databases.
    elif "-A" in args_array:
        return db_list

    # -D option or no option.
    else:
        return []


def run_program(args_array, opt_arg_list, opt_dump_list, **kwargs):

    """Function:  run_program

    Description:  Creates class instance(s) and controls flow of the program.

    Arguments:
        (input) args_array -> Array of command line options and values.
        (input) opt_arg_list -> List of commands to add to cmd line.
        (input) opt_dump_list -> Dictionary of additional options.

    """

    args_array = dict(args_array)
    opt_dump_list = dict(opt_dump_list)
    opt_arg_list = list(opt_arg_list)
    server = mysql_libs.create_instance(args_array["-c"], args_array["-d"],
                                        mysql_class.Server)
    server.connect()
    server.set_srv_gtid()
    dump_cmd = crt_dump_cmd(server, args_array, opt_arg_list, opt_dump_list)
    db_list = set_db_list(server, args_array, **kwargs)

    # Remove the -r option if database is not GTID enabled.
    if "-r" in args_array and not server.gtid_mode:
        dump_cmd.remove(opt_dump_list["-r"])

    compress = False

    if "-z" in args_array:
        compress = True

    dmp_path = "./"

    if "-o" in args_array:
        dmp_path = args_array["-o"] + "/"

    dump_db(dump_cmd, db_list, compress, dmp_path)
    cmds_gen.disconnect([server])


def main():

    """Function:  main

    Description:  Initializes program-wide used variables and processes command
        line arguments and values.

    Variables:
        dir_chk_list -> contains options which will be directories.
        dir_crt_list -> contain options that require directory to be created.
        opt_arg_list -> contains arguments to add to command line by default.
        opt_dump_list -> contains optional arguments to mysqldump.
        opt_multi_list -> contains the options that will have multiple values.
        opt_req_list -> contains the options that are required for the program.
        opt_val_list -> contains options which require values.
        opt_xor_dict -> contains options which are XOR with its values.

    Arguments:
        (input) argv -> Arguments from the command line.

    """

    dir_chk_list = ["-o", "-d", "-p"]
    dir_crt_list = ["-o"]

    # --ignore-table=mysql.event -> Skips dumping the event table.
    opt_arg_list = ["--ignore-table=mysql.event"]
    opt_dump_list = {"-s": "--single-transaction",
                     "-D": ["--all-databases", "--triggers", "--routines",
                            "--events"],
                     "-r": "--set-gtid-purged=OFF"}
    opt_multi_list = ["-B"]
    opt_req_list = ["-c", "-d"]
    opt_val_list = ["-B", "-c", "-d", "-o", "-p", "-y"]
    opt_xor_dict = {"-A": ["-B", "-D"], "-B": ["-A", "-D"], "-D": ["-A", "-B"]}

    # Process argument list from command line.
    args_array = arg_parser.arg_parse2(sys.argv, opt_val_list,
                                       multi_val=opt_multi_list)

    if not gen_libs.help_func(args_array, __version__, help_message) \
       and not arg_parser.arg_require(args_array, opt_req_list) \
       and arg_parser.arg_xor_dict(args_array, opt_xor_dict) \
       and not arg_parser.arg_dir_chk_crt(args_array, dir_chk_list,
                                          dir_crt_list):

        try:
            prog_lock = gen_class.ProgramLock(sys.argv,
                                              args_array.get("-y", ""))
            run_program(args_array, opt_arg_list, opt_dump_list,
                        multi_val=opt_multi_list)
            del prog_lock

        except gen_class.SingleInstanceException:
            print("WARNING:  Lock in place for mysql_db_dump with id: %s"
                  % (args_array.get("-y", "")))


if __name__ == "__main__":
    sys.exit(main())

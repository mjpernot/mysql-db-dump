#!/usr/bin/python
# Classification (U)

"""Program:  mysql_db_dump.py

    Description:  Runs the mysqldump program against a MySQL database and dumps
        one or more databases to file(s).

    Usage:
        mysql_db_dump.py -c file -d path
            {-B db_name [db_name ...] -o /path/name [-s] [-z] [-r] |
             -A -o /path/name [-s] [-z] [-r] |
             -D -o /path/name [-s] [-z] [-r] }
            [-p /path]  [-y flavor_id] [-w]
            [-e email {email2 email3 ...} {-t subject_line} [-u]]
            [-v | -h]

    Arguments:
        -c file => Server configuration file.  Required arg.
        -d dir path => Directory path to config file (-c). Required arg.
        -B databases => Database names, space delimited.
        -A => Dump all databases to individual files.
        -D => Dump all databases to a single dump file.
        -o dir path => Directory path to dump directory.
        -s => Run dump as a single transaction.
        -r => Remove GTID entries from dump file.
        -z => Compress database dump files.
        -p dir path => Directory path to mysql programs.  Only required
            if the mysql binary programs do not run properly.  (i.e. not
            in the $PATH variable.)
        -w => Redirect standard error out from the database dump command to an
            error file that will be co-located with the database dump file(s).
        -e email_address(es) => Send output to one or more email addresses.
            -t subject_line => Subject line of email.
            -u => Override the default mail command and use mailx.
        -y value => A flavor id for the program lock.  To create unique lock.
        -v => Display version of this program.
        -h => Help and usage message.

        NOTE 1:  -v or -h overrides the other options.
        NOTE 2:  -A, -B, and -D are XOR arguments.

    Notes:
        Database configuration file format (config/mysql_cfg.py.TEMPLATE):
            # Configuration file for Database
            user = "USER"
            japd = "PSWORD"
            host = "SERVER_IP"
            name = "HOST_NAME"
            sid = SERVER_ID
            extra_def_file = "PYTHON_PROJECT/config/mysql.cfg"
            serv_os = "Linux"
            port = 3306
            cfg_file = "MYSQL_DIRECTORY/mysqld.cnf"

        NOTE 1:  Include the cfg_file even if running remotely as the file will
            be used in future releases.
        NOTE 2:  In MySQL 5.6 - it now gives warning if password is passed on
            the command line.  To suppress this warning, will require the use
            of the --defaults-extra-file option (i.e. extra_def_file) in the
            database configuration file.  See below for the defaults-extra-file
            format.

        configuration modules -> name is runtime dependent as it can be
            used to connect to different databases with different names.

        Defaults Extra File format (config/mysql.cfg.TEMPLATE):
            [client]
            password="PASSWORD"
            socket=DIRECTORY_PATH/mysql.sock"

        NOTE:  The socket information can be obtained from the my.cnf
            file under ~/mysql directory.

    Example:
        mysql_db_dump.py -c mysql_cfg -d config -A -o /path/dumps -z -s

"""

# Libraries and Global Variables

# Standard
import sys
import subprocess
import datetime

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
        (input) **kwargs:
            errfile -> File handler for error file.

    """

    subp = gen_libs.get_inst(subprocess)
    dump_cmd = list(dump_cmd)
    e_file = kwargs.get("errfile", None)

    with open(dmp_file, "wb") as f_name:
        proc1 = subp.Popen(dump_cmd, stdout=f_name, stderr=e_file)
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
        (input) **kwargs:
            err_sup -> Suppression of standard error to standard out.
            mail -> Email class instance.

    """

    dump_cmd = list(dump_cmd)
    db_list = list(db_list)
    errfile = None

    if kwargs.get("err_sup", False):
        efile = gen_libs.crt_file_time("ErrOut", dmp_path, ".log")
        errfile = open(efile, "a")

    if db_list:
        for item in db_list:
            dump_cmd = cmds_gen.add_cmd(dump_cmd, arg=item)
            dmp_file = gen_libs.crt_file_time(item, dmp_path, ".sql")
            dump_run(dump_cmd, dmp_file, compress, errfile=errfile)

            # Remove database name from command.
            dump_cmd.pop(len(dump_cmd) - 1)

    elif "--all-databases" in dump_cmd:
        dmp_file = gen_libs.crt_file_time("All_Databases", dmp_path, ".sql")
        dump_run(dump_cmd, dmp_file, compress, errfile=errfile)

    else:
        print("WARNING:  No databases to dump or missing -D option.")

    if errfile:
        errfile.close()
        mail = kwargs.get("mail", None)

        if mail and not gen_libs.is_empty_file(efile):

            for line in gen_libs.file_2_list(efile):
                mail.add_2_msg(line)

            mail.send_mail()


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
    dump_list = []
    db_list = gen_libs.dict_2_list(mysql_libs.fetch_db_dict(server),
                                   "Database")

    # Specified databases.
    if "-B" in args_array:

        # Difference of -B databases to database list.
        for item in set(args_array["-B"]) - set(db_list):
            print("Warning: Database(%s) does not exist." % (item))

        # Intersect of -B databases to database list.
        dump_list = list(set(args_array["-B"]) & set(db_list))

    # All databases.
    elif "-A" in args_array:
        dump_list = list(db_list)

    return dump_list


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
    mail = None
    server = mysql_libs.create_instance(args_array["-c"], args_array["-d"],
                                        mysql_class.Server)
    server.connect()
    server.set_srv_gtid()
    dump_cmd = crt_dump_cmd(server, args_array, opt_arg_list, opt_dump_list)
    db_list = set_db_list(server, args_array, **kwargs)

    # Remove the -r option if database is not GTID enabled.
    if "-r" in args_array and not server.gtid_mode \
       and opt_dump_list["-r"] in dump_cmd:
        dump_cmd.remove(opt_dump_list["-r"])

    compress = args_array.get("-z", False)
    dmp_path = None

    if "-o" in args_array:
        dmp_path = args_array["-o"] + "/"

    if args_array.get("-e", False):
        dtg = datetime.datetime.strftime(datetime.datetime.now(),
                                         "%Y%m%d_%H%M%S")
        subj = args_array.get("-t", [server.name, ": mysql_db_dump: ", dtg])
        mail = gen_class.setup_mail(args_array.get("-e"), subj=subj)

    err_sup = args_array.get("-w", False)
    dump_db(dump_cmd, db_list, compress, dmp_path, err_sup=err_sup,
            mail=mail, use_mailx=args_array.get("-u", False))
    mysql_libs.disconnect(server)


def main():

    """Function:  main

    Description:  Initializes program-wide used variables and processes command
        line arguments and values.

    Variables:
        dir_chk_list -> contains options which will be directories.
        dir_crt_list -> contain options that require directory to be created.
        opt_arg_list -> contains arguments to add to command line by default.
        opt_con_req_dict -> contains options requiring other options.
        opt_dump_list -> contains optional arguments to mysqldump.
        opt_multi_list -> contains the options that will have multiple values.
        opt_req_list -> contains the options that are required for the program.
        opt_val_list -> contains options which require values.
        opt_xor_dict -> contains options which are XOR with its values.

    Arguments:
        (input) argv -> Arguments from the command line.

    """

    cmdline = gen_libs.get_inst(sys)
    dir_chk_list = ["-o", "-d", "-p"]
    dir_crt_list = ["-o"]

    # --ignore-table=mysql.event -> Skips dumping the event table.
    opt_arg_list = ["--ignore-table=mysql.event"]
    opt_con_req_dict = {"-t": ["-e"], "-A": ["-o"], "-B": ["-o"], "-D": ["-o"],
                        "-u": ["-e"]}
    opt_dump_list = {"-s": "--single-transaction",
                     "-D": ["--all-databases", "--triggers", "--routines",
                            "--events"],
                     "-r": "--set-gtid-purged=OFF"}
    opt_multi_list = ["-B", "-e", "-t"]
    opt_req_list = ["-c", "-d"]
    opt_val_list = ["-B", "-c", "-d", "-o", "-p", "-y", "-e", "-t"]
    opt_xor_dict = {"-A": ["-B", "-D"], "-B": ["-A", "-D"], "-D": ["-A", "-B"]}

    # Process argument list from command line.
    args_array = arg_parser.arg_parse2(cmdline.argv, opt_val_list,
                                       multi_val=opt_multi_list)

    if not gen_libs.help_func(args_array, __version__, help_message) \
       and not arg_parser.arg_require(args_array, opt_req_list) \
       and arg_parser.arg_xor_dict(args_array, opt_xor_dict) \
       and not arg_parser.arg_dir_chk_crt(args_array, dir_chk_list,
                                          dir_crt_list) \
       and arg_parser.arg_cond_req_or(args_array, opt_con_req_dict):

        try:
            prog_lock = gen_class.ProgramLock(cmdline.argv,
                                              args_array.get("-y", ""))
            run_program(args_array, opt_arg_list, opt_dump_list)
            del prog_lock

        except gen_class.SingleInstanceException:
            print("WARNING:  Lock in place for mysql_db_dump with id: %s"
                  % (args_array.get("-y", "")))


if __name__ == "__main__":
    sys.exit(main())

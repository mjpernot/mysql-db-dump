#!/usr/bin/python
# Classification (U)

"""Program:  mysql_db_dump.py

    Description:  Runs the mysqldump program against a MySQL database and dumps
        one or more databases to file(s).

    Usage:
        mysql_db_dump.py -c file -d path
            {-B db_name [db_name ...] -o /path/name [-s] [-z] [-r] [-w]
                [-e email {email2 email3 ...} {-t subject_line} [-u]]
                [-p dir_path] [-l] |
             -A -o /path/name [-s] [-z] [-r] [-w]
                [-e email {email2 email3 ...} {-t subject_line} [-u]]
                [-p dir_path] [-l] |
             -D -o /path/name [-s] [-z] [-r] [-w]
                [-e email {email2 email3 ...} {-t subject_line} [-u]]
                [-p dir_path] [-l]}
            [-y flavor_id]
            [-v | -h]

    Arguments:
        -c file => Server configuration file.  Required arg.
        -d dir path => Directory path to config file (-c). Required arg.

        -B databases [db_name ...] => Database names, space delimited.
            -o dir path => Directory path to dump directory.
            -s => Run dump as a single transaction.
            -r => Remove GTID entries from dump file.
            -z => Compress database dump files.
            -p dir_path => Directory path to mysql programs.  Only required
                if the mysql binary programs do not run properly.  (i.e. not
                in the $PATH variable.)
            -w => Redirect standard error out from the database dump command to
                an error file that will be co-located with the database dump
                file(s).
            -e email_address(es) => Send output to one or more email addresses.
                -t subject_line => Subject line of email.
                -u => Override the default mail command and use mailx.
            -l => Use SSL connection.

        -A => Dump all databases to individual files.
            -o dir path => Directory path to dump directory.
            -s => Run dump as a single transaction.
            -r => Remove GTID entries from dump file.
            -z => Compress database dump files.
            -p dir_path => Directory path to mysql programs.  Only required
                if the mysql binary programs do not run properly.  (i.e. not
                in the $PATH variable.)
            -w => Redirect standard error out from the database dump command to
                an error file that will be co-located with the database dump
                file(s).
            -e email_address(es) => Send output to one or more email addresses.
                -t subject_line => Subject line of email.
                -u => Override the default mail command and use mailx.
            -l => Use SSL connection.

        -D => Dump all databases to a single dump file.
            -o dir path => Directory path to dump directory.
            -s => Run dump as a single transaction.
            -r => Remove GTID entries from dump file.
            -z => Compress database dump files.
            -p dir_path => Directory path to mysql programs.  Only required
                if the mysql binary programs do not run properly.  (i.e. not
                in the $PATH variable.)
            -w => Redirect standard error out from the database dump command to
                an error file that will be co-located with the database dump
                file(s).
            -e email_address(es) => Send output to one or more email addresses.
                -t subject_line => Subject line of email.
                -u => Override the default mail command and use mailx.
            -l => Use SSL connection.

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

            # If SSL connections are being used, configure one or more of these
                entries:
            ssl_client_ca = "CAFilename"
            ssl_ca_path = "CAPath"
            ssl_client_key = "KeyFilename"
            ssl_client_cert = "CertFilename"
            ssl_mode = "PREFERRED"

            # Only changes these if necessary and have knowledge in MySQL
                SSL configuration setup:
            ssl_client_flag = None
            ssl_disabled = False
            ssl_verify_id = False
            ssl_verify_cert = False

            # TLS versions: Set the TLS versions allowed in the connection
            tls_versions = []

        NOTE 1:  Include the cfg_file even if running remotely as the file will
            be used in future releases.

        NOTE 2:  In MySQL 5.6 - it now gives warning if password is passed on
            the command line.  To suppress this warning, will require the use
            of the --defaults-extra-file option (i.e. extra_def_file) in the
            database configuration file.  See below for the defaults-extra-file
            format.

        NOTE 3:  Ignore the entries for replication login as this template is
            used for a variety of different MySQL programs.

        NOTE 4:  May have to set host to "localhost" to use sockets properly
            when using SSL connections.

        configuration modules -> name is runtime dependent as it can be
            used to connect to different databases with different names.

        Defaults Extra File format (config/mysql.cfg.TEMPLATE):
            [client]
            password="PASSWORD"
            socket=DIRECTORY_PATH/mysql.sock"

        NOTE 1:  The socket information can be obtained from the my.cnf
            file under ~/mysql directory.
        NOTE 2:  Socket use is only required to be set in certain conditions
            when connecting using localhost

    Example:
        mysql_db_dump.py -c mysql_cfg -d config -A -o /path/dumps -z -s

"""

# Libraries and Global Variables
from __future__ import print_function
from __future__ import absolute_import

# Standard
import sys
import subprocess
import datetime
import io

# Local
try:
    from .lib import arg_parser
    from .lib import gen_libs
    from .lib import gen_class
    from .mysql_lib import mysql_libs
    from .mysql_lib import mysql_class
    from . import version

except (ValueError, ImportError) as err:
    import lib.arg_parser as arg_parser
    import lib.gen_libs as gen_libs
    import lib.gen_class as gen_class
    import mysql_lib.mysql_libs as mysql_libs
    import mysql_lib.mysql_class as mysql_class
    import version

__version__ = version.__version__

# Global
SSL_ARG_DICT = {
    "ssl_client_ca": "--ssl-ca=", "ssl_ca_path": "--ssl-capath=",
    "ssl_client_key": "--ssl-key=", "ssl_client_cert": "--ssl-cert=",
    "ssl_mode": "--ssl-mode="}


def help_message():

    """Function:  help_message

    Description:  Displays the program's docstring which is the help and usage
        message when -h option is selected.

    Arguments:

    """

    print(__doc__)


def crt_dump_cmd(server, args, opt_arg_list, opt_dump_list):

    """Function:  crt_dump_cmd

    Description:  Create the database dump command line.

    Arguments:
        (input) server -> Database server instance
        (input) args -> ArgParser class instance
        (input) opt_arg_list -> List of commands to add to cmd line
        (input) opt_dump_list -> Dictionary of additional options
        (output) -> Database dump command line

    """

    opt_dump_list = dict(opt_dump_list)
    opt_arg_list = list(opt_arg_list)
    dump_args = mysql_libs.crt_cmd(
### STOPPED HERE - Need to fix arg_set_path before going forward.
        server, args.arg_set_path("-p") + "mysqldump")

    # Add arguments to dump command.
    for arg in opt_arg_list:
        dump_args = gen_libs.add_cmd(dump_args, arg=arg)

    # Append additional options to command.
    return gen_libs.is_add_cmd(args.get_args(), dump_args, opt_dump_list)


def dump_run(dump_cmd, dmp_file, compress, **kwargs):

    """Function:  dump_run

    Description:  Run the database dump command, save to file, and compress.

    Arguments:
        (input) dump_cmd -> Database dump command line
        (input) compress -> Compression flag
        (input) dmp_file -> Dump file and path name
        (input) **kwargs:
            errfile -> File handler for error file

    """

    subp = gen_libs.get_inst(subprocess)
    dump_cmd = list(dump_cmd)
    e_file = kwargs.get("errfile", None)

    with io.open(dmp_file, "wb") as f_name:
        proc1 = subp.Popen(dump_cmd, stdout=f_name, stderr=e_file)
        proc1.wait()

    if compress:
        gen_libs.compress(dmp_file)


def dump_db(dump_cmd, db_list, compress, dmp_path, **kwargs):

    """Function:  dump_db

    Description:  Runs the database dump command against one or more databases
        in the database list.  Will create a dump file for each database.

    Arguments:
        (input) dump_cmd -> Database dump command line
        (input) db_list -> Array of database names
        (input) compress -> Compression flag
        (input) dmp_path -> Database dump output directory path
        (input) **kwargs:
            err_sup -> Suppression of standard error to standard out
            mail -> Email class instance
            use_mailx -> True|False - Override postfix and use mailx

    """

    dump_cmd = list(dump_cmd)
    db_list = list(db_list)
    errfile = None

    if kwargs.get("err_sup", False):
        efile = gen_libs.crt_file_time("ErrOut", dmp_path, ".log")
        errfile = open(efile, "a")

    if db_list:
        for item in db_list:
            dump_cmd = gen_libs.add_cmd(dump_cmd, arg=item)
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

            mail.send_mail(use_mailx=kwargs.get("use_mailx", False))


def set_db_list(server, args):

    """Function:  set_db_list

    Description:  Get the database list and check if all databases or a single
        database is being selected.

    Arguments:
        (input) server -> Database server instance
        (input) args -> ArgParser class instance
        (output) -> Database list

    """

    dump_list = []
    db_list = gen_libs.dict_2_list(
        mysql_libs.fetch_db_dict(server), "Database")

    # Specified databases.
    if args.arg_exist("-B"):

        # Difference of -B databases to database list.
        for item in set(args.get_val("-B")) - set(db_list):
            print("Warning: Database(%s) does not exist." % (item))

        # Intersect of -B databases to database list.
        dump_list = list(set(args.get_val("-B")) & set(db_list))

    # All databases.
    elif args.arg_exist("-A"):
        dump_list = list(db_list)

    return dump_list


def add_ssl(cfg, dump_cmd):

    """Function:  add_ssl

    Description:  Add SSL options to the dump command line.

    Arguments:
        (input) cfg -> Configuration file module instance
        (input) dump_cmd -> Database dump command line
        (output) dump_cmd -> Database dump command line
        (output) status -> Status of SSL options
        (output) err_msg -> Error message for SSL options

    """

    global SSL_ARG_DICT

    dump_cmd = list(dump_cmd)
    status = True
    err_msg = None

    if hasattr(cfg, "ssl_client_ca") and hasattr(cfg, "ssl_client_key") \
       and hasattr(cfg, "ssl_client_cert"):

        if getattr(cfg, "ssl_client_ca") or (getattr(cfg, "ssl_client_key") and
                                             getattr(cfg, "ssl_client_cert")):

            data = [SSL_ARG_DICT[opt] + getattr(cfg, opt)
                    for opt in list(SSL_ARG_DICT.keys()) if getattr(cfg, opt)]
            dump_cmd.extend(data)

        else:
            status = False
            err_msg = "One or more values missing for required SSL settings."

    else:
        status = False
        err_msg = "Configuration file is missing SSL entries."

    return dump_cmd, status, err_msg


def add_tls(cfg, dump_cmd):

    """Function:  add_tls

    Description:  Add TLS option to the dump command line, if available.

    Arguments:
        (input) cfg -> Configuration file module instance
        (input) dump_cmd -> Database dump command line
        (output) dump_cmd -> Database dump command line

    """

    dump_cmd = list(dump_cmd)

    if hasattr(cfg, "tls_versions") and getattr(cfg, "tls_versions"):
        dump_cmd.append("--tls-version=" + str(getattr(cfg, "tls_versions")))

    return dump_cmd


def run_program(args, opt_arg_list, opt_dump_list, **kwargs):

    """Function:  run_program

    Description:  Creates class instance(s) and controls flow of the program.

    Arguments:
        (input) args -> ArgParser class instance
        (input) opt_arg_list -> List of commands to add to cmd line
        (input) opt_dump_list -> Dictionary of additional options

    """

    status = True
    err_msg = None
    opt_dump_list = dict(opt_dump_list)
    opt_arg_list = list(opt_arg_list)
    mail = None
    server = mysql_libs.create_instance(
        args.get_val("-c"), args.get_val("-d"), mysql_class.Server)
    server.connect(silent=True)

    if server.conn_msg:
        print("run_program:  Error encountered on server(%s):  %s" %
              (server.name, server.conn_msg))

    else:
        server.set_srv_gtid()
        dump_cmd = crt_dump_cmd(
            server, args, opt_arg_list, opt_dump_list)
        db_list = set_db_list(server, args, **kwargs)

        # Remove the -r option if database is not GTID enabled.
        if args.arg_exist("-r") and not server.gtid_mode \
           and opt_dump_list["-r"] in dump_cmd:
            dump_cmd.remove(opt_dump_list["-r"])

        compress = args.get_val("-z", def_val=False)
        dmp_path = None

        if args.arg_exist("-o"):
            dmp_path = args.get_val("-o") + "/"

        if args.get_val("-e", def_val=False):
            dtg = datetime.datetime.strftime(
                datetime.datetime.now(), "%Y%m%d_%H%M%S")
            subj = args.get_val(
                "-t", def_val=[server.name, ": mysql_db_dump: ", dtg])
            mail = gen_class.setup_mail(args.get_val("-e"), subj=subj)

        err_sup = args.get_val("-w", def_val=False)

        if args.arg_exist("-l"):
            cfg = gen_libs.load_module(args.get_val("-c"), args.get_val("-d"))
            dump_cmd, status, err_msg = add_ssl(cfg, dump_cmd)
            dump_cmd = add_tls(cfg, dump_cmd)

        if status:
            dump_db(dump_cmd, db_list, compress, dmp_path, err_sup=err_sup,
                    mail=mail, use_mailx=args.get_val("-u", def_val=False))

        else:
            print("run_program:  Error encountered with SSL setup: %s" %
                  (err_msg))

        mysql_libs.disconnect(server)


def main():

    """Function:  main

    Description:  Initializes program-wide used variables and processes command
        line arguments and values.

    Variables:
        dir_perms_chk -> contains options which will be directories and the
            octal permission settings
        dir_perms_crt -> contains options which require directories to be
            created along with their octal permission settings
        multi_val -> contains the options that will have multiple values
        opt_arg_list -> contains arguments to add to command line by default
        opt_con_req_dict -> contains options requiring other options
        opt_dump_list -> contains optional arguments to mysqldump
        opt_req_list -> contains the options that are required for the program
        opt_val -> contains options which require values
        opt_xor_dict -> contains options which are XOR with its values

    Arguments:
        (input) argv -> Arguments from the command line

    """

    cmdline = gen_libs.get_inst(sys)
    dir_perms_chk = {"-d": 5, "-p": 5}
    dir_perms_crt = {"-o": 6}
    multi_val = ["-B", "-e", "-t"]
    # --ignore-table=mysql.event -> Skips dumping the event table.
    opt_arg_list = ["--ignore-table=mysql.event"]
    opt_con_req_dict = {
        "-t": ["-e"], "-A": ["-o"], "-B": ["-o"], "-D": ["-o"], "-u": ["-e"]}
    opt_dump_list = {
        "-s": "--single-transaction",
        "-D": ["--all-databases", "--triggers", "--routines", "--events"],
        "-r": "--set-gtid-purged=OFF"}
    opt_req_list = ["-c", "-d"]
    opt_val = ["-B", "-c", "-d", "-o", "-p", "-y", "-e", "-t"]
    opt_xor_dict = {"-A": ["-B", "-D"], "-B": ["-A", "-D"], "-D": ["-A", "-B"]}

    # Process argument list from command line.
    args = gen_class.ArgParser(
        cmdline.argv, opt_val=opt_val, multi_val=multi_val, do_parse=True)

    if not gen_libs.help_func(args.get_args(), __version__, help_message)   \
       and args.arg_require(opt_req=opt_req_list)                           \
       and args.arg_xor_dict(opt_xor_val=opt_xor_dict)                      \
       and args.arg_dir_chk(dir_perms_chk=dir_perms_chk)                    \
       and args.arg_dir_crt(dir_chk=dir_perms_crt, dir_crt=dir_perms_crt)   \
       and args.arg_cond_req_or(opt_con_or=opt_con_req_dict):

        try:
            prog_lock = gen_class.ProgramLock(
                cmdline.argv, args.get_val("-y", def_val=""))
            run_program(args, opt_arg_list, opt_dump_list)
            del prog_lock

        except gen_class.SingleInstanceException:
            print("WARNING:  Lock in place for mysql_db_dump with id: %s"
                  % (args.get_val("-y", def_val="")))


if __name__ == "__main__":
    sys.exit(main())

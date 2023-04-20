# Classification (U)

"""Program:  crt_dump_cmd.py

    Description:  Unit testing of crt_dump_cmd in mysql_db_dump.py.

    Usage:
        test/unit/mysql_db_dump/crt_dump_cmd.py

    Arguments:

"""

# Libraries and Global Variables

# Standard
import sys
import os
import unittest

# Local
sys.path.append(os.getcwd())
import mysql_db_dump
import version

__version__ = version.__version__


class ArgParser(object):

    """Class:  ArgParser

    Description:  Class stub holder for gen_class.ArgParser class.

    Methods:
        __init__
        arg_set_path
        get_args

    """

    def __init__(self):

        """Method:  __init__

        Description:  Class initialization.

        Arguments:

        """

        self.args_array = {"-c": "mysql_cfg", "-d": "config"}

    def arg_set_path(self, arg_opt, **kwargs):

        """Method:  arg_set_path

        Description:  Method stub holder for gen_class.ArgParser.arg_set_path.

        Arguments:

        """

        return os.path.join(
            self.args_array[arg_opt] if arg_opt in self.args_array else "",
            kwargs.get("cmd", ""))

    def get_args(self):

        """Method:  get_args

        Description:  Method stub holder for gen_class.ArgParser.get_args.

        Arguments:

        """

        return self.args_array


class Server(object):

    """Class:  Server

    Description:  Class stub holder for mysql_class.Server class.

    Methods:
        __init__

    """

    def __init__(self):

        """Method:  __init__

        Description:  Class initialization.

        Arguments:

        """

        self.extra_def_file = None
        self.sql_user = "mysql"
        self.sql_pass = "pswd"
        self.host = "hostname"
        self.port = 3306


class UnitTest(unittest.TestCase):

    """Class:  UnitTest

    Description:  Class which is a representation of a unit testing.

    Methods:
        setUp
        test_multiple_opt_arg_list
        test_empty_opt_arg_list
        test_p_option2
        test_p_option
        test_crt_dump_cmd

    """

    def setUp(self):

        """Function:  setUp

        Description:  Initialization for unit testing.

        Arguments:

        """

        self.args = ArgParser()
        self.ign_tbl = "--ignore-table=mysql.event"
        self.mydump = "/opt/local/mysqldump"
        self.server = Server()
        self.args_array = {"-p": "/opt/local"}
        self.args_array2 = {"-p": "/opt/local/"}
        self.opt_arg_list = [self.ign_tbl]
        self.opt_arg_list2 = [self.ign_tbl, "--skip-system"]
        self.opt_dump_list = {
            "-s": "--single-transaction", "-D": [
                "--all-databases", "--triggers", "--routines", "--events"],
            "-r": "--set-gtid-purged=OFF"}
        self.results = ["mysqldump", "-u", "mysql", "-ppswd", "-h",
                        "hostname", "-P", "3306", self.ign_tbl]
        self.results2 = [self.mydump, "-u", "mysql", "-ppswd", "-h",
                         "hostname", "-P", "3306", self.ign_tbl]
        self.results3 = [self.mydump, "-u", "mysql", "-ppswd", "-h",
                         "hostname", "-P", "3306"]
        self.results4 = [
            self.mydump, "-u", "mysql", "-ppswd", "-h", "hostname", "-P",
            "3306", self.ign_tbl, "--skip-system"]

    def test_multiple_opt_arg_list(self):

        """Function:  test_multiple_opt_arg_list

        Description:  Test with multiple entries in list.

        Arguments:

        """

        self.args.args_array = self.args_array

        self.assertEqual(
            mysql_db_dump.crt_dump_cmd(
                self.server, self.args, self.opt_arg_list2,
                self.opt_dump_list), self.results4)

    def test_empty_opt_arg_list(self):

        """Function:  test_empty_opt_arg_list

        Description:  Test with empty opt_arg_list list.

        Arguments:

        """

        self.args.args_array = self.args_array

        self.assertEqual(
            mysql_db_dump.crt_dump_cmd(
                self.server, self.args, [], self.opt_dump_list), self.results3)

    def test_p_option2(self):

        """Function:  test_p_option2

        Description:  Test with -p option passed with ending slash.

        Arguments:

        """

        self.args.args_array = self.args_array2

        self.assertEqual(
            mysql_db_dump.crt_dump_cmd(
                self.server, self.args, self.opt_arg_list, self.opt_dump_list),
            self.results2)

    def test_p_option(self):

        """Function:  test_p_option

        Description:  Test with -p option passed.

        Arguments:

        """

        self.args.args_array = self.args_array

        self.assertEqual(
            mysql_db_dump.crt_dump_cmd(
                self.server, self.args, self.opt_arg_list, self.opt_dump_list),
            self.results2)

    def test_crt_dump_cmd(self):

        """Function:  test_crt_dump_cmd

        Description:  Test with only default arguments passed.

        Arguments:

        """

        self.args.args_array = []

        self.assertEqual(
            mysql_db_dump.crt_dump_cmd(
                self.server, self.args, self.opt_arg_list, self.opt_dump_list),
            self.results)


if __name__ == "__main__":
    unittest.main()

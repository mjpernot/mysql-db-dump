# Classification (U)

"""Program:  set_db_list.py

    Description:  Unit testing of set_db_list in mysql_db_dump.py.

    Usage:
        test/unit/mysql_db_dump/set_db_list.py

    Arguments:

"""

# Libraries and Global Variables

# Standard
import sys
import os
import unittest
import mock

# Local
sys.path.append(os.getcwd())
import mysql_db_dump
import lib.gen_libs as gen_libs
import version

__version__ = version.__version__


class ArgParser(object):

    """Class:  ArgParser

    Description:  Class stub holder for gen_class.ArgParser class.

    Methods:
        __init__
        arg_exist
        get_val

    """

    def __init__(self):

        """Method:  __init__

        Description:  Class initialization.

        Arguments:

        """

        self.args_array = {"-c": "mysql_cfg", "-d": "config"}

    def arg_exist(self, arg):

        """Method:  arg_exist

        Description:  Method stub holder for gen_class.ArgParser.arg_exist.

        Arguments:

        """

        return True if arg in self.args_array else False

    def get_val(self, skey, def_val=None):

        """Method:  get_val

        Description:  Method stub holder for gen_class.ArgParser.get_val.

        Arguments:

        """

        return self.args_array.get(skey, def_val)


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
        test_b_option_none2
        test_b_option_none
        test_b_option_some2
        test_b_option_some
        test_b_option_all
        test_a_option
        test_d_option
        test_set_db_list

    """

    def setUp(self):

        """Function:  setUp

        Description:  Initialization for unit testing.

        Arguments:

        """

        self.server = Server()
        self.args = ArgParser()
        self.local = "/opt/local"
        self.db_list = ["db1", "db2", "db3"]
        self.db_list2 = ["db1", "db3"]
        self.db_list3 = ["db4", "db5"]
        self.args_array = {"-p": self.local}
        self.args_array2 = {"-p": self.local, "-D": True}
        self.args_array3 = {"-p": self.local, "-A": True}
        self.args_array4 = {"-p": self.local, "-B": self.db_list}
        self.args_array5 = {"-p": self.local, "-B": self.db_list2}
        self.args_array6 = {"-p": self.local, "-B": self.db_list}
        self.args_array7 = {"-p": self.local, "-B": self.db_list3}
        self.results = []

    @mock.patch("mysql_db_dump.mysql_libs.fetch_db_dict",
                mock.Mock(return_value=True))
    @mock.patch("mysql_db_dump.gen_libs.dict_2_list")
    def test_b_option_none2(self, mock_list):

        """Function:  test_b_option_none2

        Description:  Test with the -B option with no databases.

        Arguments:

        """

        self.args.args_array = self.args_array4

        mock_list.return_value = self.db_list3

        with gen_libs.no_std_out():
            results = mysql_db_dump.set_db_list(self.server, self.args)

        results.sort()
        self.assertEqual(results, self.results)

    @mock.patch("mysql_db_dump.mysql_libs.fetch_db_dict",
                mock.Mock(return_value=True))
    @mock.patch("mysql_db_dump.gen_libs.dict_2_list")
    def test_b_option_none(self, mock_list):

        """Function:  test_b_option_none

        Description:  Test with the -B option with no databases.

        Arguments:

        """

        self.args.args_array = self.args_array7

        mock_list.return_value = self.db_list

        with gen_libs.no_std_out():
            results = mysql_db_dump.set_db_list(self.server, self.args)

        results.sort()
        self.assertEqual(results, self.results)

    @mock.patch("mysql_db_dump.mysql_libs.fetch_db_dict",
                mock.Mock(return_value=True))
    @mock.patch("mysql_db_dump.gen_libs.dict_2_list")
    def test_b_option_some2(self, mock_list):

        """Function:  test_b_option_some2

        Description:  Test with the -B option with some databases.

        Arguments:

        """

        self.args.args_array = self.args_array6

        mock_list.return_value = self.db_list2

        self.db_list2.sort()

        with gen_libs.no_std_out():
            results = mysql_db_dump.set_db_list(self.server, self.args)

        results.sort()
        self.assertEqual(results, self.db_list2)

    @mock.patch("mysql_db_dump.mysql_libs.fetch_db_dict",
                mock.Mock(return_value=True))
    @mock.patch("mysql_db_dump.gen_libs.dict_2_list")
    def test_b_option_some(self, mock_list):

        """Function:  test_b_option_some

        Description:  Test with the -B option with some databases.

        Arguments:

        """

        self.args.args_array = self.args_array5

        mock_list.return_value = self.db_list

        self.db_list2.sort()
        results = mysql_db_dump.set_db_list(self.server, self.args)
        results.sort()
        self.assertEqual(results, self.db_list2)

    @mock.patch("mysql_db_dump.mysql_libs.fetch_db_dict",
                mock.Mock(return_value=True))
    @mock.patch("mysql_db_dump.gen_libs.dict_2_list")
    def test_b_option_all(self, mock_list):

        """Function:  test_b_option_all

        Description:  Test with the -B option with all databases.

        Arguments:

        """

        self.args.args_array = self.args_array4

        mock_list.return_value = self.db_list

        self.db_list.sort()
        results = mysql_db_dump.set_db_list(self.server, self.args)
        results.sort()
        self.assertEqual(results, self.db_list)

    @mock.patch("mysql_db_dump.mysql_libs.fetch_db_dict",
                mock.Mock(return_value=True))
    @mock.patch("mysql_db_dump.gen_libs.dict_2_list")
    def test_a_option(self, mock_list):

        """Function:  test_a_option

        Description:  Test with the -A option.

        Arguments:

        """

        self.args.args_array = self.args_array3

        mock_list.return_value = self.db_list

        self.db_list.sort()
        results = mysql_db_dump.set_db_list(self.server, self.args)
        results.sort()
        self.assertEqual(results, self.db_list)

    @mock.patch("mysql_db_dump.mysql_libs.fetch_db_dict",
                mock.Mock(return_value=True))
    @mock.patch("mysql_db_dump.gen_libs.dict_2_list")
    def test_d_option(self, mock_list):

        """Function:  test_d_option

        Description:  Test with the -D option.

        Arguments:

        """

        self.args.args_array = self.args_array2

        mock_list.return_value = self.db_list

        self.assertEqual(
            mysql_db_dump.set_db_list(self.server, self.args), self.results)

    @mock.patch("mysql_db_dump.mysql_libs.fetch_db_dict",
                mock.Mock(return_value=True))
    @mock.patch("mysql_db_dump.gen_libs.dict_2_list")
    def test_set_db_list(self, mock_list):

        """Function:  test_set_db_list

        Description:  Test with only default arguments passed.

        Arguments:

        """

        self.args.args_array = self.args_array

        mock_list.return_value = self.db_list

        self.assertEqual(
            mysql_db_dump.set_db_list(self.server, self.args), self.results)


if __name__ == "__main__":
    unittest.main()

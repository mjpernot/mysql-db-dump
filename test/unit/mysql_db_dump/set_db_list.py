#!/usr/bin/python
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

if sys.version_info < (2, 7):
    import unittest2 as unittest
else:
    import unittest

# Third-party
import mock

# Local
sys.path.append(os.getcwd())
import mysql_db_dump
import lib.gen_libs as gen_libs
import version

__version__ = version.__version__


class Server(object):

    """Class:  Server

    Description:  Class stub holder for mysql_class.Server class.

    Methods:
        __init__ -> Class initialization.

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
        setUp -> Initialize testing environment.
        test_b_option_none2 -> Test with the -B option with no databases.
        test_b_option_none -> Test with the -B option with no databases.
        test_b_option_some2 -> Test with the -B option with some databases.
        test_b_option_some -> Test with the -B option with some databases.
        test_b_option_all -> Test with the -B option with all databases.
        test_a_option -> Test with the -A option.
        test_d_option -> Test with the -D option.
        test_set_db_list -> Test with only default arguments passed.

    """

    def setUp(self):

        """Function:  setUp

        Description:  Initialization for unit testing.

        Arguments:

        """

        self.server = Server()
        self.db_list = ["db1", "db2", "db3"]
        self.db_list2 = ["db1", "db3"]
        self.db_list3 = ["db4", "db5"]
        self.args_array = {"-p": "/opt/local"}
        self.args_array2 = {"-p": "/opt/local", "-D": True}
        self.args_array3 = {"-p": "/opt/local", "-A": True}
        self.args_array4 = {"-p": "/opt/local", "-B": self.db_list}
        self.args_array5 = {"-p": "/opt/local", "-B": self.db_list2}
        self.args_array6 = {"-p": "/opt/local", "-B": self.db_list}
        self.args_array7 = {"-p": "/opt/local", "-B": self.db_list3}
        self.results = []

    @mock.patch("mysql_db_dump.mysql_libs.fetch_db_dict",
                mock.Mock(return_value=True))
    @mock.patch("mysql_db_dump.gen_libs.dict_2_list")
    def test_b_option_none2(self, mock_list):

        """Function:  test_b_option_none2

        Description:  Test with the -B option with no databases.

        Arguments:

        """

        mock_list.return_value = self.db_list3

        with gen_libs.no_std_out():
            results = mysql_db_dump.set_db_list(self.server, self.args_array4)

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

        mock_list.return_value = self.db_list

        with gen_libs.no_std_out():
            results = mysql_db_dump.set_db_list(self.server, self.args_array7)

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

        mock_list.return_value = self.db_list2

        self.db_list2.sort()

        with gen_libs.no_std_out():
            results = mysql_db_dump.set_db_list(self.server, self.args_array6)

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

        mock_list.return_value = self.db_list

        self.db_list2.sort()
        results = mysql_db_dump.set_db_list(self.server, self.args_array5)
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

        mock_list.return_value = self.db_list

        self.db_list.sort()
        results = mysql_db_dump.set_db_list(self.server, self.args_array4)
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

        mock_list.return_value = self.db_list

        self.assertEqual(mysql_db_dump.set_db_list(
            self.server, self.args_array3), self.db_list)

    @mock.patch("mysql_db_dump.mysql_libs.fetch_db_dict",
                mock.Mock(return_value=True))
    @mock.patch("mysql_db_dump.gen_libs.dict_2_list")
    def test_d_option(self, mock_list):

        """Function:  test_d_option

        Description:  Test with the -D option.

        Arguments:

        """

        mock_list.return_value = self.db_list

        self.assertEqual(mysql_db_dump.set_db_list(
            self.server, self.args_array2), self.results)

    @mock.patch("mysql_db_dump.mysql_libs.fetch_db_dict",
                mock.Mock(return_value=True))
    @mock.patch("mysql_db_dump.gen_libs.dict_2_list")
    def test_set_db_list(self, mock_list):

        """Function:  test_set_db_list

        Description:  Test with only default arguments passed.

        Arguments:

        """

        mock_list.return_value = self.db_list

        self.assertEqual(mysql_db_dump.set_db_list(
            self.server, self.args_array), self.results)


if __name__ == "__main__":
    unittest.main()

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
        test_set_db_list -> Test with only default arguments passed.

    """

    def setUp(self):

        """Function:  setUp

        Description:  Initialization for unit testing.

        Arguments:

        """

        self.server = Server()
        self.args_array = {"-p": "/opt/local"}
        self.db_list = ["db1", "db2", "db3"]
        self.results = []

    @mock.patch("mysql_db_dump.gen_libs.dict_2_list")
    def test_set_db_list(self,  mock_list):

        """Function:  test_set_db_list

        Description:  Test with only default arguments passed.

        Arguments:

        """

        mock_list.return_value = self.db_list

        self.assertEqual(mysql_db_dump.set_db_list(
            self.server, self.args_array), self.results)


if __name__ == "__main__":
    unittest.main()

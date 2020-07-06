#!/usr/bin/python
# Classification (U)

"""Program:  dump_db.py

    Description:  Unit testing of dump_db in mysql_db_dump.py.

    Usage:
        test/unit/mysql_db_dump/dump_db.py

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


class UnitTest(unittest.TestCase):

    """Class:  UnitTest

    Description:  Class which is a representation of a unit testing.

    Methods:
        setUp -> Initialize testing environment.
        test_db_list_w_option -> Test with -w option with list of databases.
        test_all_dbs_w_option -> Test with -z option with all databases.
        test_db_list2 -> Test with list of databases.
        test_db_list -> Test with list of databases.
        test_all_dbs -> Test with all databases.
        test_dump_db -> Test with only default arguments passed.

    """

    def setUp(self):

        """Function:  setUp

        Description:  Initialization for unit testing.

        Arguments:

        """

        self.dump_cmd = ["dump_command", "params"]
        self.dump_cmd2 = ["--all-databases"]
        self.db_list = []
        self.db_list2 = ["db1"]
        self.db_list3 = ["db1", "db2"]
        self.dmp_file = "/dir/path/dump_file.dmp"
        self.err_sup = True

    @mock.patch("mysql_db_dump.dump_run", mock.Mock(return_value=True))
    def test_db_list_w_option(self):

        """Function:  test_db_list_w_option

        Description:  Test with -w option with list of databases.

        Arguments:

        """

        self.assertFalse(mysql_db_dump.dump_db(
            self.dump_cmd, self.db_list2, False, self.dmp_file,
            err_sup=self.err_sup))

    @mock.patch("mysql_db_dump.dump_run", mock.Mock(return_value=True))
    def test_all_dbs_w_option(self):

        """Function:  test_all_dbs_w_option

        Description:  Test with -z option with all databases.

        Arguments:

        """

        self.assertFalse(mysql_db_dump.dump_db(
            self.dump_cmd2, self.db_list, False, self.dmp_file,
            err_sup=self.err_sup))

    @mock.patch("mysql_db_dump.dump_run", mock.Mock(return_value=True))
    def test_db_list2(self):

        """Function:  test_db_list2

        Description:  Test with list of databases.

        Arguments:

        """

        self.assertFalse(mysql_db_dump.dump_db(self.dump_cmd, self.db_list3,
                                               False, self.dmp_file))

    @mock.patch("mysql_db_dump.dump_run", mock.Mock(return_value=True))
    def test_db_list(self):

        """Function:  test_db_list

        Description:  Test with list of databases.

        Arguments:

        """

        self.assertFalse(mysql_db_dump.dump_db(self.dump_cmd, self.db_list2,
                                               False, self.dmp_file))

    @mock.patch("mysql_db_dump.dump_run", mock.Mock(return_value=True))
    def test_all_dbs(self):

        """Function:  test_all_dbs

        Description:  Test with all databases.

        Arguments:

        """

        self.assertFalse(mysql_db_dump.dump_db(self.dump_cmd2, self.db_list,
                                               False, self.dmp_file))

    def test_dump_db(self):

        """Function:  test_dump_db

        Description:  Test with only default arguments passed.

        Arguments:

        """

        with gen_libs.no_std_out():
            self.assertFalse(mysql_db_dump.dump_db(self.dump_cmd, self.db_list,
                                                   False, self.dmp_file))


if __name__ == "__main__":
    unittest.main()

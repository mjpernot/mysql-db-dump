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
        test_dump_db -> Test with only default arguments passed.

    """

    def setUp(self):

        """Function:  setUp

        Description:  Initialization for unit testing.

        Arguments:

        """

        self.dump_cmd = []
        self.db_list = []
        self.dmp_path = "/dir/path/dump_file.dmp"

    @mock.patch("mysql_db_dump.cmds_gen.run_prog",
                mock.Mock(return_value=True))
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

#!/usr/bin/python
# Classification (U)

"""Program:  dump_run.py

    Description:  Unit testing of dump_run in mysql_db_dump.py.

    Usage:
        test/unit/mysql_db_dump/dump_run.py

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
        test_compress_true -> Test with compression set to True.
        test_compress_false -> Test with compression set to False.
        test_dump_run -> Test with only default arguments passed.

    """

    def setUp(self):

        """Function:  setUp

        Description:  Initialization for unit testing.

        Arguments:

        """

        self.dump_cmd = []
        self.dmp_file = "/dir/path/dump_file.dmp"

    @mock.patch("mysql_db_dump.gen_libs.compress",
                mock.Mock(return_value=True))
    @mock.patch("mysql_db_dump.cmds_gen.run_prog",
                mock.Mock(return_value=True))
    def test_compress_true(self):

        """Function:  test_compress_true

        Description:  Test with compression set to True.

        Arguments:

        """

        self.assertFalse(mysql_db_dump.dump_run(self.dump_cmd, self.dmp_file,
                                                True))

    @mock.patch("mysql_db_dump.cmds_gen.run_prog",
                mock.Mock(return_value=True))
    def test_compress_false(self):

        """Function:  test_compress_false

        Description:  Test with compression set to False.

        Arguments:

        """

        self.assertFalse(mysql_db_dump.dump_run(self.dump_cmd, self.dmp_file,
                                                False))

    @mock.patch("mysql_db_dump.cmds_gen.run_prog",
                mock.Mock(return_value=True))
    def test_dump_run(self):

        """Function:  test_dump_run

        Description:  Test with only default arguments passed.

        Arguments:

        """

        self.assertFalse(mysql_db_dump.dump_run(self.dump_cmd, self.dmp_file,
                                                False))


if __name__ == "__main__":
    unittest.main()

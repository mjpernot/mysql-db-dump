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
import unittest
import mock

# Local
sys.path.append(os.getcwd())
import mysql_db_dump                            # pylint:disable=E0401,C0413
import version                                  # pylint:disable=E0401,C0413

__version__ = version.__version__


class SubProcess():                                     # pylint:disable=R0903

    """Class:  SubProcess

    Description:  Class which is a representation of the subprocess class.

    Methods:
        __init__
        wait

    """

    def __init__(self):

        """Method:  __init__

        Description:  Initialization instance of the ZipFile class.

        Arguments:

        """

    def wait(self):

        """Method:  wait

        Description:  Mock representation of subprocess.wait method.

        Arguments:

        """


class UnitTest(unittest.TestCase):

    """Class:  UnitTest

    Description:  Class which is a representation of a unit testing.

    Methods:
        setUp
        test_error_file
        test_compress_true
        test_compress_false
        test_dump_run
        tearDown

    """

    def setUp(self):

        """Function:  setUp

        Description:  Initialization for unit testing.

        Arguments:

        """

        self.dump_cmd = []
        self.dmp_file = "./test/unit/mysql_db_dump/tmp/test_run_prog"
        self.err_file = "Error File"
        self.subp = SubProcess()

    @mock.patch("mysql_db_dump.subprocess.Popen")
    def test_error_file(self, mock_subp):

        """Function:  test_error_file

        Description:  Test with error file passed.

        Arguments:

        """

        mock_subp.return_value = self.subp

        self.assertFalse(mysql_db_dump.dump_run(self.dump_cmd, self.dmp_file,
                                                False, errfile=self.err_file))

    @mock.patch("mysql_db_dump.gen_libs.compress",
                mock.Mock(return_value=True))
    @mock.patch("mysql_db_dump.subprocess.Popen")
    def test_compress_true(self, mock_subp):

        """Function:  test_compress_true

        Description:  Test with compression set to True.

        Arguments:

        """

        mock_subp.return_value = self.subp

        self.assertFalse(mysql_db_dump.dump_run(self.dump_cmd, self.dmp_file,
                                                True))

    @mock.patch("mysql_db_dump.subprocess.Popen")
    def test_compress_false(self, mock_subp):

        """Function:  test_compress_false

        Description:  Test with compression set to False.

        Arguments:

        """

        mock_subp.return_value = self.subp

        self.assertFalse(mysql_db_dump.dump_run(self.dump_cmd, self.dmp_file,
                                                False))

    @mock.patch("mysql_db_dump.subprocess.Popen")
    def test_dump_run(self, mock_subp):

        """Function:  test_dump_run

        Description:  Test with only default arguments passed.

        Arguments:

        """

        mock_subp.return_value = self.subp

        self.assertFalse(mysql_db_dump.dump_run(self.dump_cmd, self.dmp_file,
                                                False))

    def tearDown(self):

        """Function:  tearDown

        Description:  Clean up of unit testing.

        Arguments:

        """

        if os.path.isfile(self.dmp_file):
            os.remove(self.dmp_file)


if __name__ == "__main__":
    unittest.main()

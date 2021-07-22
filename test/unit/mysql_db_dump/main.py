#!/usr/bin/python
# Classification (U)

"""Program:  main.py

    Description:  Unit testing of main in mysql_db_dump.py.

    Usage:
        test/unit/mysql_db_dump/main.py

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


class ProgramLock(object):

    """Class:  ProgramLock

    Description:  Class stub holder for gen_class.ProgramLock class.

    Methods:
        __init__

    """

    def __init__(self, cmdline, flavor):

        """Method:  __init__

        Description:  Class initialization.

        Arguments:
            (input) cmdline
            (input) flavor

        """

        self.cmdline = cmdline
        self.flavor = flavor


class UnitTest(unittest.TestCase):

    """Class:  UnitTest

    Description:  Class which is a representation of a unit testing.

    Methods:
        setUp
        test_programlock_id
        test_programlock_false
        test_programlock_true
        test_run_program
        test_arg_cond_req_or_true
        test_arg_cond_req_or_false
        test_arg_dir_chk_crt_false
        test_arg_dir_chk_crt_true
        test_arg_xor_dict_true
        test_arg_xor_dict_false
        test_arg_require_false
        test_arg_require_true
        test_help_false
        test_help_true

    """

    def setUp(self):

        """Function:  setUp

        Description:  Initialization for unit testing.

        Arguments:

        """

        self.args_array = {"-c": "CfgFile", "-d": "CfgDir"}
        self.args_array2 = {"-c": "CfgFile", "-d": "CfgDir", "-y": "Flavor"}
        self.proglock = ProgramLock(["cmdline"], "FlavorID")

    @mock.patch("mysql_db_dump.run_program", mock.Mock(return_value=True))
    @mock.patch("mysql_db_dump.gen_class.ProgramLock")
    @mock.patch("mysql_db_dump.gen_libs.help_func")
    @mock.patch("mysql_db_dump.arg_parser")
    def test_programlock_id(self, mock_arg, mock_help, mock_lock):

        """Function:  test_programlock_id

        Description:  Test with ProgramLock with flavor id.

        Arguments:

        """

        mock_lock.return_value = self.proglock
        mock_arg.arg_parse2.return_value = self.args_array2
        mock_help.return_value = False
        mock_arg.arg_req_xor.return_value = True
        mock_arg.arg_require.return_value = False
        mock_arg.arg_cond_req.return_value = True
        mock_arg.arg_dir_chk_crt.return_value = False
        mock_arg.arg_cond_req_or.return_value = True

        self.args_array["-y"] = "FlavorID"

        self.assertFalse(mysql_db_dump.main())

    @mock.patch("mysql_db_dump.run_program", mock.Mock(return_value=True))
    @mock.patch("mysql_db_dump.gen_class.ProgramLock")
    @mock.patch("mysql_db_dump.gen_libs.help_func")
    @mock.patch("mysql_db_dump.arg_parser")
    def test_programlock_false(self, mock_arg, mock_help, mock_lock):

        """Function:  test_programlock_false

        Description:  Test with ProgramLock returns False.

        Arguments:

        """

        mock_lock.side_effect = \
            mysql_db_dump.gen_class.SingleInstanceException
        mock_arg.arg_parse2.return_value = self.args_array
        mock_help.return_value = False
        mock_arg.arg_req_xor.return_value = True
        mock_arg.arg_require.return_value = False
        mock_arg.arg_cond_req.return_value = True
        mock_arg.arg_dir_chk_crt.return_value = False
        mock_arg.arg_cond_req_or.return_value = True

        with gen_libs.no_std_out():
            self.assertFalse(mysql_db_dump.main())

    @mock.patch("mysql_db_dump.run_program", mock.Mock(return_value=True))
    @mock.patch("mysql_db_dump.gen_class.ProgramLock")
    @mock.patch("mysql_db_dump.gen_libs.help_func")
    @mock.patch("mysql_db_dump.arg_parser")
    def test_programlock_true(self, mock_arg, mock_help, mock_lock):

        """Function:  test_programlock_true

        Description:  Test with ProgramLock returns True.

        Arguments:

        """

        mock_lock.return_value = self.proglock
        mock_arg.arg_parse2.return_value = self.args_array
        mock_help.return_value = False
        mock_arg.arg_req_xor.return_value = True
        mock_arg.arg_require.return_value = False
        mock_arg.arg_cond_req.return_value = True
        mock_arg.arg_dir_chk_crt.return_value = False
        mock_arg.arg_cond_req_or.return_value = True

        self.assertFalse(mysql_db_dump.main())

    @mock.patch("mysql_db_dump.run_program", mock.Mock(return_value=True))
    @mock.patch("mysql_db_dump.gen_class.ProgramLock")
    @mock.patch("mysql_db_dump.gen_libs.help_func")
    @mock.patch("mysql_db_dump.arg_parser")
    def test_run_program(self, mock_arg, mock_help, mock_lock):

        """Function:  test_run_program

        Description:  Test run_program function.

        Arguments:

        """

        mock_lock.return_value = self.proglock
        mock_arg.arg_parse2.return_value = self.args_array
        mock_help.return_value = False
        mock_arg.arg_require.return_value = False
        mock_arg.arg_xor_dict.return_value = True
        mock_arg.arg_dir_chk_crt.return_value = False
        mock_arg.arg_cond_req_or.return_value = True

        self.assertFalse(mysql_db_dump.main())

    @mock.patch("mysql_db_dump.run_program", mock.Mock(return_value=True))
    @mock.patch("mysql_db_dump.gen_class.ProgramLock")
    @mock.patch("mysql_db_dump.gen_libs.help_func")
    @mock.patch("mysql_db_dump.arg_parser")
    def test_arg_cond_req_or_true(self, mock_arg, mock_help, mock_lock):

        """Function:  test_arg_cond_req_or_true

        Description:  Test arg_cond_req_or if returns true.

        Arguments:

        """

        mock_lock.return_value = self.proglock
        mock_arg.arg_parse2.return_value = self.args_array
        mock_help.return_value = False
        mock_arg.arg_require.return_value = False
        mock_arg.arg_xor_dict.return_value = True
        mock_arg.arg_dir_chk_crt.return_value = False
        mock_arg.arg_cond_req_or.return_value = True

        self.assertFalse(mysql_db_dump.main())

    @mock.patch("mysql_db_dump.gen_class.ProgramLock")
    @mock.patch("mysql_db_dump.gen_libs.help_func")
    @mock.patch("mysql_db_dump.arg_parser")
    def test_arg_cond_req_or_false(self, mock_arg, mock_help, mock_lock):

        """Function:  test_arg_cond_req_or_false

        Description:  Test arg_cond_req_or if returns false.

        Arguments:

        """

        mock_lock.return_value = self.proglock
        mock_arg.arg_parse2.return_value = self.args_array
        mock_help.return_value = False
        mock_arg.arg_require.return_value = False
        mock_arg.arg_xor_dict.return_value = True
        mock_arg.arg_dir_chk_crt.return_value = False
        mock_arg.arg_cond_req_or.return_value = False

        self.assertFalse(mysql_db_dump.main())

    @mock.patch("mysql_db_dump.gen_class.ProgramLock")
    @mock.patch("mysql_db_dump.gen_libs.help_func")
    @mock.patch("mysql_db_dump.arg_parser")
    def test_arg_dir_chk_crt_false(self, mock_arg, mock_help, mock_lock):

        """Function:  test_arg_dir_chk_crt_false

        Description:  Test arg_dir_chk_crt if returns false.

        Arguments:

        """

        mock_lock.return_value = self.proglock
        mock_arg.arg_parse2.return_value = self.args_array
        mock_help.return_value = False
        mock_arg.arg_require.return_value = False
        mock_arg.arg_xor_dict.return_value = True
        mock_arg.arg_dir_chk_crt.return_value = False
        mock_arg.arg_cond_req_or.return_value = False

        self.assertFalse(mysql_db_dump.main())

    @mock.patch("mysql_db_dump.gen_libs.help_func")
    @mock.patch("mysql_db_dump.arg_parser")
    def test_arg_dir_chk_crt_true(self, mock_arg, mock_help):

        """Function:  test_arg_dir_chk_crt_true

        Description:  Test arg_dir_chk_crt if returns true.

        Arguments:

        """

        mock_arg.arg_parse2.return_value = self.args_array
        mock_help.return_value = False
        mock_arg.arg_require.return_value = False
        mock_arg.arg_xor_dict.return_value = True
        mock_arg.arg_dir_chk_crt.return_value = True

        self.assertFalse(mysql_db_dump.main())

    @mock.patch("mysql_db_dump.gen_libs.help_func")
    @mock.patch("mysql_db_dump.arg_parser")
    def test_arg_xor_dict_true(self, mock_arg, mock_help):

        """Function:  test_arg_xor_dict_true

        Description:  Test arg_xor_dict if returns true.

        Arguments:

        """

        mock_arg.arg_parse2.return_value = self.args_array
        mock_help.return_value = False
        mock_arg.arg_require.return_value = False
        mock_arg.arg_xor_dict.return_value = True
        mock_arg.arg_dir_chk_crt.return_value = True

        self.assertFalse(mysql_db_dump.main())

    @mock.patch("mysql_db_dump.gen_libs.help_func")
    @mock.patch("mysql_db_dump.arg_parser")
    def test_arg_xor_dict_false(self, mock_arg, mock_help):

        """Function:  test_arg_xor_dict_false

        Description:  Test arg_xor_dict if returns false.

        Arguments:

        """

        mock_arg.arg_parse2.return_value = self.args_array
        mock_help.return_value = False
        mock_arg.arg_require.return_value = False
        mock_arg.arg_xor_dict.return_value = False

        self.assertFalse(mysql_db_dump.main())

    @mock.patch("mysql_db_dump.gen_libs.help_func")
    @mock.patch("mysql_db_dump.arg_parser")
    def test_arg_require_false(self, mock_arg, mock_help):

        """Function:  test_arg_require_false

        Description:  Test arg_require if returns false.

        Arguments:

        """

        mock_arg.arg_parse2.return_value = self.args_array
        mock_help.return_value = False
        mock_arg.arg_require.return_value = False
        mock_arg.arg_xor_dict.return_value = False

        self.assertFalse(mysql_db_dump.main())

    @mock.patch("mysql_db_dump.gen_libs.help_func")
    @mock.patch("mysql_db_dump.arg_parser")
    def test_arg_require_true(self, mock_arg, mock_help):

        """Function:  test_arg_require_true

        Description:  Test arg_require if returns true.

        Arguments:

        """

        mock_arg.arg_parse2.return_value = self.args_array
        mock_help.return_value = False
        mock_arg.arg_require.return_value = True

        self.assertFalse(mysql_db_dump.main())

    @mock.patch("mysql_db_dump.gen_libs.help_func")
    @mock.patch("mysql_db_dump.arg_parser")
    def test_help_false(self, mock_arg, mock_help):

        """Function:  test_help_false

        Description:  Test help if returns false.

        Arguments:

        """

        mock_arg.arg_parse2.return_value = self.args_array
        mock_help.return_value = False
        mock_arg.arg_require.return_value = True

        self.assertFalse(mysql_db_dump.main())

    @mock.patch("mysql_db_dump.gen_libs.help_func")
    @mock.patch("mysql_db_dump.arg_parser.arg_parse2")
    def test_help_true(self, mock_arg, mock_help):

        """Function:  test_help_true

        Description:  Test help if returns true.

        Arguments:

        """

        mock_arg.return_value = self.args_array
        mock_help.return_value = True

        self.assertFalse(mysql_db_dump.main())


if __name__ == "__main__":
    unittest.main()

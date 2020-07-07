#!/usr/bin/python
# Classification (U)

"""Program:  run_program.py

    Description:  Unit testing of run_program in mysql_db_dump.py.

    Usage:
        test/unit/mysql_db_dump/run_program.py

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

        self.gtid_mode = True

    def connect(self):

        """Method:  connect

        Description:  Stub method holder for mysql_class.Server.connect.

        Arguments:

        """

        pass

    def set_srv_gtid(self):

        """Method:  set_srv_gtid

        Description:  Stub method holder for mysql_class.Server.set_srv_gtid.

        Arguments:

        """

        pass


class UnitTest(unittest.TestCase):

    """Class:  UnitTest

    Description:  Class which is a representation of a unit testing.

    Methods:
        setUp -> Initialize testing environment.
        test_w_option2 -> Test with -w option set to True.
        test_w_option -> Test with -w option set to False.
        test_r_option_miss -> Test with -r option value not in command list.
        test_r_option2 -> Test with -r option and GTID set to False.
        test_r_option -> Test with -r option and GTID set to True.
        test_z_option2 -> Test with -z option set to False.
        test_z_option -> Test with -z option set to True.
        test_o_option -> Test with -o option.
        test_run_program -> Test run_program with default settings.

    """

    def setUp(self):

        """Function:  setUp

        Description:  Initialization for unit testing.

        Arguments:

        """

        self.server = Server()
        self.dump_cmd = ["dump_command", "--set-gtid-purged=OFF"]
        self.dump_cmd2 = ["dump_command"]
        self.db_list = []
        self.args_array = {"-c": "config", "-d": "/dir"}
        self.args_array2 = {"-c": "config", "-d": "/dir", "-o": "/dir/path"}
        self.args_array3 = {"-c": "config", "-d": "/dir", "-z": True}
        self.args_array4 = {"-c": "config", "-d": "/dir", "-z": False}
        self.args_array5 = {"-c": "config", "-d": "/dir", "-r": True}
        self.args_array6 = {"-c": "config", "-d": "/dir", "-w": True}
        self.opt_arg_list = ["--ignore-table=mysql.event"]
        self.opt_dump_list = {
            "-s": "--single-transaction",
            "-D": ["--all-databases", "--triggers", "--routines", "--events"],
            "-r": "--set-gtid-purged=OFF"}

    @mock.patch("mysql_db_dump.dump_db", mock.Mock(return_value=True))
    @mock.patch("mysql_db_dump.cmds_gen.disconnect",
                mock.Mock(return_value=True))
    @mock.patch("mysql_db_dump.set_db_list")
    @mock.patch("mysql_db_dump.crt_dump_cmd")
    @mock.patch("mysql_db_dump.mysql_libs.create_instance")
    def test_w_option2(self, mock_inst, mock_cmd, mock_list):

        """Function:  test_w_option2

        Description:  Test with -w option set to True.

        Arguments:

        """

        mock_inst.return_value = self.server
        mock_cmd.return_value = self.dump_cmd
        mock_list.return_value = self.db_list

        self.assertFalse(mysql_db_dump.run_program(self.args_array6,
                                                   self.opt_arg_list,
                                                   self.opt_dump_list))

    @mock.patch("mysql_db_dump.dump_db", mock.Mock(return_value=True))
    @mock.patch("mysql_db_dump.cmds_gen.disconnect",
                mock.Mock(return_value=True))
    @mock.patch("mysql_db_dump.set_db_list")
    @mock.patch("mysql_db_dump.crt_dump_cmd")
    @mock.patch("mysql_db_dump.mysql_libs.create_instance")
    def test_w_option(self, mock_inst, mock_cmd, mock_list):

        """Function:  test_w_option

        Description:  Test with -w option set to False.

        Arguments:

        """

        mock_inst.return_value = self.server
        mock_cmd.return_value = self.dump_cmd
        mock_list.return_value = self.db_list

        self.assertFalse(mysql_db_dump.run_program(self.args_array,
                                                   self.opt_arg_list,
                                                   self.opt_dump_list))

    @unittest.skip("Bug:  If -r option value not in command list.")
    @mock.patch("mysql_db_dump.dump_db", mock.Mock(return_value=True))
    @mock.patch("mysql_db_dump.cmds_gen.disconnect",
                mock.Mock(return_value=True))
    @mock.patch("mysql_db_dump.set_db_list")
    @mock.patch("mysql_db_dump.crt_dump_cmd")
    @mock.patch("mysql_db_dump.mysql_libs.create_instance")
    def test_r_option_miss(self, mock_inst, mock_cmd, mock_list):

        """Function:  test_r_option_miss

        Description:  Test with -r option value not in command list.

        Arguments:

        """

        self.server.gtid_mode = False

        mock_inst.return_value = self.server
        mock_cmd.return_value = self.dump_cmd2
        mock_list.return_value = self.db_list

        self.assertFalse(mysql_db_dump.run_program(self.args_array5,
                                                   self.opt_arg_list,
                                                   self.opt_dump_list))

    @mock.patch("mysql_db_dump.dump_db", mock.Mock(return_value=True))
    @mock.patch("mysql_db_dump.cmds_gen.disconnect",
                mock.Mock(return_value=True))
    @mock.patch("mysql_db_dump.set_db_list")
    @mock.patch("mysql_db_dump.crt_dump_cmd")
    @mock.patch("mysql_db_dump.mysql_libs.create_instance")
    def test_r_option2(self, mock_inst, mock_cmd, mock_list):

        """Function:  test_r_option2

        Description:  Test with -r option and GTID set to False.

        Arguments:

        """

        self.server.gtid_mode = False

        mock_inst.return_value = self.server
        mock_cmd.return_value = self.dump_cmd
        mock_list.return_value = self.db_list

        self.assertFalse(mysql_db_dump.run_program(self.args_array5,
                                                   self.opt_arg_list,
                                                   self.opt_dump_list))

    @mock.patch("mysql_db_dump.dump_db", mock.Mock(return_value=True))
    @mock.patch("mysql_db_dump.cmds_gen.disconnect",
                mock.Mock(return_value=True))
    @mock.patch("mysql_db_dump.set_db_list")
    @mock.patch("mysql_db_dump.crt_dump_cmd")
    @mock.patch("mysql_db_dump.mysql_libs.create_instance")
    def test_r_option(self, mock_inst, mock_cmd, mock_list):

        """Function:  test_r_option

        Description:  Test with -r option and GTID set to True.

        Arguments:

        """

        mock_inst.return_value = self.server
        mock_cmd.return_value = self.dump_cmd
        mock_list.return_value = self.db_list

        self.assertFalse(mysql_db_dump.run_program(self.args_array5,
                                                   self.opt_arg_list,
                                                   self.opt_dump_list))

    @mock.patch("mysql_db_dump.dump_db", mock.Mock(return_value=True))
    @mock.patch("mysql_db_dump.cmds_gen.disconnect",
                mock.Mock(return_value=True))
    @mock.patch("mysql_db_dump.set_db_list")
    @mock.patch("mysql_db_dump.crt_dump_cmd")
    @mock.patch("mysql_db_dump.mysql_libs.create_instance")
    def test_z_option2(self, mock_inst, mock_cmd, mock_list):

        """Function:  test_z_option2

        Description:  Test with -z option set to False.

        Arguments:

        """

        mock_inst.return_value = self.server
        mock_cmd.return_value = self.dump_cmd
        mock_list.return_value = self.db_list

        self.assertFalse(mysql_db_dump.run_program(self.args_array4,
                                                   self.opt_arg_list,
                                                   self.opt_dump_list))

    @mock.patch("mysql_db_dump.dump_db", mock.Mock(return_value=True))
    @mock.patch("mysql_db_dump.cmds_gen.disconnect",
                mock.Mock(return_value=True))
    @mock.patch("mysql_db_dump.set_db_list")
    @mock.patch("mysql_db_dump.crt_dump_cmd")
    @mock.patch("mysql_db_dump.mysql_libs.create_instance")
    def test_z_option(self, mock_inst, mock_cmd, mock_list):

        """Function:  test_z_option

        Description:  Test with -z option set to True.

        Arguments:

        """

        mock_inst.return_value = self.server
        mock_cmd.return_value = self.dump_cmd
        mock_list.return_value = self.db_list

        self.assertFalse(mysql_db_dump.run_program(self.args_array3,
                                                   self.opt_arg_list,
                                                   self.opt_dump_list))

    @mock.patch("mysql_db_dump.dump_db", mock.Mock(return_value=True))
    @mock.patch("mysql_db_dump.cmds_gen.disconnect",
                mock.Mock(return_value=True))
    @mock.patch("mysql_db_dump.set_db_list")
    @mock.patch("mysql_db_dump.crt_dump_cmd")
    @mock.patch("mysql_db_dump.mysql_libs.create_instance")
    def test_o_option(self, mock_inst, mock_cmd, mock_list):

        """Function:  test_o_option

        Description:  Test with -o option.

        Arguments:

        """

        mock_inst.return_value = self.server
        mock_cmd.return_value = self.dump_cmd
        mock_list.return_value = self.db_list

        self.assertFalse(mysql_db_dump.run_program(self.args_array2,
                                                   self.opt_arg_list,
                                                   self.opt_dump_list))

    @mock.patch("mysql_db_dump.dump_db", mock.Mock(return_value=True))
    @mock.patch("mysql_db_dump.cmds_gen.disconnect",
                mock.Mock(return_value=True))
    @mock.patch("mysql_db_dump.set_db_list")
    @mock.patch("mysql_db_dump.crt_dump_cmd")
    @mock.patch("mysql_db_dump.mysql_libs.create_instance")
    def test_run_program(self, mock_inst, mock_cmd, mock_list):

        """Function:  test_run_program

        Description:  Test run_program with default settings.

        Arguments:

        """

        mock_inst.return_value = self.server
        mock_cmd.return_value = self.dump_cmd
        mock_list.return_value = self.db_list

        self.assertFalse(mysql_db_dump.run_program(self.args_array,
                                                   self.opt_arg_list,
                                                   self.opt_dump_list))


if __name__ == "__main__":
    unittest.main()

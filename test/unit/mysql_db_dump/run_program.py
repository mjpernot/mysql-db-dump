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
        self.name = "ServerName"
        self.conn_msg = None

    def connect(self, silent=False):

        """Method:  connect

        Description:  Stub method holder for mysql_class.Server.connect.

        Arguments:

        """

        status = True

        if silent:
            status = True

        return status


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
        test_connect_failure -> Test with failed connection.
        test_connect_success -> Test with successful connection.
        test_mailx2 -> Test with using mailx option.
        test_mailx -> Test with using no mailx option.
        test_multiple_options2 -> Test with multiple options passed 2.
        test_multiple_options -> Test with multiple options passed.
        test_no_email -> Test with no email configured.
        test_email_subj -> Test with subject line passed.
        test_email_no_subj -> Test with no subject line passed.
        test_email -> Test with email configured.
        test_w_option2 -> Test with -w option set to True.
        test_w_option -> Test with -w option set to False.
        test_r_option_miss -> Test with -r option value not in command list.
        test_r_option3 -> Test with -r option and GTID set to False.
        test_r_option2 -> Test with -r option and GTID set to False.
        test_r_option -> Test with -r option and GTID set to True.
        test_z_option2 -> Test with -z option set to False.
        test_z_option -> Test with -z option set to True.
        test_no_o_option -> Test with no -o option.
        test_o_option -> Test with -o option.
        test_run_program -> Test run_program with default settings.

    """

    def setUp(self):

        """Function:  setUp

        Description:  Initialization for unit testing.

        Arguments:

        """

        gtid_arg = "--set-gtid-purged=OFF"
        self.server = Server()
        self.dump_cmd = ["dump_command", gtid_arg]
        self.dump_cmd2 = ["dump_command"]
        self.dump_cmd3 = ["dump_command", gtid_arg]
        self.db_list = []
        self.args_array = {"-c": "config", "-d": "/dir"}
        self.args_array2 = {"-c": "config", "-d": "/dir", "-o": "/dir/path"}
        self.args_array3 = {"-c": "config", "-d": "/dir", "-z": True}
        self.args_array4 = {"-c": "config", "-d": "/dir", "-z": False}
        self.args_array5 = {"-c": "config", "-d": "/dir", "-r": True}
        self.args_array6 = {"-c": "config", "-d": "/dir", "-w": True}
        self.args_array7 = {"-c": "config", "-d": "/dir", "-e": ["EmailAdr"]}
        self.args_array8 = {"-c": "config", "-d": "/dir", "-e": ["EmailAdr"],
                            "t": ["Subject", "Line"]}
        self.args_array8a = {"-c": "config", "-d": "/dir", "-e": ["EmailAdr"],
                             "t": ["Subject", "Line"], "-u": True}
        self.args_array9 = {"-c": "config", "-d": "/dir", "-e": ["EmailAdr"],
                            "t": ["Subject", "Line"], "-z": True}
        self.args_array10 = {"-c": "config", "-d": "/dir", "-e": ["EmailAdr"],
                             "t": ["Subject", "Line"], "-z": True, "-w": True}
        self.opt_arg_list = ["--ignore-table=mysql.event"]
        self.opt_dump_list = {
            "-s": "--single-transaction",
            "-D": ["--all-databases", "--triggers", "--routines", "--events"],
            "-r": gtid_arg}

    @mock.patch("mysql_db_dump.mysql_libs.create_instance")
    def test_connect_failure(self, mock_inst):

        """Function:  test_connect_failure

        Description:  Test with failed connection.

        Arguments:

        """

        self.server.conn_msg = "Error connection message"

        mock_inst.return_value = self.server

        with gen_libs.no_std_out():
            self.assertFalse(mysql_db_dump.run_program(
                self.args_array, self.opt_arg_list, self.opt_dump_list))

    @mock.patch("mysql_db_dump.dump_db", mock.Mock(return_value=True))
    @mock.patch("mysql_db_dump.mysql_libs.disconnect",
                mock.Mock(return_value=True))
    @mock.patch("mysql_db_dump.set_db_list")
    @mock.patch("mysql_db_dump.crt_dump_cmd")
    @mock.patch("mysql_db_dump.mysql_libs.create_instance")
    def test_connect_success(self, mock_inst, mock_cmd, mock_list):

        """Function:  test_connect_success

        Description:  Test with successful connection.

        Arguments:

        """

        mock_inst.return_value = self.server
        mock_cmd.return_value = self.dump_cmd
        mock_list.return_value = self.db_list

        self.assertFalse(mysql_db_dump.run_program(
            self.args_array, self.opt_arg_list, self.opt_dump_list))

    @mock.patch("mysql_db_dump.dump_db", mock.Mock(return_value=True))
    @mock.patch("mysql_db_dump.mysql_libs.disconnect",
                mock.Mock(return_value=True))
    @mock.patch("mysql_db_dump.set_db_list")
    @mock.patch("mysql_db_dump.crt_dump_cmd")
    @mock.patch("mysql_db_dump.mysql_libs.create_instance")
    def test_mailx2(self, mock_inst, mock_cmd, mock_list):

        """Function:  test_mailx2

        Description:  Test with using mailx option.

        Arguments:

        """

        mock_inst.return_value = self.server
        mock_cmd.return_value = self.dump_cmd
        mock_list.return_value = self.db_list

        self.assertFalse(mysql_db_dump.run_program(
            self.args_array8a, self.opt_arg_list, self.opt_dump_list))

    @mock.patch("mysql_db_dump.dump_db", mock.Mock(return_value=True))
    @mock.patch("mysql_db_dump.mysql_libs.disconnect",
                mock.Mock(return_value=True))
    @mock.patch("mysql_db_dump.set_db_list")
    @mock.patch("mysql_db_dump.crt_dump_cmd")
    @mock.patch("mysql_db_dump.mysql_libs.create_instance")
    def test_mailx(self, mock_inst, mock_cmd, mock_list):

        """Function:  test_mailx

        Description:  Test with using no mailx option.

        Arguments:

        """

        mock_inst.return_value = self.server
        mock_cmd.return_value = self.dump_cmd
        mock_list.return_value = self.db_list

        self.assertFalse(mysql_db_dump.run_program(
            self.args_array8, self.opt_arg_list, self.opt_dump_list))

    @mock.patch("mysql_db_dump.dump_db", mock.Mock(return_value=True))
    @mock.patch("mysql_db_dump.mysql_libs.disconnect",
                mock.Mock(return_value=True))
    @mock.patch("mysql_db_dump.set_db_list")
    @mock.patch("mysql_db_dump.crt_dump_cmd")
    @mock.patch("mysql_db_dump.mysql_libs.create_instance")
    def test_multiple_options2(self, mock_inst, mock_cmd, mock_list):

        """Function:  test_multiple_options2

        Description:  Test with multiple options passed 2.

        Arguments:

        """

        mock_inst.return_value = self.server
        mock_cmd.return_value = self.dump_cmd
        mock_list.return_value = self.db_list

        self.assertFalse(mysql_db_dump.run_program(
            self.args_array10, self.opt_arg_list, self.opt_dump_list))

    @mock.patch("mysql_db_dump.dump_db", mock.Mock(return_value=True))
    @mock.patch("mysql_db_dump.mysql_libs.disconnect",
                mock.Mock(return_value=True))
    @mock.patch("mysql_db_dump.set_db_list")
    @mock.patch("mysql_db_dump.crt_dump_cmd")
    @mock.patch("mysql_db_dump.mysql_libs.create_instance")
    def test_multiple_options(self, mock_inst, mock_cmd, mock_list):

        """Function:  test_multiple_options

        Description:  Test with multiple options passed.

        Arguments:

        """

        mock_inst.return_value = self.server
        mock_cmd.return_value = self.dump_cmd
        mock_list.return_value = self.db_list

        self.assertFalse(mysql_db_dump.run_program(
            self.args_array9, self.opt_arg_list, self.opt_dump_list))

    @mock.patch("mysql_db_dump.dump_db", mock.Mock(return_value=True))
    @mock.patch("mysql_db_dump.mysql_libs.disconnect",
                mock.Mock(return_value=True))
    @mock.patch("mysql_db_dump.set_db_list")
    @mock.patch("mysql_db_dump.crt_dump_cmd")
    @mock.patch("mysql_db_dump.mysql_libs.create_instance")
    def test_no_email(self, mock_inst, mock_cmd, mock_list):

        """Function:  test_no_email

        Description:  Test with no email configured.

        Arguments:

        """

        mock_inst.return_value = self.server
        mock_cmd.return_value = self.dump_cmd
        mock_list.return_value = self.db_list

        self.assertFalse(mysql_db_dump.run_program(
            self.args_array, self.opt_arg_list, self.opt_dump_list))

    @mock.patch("mysql_db_dump.dump_db", mock.Mock(return_value=True))
    @mock.patch("mysql_db_dump.mysql_libs.disconnect",
                mock.Mock(return_value=True))
    @mock.patch("mysql_db_dump.set_db_list")
    @mock.patch("mysql_db_dump.crt_dump_cmd")
    @mock.patch("mysql_db_dump.mysql_libs.create_instance")
    def test_email_subj(self, mock_inst, mock_cmd, mock_list):

        """Function:  test_email_subj

        Description:  Test with subject line passed.

        Arguments:

        """

        mock_inst.return_value = self.server
        mock_cmd.return_value = self.dump_cmd
        mock_list.return_value = self.db_list

        self.assertFalse(mysql_db_dump.run_program(
            self.args_array8, self.opt_arg_list, self.opt_dump_list))

    @mock.patch("mysql_db_dump.dump_db", mock.Mock(return_value=True))
    @mock.patch("mysql_db_dump.mysql_libs.disconnect",
                mock.Mock(return_value=True))
    @mock.patch("mysql_db_dump.set_db_list")
    @mock.patch("mysql_db_dump.crt_dump_cmd")
    @mock.patch("mysql_db_dump.mysql_libs.create_instance")
    def test_email_no_subj(self, mock_inst, mock_cmd, mock_list):

        """Function:  test_email_no_subj

        Description:  Test with no subject line passed.

        Arguments:

        """

        mock_inst.return_value = self.server
        mock_cmd.return_value = self.dump_cmd
        mock_list.return_value = self.db_list

        self.assertFalse(mysql_db_dump.run_program(
            self.args_array7, self.opt_arg_list, self.opt_dump_list))

    @mock.patch("mysql_db_dump.dump_db", mock.Mock(return_value=True))
    @mock.patch("mysql_db_dump.mysql_libs.disconnect",
                mock.Mock(return_value=True))
    @mock.patch("mysql_db_dump.set_db_list")
    @mock.patch("mysql_db_dump.crt_dump_cmd")
    @mock.patch("mysql_db_dump.mysql_libs.create_instance")
    def test_email(self, mock_inst, mock_cmd, mock_list):

        """Function:  test_email

        Description:  Test with email configured.

        Arguments:

        """

        mock_inst.return_value = self.server
        mock_cmd.return_value = self.dump_cmd
        mock_list.return_value = self.db_list

        self.assertFalse(mysql_db_dump.run_program(
            self.args_array7, self.opt_arg_list, self.opt_dump_list))

    @mock.patch("mysql_db_dump.dump_db", mock.Mock(return_value=True))
    @mock.patch("mysql_db_dump.mysql_libs.disconnect",
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

        self.assertFalse(mysql_db_dump.run_program(
            self.args_array6, self.opt_arg_list, self.opt_dump_list))

    @mock.patch("mysql_db_dump.dump_db", mock.Mock(return_value=True))
    @mock.patch("mysql_db_dump.mysql_libs.disconnect",
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

        self.assertFalse(mysql_db_dump.run_program(
            self.args_array, self.opt_arg_list, self.opt_dump_list))

    @mock.patch("mysql_db_dump.dump_db", mock.Mock(return_value=True))
    @mock.patch("mysql_db_dump.mysql_libs.disconnect",
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

        self.assertFalse(mysql_db_dump.run_program(
            self.args_array5, self.opt_arg_list, self.opt_dump_list))

    @mock.patch("mysql_db_dump.dump_db", mock.Mock(return_value=True))
    @mock.patch("mysql_db_dump.mysql_libs.disconnect",
                mock.Mock(return_value=True))
    @mock.patch("mysql_db_dump.set_db_list")
    @mock.patch("mysql_db_dump.crt_dump_cmd")
    @mock.patch("mysql_db_dump.mysql_libs.create_instance")
    def test_r_option3(self, mock_inst, mock_cmd, mock_list):

        """Function:  test_r_option3

        Description:  Test with -r option and GTID set to False.

        Arguments:

        """

        self.server.gtid_mode = False

        mock_inst.return_value = self.server
        mock_cmd.return_value = self.dump_cmd3
        mock_list.return_value = self.db_list

        self.assertFalse(mysql_db_dump.run_program(
            self.args_array5, self.opt_arg_list, self.opt_dump_list))

    @mock.patch("mysql_db_dump.dump_db", mock.Mock(return_value=True))
    @mock.patch("mysql_db_dump.mysql_libs.disconnect",
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

        self.assertFalse(mysql_db_dump.run_program(
            self.args_array5, self.opt_arg_list, self.opt_dump_list))

    @mock.patch("mysql_db_dump.dump_db", mock.Mock(return_value=True))
    @mock.patch("mysql_db_dump.mysql_libs.disconnect",
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

        self.assertFalse(mysql_db_dump.run_program(
            self.args_array5, self.opt_arg_list, self.opt_dump_list))

    @mock.patch("mysql_db_dump.dump_db", mock.Mock(return_value=True))
    @mock.patch("mysql_db_dump.mysql_libs.disconnect",
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

        self.assertFalse(mysql_db_dump.run_program(
            self.args_array4, self.opt_arg_list, self.opt_dump_list))

    @mock.patch("mysql_db_dump.dump_db", mock.Mock(return_value=True))
    @mock.patch("mysql_db_dump.mysql_libs.disconnect",
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

        self.assertFalse(mysql_db_dump.run_program(
            self.args_array3, self.opt_arg_list, self.opt_dump_list))

    @mock.patch("mysql_db_dump.dump_db", mock.Mock(return_value=True))
    @mock.patch("mysql_db_dump.mysql_libs.disconnect",
                mock.Mock(return_value=True))
    @mock.patch("mysql_db_dump.set_db_list")
    @mock.patch("mysql_db_dump.crt_dump_cmd")
    @mock.patch("mysql_db_dump.mysql_libs.create_instance")
    def test_no_o_option(self, mock_inst, mock_cmd, mock_list):

        """Function:  test_no_o_option

        Description:  Test with no -o option.

        Arguments:

        """

        mock_inst.return_value = self.server
        mock_cmd.return_value = self.dump_cmd
        mock_list.return_value = self.db_list

        self.assertFalse(mysql_db_dump.run_program(
            self.args_array, self.opt_arg_list, self.opt_dump_list))

    @mock.patch("mysql_db_dump.dump_db", mock.Mock(return_value=True))
    @mock.patch("mysql_db_dump.mysql_libs.disconnect",
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

        self.assertFalse(mysql_db_dump.run_program(
            self.args_array2, self.opt_arg_list, self.opt_dump_list))

    @mock.patch("mysql_db_dump.dump_db", mock.Mock(return_value=True))
    @mock.patch("mysql_db_dump.mysql_libs.disconnect",
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

        self.assertFalse(mysql_db_dump.run_program(
            self.args_array, self.opt_arg_list, self.opt_dump_list))


if __name__ == "__main__":
    unittest.main()

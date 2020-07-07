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


class Mail(object):

    """Class:  Mail

    Description:  Class stub holder for gen_class.Mail class.

    Methods:
        __init__ -> Class initialization.
        add_2_msg -> Stub method holder for Mail.add_2_msg.
        send_mail -> Stub method holder for Mail.send_mail.

    """

    def __init__(self):

        """Method:  __init__

        Description:  Class initialization.

        Arguments:

        """

        self.data = None

    def add_2_msg(self, data):

        """Method:  add_2_msg

        Description:  Stub method holder for Mail.add_2_msg.

        Arguments:
            (input) data -> Message line to add to email body.

        """

        self.data = data

        return True

    def send_mail(self):

        """Method:  send_mail

        Description:  Stub method holder for Mail.send_mail.

        Arguments:

        """

        return True


class UnitTest(unittest.TestCase):

    """Class:  UnitTest

    Description:  Class which is a representation of a unit testing.

    Methods:
        setUp -> Initialize testing environment.
        test_email_single_line -> Test with email with single line.
        test_email_multiple_lines -> Test with email with multiple lines.
        test_email_empty -> Test with empty file.
        test_email -> Test with email option.
        test_db_list_w_option -> Test with -w option with list of databases.
        test_all_dbs_w_option -> Test with -z option with all databases.
        test_db_list2 -> Test with list of databases.
        test_db_list -> Test with list of databases.
        test_all_dbs -> Test with all databases.
        test_dump_db -> Test with only default arguments passed.
        tearDown -> Clean up of unit testing.

    """

    def setUp(self):

        """Function:  setUp

        Description:  Initialization for unit testing.

        Arguments:

        """

        self.mail = Mail()
        self.dump_cmd = ["dump_command", "params"]
        self.dump_cmd2 = ["--all-databases"]
        self.db_list = []
        self.db_list2 = ["db1"]
        self.db_list3 = ["db1", "db2"]
        self.dmp_path = "./test/unit/mysql_db_dump/tmp/"
        self.err_sup = True
        self.filelist = ["Line 1", "Line 2"]
        self.filelist2 = ["Line 1"]

    @mock.patch("mysql_db_dump.gen_libs.is_empty_file",
                mock.Mock(return_value=False))
    @mock.patch("mysql_db_dump.dump_run", mock.Mock(return_value=True))
    @mock.patch("mysql_db_dump.gen_libs.file_2_list")
    def test_email_single_line(self, mock_list):

        """Function:  test_email_single_line

        Description:  Test with email with single line.

        Arguments:

        """

        mock_list.return_value = self.filelist2

        self.assertFalse(mysql_db_dump.dump_db(
            self.dump_cmd, self.db_list2, False, self.dmp_path,
            err_sup=self.err_sup, mail=self.mail))

    @mock.patch("mysql_db_dump.gen_libs.is_empty_file",
                mock.Mock(return_value=False))
    @mock.patch("mysql_db_dump.dump_run", mock.Mock(return_value=True))
    @mock.patch("mysql_db_dump.gen_libs.file_2_list")
    def test_email_multiple_lines(self, mock_list):

        """Function:  test_email_multiple_lines

        Description:  Test with email with multiple lines.

        Arguments:

        """

        mock_list.return_value = self.filelist

        self.assertFalse(mysql_db_dump.dump_db(
            self.dump_cmd, self.db_list2, False, self.dmp_path,
            err_sup=self.err_sup, mail=self.mail))

    @mock.patch("mysql_db_dump.gen_libs.is_empty_file",
                mock.Mock(return_value=True))
    @mock.patch("mysql_db_dump.dump_run", mock.Mock(return_value=True))
    @mock.patch("mysql_db_dump.gen_libs.file_2_list")
    def test_email_empty(self, mock_list):

        """Function:  test_email_empty

        Description:  Test with empty file.

        Arguments:

        """

        mock_list.return_value = self.filelist

        self.assertFalse(mysql_db_dump.dump_db(
            self.dump_cmd, self.db_list2, False, self.dmp_path,
            err_sup=self.err_sup, mail=self.mail))

    @mock.patch("mysql_db_dump.gen_libs.is_empty_file",
                mock.Mock(return_value=False))
    @mock.patch("mysql_db_dump.dump_run", mock.Mock(return_value=True))
    @mock.patch("mysql_db_dump.gen_libs.file_2_list")
    def test_email(self, mock_list):

        """Function:  test_email

        Description:  Test with email option.

        Arguments:

        """

        mock_list.return_value = self.filelist

        self.assertFalse(mysql_db_dump.dump_db(
            self.dump_cmd, self.db_list2, False, self.dmp_path,
            err_sup=self.err_sup, mail=self.mail))

    @mock.patch("mysql_db_dump.dump_run", mock.Mock(return_value=True))
    def test_db_list_w_option(self):

        """Function:  test_db_list_w_option

        Description:  Test with -w option with list of databases.

        Arguments:

        """

        self.assertFalse(mysql_db_dump.dump_db(
            self.dump_cmd, self.db_list2, False, self.dmp_path,
            err_sup=self.err_sup))

    @mock.patch("mysql_db_dump.dump_run", mock.Mock(return_value=True))
    def test_all_dbs_w_option(self):

        """Function:  test_all_dbs_w_option

        Description:  Test with -z option with all databases.

        Arguments:

        """

        self.assertFalse(mysql_db_dump.dump_db(
            self.dump_cmd2, self.db_list, False, self.dmp_path,
            err_sup=self.err_sup))

    @mock.patch("mysql_db_dump.dump_run", mock.Mock(return_value=True))
    def test_db_list2(self):

        """Function:  test_db_list2

        Description:  Test with list of databases.

        Arguments:

        """

        self.assertFalse(mysql_db_dump.dump_db(self.dump_cmd, self.db_list3,
                                               False, self.dmp_path))

    @mock.patch("mysql_db_dump.dump_run", mock.Mock(return_value=True))
    def test_db_list(self):

        """Function:  test_db_list

        Description:  Test with list of databases.

        Arguments:

        """

        self.assertFalse(mysql_db_dump.dump_db(self.dump_cmd, self.db_list2,
                                               False, self.dmp_path))

    @mock.patch("mysql_db_dump.dump_run", mock.Mock(return_value=True))
    def test_all_dbs(self):

        """Function:  test_all_dbs

        Description:  Test with all databases.

        Arguments:

        """

        self.assertFalse(mysql_db_dump.dump_db(self.dump_cmd2, self.db_list,
                                               False, self.dmp_path))

    def test_dump_db(self):

        """Function:  test_dump_db

        Description:  Test with only default arguments passed.

        Arguments:

        """

        with gen_libs.no_std_out():
            self.assertFalse(mysql_db_dump.dump_db(self.dump_cmd, self.db_list,
                                                   False, self.dmp_path))

    def tearDown(self):

        """Function:  tearDown

        Description:  Clean up of unit testing.

        Arguments:

        """

        file_list = gen_libs.filename_search(self.dmp_path, "ErrOut.*.log",
                                             add_path=True)

        for item in file_list:
            if os.path.isfile(item):
                os.remove(item)


if __name__ == "__main__":
    unittest.main()

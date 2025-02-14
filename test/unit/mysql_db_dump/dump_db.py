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
import unittest
import mock

# Local
sys.path.append(os.getcwd())
import mysql_db_dump                            # pylint:disable=E0401,C0413
import lib.gen_libs as gen_libs             # pylint:disable=E0401,C0413,R0402
import version                                  # pylint:disable=E0401,C0413

__version__ = version.__version__


class Mail():

    """Class:  Mail

    Description:  Class stub holder for gen_class.Mail class.

    Methods:
        __init__
        add_2_msg
        send_mail

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
            (input) data

        """

        self.data = data

        return True

    def send_mail(self, use_mailx=False):

        """Method:  send_mail

        Description:  Stub method holder for Mail.send_mail.

        Arguments:
            (input) use_mailx

        """

        status = True

        if use_mailx:
            status = True

        return status


class UnitTest(unittest.TestCase):

    """Class:  UnitTest

    Description:  Class which is a representation of a unit testing.

    Methods:
        setUp
        test_email_mailx
        test_email_no_mailx
        test_email_single_line
        test_email_multiple_lines
        test_email_empty
        test_email
        test_db_list_w_option
        test_all_dbs_w_option
        test_db_list2
        test_db_list
        test_all_dbs
        test_dump_db
        tearDown

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
    def test_email_mailx(self, mock_list):

        """Function:  test_email_mailx

        Description:  Test with override postfix and use mailx.

        Arguments:

        """

        mock_list.return_value = self.filelist

        self.assertFalse(mysql_db_dump.dump_db(
            self.dump_cmd, self.db_list2, False, self.dmp_path,
            err_sup=self.err_sup, mail=self.mail, use_mailx=True))

    @mock.patch("mysql_db_dump.gen_libs.is_empty_file",
                mock.Mock(return_value=False))
    @mock.patch("mysql_db_dump.dump_run", mock.Mock(return_value=True))
    @mock.patch("mysql_db_dump.gen_libs.file_2_list")
    def test_email_no_mailx(self, mock_list):

        """Function:  test_email_no_mailx

        Description:  Test with using postfix email command.

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

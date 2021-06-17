#!/usr/bin/python
# Classification (U)

"""Program:  add_ssl.py

    Description:  Unit testing of add_ssl in mysql_db_dump.py.

    Usage:
        test/unit/mysql_db_dump/add_ssl.py

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

# Local
sys.path.append(os.getcwd())
import mysql_db_dump
import version

__version__ = version.__version__


class CfgTest2(object):

    """Class:  CfgTest

    Description:  Class which is a representation of a cfg module.

    Methods:
        __init__ -> Initialize configuration environment.

    """

    def __init__(self):

        """Method:  __init__

        Description:  Initialization instance of the CfgTest class.

        Arguments:

        """

        self.ssl_ca_path = None
        self.ssl_client_key = None
        self.ssl_client_cert = None
        self.ssl_mode = "PREFERRED"


class CfgTest(object):

    """Class:  CfgTest

    Description:  Class which is a representation of a cfg module.

    Methods:
        __init__ -> Initialize configuration environment.

    """

    def __init__(self):

        """Method:  __init__

        Description:  Initialization instance of the CfgTest class.

        Arguments:

        """

        self.ssl_client_ca = None
        self.ssl_ca_path = None
        self.ssl_client_key = None
        self.ssl_client_cert = None
        self.ssl_mode = "PREFERRED"


class UnitTest(unittest.TestCase):

    """Class:  UnitTest

    Description:  Class which is a representation of a unit testing.

    Methods:
        setUp -> Initialize testing environment.
        test_ca_path2 -> Test with ca path passed.
        test_ca_path -> Test with ca path passed.
        test_all2 -> Test with ca, key and cert passed.
        test_all -> Test with ca, key and cert passed.
        test_cert_only2 -> Test with only cert passed.
        test_cert_only -> Test with only cert passed.
        test_key_only2 -> Test with only key passed.
        test_key_only -> Test with only key passed.
        test_key_cert2 -> Test with key and client passed.
        test_key_cert -> Test with key and client passed.
        test_ca_only2 -> Test with only client CA passed.
        test_ca_only -> Test with only client CA passed.
        test_missing2 -> Test with missing an argument.
        test_missing -> Test with missing an argument.
        test_default2 -> Test with only default arguments passed.
        test_default -> Test with only default arguments passed.
        tearDown -> Clean up of unit testing.

    """

    def setUp(self):

        """Function:  setUp

        Description:  Initialization for unit testing.

        Arguments:

        """

        ssl_ca = "--ssl-ca="
        ssl_capath = "--ssl-capath="
        ssl_cert = "--ssl-cert="
        ssl_key = "--ssl-key="
        self.cfg = CfgTest()
        self.cfg2 = CfgTest2()
        self.dump_cmd = ["dump_command"]
        self.err_msg1 = "One or more values missing for required SSL settings."
        self.err_msg2 = "Configuration file is missing SSL entries."
        self.mode = "--ssl-mode=PREFERRED"
        self.ca_pem = "/path/ca.pem"
        self.key = "/path/key.pem"
        self.cert = "/path/cert.pem"
        self.ca_path = "/path"
        self.results = list(self.dump_cmd)
        self.results.append(ssl_ca + self.ca_pem)
        self.results.append(self.mode)
        self.results2 = list(self.dump_cmd)
        self.results2.append(ssl_cert + self.cert)
        self.results2.append(self.mode)
        self.results2.append(ssl_key + self.key)
        self.results3 = list(self.dump_cmd)
        self.results3.append(ssl_cert + self.cert)
        self.results3.append(ssl_ca + self.ca_pem)
        self.results3.append(self.mode)
        self.results3.append(ssl_key + self.key)
        self.results4 = list(self.dump_cmd)
        self.results4.append(ssl_cert + self.cert)
        self.results4.append(ssl_ca + self.ca_pem)
        self.results4.append(self.mode)
        self.results4.append(ssl_capath + self.ca_path)
        self.results4.append(ssl_key + self.key)

    def test_ca_path2(self):

        """Function:  test_ca_path2

        Description:  Test with ca path passed.

        Arguments:

        """

        self.cfg.ssl_client_ca = self.ca_pem
        self.cfg.ssl_client_key = self.key
        self.cfg.ssl_client_cert = self.cert
        self.cfg.ssl_ca_path = self.ca_path
        dump_cmd = mysql_db_dump.add_ssl(self.cfg, self.dump_cmd)

        self.assertEqual((dump_cmd[1], dump_cmd[2]), (True, None))

    def test_ca_path(self):

        """Function:  test_ca_path

        Description:  Test with ca path passed.

        Arguments:

        """

        self.cfg.ssl_client_ca = self.ca_pem
        self.cfg.ssl_client_key = self.key
        self.cfg.ssl_client_cert = self.cert
        self.cfg.ssl_ca_path = self.ca_path
        dump_cmd = mysql_db_dump.add_ssl(self.cfg, self.dump_cmd)

        self.assertEqual(dump_cmd[0], self.results4)

    def test_all2(self):

        """Function:  test_all2

        Description:  Test with ca, key and cert passed.

        Arguments:

        """

        self.cfg.ssl_client_ca = self.ca_pem
        self.cfg.ssl_client_key = self.key
        self.cfg.ssl_client_cert = self.cert
        dump_cmd = mysql_db_dump.add_ssl(self.cfg, self.dump_cmd)

        self.assertEqual((dump_cmd[1], dump_cmd[2]), (True, None))

    def test_all(self):

        """Function:  test_all

        Description:  Test with ca, key and cert passed.

        Arguments:

        """

        self.cfg.ssl_client_ca = self.ca_pem
        self.cfg.ssl_client_key = self.key
        self.cfg.ssl_client_cert = self.cert
        dump_cmd = mysql_db_dump.add_ssl(self.cfg, self.dump_cmd)

        self.assertEqual(dump_cmd[0], self.results3)

    def test_cert_only2(self):

        """Function:  test_cert_only2

        Description:  Test with only cert passed.

        Arguments:

        """

        self.cfg.ssl_client_cert = self.cert
        dump_cmd = mysql_db_dump.add_ssl(self.cfg, self.dump_cmd)

        self.assertEqual((dump_cmd[1], dump_cmd[2]), (False, self.err_msg1))

    def test_cert_only(self):

        """Function:  test_cert_only

        Description:  Test with only cert passed.

        Arguments:

        """

        self.cfg.ssl_client_cert = self.cert
        dump_cmd = mysql_db_dump.add_ssl(self.cfg, self.dump_cmd)

        self.assertEqual(dump_cmd[0], self.dump_cmd)

    def test_key_only2(self):

        """Function:  test_key_only2

        Description:  Test with only key passed.

        Arguments:

        """

        self.cfg.ssl_client_key = self.key
        dump_cmd = mysql_db_dump.add_ssl(self.cfg, self.dump_cmd)

        self.assertEqual((dump_cmd[1], dump_cmd[2]), (False, self.err_msg1))

    def test_key_only(self):

        """Function:  test_key_only

        Description:  Test with only key passed.

        Arguments:

        """

        self.cfg.ssl_client_key = self.key
        dump_cmd = mysql_db_dump.add_ssl(self.cfg, self.dump_cmd)

        self.assertEqual(dump_cmd[0], self.dump_cmd)

    def test_key_cert2(self):

        """Function:  test_key_cert2

        Description:  Test with key and cert passed.

        Arguments:

        """

        self.cfg.ssl_client_key = self.key
        self.cfg.ssl_client_cert = self.cert
        dump_cmd = mysql_db_dump.add_ssl(self.cfg, self.dump_cmd)

        self.assertEqual((dump_cmd[1], dump_cmd[2]), (True, None))

    def test_key_cert(self):

        """Function:  test_key_cert

        Description:  Test with key and cert passed.

        Arguments:

        """

        self.cfg.ssl_client_key = self.key
        self.cfg.ssl_client_cert = self.cert
        dump_cmd = mysql_db_dump.add_ssl(self.cfg, self.dump_cmd)

        self.assertEqual(dump_cmd[0], self.results2)

    def test_ca_only2(self):

        """Function:  test_ca_only2

        Description:  Test with only client CA passed.

        Arguments:

        """

        self.cfg.ssl_client_ca = self.ca_pem
        dump_cmd = mysql_db_dump.add_ssl(self.cfg, self.dump_cmd)

        self.assertEqual((dump_cmd[1], dump_cmd[2]), (True, None))

    def test_ca_only(self):

        """Function:  test_ca_only

        Description:  Test with only client CA passed.

        Arguments:

        """

        self.cfg.ssl_client_ca = self.ca_pem
        dump_cmd = mysql_db_dump.add_ssl(self.cfg, self.dump_cmd)

        self.assertEqual(dump_cmd[0], self.results)

    def test_missing2(self):

        """Function:  test_missing2

        Description:  Test with missing an argument.

        Arguments:

        """

        dump_cmd = mysql_db_dump.add_ssl(self.cfg2, self.dump_cmd)

        self.assertEqual((dump_cmd[1], dump_cmd[2]), (False, self.err_msg2))

    def test_missing(self):

        """Function:  test_missing

        Description:  Test with missing an argument.

        Arguments:

        """

        dump_cmd = mysql_db_dump.add_ssl(self.cfg2, self.dump_cmd)

        self.assertEqual(dump_cmd[0], self.dump_cmd)

    def test_default2(self):

        """Function:  test_default2

        Description:  Test with only default arguments passed.

        Arguments:

        """

        dump_cmd = mysql_db_dump.add_ssl(self.cfg, self.dump_cmd)

        self.assertEqual((dump_cmd[1], dump_cmd[2]), (False, self.err_msg1))

    def test_default(self):

        """Function:  test_default

        Description:  Test with only default arguments passed.

        Arguments:

        """

        dump_cmd = mysql_db_dump.add_ssl(self.cfg, self.dump_cmd)

        self.assertEqual(dump_cmd[0], self.dump_cmd)


if __name__ == "__main__":
    unittest.main()

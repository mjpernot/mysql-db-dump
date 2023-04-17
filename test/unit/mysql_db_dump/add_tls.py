# Classification (U)

"""Program:  add_tls.py

    Description:  Unit testing of add_tls in mysql_db_dump.py.

    Usage:
        test/unit/mysql_db_dump/add_tls.py

    Arguments:

"""

# Libraries and Global Variables

# Standard
import sys
import os
import unittest

# Local
sys.path.append(os.getcwd())
import mysql_db_dump
import version

__version__ = version.__version__


class CfgTest3(object):

    """Class:  CfgTest3

    Description:  Class which is a representation of a cfg module.

    Methods:
        __init__

    """

    def __init__(self):

        """Method:  __init__

        Description:  Initialization instance of the CfgTest class.

        Arguments:

        """

        self.ssl_client_ca = None


class CfgTest2(object):

    """Class:  CfgTest2

    Description:  Class which is a representation of a cfg module.

    Methods:
        __init__

    """

    def __init__(self):

        """Method:  __init__

        Description:  Initialization instance of the CfgTest class.

        Arguments:

        """

        self.tls_versions = []


class CfgTest(object):

    """Class:  CfgTest

    Description:  Class which is a representation of a cfg module.

    Methods:
        __init__

    """

    def __init__(self):

        """Method:  __init__

        Description:  Initialization instance of the CfgTest class.

        Arguments:

        """

        self.tls_versions = ["TLSv1.2", "TLSv1.3"]


class UnitTest(unittest.TestCase):

    """Class:  UnitTest

    Description:  Class which is a representation of a unit testing.

    Methods:
        setUp
        test_empty_tls
        test_add_tls

    """

    def setUp(self):

        """Function:  setUp

        Description:  Initialization for unit testing.

        Arguments:

        """

        dmp_cmd = "dump_command"

        self.cfg = CfgTest()
        self.cfg2 = CfgTest2()
        self.cfg3 = CfgTest3()
        self.dump_cmd = [dmp_cmd]
        self.results = [dmp_cmd, "--tls-version=['TLSv1.2', 'TLSv1.3']"]
        self.results2 = [dmp_cmd]

    def test_missing_tls(self):

        """Function:  test_missing_tls

        Description:  Test with missing TLS entry.

        Arguments:

        """

        dump_cmd = mysql_db_dump.add_tls(self.cfg3, self.dump_cmd)

        self.assertEqual(dump_cmd, self.results2)

    def test_empty_tls(self):

        """Function:  test_empty_tls

        Description:  Test with empty TLS list.

        Arguments:

        """

        dump_cmd = mysql_db_dump.add_tls(self.cfg2, self.dump_cmd)

        self.assertEqual(dump_cmd, self.results2)

    def test_add_tls(self):

        """Function:  test_add_tls

        Description:  Test with adding TLS to command line.

        Arguments:

        """

        dump_cmd = mysql_db_dump.add_tls(self.cfg, self.dump_cmd)

        self.assertEqual(dump_cmd, self.results)


if __name__ == "__main__":
    unittest.main()

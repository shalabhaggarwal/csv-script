#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''
    test_script

    :copyright: (c) 2013 by Shalabh Aggarwal
    :license: GPLv3, see LICENSE for more details
'''

import unittest
from script import process_csv


class TestScript(unittest.TestCase):
    """Test the CSV process script
    """
    def setUp(self):
        "This runs before the test cases are executed"
        pass

    def test_0010_static_file(self):
        "Test the script with a static sample file"
        file_path = 'sample_data.csv'
        result = process_csv(file_path)

        self.assertEqual(result['Company A']['Month'], 'Jan')
        self.assertEqual(result['Company A']['Year'], '1993')
        self.assertEqual(result['Company A']['Price'], '37')
        self.assertEqual(result['Company B']['Month'], 'Jul')
        self.assertEqual(result['Company B']['Year'], '1992')
        self.assertEqual(result['Company B']['Price'], '58')
        self.assertEqual(result['Company C']['Month'], 'Nov')
        self.assertEqual(result['Company C']['Year'], '1991')
        self.assertEqual(result['Company C']['Price'], '53')
        self.assertEqual(result['Company D']['Month'], 'Jan')
        self.assertEqual(result['Company D']['Year'], '1993')
        self.assertEqual(result['Company D']['Price'], '58')


def suite():
    "Test suite"
    suite = unittest.TestSuite()
    suite.addTests(
        unittest.TestLoader().loadTestsFromTestCase(TestScript)
    )
    return suite


if __name__ == '__main__':
    unittest.TextTestRunner(verbosity=2).run(suite())

# Copyright (c) 2026, BWH and Contributors
# See license.txt

# import frappe
# from frappe.tests.utils import IntegrationTestCase

import unittest
import frappe
# On IntegrationTestCase, the doctype test records and all
# link-field test record dependencies are recursively loaded
# Use these module variables to add/remove to/from that list
EXTRA_TEST_RECORD_DEPENDENCIES = []  # eg. ["User"]
IGNORE_TEST_RECORD_DEPENDENCIES = []  # eg. ["User"]



# class IntegrationTestDriver(IntegrationTestCase):
class TestDriver(unittest.TestCase):
    """
    Integration tests for Driver.
    Use this class for testing interactions between multiple components.
    """
    def test_full_name_correctly_set(self):
        test_driver = frappe.new_doc("Driver")
        test_driver.first_name = "John"
        test_driver.last_name = "Doe"
        test_driver.license_number = "D1234567"
        # test_driver.insert()
        self.assertEqual(test_driver.full_name, "John Doe")
        test_driver.save()

        # self.assertEqual(test_driver.full_name, "John Doe")
import unittest
import HTMLTestRunner
from time import strftime
from test_valid_license import ValidLicenseTest
from test_license_expired import LicenseExpiredTest
from test_license_not_yet_valid import LicenseNotYetValidTest
from test_incorrect_ip_address import IncorrectIPAddressTest
from test_license_invalid_version import InvalidVersionTest
from test_corrupted_license import CorruptedLicenseTest
from test_remove_license_table import RemoveLicenseTableTest
from test_remove_license import RemoveLicenseTest
from test_no_license import NoLicenseTest
 
dir = "c:\TestResults"
# get all tests from the test classes
valid_license_tests = unittest.TestLoader().loadTestsFromTestCase(ValidLicenseTest)
license_expired_tests = unittest.TestLoader().loadTestsFromTestCase(LicenseExpiredTest)
license_not_yet_valid_tests = unittest.TestLoader().loadTestsFromTestCase(LicenseNotYetValidTest)
incorrect_ip_address_tests = unittest.TestLoader().loadTestsFromTestCase(IncorrectIPAddressTest)
license_invalid_version_tests = unittest.TestLoader().loadTestsFromTestCase(InvalidVersionTest)
corrupted_license_tests = unittest.TestLoader().loadTestsFromTestCase(CorruptedLicenseTest)
remove_license_table_tests = unittest.TestLoader().loadTestsFromTestCase(RemoveLicenseTableTest)
remove_license_tests = unittest.TestLoader().loadTestsFromTestCase(RemoveLicenseTest)
no_license_tests = unittest.TestLoader().loadTestsFromTestCase(NoLicenseTest)

# create a test suite
test_suite = unittest.TestSuite([valid_license_tests, license_expired_tests, license_not_yet_valid_tests, incorrect_ip_address_tests, license_invalid_version_tests, corrupted_license_tests, remove_license_table_tests, remove_license_tests, no_license_tests])
# test_suite = unittest.TestSuite([remove_license_tests])

# Use this line to run tests outside of TestRunner. Need to comment out all the TestRunner code below
#unittest.TextTestRunner(verbosity=2).run(test_suite)
 
# # open the report file
time = strftime("%Y_%m_%d_%H_%M")
outfile = open(dir + "\UMTests_" + time + ".html", "w")
 
# # configure HTMLTestRunner options
runner = HTMLTestRunner.HTMLTestRunner(stream=outfile,title='Go! User Management Test Report', version='T 6.9.0.5')
 
# # run the suite using HTMLTestRunner
runner.run(test_suite)
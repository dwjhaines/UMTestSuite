import unittest
import HTMLTestRunner
from time import strftime
from test_valid_license import ValidLicenseTest
from test_license_expired import LicenseExpiredTest
from test_license_not_yet_valid import LicenseNotYetValidTest
from test_incorrect_ip_address import IncorrectIPAddressTest
from test_license_invalid_version import InvalidVersionTest
from test_corrupted_license import CorruptedLicenseTest
 
dir = "c:\TestResults"
# get all tests from ValidLicenseTest class
valid_license_tests = unittest.TestLoader().loadTestsFromTestCase(ValidLicenseTest)
license_expired_tests = unittest.TestLoader().loadTestsFromTestCase(LicenseExpiredTest)
license_not_yet_valid_tests = unittest.TestLoader().loadTestsFromTestCase(LicenseNotYetValidTest)
incorrect_ip_address_tests = unittest.TestLoader().loadTestsFromTestCase(IncorrectIPAddressTest)
license_invalid_version_tests = unittest.TestLoader().loadTestsFromTestCase(InvalidVersionTest)
corrupted_license_tests = unittest.TestLoader().loadTestsFromTestCase(CorruptedLicenseTest)

# create a test suite
test_suite = unittest.TestSuite([valid_license_tests, license_expired_tests, license_not_yet_valid_tests, incorrect_ip_address_tests, license_invalid_version_tests, corrupted_license_tests])
test_suite = unittest.TestSuite([license_invalid_version_tests])

# Use this line to run tests outside of TestRunner
# unittest.TextTestRunner(verbosity=2).run(test_suite)
 
# open the report file
time = strftime("%Y_%m_%d_%H_%M")
outfile = open(dir + "\UMTests_" + time + ".html", "w")
 
# configure HTMLTestRunner options
runner = HTMLTestRunner.HTMLTestRunner(stream=outfile,title='Go! User Management Test Report', version='T 6.9.0.3')
 
# run the suite using HTMLTestRunner
runner.run(test_suite)
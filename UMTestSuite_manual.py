import unittest
import HTMLTestRunner
from time import strftime
from test_valid_license import ValidLicenseTest
from test_license_expired import LicenseExpiredTest
from test_license_not_yet_valid import LicenseNotYetValidTest
from test_incorrect_ip_address import IncorrectIPAddressTest
 
dir = "c:\TestResults"
# get all tests from ValidLicenseTest class
valid_license_tests = unittest.TestLoader().loadTestsFromTestCase(ValidLicenseTest)
license_expired_tests = unittest.TestLoader().loadTestsFromTestCase(LicenseExpiredTest)
license_not_yet_valid_tests = unittest.TestLoader().loadTestsFromTestCase(LicenseNotYetValidTest)
incorrect_ip_address_tests = unittest.TestLoader().loadTestsFromTestCase(IncorrectIPAddressTest)

# create a test suite
# test_suite = unittest.TestSuite([valid_license_tests, license_expired_tests, license_not_yet_valid_tests, incorrect_ip_address_tests])
test_suite = unittest.TestSuite([incorrect_ip_address_tests])

# Use this line to run tests outside of TestRunner
unittest.TextTestRunner(verbosity=2).run(test_suite)
 
# open the report file
#time = strftime("%Y_%m_%d_%H_%M")
#outfile = open(dir + "\UMTests_" + time + ".html", "w")
 
# configure HTMLTestRunner options
#runner = HTMLTestRunner.HTMLTestRunner(stream=outfile,title='Test Report', description='Acceptance Tests', version='T6.9.0.3')
 
# run the suite using HTMLTestRunner
#runner.run(test_suite)
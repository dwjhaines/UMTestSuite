import unittest
import HTMLTestRunner
from time import strftime
from test_valid_license import ValidLicenseTest
 
dir = "c:\TestResults"
# get all tests from ValidLicenseTest class
valid_license_tests = unittest.TestLoader().loadTestsFromTestCase(ValidLicenseTest)

# create a test suite
test_suite = unittest.TestSuite([valid_license_tests])

# Use this line to run tests outside of TestRunner
# unittest.TextTestRunner(verbosity=2).run(test_suite)
 
# open the report file
time = strftime("%Y_%m_%d_%H_%M")
outfile = open(dir + "\UMTests_" + time + ".html", "w")
 
# configure HTMLTestRunner options
runner = HTMLTestRunner.HTMLTestRunner(stream=outfile,title='Test Report', description='Acceptance Tests')
 
# run the suite using HTMLTestRunner
runner.run(test_suite)
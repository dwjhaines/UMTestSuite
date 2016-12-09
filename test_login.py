###############################################################################################
#                                                                                             # 
# test_login.py                                                                               #
#                                                                                             # 
# Checks that the emergency login can be used when there is no valid license and when the max #
# number of users has been reached.                                                           #
#                                                                                             #
###############################################################################################
import unittest
import time
import um_utils
import db_utils
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
import pyodbc

class LoginTest(unittest.TestCase):
    @classmethod
    def setUpClass(inst):
        print 'Start of test: test_login'
        # Username to be used for this test
        username = 'avaa.johnsona'
        inst.user = um_utils.user(username, 'quantel@')
        
        # Set up connection to database
        inst.connection = db_utils.connectToDb()    
        inst.cur = inst.connection.cursor()
         
        # Delete all existing licenses and install license for five users
        db_utils.deleteAllLicenses(inst.connection, inst.cur)
        inst.maxUsers = db_utils.addFiveUserLicense(inst.connection, inst.cur)
        print 'License installed for %d users' % inst.maxUsers  
        
    def est_login(self):
        # Check that user is not already logged in
        self.assertFalse(db_utils.isUserLoggedIn(self.connection, self.cur, self.user), 'Test not valid. User is already logged in')
        # Try and log in user.
        result = um_utils.login(self.user)
        if (result == 0):
            self.user.loggedin = True 
        self.assertTrue((db_utils.isUserLoggedIn(self.connection, self.cur, self.user)), 'User not logged in' )
         
        print 'Sleeping for 2 secs.................'
        time.sleep( 2 )
        
    def est_logout(self):      
        # log user in
        um_utils.loginPage(self.user)
        result = um_utils.login(self.user)
        if (result == 0):
            self.user.loggedin = True 
        # Check that user is logged in
        self.assertTrue(db_utils.isUserLoggedIn(self.connection, self.cur, self.user), 'Test not valid. User is not logged in')
        print 'Sleeping for 2 secs.................'
        time.sleep( 2 )
        # Try and log user out.
        um_utils.logout(self.user)
        self.user.loggedin = db_utils.isUserLoggedIn(self.connection, self.cur, self.user)

        # Check user is no longer logged in
        self.assertFalse((db_utils.isUserLoggedIn(self.connection, self.cur, self.user)), 'User is still logged in' )
        
    def test_ten_wrong_passwords(self):
        # Set user password to be incorrect
        self.user.password = 'snell'
        # Reset failed password count
        db_utils.resetFailedPasswordAttemptCount(self.connection, self.cur, self.user)
        
        for count in range(0, 10):
            # Try and log in user.
            result = um_utils.login(self.user)
            print 'Attempts = %d  Result = %d' % (count + 1, result)
            lockedout = db_utils.isUserLockedOut(self.connection, self.cur, self.user)
            print 'Lockedout = %d' % lockedout

        # ****************** Test needs finishing ****************************
        # Reset failed password count
        # db_utils.resetFailedPasswordAttemptCount(self.connection, self.cur, self.user)
        
    def tearDown(inst):
        # Log out user at the end of each test
        if (inst.user.loggedin == True):
            um_utils.logout(inst.user)
            inst.user.loggedin = False
        time.sleep( 1 )

    @classmethod
    def tearDownClass(inst):
        um_utils.closeBrowser(inst.user)
        # Delete license and reinstall license for twenty-five users
        db_utils.deleteAllLicenses(inst.connection, inst.cur)
        maxUsers = db_utils.addTwentyFiveUserLicense(inst.connection, inst.cur)
        print 'License installed for %d users' % maxUsers
        
        # Close connection to database
        db_utils.closeConnection(inst.connection, inst.cur)
        
if __name__ == '__main__':
    unittest.main()
    

###############################################################################################
#                                                                                             # 
# test_login.py                                                                               #
#                                                                                             # 
# Runs tests for logging in and out, etc                                                      #
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
        
    def test_login(self):
        # Check that user is not already logged in
        self.assertFalse(db_utils.isUserLoggedIn(self.connection, self.cur, self.user), 'Test not valid. User is already logged in')
        # Try and log in user.
        result = um_utils.login(self.user)
        if (result == 0):
            self.user.loggedin = True 
        self.assertTrue((db_utils.isUserLoggedIn(self.connection, self.cur, self.user)), 'User not logged in' )
         
        print 'Sleeping for 2 secs.................'
        time.sleep( 2 )
        
    def test_logout(self):      
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
            # Check that account is not blocked
            self.assertFalse(db_utils.isUserLockedOut(self.connection, self.cur, self.user))
            # Try and log in user.
            result = um_utils.login(self.user)
            lockedout = db_utils.isUserLockedOut(self.connection, self.cur, self.user)
            self.assertTrue(result == 2, 'Wrong error message displayed')
            print 'Attempts = %d  Result = %d  Locked out = %d' % (count + 1, result, lockedout)
        
        # Check that users account is blocked
        print 'User has entered 10 incorrect passwords. Account should be blocked:'
        print 'Locked out = %d' % db_utils.isUserLockedOut(self.connection, self.cur, self.user)
        self.assertTrue(db_utils.isUserLockedOut(self.connection, self.cur, self.user))
        
        # Reset failed password count and unblock user
        print 'Unlocking user account......'
        db_utils.resetFailedPasswordAttemptCount(self.connection, self.cur, self.user)
        db_utils.unBlockUser(self.connection, self.cur, self.user)
        # Check that user has been unlocked
        lockedout = db_utils.isUserLockedOut(self.connection, self.cur, self.user)
        print 'Locked out = %d' % lockedout
        
    def test_forgotten_password(self):
        # Check that user is not already logged in
        self.assertFalse(db_utils.isUserLoggedIn(self.connection, self.cur, self.user), 'Test not valid. User is already logged in')    
        
        # Click on forgotten password button, answer security question and recieve new password
        new_password_text  = um_utils.forgottenPassword(self.user)
        print 'Message: %s' % new_password_text
        self.assertTrue(new_password_text.startswith('Your password has been successfully reset to:'),"Password not reset")
        # New password is the last 14 chars of the string
        new_password = new_password_text[-14:]
        print 'New Password: %s' % new_password
        
        # Reset the new password back to quantel@
        confirmation = um_utils.resetPassword (self.user, new_password)
        print 'Message: %s' % confirmation
        self.assertTrue(confirmation.startswith('Change Password Complete'),"Password change failed")

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
    

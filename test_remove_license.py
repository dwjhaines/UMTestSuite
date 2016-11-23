###############################################################################################
#                                                                                             # 
# test_remove_license.py                                                                      #
#                                                                                             # 
# When all licences are removed, an administrator should not be logged out                    #
# This test logs in an administrator and checks that she is still logged in after six minutes #
# Repeats the test and checks that a manager is not logged out but and editor is.             # 
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

class RemoveLicenseTest(unittest.TestCase):
    @classmethod
    def setUpClass(inst):
        print 'Start of test: test_remove_license'
        # Name of administrator to be used for this test
        inst.admin = 'avaa.johnsona'
        # Name of editor to be used for this test
        inst.editor = 'chloe.anderson'
        # Name of manager to be used for this test
        inst.manager = 'maria.a'
        
        # Set up connection to database
        inst.connection = db_utils.connectToDb()    
        inst.cur = inst.connection.cursor()
        
        # Delete all existing licenses
        db_utils.deleteAllLicenses(inst.connection, inst.cur)
        
    def setUp(inst):       
        # Install license for five users
        print 'Install license for five users'
        db_utils.addFiveUserLicense(inst.connection, inst.cur)
        
    def test_administrators(self):
        self.user = um_utils.user(self.admin, 'quantel@')
        result = um_utils.login(self.user)
        if (result == 0 or result == 1):
            self.user.loggedin = True
        self.assertTrue ((result == 0 or result == 1), 'Test Failed: User could not log in.')
        
        # Delete all existing licenses
        db_utils.deleteAllLicenses(self.connection, self.cur)
        
        for x in range(0, 7):
            # Check user every minute to see if still logged in
            print 'Sleeping for 60 secs.................'
            time.sleep( 60 )
        
            # Check that user is still logged in
            if (db_utils.isUserLoggedIn(self.connection, self.cur, self.user)):
                print 'User still logged in after %d minutes' % (x + 1)
            self.assertTrue ((db_utils.isUserLoggedIn(self.connection, self.cur, self.user)), 'Test Failed: User has been logged out')   
             
        print 'Sleeping for 2 secs.................'
        time.sleep( 2 )
    
    def test_editors(self):
        self.user = um_utils.user(self.editor, 'quantel@')
        result = um_utils.login(self.user)
        print 'Result = %d' % result
        if (result == 0 or result == 1):
            self.user.loggedin = True
        self.assertTrue ((result == 0 or result == 1), 'Test Failed: User could not log in.')
        
        # Delete all existing licenses
        db_utils.deleteAllLicenses(self.connection, self.cur)
        
        for x in range(0, 5):
            # Check user every minute to see if still logged in
            print 'Sleeping for 60 secs.................'
            time.sleep( 60 )
        
            # Check that user is still logged in
            if (db_utils.isUserLoggedIn(self.connection, self.cur, self.user)):
                print 'User still logged in after %d minutes' % (x + 1)
            self.assertTrue ((db_utils.isUserLoggedIn(self.connection, self.cur, self.user)), 'Test Failed: User has been logged out after %d minutes' % (x + 1))  
        
        # If still logged in after five minutes, wait another 120 seconds and check that user has been logged out
        print 'Sleeping for 120 secs.................'
        time.sleep( 120 )
        if (db_utils.isUserLoggedIn(self.connection, self.cur, self.user) == False):
            print 'User has been successfully logged out'
            
        self.assertFalse(db_utils.isUserLoggedIn(self.connection, self.cur, self.user), 'Test Failed: User has not been logged out after seven minutes')
             
        print 'Sleeping for 2 secs.................'
        time.sleep( 2 )
     
    def test_managers(self):
        self.user = um_utils.user(self.manager, 'quantel@')
        result = um_utils.login(self.user)
        if (result == 0 or result == 1):
            self.user.loggedin = True
        self.assertTrue ((result == 0 or result == 1), 'Test Failed: User could not log in.')
        
        # Delete all existing licenses
        db_utils.deleteAllLicenses(self.connection, self.cur)
        
        for x in range(0, 7):
            # Check user every minute to see if still logged in
            print 'Sleeping for 60 secs.................'
            time.sleep( 60 )
        
            # Check that user is still logged in
            if (db_utils.isUserLoggedIn(self.connection, self.cur, self.user)):
                print 'User still logged in after %d minutes' % (x + 1)
            self.assertTrue ((db_utils.isUserLoggedIn(self.connection, self.cur, self.user)), 'Test Failed: User has been logged out')   
             
        print 'Sleeping for 2 secs.................'
        time.sleep( 2 )
    
    def tearDown(inst):
        # Log out any users that were logged in and close all the browsers
        if (inst.user.loggedin == True):
            um_utils.logout(inst.user)
            inst.user.loggedin = False
        time.sleep( 1 )
        um_utils.closeBrowser(inst.user)
            
    @classmethod
    def tearDownClass(inst):
        # Delete license and reinstall license for twenty-five users
        db_utils.deleteAllLicenses(inst.connection, inst.cur)
        maxUsers = db_utils.addTwentyFiveUserLicense(inst.connection, inst.cur)
        print 'License installed for %d users' % maxUsers
        
        # Close connection to database
        db_utils.closeConnection(inst.connection, inst.cur)
        
if __name__ == '__main__':
    unittest.main()
    

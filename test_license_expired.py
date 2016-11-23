###############################################################################################
#                                                                                             # 
# test_license_expired.py                                                                     #
#                                                                                             # 
# Tests that up to five administrators can log in when the license has expired. Repeats the   #
# test and checks that five managers can log in but no editors should be able to              #
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

class LicenseExpiredTest(unittest.TestCase):
    @classmethod
    def setUpClass(inst):
        print 'Start of test: test_license_expired'
        # List of editors i.e. users that do not have admin rights
        inst.editors = ['chloe.anderson', 'chloe.garcia', 'chloe.jackson', 'chloe.johnson', 'chloe.jones', 'chloe.lee']
        # List of managers i.e. users with manager rights
        inst.managers = ['maria.a', 'maria.b', 'maria.c', 'maria.d', 'maria.e', 'maria.f', 'maria.g']
        # List of administrators i.e. users with administrator rights
        inst.admins = ['avaa.johnsona', 'avaa.whitea', 'avac.whitec', 'avad.johnsond', 'avaf.whitef', 'avag.johnsong', 'avag.wilsong']
        
        # Set up connection to database
        inst.connection = db_utils.connectToDb()    
        inst.cur = inst.connection.cursor()
        
        # Delete all existing licenses
        db_utils.deleteAllLicenses(inst.connection, inst.cur)
        
        # Install license with end date in the past
        inst.maxUsers = db_utils.addUserLicenseExpired (inst.connection, inst.cur)
        print 'License installed with expired end date'
        
    def test_administrators(self):
        # Empty list to be filled with user objects
        self.users = []  
        
        maxAdmins = self.maxUsers + 5
        # Get the number of users already logged in
        count = db_utils.getNumberOfActiveUsers(self.connection, self.cur)
    
        print 'Max users allowed: %d' % self.maxUsers
        print 'Max administrators allowed: %d' % maxAdmins
        print 'Number of users already logged in: %d' % count
        print 'Opening browsers........'

        for admin in self.admins:
            # For each administrator, create a user object and add object to users list
            self.users.append(um_utils.user(admin, 'quantel@'))
           
        # Keep trying to log in each of the editors. Once the max number of users have been logged in, no further logins should be allowed.
        for user in self.users:
            result = um_utils.login(user)
            if (result == 0 or result == 1):
                user.loggedin = True 
            count = db_utils.getNumberOfActiveUsers(self.connection, self.cur)
            print '\tNumber of active users (max: %d): %d' % (maxAdmins, count)
            self.assertFalse ((count > maxAdmins), 'Test Failed: Max number of users exceded.')
                
        print 'Sleeping for 2 secs.................'
        time.sleep( 2 )
        
    def test_editors(self):
        # Empty list to be filled with user objects
        self.users = []  
        
        # Get the number of users already logged in
        count = db_utils.getNumberOfActiveUsers(self.connection, self.cur)
    
        print 'Max users allowed: %d' % self.maxUsers
        print 'Number of users already logged in: %d' % count
        print 'Opening browsers........'
       
        for editor in self.editors:
            # For each editor, create a user object and add object to users list
            self.users.append(um_utils.user(editor, 'quantel@'))
           
        # Keep trying to log in each of the editors. If any editor can log in, the test has failed.
        for user in self.users:
            result = um_utils.login(user)
            if (result == 0 or result == 1):
                user.loggedin = True 
            self.assertTrue ((result > 1), 'Test Failed: User successfully logged in.')
                
        print 'Sleeping for 2 secs.................'
        time.sleep( 2 )
     
    def test_managers(self):
        # Empty list to be filled with user objects
        self.users = []  
        
        maxManagers = self.maxUsers + 5
        # Get the number of users already logged in
        count = db_utils.getNumberOfActiveUsers(self.connection, self.cur)
    
        print 'Max users allowed: %d' % self.maxUsers
        print 'Max managers allowed: %d' % maxManagers
        print 'Number of users already logged in: %d' % count
        print 'Opening browsers........'

        for manager in self.managers:
            # For each manager, create a user object and add object to users list
            self.users.append(um_utils.user(manager, 'quantel@'))
           
        # Keep trying to log in each of the editors. Once the max number of users have been logged in, no further logins should be allowed.
        for user in self.users:
            result = um_utils.login(user)
            if (result == 0 or result == 1):
                user.loggedin = True 
            count = db_utils.getNumberOfActiveUsers(self.connection, self.cur)
            print '\tNumber of active users (max: %d): %d' % (maxManagers, count)
            self.assertFalse ((count > maxManagers), 'Test Failed: Max number of users exceded.')
                
        print 'Sleeping for 2 secs.................'
        time.sleep( 2 )
            
    def tearDown(inst):
        # Log out any users that were logged in and close all the browsers
        for user in inst.users:
            if (user.loggedin == True):
                um_utils.logout(user)
                user.loggedin = False
            time.sleep( 1 )
            um_utils.closeBrowser(user)

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
    

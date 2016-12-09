###############################################################################################
#                                                                                             # 
# test_emergency_login.py                                                                     #
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

class EmergencyLoginTest(unittest.TestCase):
    @classmethod
    def setUpClass(inst):
        print 'Start of test: test_emergency_login'
        # List of administrators i.e. users with administrator rights
        inst.admins = ['avaa.johnsona', 'avaa.whitea', 'avac.whitec', 'avad.johnsond', 'avaf.whitef', 'avag.johnsong', 'avag.wilsong', 'avai.robinsoni', 'aval.wilsonl', 'avag.whiteg']
        
        # Set up connection to database
        inst.connection = db_utils.connectToDb()    
        inst.cur = inst.connection.cursor()
        
    def setUp(inst):    
        # Delete all existing licenses at the start of each test
        db_utils.deleteAllLicenses(inst.connection, inst.cur)        
        
    def test_valid_license(self):
        # Install license for five users and set the value of maxUsers
        self.maxUsers = db_utils.addFiveUserLicense(self.connection, self.cur)
        print 'License installed for %d users' % self.maxUsers  
        
        # Empty list to be filled with user objects
        self.users = []  
        maxAdmins = self.maxUsers + 5
        print 'Maximum number of administrators = %d' % maxAdmins
        count = db_utils.getNumberOfActiveUsers(self.connection, self.cur)
        
        print 'Max users allowed: %d' % self.maxUsers
        print 'Max administrators allowed: %d' % maxAdmins
        print 'Number of users already logged in: %d' % count
        print 'Opening browsers........'

        for admin in self.admins:
            # For each administrator, create a user object and add object to users list
            self.users.append(um_utils.user(admin, 'quantel@'))
        # Set up emergency admin user
        self.ea = um_utils.user('emergencyadmin', 'faelj*34#7k89@jkl')
         
        # Keep logging in users until maxAdmins has been reached.
        for user in self.users:
            result = um_utils.login(user)
            if (result == 0 or result == 1):
                user.loggedin = True 
            count = db_utils.getNumberOfActiveUsers(self.connection, self.cur)

        # Try and log in as emergency admin
        print '\tNumber of active users (max: %d): %d' % (maxAdmins, count)
        result = um_utils.login(self.ea)
        if (result == 0 or result == 1):
            self.ea.loggedin = True 
        self.assertTrue((result == 0), 'Emergency admin unable to log in' )
         
        print 'Sleeping for 2 secs.................'
        time.sleep( 2 )

    def test_no_valid_license(self):
        # Empty list to be filled with user objects (not used in this test but needed for teardown)
        self.users = []  
        # Set up emergency admin user
        self.ea = um_utils.user('emergencyadmin', 'faelj*34#7k89@jkl')
        # No license is installed. Try and log in as emergency admin
        result = um_utils.login(self.ea)
        if (result == 0 or result == 1):
            self.ea.loggedin = True 
        self.assertTrue((result == 0), 'Emergency admin unable to log in' )
         
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
        # Log out emergency admin
        if (inst.ea.loggedin == True):
            um_utils.logout(inst.ea)
            inst.ea.loggedin = False
        um_utils.closeBrowser(inst.ea)
        
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
    

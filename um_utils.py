import time
import os
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait # available since 2.4.0
from selenium.webdriver.support import expected_conditions as EC # available since 2.26.0
from selenium.webdriver.common.action_chains import ActionChains

#Comment out one of the IP Addresses below depending on which transformer you want to use
# ipAddress = "http://10.165.250.201"
ipAddress = "http://10.165.250.249"


class user:
    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.admin = False
        self.manager = False
        self.loggedin = False
        
        # Create a new instance of the Chrome driver
        # Use incognito mode so that multiple users can be set up
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_argument("--start-maximized")
        chrome_options.add_argument("--incognito")
        self.driver = webdriver.Chrome(chrome_options=chrome_options)

        # Go to the Go! login page
        self.driver.get(ipAddress + "/quantel/um/login.aspx?ReturnUrl=/go/")
        
    def setAdmin(user, isAdmin):
        user.admin = isAdmin
        
def login (user):
    # Logs in the user
    print 'Attempting Login: %s' % user.username
    time.sleep( 2 )
    # Go to the Go! login page if not already there
    user.driver.get(ipAddress + "/quantel/um/login.aspx?ReturnUrl=/go/")
    
    # Enter username into UserName dialog
    username = WebDriverWait(user.driver, 10).until(EC.presence_of_element_located((By.NAME, "UserName")))
    username.clear()
    username.send_keys(user.username)

    # Enter password into Password dialog (assume password is quantel@)
    password = WebDriverWait(user.driver, 10).until(EC.presence_of_element_located((By.NAME, "Password")))
    password.send_keys(user.password)

    # Select and click on the login button
    user.driver.find_element_by_id('LoginButton').click()
    
    # Wait until we have moved on from the login page
    try:
        page_loaded = WebDriverWait( user.driver, 10 ).until_not(
        lambda driver: user.driver.current_url == ipAddress + "/quantel/um/login.aspx?ReturnUrl=/go/"
    )
    except TimeoutException:
        self.fail( "Loading timeout expired" )
        
    result = 99
    if ( user.driver.current_url == ipAddress + "/go/"):
        # If the Go! page has been loaded then login has been successful
        print '\t%s successfullly logged in' % user.username
        result = 0
    elif ( user.driver.current_url == ipAddress + "/quantel/um/login.aspx?ReturnUrl=%2fgo%2f" ):
        divText = user.driver.find_element_by_id('LoginDiv').text
        if 'You are already logged in' in divText:
            print '\tLogin failed: User already logged in'
            # Click on the OK button to get to the Go! page
            user.driver.find_element_by_id('ButtonOK').click()
            result = 1
        elif 'Please check your user name and password' in divText:
            print '\tLogin failed: Username or password incorrect'
            result = 2        
        elif 'Maximum number of users are logged in.' in divText:
            print '\tLogin failed: Maximum number of users already logged in'
            result = 3
        elif 'Your account has been blocked' in divText:
            print '\tLogin failed: Account has been blocked'
            result = 4

    return result
    
def forgottenPassword (user):
    # Select and click on the forgotten password button
    user.driver.find_element_by_id('ForgottenPasswordLink').click()
    
    # Entre username and click on the Submit button
    username = WebDriverWait(user.driver, 10).until(EC.presence_of_element_located((By.ID, "MainContent_UserNameTxtBox")))
    username.clear()
    username.send_keys(user.username)
    time.sleep( 2 )
    user.driver.find_element_by_id('MainContent_AskQuestionButton').click()
    time.sleep( 2 )
    
    # Enter answer to security question (Cat). This should not really be hardcoded but should work as long as the 
    # question is asked.  
    answer = WebDriverWait(user.driver, 10).until(EC.presence_of_element_located((By.ID, "MainContent_AnswerTxtBox")))
    answer.clear()
    answer.send_keys('Cat')
    time.sleep( 2 )
    user.driver.find_element_by_id('MainContent_SubmitAnswerButton').click()
    time.sleep( 2 )
    
    # Retrieve new password string 
    new_password_text = user.driver.find_element_by_id('MainContent_FeedbackLabel').text
    # return to login page
    user.driver.find_element_by_id('MainContent_LoginLink').click()
    # Return new password string
    return new_password_text
    
def resetPassword (user, password):
    # Changes specified password to the standard quantel password
    user.password = password
    login (user)
    user.loggedin = True
    # Go to the Go! login page
    user.driver.get(ipAddress + "/quantel/um/go/changepassword.aspx")
    time.sleep( 2 )
    
    # Populate the change password dialog and submit
    user.driver.find_element_by_id('MainContent_ChangePasswordControl_ChangePasswordContainerID_CurrentPassword').send_keys(user.password)
    user.driver.find_element_by_id('MainContent_ChangePasswordControl_ChangePasswordContainerID_NewPassword').send_keys('quantel@')
    user.driver.find_element_by_id('MainContent_ChangePasswordControl_ChangePasswordContainerID_ConfirmNewPassword').send_keys('quantel@')
    user.driver.find_element_by_id('MainContent_ChangePasswordControl_ChangePasswordContainerID_ChangePasswordPushButton').click()

    # Get the confirmation message to be returned
    confirmation = user.driver.find_element_by_id('MainContent_ChangePasswordControl').text
    time.sleep( 2 )
    user.password = 'quantel@'
    #MainContent_ChangePasswordControl_SuccessContainerID_ContinuePushButton
    user.driver.find_element_by_id('MainContent_ChangePasswordControl_SuccessContainerID_ContinuePushButton').click()
    time.sleep( 2 )
    # Go to main Go! page (we currently have to be here to log out)
    user.driver.get(ipAddress + "/quantel/go/index.html")
    time.sleep( 2 )
    return confirmation
    
def logout (user):
    element = user.driver.find_element_by_class_name('icon-user')
    hov = ActionChains(user.driver).move_to_element(element)
    hov.perform()

    print 'Logging out: %s' % user.username
    form = user.driver.find_element_by_id('logout').click()
    
def closeBrowser(user):
    print 'Closing browser'
    user.driver.close()
    
def loginPage(user):
    user.driver.get(ipAddress + "/quantel/um/login.aspx?ReturnUrl=/go/")
    
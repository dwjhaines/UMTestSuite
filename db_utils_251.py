import pyodbc

def connectToDb():
    # Returns a connection to the sql databse specified in the connection string below
    connection = pyodbc.connect('Driver={SQL Server}; Server=10.165.250.244; Database=session_db; uid=sa; pwd=0sql0')
    return connection
  
def closeConnection(connection, cur):
    # Closes the specified connection 
    cur.close()
    del cur
    connection.close()
    
def deleteAllLicenses (connection, cur):
    # Deletes all licenses from the database
    sql_command= 'DELETE FROM [session_db].[dbo].[Licenses]'
    cur.execute(sql_command)
    connection.commit()
    
def addFiveUserLicense (connection, cur):
    # Adds a license for five users. Returns the number of licenses that have been added
    sql_command= '''
    INSERT INTO [session_db].[dbo].[Licenses]
    VALUES ('PVG-test-license-for-5-users------------------------8d301647-cfb4-9232-433c-bb326a672cac5f9ded41-6534-4122-0C3C-8a0667390e8007061414-522524300-8aaf-4306c6972b0007061414-1926-4cdc-8064-34042442e4c951e51f53-d36f-46d6-b208-b1778b9eda64a74ee69c-21b0-42b4-ab75-7b9523da0381f56275a9-6a94-4a26-b77a-b175813d7622795342ec-9216-47f9-990f-3b333915ff3067ae5341-0d7e-4366-8780-82879e03257c2667d4d0-bd98-47ea-b6ee-f5ab521a993d495b7c5f-4983-42da-aa0d-6c35d2dd87b2fb93be4e-c34d-401a-9521-a7e1b399182763a04d2c-6526-4e95-a35b-6134ba28292b7c8588df-2d2f-45a2-ac20-1f2f183a98dd211c2f3b-5f67-47a1-9880-1378cc12e358ed7144b8-8ef6-4ac6-ac2c-f622a777945ef9d1c782-60e1-482f-8d7d-ccbd1ab23ba9786cdc05-bd1b-49db-96db-71888229325d62f6d173-39e3-4dd6-915f-efea22c2eb55c22e2b0f-3d7f-48d5-bb5c-e467e6057f74e6cfef94-1b2b-4de5-bdaf-9eb85b4844787097df8e-2457-4581-a236-e62297a238646ae45af5-a21b-43da-9fbf-174aadf79175c8a44b22-7825-4fc5-bbf3-995789efeff0c41ba3e3-7ef0-41ab-8a65-6815f6c60cabe4bf4416-9ed0-4f41-9149-8d65b429a9e9bf189b14-570c-4023-8119-09efc983c003')'''
    cur.execute(sql_command)
    connection.commit()
    # Return the number of users that can log in
    return 5
    
def addTenUserLicense (connection, cur):
    # Adds a license for ten users. Returns the number of licenses that have been added
    sql_command= '''
    INSERT INTO [session_db].[dbo].[Licenses]
    VALUES ('PVG-test-license-for-10-users-----------------------4c624aa8-fae3-7777-7526-66f89ad725572f1e4df5-8018-4162-0C3C-e506a4a571f00adcda4b-222524f93-9287-db0704038e700adcda4b-7e59-4418-a1fe-74c66867270d76276303-0503-4450-8880-f774ebb452d0ae4b3902-0c6f-422c-898b-4c25a45fc386d93c49ed-f55d-496c-8e51-94dd9449f7910ac34a9d-e309-4009-a149-b7a1bc77dbfd2cfc16a3-584a-493d-b324-d32c487f4b29cccd43a0-24b3-438c-8cff-7c64900b1606ba89b037-9a90-4b53-b593-9cdf33976c6a58d6574e-5d55-465b-8047-9ed16fb006f98b54104d-0be5-4613-a72a-afe10321edee6f1fcf28-0476-4c91-9811-89cb8807bb1f51902f6d-ad00-459e-85eb-c90dac782b470cc2b49b-4f7c-47f2-a670-7449229fc6d43d1616a3-c7ab-4872-84fb-0b0085e36a532f3653a1-614d-40a4-b7bb-6f5375b587f20599cf2f-0ecf-4459-a02d-c697892fb32b410752b3-65f0-452e-b566-d41ab95cbc0ce6ddce77-4004-4f8b-bfb3-05faff1b50b6ba97da32-bf50-4f60-a6a3-3e6203333a851c6b2e56-5580-40a1-a252-4a62ec1e0fab425a6e20-f203-4d37-84e8-a0c42cb15062680e49c2-8973-4a0d-92b9-018f2e3cd570e16bb304-c53c-40e5-8d90-d82ba9084050e39fa0c1-6704-4001-9964-2037ea61a003')'''
    cur.execute(sql_command)
    connection.commit()
    # Return the number of users that can log in
    return 10
    
def addTwentyFiveUserLicense (connection, cur):
    # Adds a license for twenty-five users. Returns the number of licenses that have been added
    sql_command= '''
    INSERT INTO [session_db].[dbo].[Licenses]
    VALUES ('PVG-test-license-for-25-users-----------------------d0ccfbbd-e1cb-7cd5-df3a-b97790bb75aa71fbf823-0966-4d81-0C3C-f607265f946012f87c67-144804e8c-811f-9a07e51b81b012f87c67-7dc6-4ff2-98e4-458b30b3abd5c2ac2bc0-29aa-4e09-bf7d-fdc250ecffd0862e619a-40e2-48be-a8ad-8038633bd3e8b5e4b6ec-1dc3-4888-a944-b67eaf81ce1b00294a2d-ee3d-420b-96ad-bcb0645973a68263940d-3033-40b3-9feb-13101938663b15340c75-0ef5-4ba4-9bc1-c532cb199893d89d6e91-060f-4a01-8a04-868ca9c7c0cb3a14cd3c-4e63-44ed-9b3d-c10106685352f1354d44-faf7-46e8-99ca-5485c2de56152e37f0d5-a1ae-455a-9bb8-25a1819854d7d47055b8-23c3-456c-80d8-14bade2ff792c6507898-45c1-4eab-9128-570e49a6dcdc952ea2f1-a8ad-476d-84bc-502f65a57117dba1d59a-2aad-4ed3-85f5-7dea0b399c83fa48fe62-9810-4cce-9cda-669e8bb3b5c789cade6f-2f9e-4d80-bdc7-a3bc643b54d980df2e68-98ba-4d9c-8f59-8a77932c6e3978a5b375-66a4-4c2a-bd9d-44a4a1d33b9230f9707d-8355-460a-82a3-f946f376f42dad31a780-1502-41bf-8811-2f1190e378db02428f8f-d36a-4459-9acf-fb35537bf8cfd43f0eeb-7803-4a34-99ca-5128f04ae41f4481ab88-018e-45c6-8053-ad15f5469003')'''
    cur.execute(sql_command)
    connection.commit()
    # Return the number of users that can log in
    return 25
    
def addUserLicenseIncorrectIPAddress (connection, cur):
    # Adds a license with an incorrect IP address. i.e. one that is not 10.165.250.251
    sql_command= '''
    INSERT INTO [session_db].[dbo].[Licenses]
    VALUES ('PVG-test-license---incorrect-IP-address-------------64461247-61bc-fe3a-59ad-636e017f6c548a2eab9a-d1ea-4cf0-0C3C-960681a184a008ac9b76-322524588-aff5-0306e0ffa12008ac9b76-9976-43c8-9463-81751d5275c261759812-96bf-475d-88af-20bb4542212e5843e6eb-4685-43f2-bfaa-8f70edf6df079e041cdd-f036-4994-9106-06e18020c6933e120b49-4b17-461c-9171-c4493346779cdd7568b6-2ac5-432f-9f75-6d06c1f068f11bc99e4a-ff0e-46ed-8fe1-49498a8ed93c0b2db46d-7c63-4782-ac09-1a23fa1c7c5130a3310f-b993-483d-bf98-6b071ff70fb178fd498e-4428-44e2-9e07-36dbfc6d33be6c203703-a880-4ed6-a62c-bf8cff315bfcccf616b2-7df8-41de-abbd-9f60c66943750b676d72-b1c5-4de8-b575-873647ab414b71fdbbe0-ab5e-493c-809c-4308e44926ddbff3bb30-81e6-4130-9e97-4c1559de2ac0bd43e785-a960-483c-96fd-cf4afacdcf9cf7a23d11-d594-4a2d-84da-2c38ffa2eabfd5e3fe04-82d5-47cf-875c-f7f422719d472eddd857-33ea-4f3d-a94e-be1652a0e5265496fd36-c0f4-4d4f-ba57-19d07433370f5e4e1554-1375-4196-9c82-5afc3f485796765abe44-b827-4e7a-aa3e-2454ca5dac38051bd21a-d2e0-48c7-8a0d-c81ed26d6821453197d1-589d-4b39-be89-0de3b1724003')'''
    cur.execute(sql_command)
    connection.commit()
    # Return
    return 0
    
def addUserLicenseNotStarted (connection, cur):
    # Adds a license with a start date in the future. This license starts on 1st Jan 2017. Will need to be changed for tests after that date!!!!!!
    sql_command= '''
    INSERT INTO [session_db].[dbo].[Licenses]
    VALUES ('PVG-test-license---Start-Date-Jan-1st-2017----------25c751be-6271-8210-d92c-794bfc42396a90438120-c459-4c6a-0C3C-55077eea64d0128b4bfd-6223a41eb-a2a9-a907de487ec0128b4bfd-ef43-4964-a157-472af0afab95beabeb25-4ca0-4570-ab1c-2d5b8c8a44a36da301f7-bcdd-4601-a37f-47b0370235d346a8af66-ba83-40a6-a7b8-903105441cee593f019d-e883-4f21-b6a7-b07be246e1eded8c1c0e-7691-4c2a-b0f0-8557e06fd6461a2431e9-e273-4266-90b1-70ee2f2054489c4e5c0c-f635-410e-a8ad-bad1867f4359ee3f8452-df90-428b-b580-af30ef1afaff01a27d33-65b1-47c8-878d-c1edd4e7f1da20fb5be4-234e-4cc1-a0e2-1fcd29be766879379c2e-bec0-49bc-b784-0da5a7aad5933c111963-d68e-475f-90e2-eabb5bf3508ffa437097-929c-49dc-97ac-c24aee203fbb1149d251-6abc-4ff0-8cba-78a674eb51ad5c878213-479f-4c14-bde8-594f3eef3d9a24e8a2f5-2b12-4a53-be3c-a9085ac091f9944a601d-3c9f-4741-84fb-1df26548136c2228688b-89e6-4d13-9d6d-e1cd1f9ed1a0d8b989d9-67ea-42cd-bc7e-715e1e81285e39566ebc-ce13-49f2-870e-f3704131320eca899724-341f-45a4-9332-d30590d415a449e13a68-4d42-4077-a1e2-a9141cb428597f4b5333-9c95-4490-bbf3-1afde93b4003')'''
    cur.execute(sql_command)
    connection.commit()
    # Return
    return 0
    
def addUserLicenseExpired (connection, cur):
    # Adds a license that has expired (ended 31st Aug 2016)
    sql_command= '''
    INSERT INTO [session_db].[dbo].[Licenses]
    VALUES ('PVG-test-license---End-Date-Aug-31st-2016-----------d2c0aa40-75d4-aa2d-d359-5665152a0a47a958d400-6874-4a56-0C3C-0a0717183a20120406ce-116ca455b-89e6-4b071e0e80a0120406ce-243b-4a2c-a490-d28aa0aaab45b9ab1be5-0f79-4b70-9204-c88e981592a9c3ab60bb-7466-4730-8058-c5b5cc5088667b376647-808d-400f-8272-617538cf638c93d1f7cb-9065-4807-80b8-0cf64fa13afa8eab27a3-9531-47a9-8e15-f431e5b9234179161e45-b080-444b-8832-8b2efd7aecdeaebce51f-b408-4a71-8b34-01b19e659c195ef54e93-168b-414b-836c-f271666b3fbffba49906-be01-499c-9eac-41331e22cdb3b4272c32-580e-4e58-b60e-e9387efaa1bd44d48520-c9ed-43b4-b441-557bd497c04ed345d6e2-76ab-4057-9e67-0261b90239cd788fc702-f2e9-4068-998e-c4c5a50566d5c2f8eb68-163a-4227-8205-57fab058274734d596c2-4ea8-4c2b-8036-3d2447e59e2b3f743815-8b5f-48e3-8a73-95ff7e8432494e62c6ed-00ad-4690-9d7a-c8f2a5bb2cc117db53cd-cbf8-40f7-9515-cc3f2e08c4fc1cf11c49-5dc7-4dca-9f89-0d78341906613dac56e6-3e65-4ab4-a950-f45a1556f09898723960-7986-4bd7-b21f-54d5fe41a7a20b3b9269-50c0-4028-81c6-78abe1c1d9499df03b67-072e-43fd-b8e0-4cdc2fa49003')'''
    cur.execute(sql_command)
    connection.commit()
    # Return
    return 0    
    
def addUserLicenseInvalidVersion (connection, cur):
    # Adds a license with the version number changed to be invalid. Version number set to 005
    sql_command= '''
    INSERT INTO [session_db].[dbo].[Licenses]
    VALUES ('PVG-test-license-for-10-users-----------------------4c624aa8-fae3-7777-7526-66f89ad725572f1e4df5-8018-4162-0C3C-e506a4a571f00adcda4b-222524f93-9287-db0704038e700adcda4b-7e59-4418-a1fe-74c66867270d76276303-0503-4450-8880-f774ebb452d0ae4b3902-0c6f-422c-898b-4c25a45fc386d93c49ed-f55d-496c-8e51-94dd9449f7910ac34a9d-e309-4009-a149-b7a1bc77dbfd2cfc16a3-584a-493d-b324-d32c487f4b29cccd43a0-24b3-438c-8cff-7c64900b1606ba89b037-9a90-4b53-b593-9cdf33976c6a58d6574e-5d55-465b-8047-9ed16fb006f98b54104d-0be5-4613-a72a-afe10321edee6f1fcf28-0476-4c91-9811-89cb8807bb1f51902f6d-ad00-459e-85eb-c90dac782b470cc2b49b-4f7c-47f2-a670-7449229fc6d43d1616a3-c7ab-4872-84fb-0b0085e36a532f3653a1-614d-40a4-b7bb-6f5375b587f20599cf2f-0ecf-4459-a02d-c697892fb32b410752b3-65f0-452e-b566-d41ab95cbc0ce6ddce77-4004-4f8b-bfb3-05faff1b50b6ba97da32-bf50-4f60-a6a3-3e6203333a851c6b2e56-5580-40a1-a252-4a62ec1e0fab425a6e20-f203-4d37-84e8-a0c42cb15062680e49c2-8973-4a0d-92b9-018f2e3cd570e16bb304-c53c-40e5-8d90-d82ba9084050e39fa0c1-6704-4001-9964-2037ea61a005')'''
    cur.execute(sql_command)
    connection.commit()
    # Return
    return 0
    
def addUserLicenseCorrupted (connection, cur):
    # Adds a license with random characters altered
    sql_command= '''
    INSERT INTO [session_db].[dbo].[Licenses]
    VALUES ('PVG-test-license-for-10-users-----------------------4c624aa8-fae3-7777-7526-66f89ad725572f1e4df5-8018-4162-0C3C-e506a4a571f00adcda4b-222524f93-9287-db0704038e700adcda4b-7e59-4418-a1fe-74c66867270d76276303-0503-4450-8880-f774ebb452d0ae4b3902-0c6f-422c-898b-4c25a45fc386d93c49ed-f55d-496c-8e51-94dd9449f7910ac34a9d-e309-4009-a149-b7a1bc77dbfd2cfc16a3-584a-493d-b324-d32c487f4b29cccd43a0-24b3-438c-8cff-7c64900b1606ba89b037-9a90-4b53-b593-9cdf33976c6a58d6574e-5d55-465b-8043-9ed16fb006b98b54104d-0be5-4613-a72a-afe10321edee6f1fcf28-0476-4c91-9811-89cb8807bb1f51902f6d-ad00-459e-85eb-c90dac782b470cc2b49b-4f7c-47f2-a670-7449229fc6d43d1616a3-c7ab-4872-84fb-0b0085e36a532f3653a1-614d-40a4-b7bb-6f5375b587f20599cf2f-0ecf-4459-a02d-c697892fb32b410752b3-65f0-452e-b566-d41ab95cbc0ce6ddce77-4004-4f8b-bfb3-05faff1b50b6ba97da32-bf30-4f60-a6a3-3e6203333a851c6b2e56-5580-40a1-a252-4a62ec1e0fab425a6e20-f203-4d37-84e8-a0c42cb15062680e49c2-8973-4a0d-92b9-018f2e3cd570e16bb304-c53c-40e5-8d90-d82ba9084050e39fa0c1-6704-4001-9964-2037ea61a003')'''
    cur.execute(sql_command)
    connection.commit()
    # Return
    return 0
    
def getNumberOfActiveUsers (connection, cur):
    # Returns the number of active users from the database
    sql_command= '''
    SELECT COUNT(*) 
    FROM [session_db].[dbo].[ActiveSessions]
    WHERE forcelogout = 0'''
    cur.execute(sql_command)
    count = int(str(cur.fetchall()[0][0]))
    return count

def getMaxConcurrentUsers (connection, cur):
    # Returns the max number of concurrent users from the database
    sql_command= """
    SELECT [Value]
    FROM [session_db].[dbo].[UMSettings]
    WHERE Setting = 'MaxConcurrentUsers'"""
    cur.execute(sql_command)
    count = int(str(cur.fetchall()[0][0]))
    return count
    
def isUserLoggedIn (connection, cur, user): 
    username = user.username
    sql_command= """
    SELECT COUNT(*)
    FROM [session_db].[dbo].[ActiveSessions]
    WHERE username = '""" + username + """'
    AND forcelogout = 0"""
    cur.execute(sql_command)
    count = int(str(cur.fetchall()[0][0]))
    if (count == 1):
        return True
    else:
        return False

def deleteLicencesTable (connection, cur): 
    # Delete the license table if it exists
    sql_command= """
    IF OBJECT_ID('[session_db].[dbo].[Licenses]', 'U') IS NOT NULL
    DROP TABLE [session_db].[dbo].[Licenses];"""
    cur.execute(sql_command)    
    connection.commit()

def createLicencesTable (connection, cur): 
    sql_command= 'CREATE TABLE [session_db].[dbo].[Licenses](license NCHAR(1024) NULL)'
    cur.execute(sql_command)    
    connection.commit()
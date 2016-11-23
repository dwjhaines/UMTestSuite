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
    VALUES ('PVG-test-license-for-5-users------------------------f279079b-800c-8bd0-8c35-a1481b2ada924eac47e6-083b-4578-0C3C-2906c03515c00c95d80b-4448a42b8-8e5f-cc077ef13fa00c95d80b-fca6-46fd-ac92-09e76c776811866860db-c869-4e11-84af-4a9d410362bd8debc300-3532-4988-8b2c-30ce4b930a83741bfd10-50e4-41e2-a12d-961dd560a57e52aeeed5-d595-4033-8f6c-cb3ca001b8bd3a443db5-82b6-43d7-9c6e-39395a728754797e81dd-f376-4ea0-93a6-6c502499890dab3c2144-63f3-4869-b0cc-3edd033af5da6516007b-a51b-43b9-8140-fc345354ad2a154d954c-07bb-4757-a6c5-bdbe7a625f71850be65d-2319-486a-80aa-723e47e0bc070e250c1d-3ffa-4d85-88c1-f3a212fe0ee1d503b002-b983-435d-808e-4df3f4a4451c8e88964b-4420-4d6a-99e7-a59afe5e7c9bde625965-d40a-4980-9916-57b891110a279ab0d496-1f11-4b58-b9d8-c35c6d5fe56c18f0f14a-7882-460c-80a6-92d77bff3d8b64d92c8e-0b0a-4ed9-a314-4afaa437272211c125b2-2641-41b0-b0be-e59f77526cc41fc5f9ee-91e1-4dde-b989-cdb65a12b4c8829eff37-742c-4db0-8686-42286541ed9063bcea92-ae6f-4315-81b7-4ed457c788abe3e15520-94ed-4f21-afc5-6c88f96e1ed0126346e5-555a-4318-acd6-7f829e079003')'''
    cur.execute(sql_command)
    connection.commit()
    # Return the number of users that can log in
    return 5
    
def addTenUserLicense (connection, cur):
    # Adds a license for ten users. Returns the number of licenses that have been added
    sql_command= '''
    INSERT INTO [session_db].[dbo].[Licenses]
    VALUES ('PVG-test-license-for-10-users-----------------------95cf2fa3-14af-0836-e1b6-d354b34d15c55b8a1ce4-914c-4600-0C3C-030728fd9e5013226094-8448a41c3-8d3e-ce07e7b9c83013226094-f7f6-4938-b98f-23bb49b53beec43c3de9-2dd3-4897-8cac-680d3d172fa2d8153de3-fe5c-457a-98cf-510097095047f220c321-1676-4f35-a5b8-eda081cfa97ee8b89b0c-3955-4d1b-9a0f-8657486d4c266342e9ea-1119-4928-8a15-70c27f147a3c08292cc4-4d45-4e36-9451-dc3e699598a7683fec7d-4ab9-4aa2-83ce-c7806d1542646b032d49-d4e5-45b8-81e9-058b32dc750299aab9ba-001b-42b1-8968-a91439f9d4025e74b60b-a5c9-4b1e-9d57-6f0a96d54910cb4c5f37-a2ed-478a-b35a-709bbec87dae2c5da6ac-7a58-4a3b-ac95-5635a45f4cd98e5f2b86-9eaf-4a51-8182-6f1c6378f6e8d9d41147-ebf6-4054-9515-2635e3d89170c8abf5ee-ba87-439d-aac9-a784030c91286ae8fdcd-67ef-430c-ad10-0086884f493ccbff002e-9340-4bcc-ad7c-267fc232d0d623abce08-6165-4341-a6e3-f346dbfd0a6f30d2b969-dec1-4b63-96ec-60e84faf2386c4b14c3d-5bf2-4935-b5fa-9d04ec857610dfc49b19-c91b-4743-b35f-221f39561289a661fad9-7004-488a-a69f-3edbbee3c60aca8d6e24-d4f2-4fb8-a79b-46ecfa43e003')'''
    cur.execute(sql_command)
    connection.commit()
    # Return the number of users that can log in
    return 10
    
def addTwentyFiveUserLicense (connection, cur):
    # Adds a license for twenty-five users. Returns the number of licenses that have been added
    sql_command= '''
    INSERT INTO [session_db].[dbo].[Licenses]
    VALUES ('PVG-test-license-for-25-users-----------------------e6d40fc5-0fac-18fb-e6d5-db49bddf3acdd13ddee5-2ff3-4c14-0C3C-7a072f286c2013850d71-2448a4094-a59b-6007ede4960013850d71-3882-480d-b914-054b83b8dc28c7dc773c-f3e0-472b-924b-4fef790eacaacaeee3c4-bfe4-42c9-9baa-23699ad82e823db6ea6a-6571-4ab1-8c0e-b9ab0d4e5ca445303853-8a84-43b2-9e74-c492c0f4b6760f9a886c-1655-4e66-b4cf-1bfa7fd6aba5afaeaba9-3c82-425c-a98b-375b8a2b0b7ec200c7c1-5113-40c3-b324-1c785c78c58c2ca7abad-2259-4863-9d74-42bc9b5a333a143b121f-a7d7-4449-93c1-0790332d33eef91ac2b9-429f-49e7-ac3d-4b2d234a0ed4afefd1af-d87f-411c-9eed-25c7ec0c614f0ee11394-f02e-460f-92b8-a34852fcd554ce82d190-9c88-463c-abbb-253949fa839b95f388e6-698e-4964-9669-113ba841c8b56c8224d9-6e56-4b79-b90f-8de9bbe118beabff22df-5015-49ba-a59e-89270f2db0231c93f751-c639-44a2-bf7a-1cacb5c42717d25d806a-cca8-4ac9-990a-27bbb3d8f21f20df0dce-c73c-4405-81c4-de0d0b46652b59c54758-5004-4721-a337-1cd67a48487e6df1aafc-2f12-4850-8751-15db96c8469c3a06e594-58a8-4c6b-a877-6061cc2aa3d16d606c95-fd0a-46e0-ad65-fcf434a77003')'''
    cur.execute(sql_command)
    connection.commit()
    # Return the number of users that can log in
    return 25
    
def addUserLicenseIncorrectIPAddress (connection, cur):
    # Adds a license with an incorrect IP address. i.e. one that is not 10.165.250.251
    sql_command= '''
    INSERT INTO [session_db].[dbo].[Licenses]
    VALUES ('PVG-test-license-Incorrect-IP-Address---------------45684c5b-9361-d5ea-7b93-7443424f4a655fbc11bc-e54c-4875-0C3C-ff06ab8576100b4ade10-a448a44e8-9705-88076a419ff00b4ade10-bd3a-4c0c-a8a1-4b06a96b374e7a37a4ae-1069-4813-a99c-329a41e78e9137279312-f9b6-45e3-9174-ced82b3377933f8d9709-e01d-40f4-b1e4-23c50065d3ae7f46bcc2-7dc4-4440-82a6-42e317fcf19504a02eae-9449-454c-8f0b-396dd9e9912799d07eec-d617-4367-8165-6c6423e2b0cc5f9e7d5c-6678-4eb4-b877-e9d51ab7c1e836081f38-f539-4e42-b9ba-c5e85b9923a09cc3a357-c0a0-406a-a5e3-bf967552bc22f2a6033e-afab-464d-b2e2-4dd8d86b554756e4c883-5405-470f-99ab-d6909df777274403cabf-02e3-4b9b-abc9-f9cf9e547fbfcab1d580-7433-48bf-8a26-7298313e51cf29d26677-00b2-4df2-8762-5974cdb39840036fc97e-1c6e-47da-afd9-71c47415923e7bce460c-4db8-4562-a622-f234e7bf4b26748fee33-5078-4823-a4f4-40fb5917015e907226ec-13a3-4689-9dbb-a2566136fcdfee00febb-6215-4f34-b826-264067385792107672ab-4c3f-411c-9047-0c5623c8022b661abef1-1a6e-488f-8ec1-760e6eae8f1e26358df4-538c-4b33-be03-980ebc5e31b92947ecae-a997-4862-b10f-03ff24423003')'''
    cur.execute(sql_command)
    connection.commit()
    # Return
    return 0
    
def addUserLicenseNotStarted (connection, cur):
    # Adds a license with a start date in the future. This license starts on 1st Jan 2017. Will need to be changed for tests after that date!!!!!!
    sql_command= '''
    INSERT INTO [session_db].[dbo].[Licenses]
    VALUES ('PVG-test-license---Start-Date-Jan-1st-2017----------7488f34f-5c85-91cd-9b4f-ad860b7b969e59be096e-eb26-4f64-0C3C-f20731d095a00db9af09-a223a49cc-b8fa-3107912eaf800db9af09-78a7-4732-a4f0-faa8188228bd91290c65-86cd-4762-8064-fa04495e4030981dc08c-2146-455a-816b-99f908592bd92b789af5-4dbe-40e5-bff2-aa9c4bc29b665dd1964c-ebd0-49f5-89c7-3e196ddd1793cbda5a87-bbc6-48a3-9669-337ab6242577243627f0-bbeb-4fda-9917-4f71b9c4599dacfb8652-0e66-417f-888a-fe14289650939d4c00dd-0538-4be7-aa29-f7d7b88b3a715cbe2cbc-bdad-4dc9-9d88-dbb529fe5632c378b3ec-8729-4365-86b8-8aabf53389e07640f3a4-359c-4880-a0db-4b327f873aa95d880a4b-27fb-4656-8b4e-766fc20bae9e22ebc32a-48b8-40b4-b856-1925a4dfa0d497903942-3ba6-470e-acee-f71fef22d172437c4360-c38f-4205-95ce-807dbb62a506d306e749-ec47-4057-90f5-a8970990b202edd30d35-fa3c-4d8b-a437-502fa9c70a45d6f2d9a4-ad47-4db5-be49-cb8a05b69b1f7fed8f30-9290-47a1-9a85-3d4ae57211b69e3de01a-a70a-4a37-831e-0fcb6ade7958c18c48dc-581a-4139-96ab-89df1ed04ee282758b19-d391-4b97-8512-7fbaffd58bd6a77c1c00-d405-40fb-95f4-d3529c84f003')'''
    cur.execute(sql_command)
    connection.commit()
    # Return
    return 0
    
def addUserLicenseExpired (connection, cur):
    # Adds a license that has expired (ended 31st Oct 2016)
    sql_command= '''
    INSERT INTO [session_db].[dbo].[Licenses]
    VALUES ('PVG-test-license---End-Date-Oct-31st-2016-----------d55c850a-4174-292b-6ee6-b6aaef11a5a8e16d2146-30eb-4fac-0C3C-98069c6efc300a597672-91c9a4153-a82b-f406a5f86e100a597672-c6f7-4752-b99c-26561a6246bf71470e3d-10c9-4467-8906-4cb1c028f39f06bfc546-2c2a-4abe-8892-7040e4509a793ec85397-d066-4892-80e3-999053e2dccc3e39a205-fdc4-4b6b-b91d-07e7b8116ef4c9ee329a-9d93-427b-aab0-79be1212220bb9f48cf4-94fe-4a37-a40a-8bc493a8f16c34aa129f-64cb-4fac-9d3f-4ff46fb79846e1f6b124-338c-4360-b784-de211f2f54bdc8a4ee1d-e2d4-46c6-b754-10f2a7248e1f4d292abb-a141-44c6-a26f-da063509f604463af6a1-1d33-404c-afb4-d12b10be3b450247a01f-6218-41b8-b46b-1392654af6c3044791c4-ab79-4e14-a909-77a534cc9b74eeb5c0c2-56ee-4732-892e-03394063d919b93829a3-2862-4c4e-b7a7-31db71a8be0196968b6a-ca4c-414b-bfb6-f81ec7a28d7f6597db70-5752-4c84-8b94-1c2c1654c4ef824ae41e-309f-43ff-9811-8f7fd53883965f0ae96a-3a95-445c-a169-b6d9a2c9ba93b0f2b823-f8f0-4b20-baa3-bc171d392551bc308620-672a-444c-9678-a8eed4d0aa2b48ebc49a-1ecf-469c-a55b-c4eb2edbafdbdf1e5b9e-1cfb-4702-811e-e5a3f54ac003')'''
    cur.execute(sql_command)
    connection.commit()
    # Return
    return 0    
    
def addUserLicenseInvalidVersion (connection, cur):
    # Adds a license with the version number changed to be invalid. Version number set to 005
    sql_command= '''
    INSERT INTO [session_db].[dbo].[Licenses]
    VALUES ('PVG-test-license---Invalid-Version------------------f82fdad8-03e2-40cb-41fd-d043b1a410c295a6ab67-a69f-486a-0C3C-03066505294006e2d943-d448a496f-a6b8-b60723c1532006e2d943-33b1-4dc3-85af-c4840f4194b450950324-23fc-4e4a-b264-457402b389f09f64270a-7c59-4b3f-91ed-59e4a983855dda49d203-ac90-4aa6-8dac-84f84738c27e57e0c74b-4a7f-46c0-b287-f775262d0984e4abfc19-f2b0-4b8b-baed-2486c19a8824147d477c-9472-44be-944d-c4bed9c3c5b8c743be5e-650b-4e41-9c5b-f2f45a5fad98ce489df7-93f0-4322-b7a6-a21f921c36d520662ba7-6ab3-49b9-8976-0dfc9ec57748a23fcc1c-05eb-448b-ba53-fee660307b83174f261e-d800-4df3-8971-aa17d63e109203299c19-cbd3-4e80-927a-8081601819bbe641626d-a5c9-4e46-bf09-59ea3eb810e943b3975f-a8a3-4ddc-adab-67142e70bbaf4c9d004b-d126-4249-b8be-339fbba2b20de3eda92f-0947-4abf-9d72-a6f23ee18e40b9062a29-976a-424e-adf8-95ec7ac5ee8b2cfc0561-6c24-48b8-9b70-a6f42e8324734dd32255-ab44-41cf-acf4-8b2107d932b65b1f561a-d2c1-4ae7-ad14-560d3bdccfbd90800203-e4c0-4125-9cdf-20b102fc5b310eae2faa-3d8f-411d-8ff7-ee1261bafc3e40381178-7065-4734-8d1e-9f67ef164005')'''
    cur.execute(sql_command)
    connection.commit()
    # Return
    return 0
    
def addUserLicenseCorrupted (connection, cur):
    # Adds a license with random characters altered
    sql_command= '''
    INSERT INTO [session_db].[dbo].[Licenses]
    VALUES ('PVG-test-license---Corrupted------------------------1592c39c-1c36-63b3-a421-ab3eca7d669ca6460e4d-1107-4582-0C3C-bf06bbb6b2f00c4df1de-f448a482b-ad6c-b4077a72dcd00c4df1de-1d19-4e1c-b9dc-a2474174b7e683b83515-3834-4d67-a8db-9e963dd72ee2119e2795-de87-4f5a-b637-4f116a18d9022e01d930-5d08-4447-dba3-b6ab46ba9145fef08801-8031-4b50-af4e-f150ec4bccfa69856372-f8c0-75eb-bda4-38a348387f1de2d2a79a-4b12-4ad3-9eb6-cde0252a316fe11582a0-094f-46fd-b953-a5f1ff39874df6b6c868-0e82-49ff-b072-b8fc5a6118ca6622adce-4a59-4bc9-9e71-ce4e0d28570e688a54e6-b1a6-488a-8b07-4a6cf08e53da7cf760e2-396c-4a89-b719-fb2e50cbe5b95701dc93-fc46-4c9d-ab2f-01b3528061b608b1182f-4d99-4221-ad38-72e820dbfeedea791796-14b1-4217-a4f0-5b816156ee3aad418c8a-fd18-4f0e-90cc-66de501d47da0faa5441-0d9a-4dfe-ac00-993beaff31b9d216876b-46ce-492b-aae5-83257f7eba1f4fe5be22-8e3e-49c8-9805-10994e91a95fae5ec6b7-111c-402f-be76-a7c1887eccb24db24ec0-232e-4bf8-a492-d24c56a4919114b577aa-8db6-4fa4-a928-8eaa7f8e3f2d9d4159ec-572e-4206-aada-974de9b8bebaa342382b-713a-424d-86e1-c6acc0883003')'''
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
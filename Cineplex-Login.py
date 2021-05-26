from selenium import webdriver
try:
        with open('credentials.txt', 'r') as credentialFile:
                credentialList = credentialFile.readlines()
                storedUsername = str(credentialList[0])
                storedPassword = str(credentialList[1])

                browser = webdriver.Chrome()
                browser.get(('https://t11.ultipro.ca/Login.aspx?ReturnUrl=%2f'))

                browser.find_element_by_id('ctl00_Content_Login1_UserName').send_keys(storedUsername)
                browser.find_element_by_id('ctl00_Content_Login1_Password').send_keys(storedPassword)
                browser.find_element_by_id('ctl00_Content_Login1_LoginButton').click()

                browser.get(('https://t11.ultipro.ca/Customs/CNPLX/Pages/View/WorkBrainSSO.aspx?USParams=PK=ESS!MenuID=81!PageRerId=5000005!ParentRerId=81!wbsso=employee!environment=production'))

                browser.get(('https://workbrain.cineplex.com/etm/time/timesheet/etmTnsMonth.jsp?selectedTocID=181&parentID=10'))
  
except IOError:
        print("Could not open credentials.txt")

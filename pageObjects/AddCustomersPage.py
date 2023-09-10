import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium import webdriver

class AddCustomer():
    #Add Customer Page
    link_Customers_Menu_Xpath = "/html/body/div[3]/aside/div/div[4]/div/div/nav/ul/li[4]/a/p"
    link_Customers_MenuItem_Xpath = "/html/body/div[3]/aside/div/div[4]/div/div/nav/ul/li[4]/ul/li[1]/a/p"
    btn_AddNew_Xpath = "//a[@class='btn btn-primary']"
    txt_Email_Xpath = "//input[@id='Email']"
    txt_Password_Xpath = "//input[@id='Password']"
    txt_FirstName_Xpath = "//input[@id='FirstName']"
    txt_LastName_Xpath = "//*[@id='LastName']"
    rd_Btn_Male_Xpath = "//input[@id='Gender_Male']"
    rd_Btn_FeMale_Xpath = "//input[@id='Gender_Female']"
    txt_Dob_Xpath = "//input[@id='DateOfBirth']"
    txt_CompanyName_Xpath = "//input[@id='Company']"
    is_Tax_Exempt_Xpath = "//*[@id='IsTaxExempt']"
    txt_NewsLetter_Xpath = "//*[@id='customer-info']/div[2]/div[9]/div[2]/div/div[1]/div/div"
    txt_YourSoreName_Xpath = "//*[@id='42301337-7982-4b3e-891e-425eec6ec992']"
    txt_TestStore2_Xpath = "//*[@id='SelectedNewsletterSubscriptionStoreIds_listbox']/li[2]"
    txt_CompanyRoles_Xpath = "//*[@id='customer-info']/div[2]/div[10]/div[2]/div/div[1]/div/div"
    lstItem_Registered_Xpath = "//*[@id='SelectedCustomerRoleIds_taglist']/li/span[2]"
    lstItem_Administrators_Xpath = "//*[@id='SelectedCustomerRoleIds_listbox']/li[1]"
    lstItem_ForumModerators_Xpath = "//*[@id='SelectedCustomerRoleIds_listbox']/li[2]"
    lstItem_Guests_Xpath = "//*[@id='SelectedCustomerRoleIds_listbox']/li[3]"
    lstItem_Vendor_Xpath = "//*[@id='SelectedCustomerRoleIds_listbox']/li[5]"
    drpmg_Vendor_Xpath = "//select[@id='VendorId']"
    txt_isActive_Xpath = "//*[@id='Active']"
    txt_AdminContent_Xpath = "//*[@id='AdminComment']"
    btnSave_Xpath = "/html/body/div[3]/div[1]/form/div[1]/div/button[1]"


    def __init__(self,driver):
        self.driver = driver

    def clickOnCustomersMenu(self):
        self.driver.find_element(By.XPATH, self.link_Customers_Menu_Xpath).click()

    def clickOnCustomersMenuItem(self):
        self.driver.find_element(By.XPATH, self.link_Customers_MenuItem_Xpath).click()

    def clickOnAddNew(self):
        self.driver.find_element(By.XPATH, self. btn_AddNew_Xpath).click()

    def setMail(self,email):
        self.driver.find_element(By.XPATH, self.txt_Email_Xpath).send_keys(email)

    def setPassword(self,password):
        self.driver.find_element(By.XPATH, self.txt_Password_Xpath).send_keys(password)

    def setFirstName(self,fname):
        self.driver.find_element(By.XPATH, self.txt_FirstName_Xpath).send_keys(fname)

    def setLastName(self,lname):
        self.driver.find_element(By.XPATH, self.txt_LastName_Xpath).send_keys(lname)

    def setGender(self,gender):
        if gender == 'Male':
            self.driver.find_element(By.XPATH, self.rd_Btn_Male_Xpath).click()
        elif gender == 'Female':
            self.driver.find_element(By.XPATH, self.rd_Btn_FeMale_Xpath).click()
        else:
            self.driver.find_element(By.XPATH, self.rd_Btn_Male_Xpath).click()

    def setDob(self,dob):
        self.driver.find_element(By.XPATH,self.txt_Dob_Xpath).send_keys(dob)

    def setCompanyName(self,comname):
        self.driver.find_element(By.XPATH,self.txt_CompanyName_Xpath).send_keys(comname)

    def setTaxexempt(self):
        self.driver.find_element(By.XPATH, self.is_Tax_Exempt_Xpath).click()

    def setNewsLetter(self,value):
        self.driver.find_element(By.XPATH, self. txt_NewsLetter_Xpath).click()
        time.sleep(3)
        if value == 'Your store name':
            self.driver.find_element(By.XPATH, self.txt_YourSoreName_Xpath).click()
        else:
            self.driver.find_element(By.XPATH, self.txt_TestStore2_Xpath).click()

    def setCustomerRoles(self,role):
        self.driver.find_element(By.XPATH, self.txt_CompanyRoles_Xpath).click()
        time.sleep(3)
        if role == 'Registered':
            self.listItem = self.driver.find_element(By.XPATH, self.lstItem_Registered_Xpath)
        elif role == 'Administrators':
            self.listItem = self.driver.find_element(By.XPATH,self.lstItem_Administrators_Xpath)
        elif role == 'Forum Moderators':
            self.listItem = self.driver.find_element(By.XPATH,self.lstItem_ForumModerators_Xpath)
        elif role == 'Guests':
            self.driver.find_element(By.XPATH, self.lstItem_Registered_Xpath).click()
            self.listItem = self.driver.find_element(By.XPATH, self.lstItem_Guests_Xpath)
        elif role == 'Registered':
            self.listItem = self.driver.find_element(By.XPATH, self.lstItem_Registered_Xpath)
        elif role == 'Vendors':
            self.listItem = self.driver.find_element(By.XPATH, self.lstItem_Vendor_Xpath )
        else:
            self.listItem = self.driver.find_element(By.XPATH, self.lstItem_Guests_Xpath)

        time.sleep(3)
        self.driver.execute_script('arguments[0].click()' ,self.listItem)

    def setManagerOfVendor(self,value):
        drp = Select(self.driver.find_element(By.XPATH, self.drpmg_Vendor_Xpath))
        drp.select_by_visible_text(value)

    def setAdminContent(self,content):
        self.driver.find_element(By.XPATH,self.txt_AdminContent_Xpath).send_keys(content)

    def setActive(self):
        self.driver.find_element(By.XPATH, self.txt_isActive_Xpath).click()

    def clickOnSave(self):
        self.driver.find_element(By.XPATH,self.btnSave_Xpath).click()


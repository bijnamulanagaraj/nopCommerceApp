import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium import webdriver

class SearchCustomer():
    # Add Customer Page
    txt_email_Xpath = "//*[@id='SearchEmail']"
    txt_firstName_Xpath = "//*[@id='SearchFirstName']"
    txt_lastName_Xpath = "//*[@id='SearchLastName']"
    btn_search_Xpath = "//*[@id='search-customers']"
    table_Xpath = "//*[@id='customers-grid_wrapper']/div[1]/div"
    tabel_rows_Xpath = "//*[@id='customers-grid']//tbody//tr"
    table_column_Xpath = "//*[@id='customers-grid']//tbody//tr//td"

    def __init__(self,driver):
        self.driver = driver

    def setEmail(self,email):
        self.driver.find_element(By.XPATH, self.txt_email_Xpath).clear()
        self.driver.find_element(By.XPATH, self.txt_email_Xpath).send_keys(email)

    def setFirstName(self,fname):
        self.driver.find_element(By.XPATH, self.txt_firstName_Xpath).clear()
        self.driver.find_element(By.XPATH, self.txt_firstName_Xpath).send_keys(fname)

    def setLastName(self,lname):
        self.driver.find_element(By.XPATH, self.txt_lastName_Xpath).clear()
        self.driver.find_element(By.XPATH, self.txt_lastName_Xpath).send_keys(lname)

    def clickSearch(self):
        self.driver.find_element(By.XPATH, self.btn_search_Xpath).click()

    def getNoRows(self):
        return len(self.driver.find_elements(By.XPATH,self.tabel_rows_Xpath))

    def getNoColumns(self):
        return len(self.driver.find_elements(By.XPATH,self.table_column_Xpath))

    def searchCustomerByEmail(self,email):
        flag = False
        for r in range(1,self.getNoRows()+1):
           table =  self.driver.find_element(By.XPATH,self.table_Xpath)
           emailId = table.find_element(By.XPATH,"//*[@id='customers-grid']/tbody/tr["+ str(r) +"]/td[2]").text
           if emailId == email:
               flag = True
               break
        return flag

    def searchCustomerByName(self,Name):
        flag = False
        for r in range(1,self.getNoRows()+1):
           table =  self.driver.find_element(By.XPATH,self.table_Xpath)
           name = table.find_element(By.XPATH,"//*[@id='customers-grid']/tbody/tr[" +str(r) + "]/td[3]").text
           if name == Name:
               flag = True
               break
        return flag
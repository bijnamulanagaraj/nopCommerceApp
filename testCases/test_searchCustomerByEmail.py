import time
import pytest
import string
import random
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pageObjects.LoginPage import LoginPage
from pageObjects.AddCustomersPage import AddCustomer
from pageObjects.SearchCustomerPage import SearchCustomer
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen

class Test_SearchCustomerByEmail_004():
    baseURL = ReadConfig.getApplicationUrl()
    username = ReadConfig.getUserEmail()
    password = ReadConfig.getPasword()

    logger = LogGen.loggen()

    @pytest.mark.regression
    def test_customerByEmail(self,setup):
        self.logger.info("*** SearchCustomerByEmail_004 ***")
        self.logger.info("*** Verifying Customer ***")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.driver.maximize_window()
        self.lp = LoginPage(self.driver)
        self.lp.setUserName(self.username)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()
        self.logger.info("*** Login Successful ***")
        self.logger.info("*** Start Search Customer By Email ***")
        self.addCust = AddCustomer(self.driver)
        self.addCust.clickOnCustomersMenu()
        self.addCust.clickOnCustomersMenuItem()
        self.logger.info("*** searching Customer By emailID ***")
        searchCust = SearchCustomer(self.driver)
        searchCust.setEmail('admin@yourStore.com')
        searchCust.clickSearch()
        time.sleep(3)
        status = searchCust.searchCustomerByEmail('admin@yourStore.com')
        time.sleep(5)
        assert True == status
        self.logger.info("*** Tc_SearchCustomerByEmail_004 Finished ***")
        self.driver.close()



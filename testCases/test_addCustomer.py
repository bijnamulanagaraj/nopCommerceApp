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
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen

class Test_003_AddCustomer():
    baseURL = ReadConfig.getApplicationUrl()
    username = ReadConfig.getUserEmail()
    password = ReadConfig.getPasword()

    logger = LogGen.loggen()

    @pytest.mark.sanity
    def test_addCustomer(self, setup):
        self.logger.info("*** Test_003_AddCustomer ***")
        self.logger.info("*** Verifying Customer Module ***")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.driver.maximize_window()
        self.lp = LoginPage(self.driver)
        self.lp.setUserName(self.username)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()
        self.logger.info("*** Login Successful ***")
        self.logger.info("*** Start Add Customer Test ***")
        self.addCust = AddCustomer(self.driver)
        self.addCust.clickOnCustomersMenu()
        self.addCust.clickOnCustomersMenuItem()
        self.addCust.clickOnAddNew()
        self.logger.info("*** Providing Customer Info ***")

        self.email = random_generator() + '@gmail.com'
        self.addCust.setMail(self.email)
        self.addCust.setPassword('test123')
        self.addCust.setFirstName('Nagaraj')
        self.addCust.setLastName('Bijnamula')
        self.addCust.setGender('Male')
        self.addCust.setDob('04/06/1994')
        self.addCust.setCompanyName('Chemol Technologies India Pvt Ltd')
        self.addCust.setTaxexempt()
        self.addCust.setNewsLetter('Test store 2')
        self.addCust.setCustomerRoles('Guests')
        self.addCust.setManagerOfVendor('Vendor 2')
        self.addCust.setAdminContent('This is for Testing')
        self.addCust.setActive()
        self.addCust.clickOnSave()
        time.sleep(3)
        self.logger.info("*** Saving Customer Info ***")

        self.logger.info("*** Add Customer Validation Started ***")
        self.msg = self.driver.find_element(By.TAG_NAME,'body').text

        if 'The new customer has been added successfully.' in self.msg:
            assert True == True
            self.logger.info("*** Add Customer Test Passed ***")
        else:
            self.driver.save_screenshot(".\\Screenshots\\" + "test_addCustomer_scr.png")
            self.logger.error("*** Add Customer Test Failed ***")
            assert True == False

        self.driver.close()
        self.logger.info("*** Ending Test_003_AddCustomer Test ***")


def random_generator(size=8, chars=string.ascii_lowercase + string.digits):
    return ''.join(random.choice(chars) for x in range(size))


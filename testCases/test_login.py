import time
import pytest
from selenium import webdriver
from pageObjects.LoginPage import LoginPage
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen

class Test_001_Login():
    baseURL = ReadConfig.getApplicationUrl()
    username = ReadConfig.getUserEmail()
    password = ReadConfig.getPasword()

    logger = LogGen.loggen()

    @pytest.mark.regression
    def test_home_PageTitle(self,setup):
        self.logger.info("*** Test_001_Login ***")
        self.logger.info("*** Verifying Home Page Title ***")
        self.driver = setup
        self.driver.get(self.baseURL)
        act_title = self.driver.title
        if act_title == "Your store. Login":
            assert True
            self.driver.close()
            self.logger.info("***  Home Page Title test is passed ***")
        else:
            self.driver.save_screenshot(".\\Screenshots\\" + "test_home_PageTitle.png")
            self.driver.close()
            self.logger.error("***  Home Page Title test is failed ***")
            assert False

    @pytest.mark.sanity
    @pytest.mark.regression
    def test_Login(self,setup):
        self.logger.info("*** Verifying Login Test ***")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.lp = LoginPage(self.driver)
        self.lp.setUserName(self.username)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()
        act_title = self.driver.title
        if act_title == "Dashboard / nopCommerce administration":
            assert True
            self.logger.info("*** Login test is passed ***")
            self.driver.close()
        else:
            self.driver.save_screenshot(".\\Screenshots\\" + "test_Login.png")
            self.logger.error("*** Login test is failed ***")
            self.driver.close()
            assert False

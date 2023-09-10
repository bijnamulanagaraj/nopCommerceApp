from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from utilities.customLogger import LogGen

import pytest

@pytest.fixture()
def setup(browser):
    if browser == "chrome":
        serv_obj = Service("C:\\Drivers\\chromedriver-win64\\chromedriver-win64\\chromedriver.exe")
        driver = webdriver.Chrome(service=serv_obj)
        print(" *** Launching Chrome browser *** ")
    elif browser == "firefox":
        serv_obj = Service("C:\\Drivers\\geckodriver-v0.33.0-win64\\geckodriver.exe")
        driver = webdriver.Firefox(service=serv_obj)
        print(" *** Launching Firefox browser *** ")
    else:
        serv_obj = Service("C:\\Drivers\\edgedriver_win64\\msedgedriver.exe")
        driver = webdriver.ChromiumEdge(service=serv_obj)
        print(" *** Launching MicroSoft Edge browser *** ")

    return driver


def pytest_addoption(parser): # This will get the value from CLI/Hooks
    parser.addoption("--browser")

@pytest.fixture()
def browser(request): # This will return the Browser value to Setup method
    return request.config.getoption("--browser")

##### Pytest HTML Reports #####


# It is hook for adding Enviornment info to HTML Report
def pytest_configure(config):
    config._metadata = {
        "Project Name": "nop Commerce",
        "Module Name": "Customers",
        "Autoamtion Tester": "Nagaraj Bijnamula"
    }







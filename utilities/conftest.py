import pytest
from selenium import webdriver
from utilities.readProperties import ReadConfig

@pytest.fixture()
def setup(browser):
    if browser=='chrome':
        driver=webdriver.Chrome("C:\\Users\\bahti\\PycharmProjects\\pythonProject\\GranularTest\\Driver\\chromedriver.exe")
        print("Launching chrome browser.........")
    elif browser=='edge':
        driver = webdriver.Edge("C:\\Users\\bahti\\PycharmProjects\\pythonProject\\GranularTest\\Driver\\msedgedriver.exe")
        print("Launching edge browser.........")
    else:
        driver=webdriver.Chrome("C:\\Users\\bahti\\PycharmProjects\\pythonProject\\GranularTest\\Driver\\chromedriver.exe")
    return driver

def pytest_addoption(parser):    # This will get the value from CLI /hooks
    parser.addoption("--browser")
########### pytest HTML Report ################

# It is hook for Adding Environment info to HTML Report
def pytest_configure(config):
    config._metadata['Project Name'] = 'Google Search'
    config._metadata['Module Name'] = 'Search for Granular'
    config._metadata['Tester'] = 'Bahtiyar'

# It is hook for delete/Modify Environment info to HTML Report
@pytest.mark.optionalhook
def pytest_metadata(metadata):
    metadata.pop("JAVA_HOME", None)
    metadata.pop("Plugins", None)
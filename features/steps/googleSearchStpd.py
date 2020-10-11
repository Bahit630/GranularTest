from behave import *
from selenium.webdriver.common.keys import Keys
from utilities.readProperties import ReadConfig
from selenium import webdriver


baseURL = ReadConfig.getURL()



@given('launch chrome browser')
def launchBrowser(context):
    options = webdriver.ChromeOptions()
    options.add_experimental_option("detach", True)
    context.driver = webdriver.Chrome(chrome_options=options)
    context.driver.maximize_window()


@when('Open the google search page')
def openGoogle(context):

    context.driver.get(baseURL)


@then('User searches for "{value}"')
def search(context,value):

    context.driver.find_element_by_name("q").send_keys(value + Keys.ENTER)

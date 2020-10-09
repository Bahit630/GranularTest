from behave import *
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from pageObjects.googleSearchPage import googlePage
from utilities.readProperties import ReadConfig
from selenium import webdriver

baseURL = ReadConfig.getURL()

        
@given('launch chrome browser')
def launchBrowser(context):

    context.driver = webdriver.Chrome()


@when('Open the google search page')
def openGoogle(context):

    context.driver.get(baseURL)



@then('User searches for Granular')
def search(context):

    context.driver.find_element_by_name("q").send_keys("Granular"+ Keys.ENTER)



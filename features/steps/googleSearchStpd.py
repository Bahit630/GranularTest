from behave import *
from selenium.webdriver.common.keys import Keys
from utilities.readProperties import ReadConfig
from selenium import webdriver
from pages.googel_page import google_seach_page

baseURL = ReadConfig.getURL()


@given('Open the google search page')
def openGoogle(context):
    context.driver.get(baseURL)


@then('User searches for "{value}"')
def search(context, value):
    context.driver.find_element_by_name(google_seach_page.search_box_name).send_keys(value + Keys.ENTER)

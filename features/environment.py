from selenium import webdriver
from utilities.readProperties import ReadConfig


def before_feature(context, feature):
    browser = ReadConfig.getBrowser()
    if browser == 'chrome':

        options = webdriver.ChromeOptions()
        options.add_experimental_option("detach", True)
        context.driver = webdriver.Chrome(chrome_options=options)
        context.driver.maximize_window()
        context.driver.implicitly_wait(5)

    if browser == 'edge':
        context.driver = webdriver.Edge()
        context.driver.maximize_window()
        context.driver.implicitly_wait(5)

    if browser == 'firefox':
        context.driver = webdriver.Firefox()
        context.driver.maximize_window()
        context.driver.implicitly_wait(5)

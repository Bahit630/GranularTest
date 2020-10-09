from selenium import webdriver
from selenium.webdriver.common.keys import Keys


class googlePage:

    searchBox_name = "q"


    def __init__(self,driver):
        self.driver=driver

    def setSearchBox(self):
        self.driver.find_element_by_id(self.searchBox_name).clear()
        self.driver.find_element_by_id(self.searchBox_name).send_keys("Granular"+ Keys.ENTER)


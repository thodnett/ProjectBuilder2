from selenium.webdriver import Chrome
from selenium import webdriver 
from Library import config_reader

def startBrowser():
    global driver
    driver=webdriver.Chrome()
    driver.get(config_reader.read_configData('Details', 'Application_URL'))
    return driver

def closeBrowser():
    driver.close()
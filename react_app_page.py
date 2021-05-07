from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys


CHROMEDRIVER_PATH = '../chromedriver_linux64/chromedriver'
URL = 'http://ec2-54-208-152-154.compute-1.amazonaws.com'

def open_page():
    ''' Opens google chrome to the webpage for the scaling simulation and maxamizes the window '''

    chrome_driver = webdriver.Chrome(CHROMEDRIVER_PATH)
    
    chrome_driver.get(URL)
    chrome_driver.maximize_window()

    return chrome_driver


def click_weigh_button(driver):
    ''' Clicks the weigh button '''

    button = driver.find_element_by_id('weigh')
    button.click()


def click_reset_button(driver):
    '''Clicks the reset button'''

    button = driver.find_element_by_xpath('/html/body/div/div/div[1]/div[4]/button[1]')
    button.click()
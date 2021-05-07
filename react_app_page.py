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


def get_measure_results(driver):
    ''' Gets the measure results (field between the bowls)'''

    button = driver.find_element_by_xpath('/html/body/div/div/div[1]/div[2]/button')
    results = button.text

    return results


def fill_bowl_grid_box(driver, grid, box_number, bar_number):
    ''' 
        Puts the value of 'bar_number' into 'box_number' on 'gird'
        
        Parameters:
            grid : str 
                which bowl the bar number should be put in 'left' or 'right'
            
            box_number : int
                box number that the bar number should be put into boxes are numbered right to left top to bottom and are zero indexed 

            bar_number : int
                the number that will be typed into the field 
    '''

    cell = driver.find_element_by_id('{}_{}'.format(grid, box_number))
    cell.send_keys(bar_number)
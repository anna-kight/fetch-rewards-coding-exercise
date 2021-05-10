from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait

CHROMEDRIVER_PATH = "./chromedriver"
URL = "http://ec2-54-208-152-154.compute-1.amazonaws.com"

# allert message strings
ALLERT_MESSAGE_RIGHT = "Yay! You find it!"
ALLERT_MESSAGE_WRONG = "Oops! Try Again!"

# bowls
LEFT = "left"
RIGHT = "right"


def open_page():
    """ Opens google chrome to the webpage for the scaling simulation and maxamizes the window """

    chrome_driver = webdriver.Chrome(CHROMEDRIVER_PATH)

    chrome_driver.get(URL)
    chrome_driver.maximize_window()

    return chrome_driver


def click_weigh_button(driver):
    """ Clicks the weigh button """
    original_length_of_weighings = len(get_list_of_weighings(driver))

    button = driver.find_element_by_id("weigh")
    button.click()

    WebDriverWait(driver, 10).until(
        lambda driver: len(get_list_of_weighings(driver)) > original_length_of_weighings
    )


def click_reset_button(driver):
    """Clicks the reset button"""

    button = driver.find_element_by_xpath("/html/body/div/div/div[1]/div[4]/button[1]")
    button.click()


def get_measure_results(driver):
    """ Gets the measure results (field between the bowls)"""

    button = driver.find_element_by_xpath("/html/body/div/div/div[1]/div[2]/button")
    results = button.text

    return results


def fill_cell_in_grid_box(driver, bowl, box_number, bar_number):
    """ 
        Enters the value of 'bar_number' into 'box_number' in 'bowl'
        
        Parameters:
            driver : webdriver

            bowl : str 
                which bowl the bar number should be put in 'left' or 'right'
            
            box_number : int
                box number that the bar number should be put into boxes are numbered right to left top to bottom and are zero indexed 

            bar_number : int
                the number that will be typed into the field 
    """

    cell = driver.find_element_by_id("{}_{}".format(bowl, box_number))
    cell.send_keys(bar_number)

    WebDriverWait(driver, 10).until(
        lambda driver: cell.get_attribute("value") == str(bar_number)
    )


def fill_bowl(driver, bowl, list_of_boxes_and_bars):
    """ 
        Fills the indicated bowl using the values and box numbers in the list

        Parameters:
            driver : webdriver

            bowl : str
                which bowl should be filled 'left' or 'right'

            list_of_boxes_and_bars : list
                list of tuples containting the box number that a bar number should be placed in [(box_number, bar_number)]
    """
    for index, box_bar_pair in enumerate(list_of_boxes_and_bars):
        box_number = box_bar_pair[0]
        bar_number = box_bar_pair[1]
        fill_cell_in_grid_box(driver, bowl, box_number, bar_number)


def get_list_of_weighings(driver):
    """ Gets the list of weighings"""

    ol = driver.find_element_by_css_selector(
        "#root > div > div.game > div.game-info > ol"
    )
    weighings = ol.get_property("innerText")

    return weighings


def click_gold_bar_number_and_get_message(driver, bar_number):
    """ Clicks the gold bar number at the bottom of the website, accepts the allert and returns the alert message """

    bar = driver.find_element_by_id("coin_{}".format(bar_number))
    bar.click()

    alert = driver.switch_to.alert

    message = alert.text

    alert.accept()

    return message


def verify_alert_message(expected_alert, actual_alert):
    """ 
        Verifies that the allert text is the expected text 
            Parameters:
                driver : webdriver

                expected_alert : bool
                    the expected allert response true if the user has correctly identified the fake bar false if the user has not
                acutal_alert : str
                    the actual allert message text
            Return: 
                The return value. True for allert is as expected, False otherwise.
                                        
    """
    if expected_alert == True:
        return ALLERT_MESSAGE_RIGHT == actual_alert

    else:
        return ALLERT_MESSAGE_WRONG == actual_alert

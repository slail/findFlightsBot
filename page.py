from locator import *
from element import BasePageElement
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys

class SearchTextElement(BasePageElement):
    locator = "ss"

class BasePage(object):
    def __init__(self, driver):
        self.driver = driver
    
class MainPage(BasePage):
 
    search_text_element = SearchTextElement() # This is what we'll be looking for! Advanced python concept called decorator!

    def is_title_matches(self):
        return "Booking.com" in self.driver.title
 
    def update_currency(self):
        moveToSelectCurrency = ActionChains(self.driver)

        element = self.driver.find_element(*MainPageLocators.CURRENCY_BUTTON)
        moveToSelectCurrency.move_to_element(element).click()
        moveToSelectCurrency.perform()

        selectCurrency = ActionChains(self.driver)

        currency = WebDriverWait(self.driver, 10).until(lambda x: x.find_element(*MainPageLocators.COUNTRY_BUTTON)) 
        selectCurrency.move_to_element(currency).click()
        selectCurrency.perform()
    
    def searching_destination(self):
        firstOption =  WebDriverWait(self.driver, 10).until(lambda x: x.find_element(*MainPageLocators.FIRST_LIST_ITEM)) 

        selectDestination = ActionChains(self.driver)
        selectDestination.move_to_element(firstOption).click()

        calendar = self.driver.find_element(*MainPageLocators.DATE_PICKER)

        selectDestination.move_to_element(calendar).double_click()

        departDate = WebDriverWait(self.driver, 10).until(lambda x: x.find_element(*MainPageLocators.DEPART_DATE_ELEMENT))
        returnDate = WebDriverWait(self.driver, 10).until(lambda x: x.find_element(*MainPageLocators.RETURN_DATE_ELEMENT))

        selectDestination.move_to_element(departDate).click()
        selectDestination.move_to_element(returnDate).click()


        selectPeople = WebDriverWait(self.driver, 10).until(lambda x: x.find_element(*MainPageLocators.NUMBER_OF_PEOEPLE))
        decreaseAdult = WebDriverWait(self.driver, 10).until(lambda x: x.find_element(*MainPageLocators.DECREASE_ADULTS))
        increaseKids = WebDriverWait(self.driver, 10).until(lambda x: x.find_element(*MainPageLocators.INCREASE_KIDS))
        selectDestination.move_to_element(selectPeople).click()
        selectDestination.move_to_element(decreaseAdult).click()
        selectDestination.move_to_element(increaseKids).click()
        
        selectDestination.perform()

        selectDestination2 = ActionChains(self.driver)
        selectAge = WebDriverWait(self.driver, 10).until(lambda x: x.find_element(*MainPageLocators.SELECT_AGE))
        selectDestination2.move_to_element(selectAge).click()
        selectDestination2.send_keys(Keys.NUMPAD6)
        selectDestination2.send_keys(Keys.RETURN)

        increaseRooms = WebDriverWait(self.driver, 10).until(lambda x: x.find_element(*MainPageLocators.INCREASE_ROOMS))
        selectDestination2.move_to_element(increaseRooms).click()

        submitButton = self.driver.find_element(*MainPageLocators.SUBMIT)
        selectDestination2.move_to_element(submitButton).click()

        selectDestination2.perform()
 
class SearchResultPage(BasePage):

    def is_results_found(self):
        return "No result found." not in self.driver.page_source
    
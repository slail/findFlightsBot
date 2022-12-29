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
 
    def update_currency(self, date):
        moveToSelectCurrency = ActionChains(self.driver)

        element = self.driver.find_element(*MainPageLocators.CURRENCY_BUTTON)
        moveToSelectCurrency.move_to_element(element).click()
        moveToSelectCurrency.perform()

        selectCurrency = ActionChains(self.driver)

        mainPageObject = MainPageLocators(CURRENCY=date)
        currency = WebDriverWait(self.driver, 10).until(lambda x: x.find_element(*mainPageObject.COUNTRY_BUTTON)) 
        selectCurrency.move_to_element(currency).click()
        selectCurrency.perform()
    
    def searching_destination(self, date1, date2, givenAge, numberOfRooms):
        firstOption =  WebDriverWait(self.driver, 10).until(lambda x: x.find_element(*MainPageLocators.FIRST_LIST_ITEM)) 

        selectDestination = ActionChains(self.driver)
        selectDestination.move_to_element(firstOption).click()

        calendar = self.driver.find_element(*MainPageLocators.DATE_PICKER)

        selectDestination.move_to_element(calendar).double_click()

        mainPageObject = MainPageLocators(date1, date2)
        departDate = WebDriverWait(self.driver, 10).until(lambda x: x.find_element(*mainPageObject.DEPART_DATE_ELEMENT))
        returnDate = WebDriverWait(self.driver, 10).until(lambda x: x.find_element(*mainPageObject.RETURN_DATE_ELEMENT))

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
        
        for i in range(19):
            if givenAge == str(i):
                selectDestination2.send_keys(givenAge)

        increaseRooms = WebDriverWait(self.driver, 10).until(lambda x: x.find_element(*MainPageLocators.INCREASE_ROOMS))
        for i in range(numberOfRooms - 1):
            selectDestination2.move_to_element(increaseRooms).click()

        submitButton = self.driver.find_element(*MainPageLocators.SUBMIT)
        selectDestination2.move_to_element(submitButton).click()

        selectDestination2.perform()

 
class SearchResultPage(BasePage):

    def is_results_found(self):
        return "No result found." not in self.driver.page_source
    
    def apply_filtration(self, *star_values):
        
        oneStars = WebDriverWait(self.driver, 20).until(lambda x: x.find_element(*SearchResultsPageLocators.INCLUDE_ONESTARS))
        twoStars = WebDriverWait(self.driver, 20).until(lambda x: x.find_element(*SearchResultsPageLocators.INCLUDE_TWOSTARS))
        threeStars = WebDriverWait(self.driver, 20).until(lambda x: x.find_element(*SearchResultsPageLocators.INCLUDE_THREESTARS))
        fourStars = WebDriverWait(self.driver, 20).until(lambda x: x.find_element(*SearchResultsPageLocators.INCLUDE_FOURSTARS))
        fiveStars = WebDriverWait(self.driver, 20).until(lambda x: x.find_element(*SearchResultsPageLocators.INCLUDE_FIVESTARS))

        stars = [oneStars, twoStars, threeStars, fourStars, fiveStars]

        filters = ActionChains(self.driver)
        for star_value in star_values:                
            star_value = stars[star_value - 1] 
            filters.move_to_element(star_value).click()

        filters.perform()


class ThirdPageResult(BasePage):
    def is_results_found(self):
        return "No result found." not in self.driver.page_source

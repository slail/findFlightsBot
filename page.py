from locator import *
from element import BasePageElement
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from prettytable import PrettyTable
import time


class SearchTextElement(BasePageElement):
    locator = "ss"


class BasePage(object):
    def __init__(self, driver):
        self.driver = driver


class MainPage(BasePage):

    # This is what we'll be looking for! Advanced python concept called decorator!
    search_text_element = SearchTextElement()

    def is_title_matches(self):
        return "Booking.com" in self.driver.title

    def update_currency(self, date):
        moveToSelectCurrency = ActionChains(self.driver)

        element = self.driver.find_element(*MainPageLocators.CURRENCY_BUTTON)
        WebDriverWait(self.driver, 15).until(EC.visibility_of(element))
        moveToSelectCurrency.move_to_element(element).click()
        moveToSelectCurrency.perform()

        selectCurrency = ActionChains(self.driver)

        mainPageObject = MainPageLocators(CURRENCY=date)
        currency = WebDriverWait(self.driver, 10).until(
            lambda x: x.find_element(*mainPageObject.COUNTRY_BUTTON))
        selectCurrency.move_to_element(currency).click()
        selectCurrency.perform()

    def searching_destination(self, date1, date2, givenAge, numberOfAdults, numberOfRooms):
        firstOption = WebDriverWait(self.driver, 10).until(
            lambda x: x.find_element(*MainPageLocators.FIRST_LIST_ITEM))

        selectDestination = ActionChains(self.driver)
        selectDestination.move_to_element(firstOption).click()

        calendar = self.driver.find_element(*MainPageLocators.DATE_PICKER)

        selectDestination.move_to_element(calendar).double_click()

        mainPageObject = MainPageLocators(date1, date2)
        departDate = WebDriverWait(self.driver, 10).until(
            lambda x: x.find_element(*mainPageObject.DEPART_DATE_ELEMENT))
        returnDate = WebDriverWait(self.driver, 10).until(
            lambda x: x.find_element(*mainPageObject.RETURN_DATE_ELEMENT))

        selectDestination.move_to_element(departDate).click()
        selectDestination.move_to_element(returnDate).click()

        selectPeople = WebDriverWait(self.driver, 10).until(
            lambda x: x.find_element(*MainPageLocators.NUMBER_OF_PEOEPLE))
        decreaseAdult = WebDriverWait(self.driver, 10).until(
            lambda x: x.find_element(*MainPageLocators.DECREASE_ADULTS))
        increaseAdult = WebDriverWait(self.driver, 10).until(
            lambda x: x.find_element(*MainPageLocators.INCREASE_ADULTS))
        increaseKids = WebDriverWait(self.driver, 10).until(
            lambda x: x.find_element(*MainPageLocators.INCREASE_KIDS))
        selectDestination.move_to_element(selectPeople).click()

        if numberOfAdults > 2:
            for i in range(numberOfAdults - 2):
                selectDestination.move_to_element(increaseAdult).click()
        else:
            selectDestination.move_to_element(decreaseAdult).click()

        selectDestination.move_to_element(increaseKids).click()  # For ONE kid

        selectDestination.perform()

        selectDestination2 = ActionChains(self.driver)
        selectAge = WebDriverWait(self.driver, 10).until(
            lambda x: x.find_element(*MainPageLocators.SELECT_AGE))
        selectDestination2.move_to_element(selectAge).click()

        for i in range(19):
            if givenAge == str(i):
                selectDestination2.send_keys(givenAge)

        increaseRooms = WebDriverWait(self.driver, 10).until(
            lambda x: x.find_element(*MainPageLocators.INCREASE_ROOMS))
        for i in range(numberOfRooms - 1):
            selectDestination2.move_to_element(increaseRooms).click()

        submitButton = self.driver.find_element(*MainPageLocators.SUBMIT)
        selectDestination2.move_to_element(submitButton).click()

        selectDestination2.perform()


class SearchResultPage(BasePage):

    def is_results_found(self):
        return "No result found." not in self.driver.page_source

    def apply_stars(self, star_value):
        filters = ActionChains(self.driver)

        searchObject = SearchResultsPageLocators(star_value)
        try:
            star = WebDriverWait(self.driver, 10).until(
                lambda x: x.find_element(*searchObject.INCLUDE_STAR))
        except:
            print("Star Rating Not Found!")

        filters.move_to_element(star).click()
        filters.perform()

    def apply_sort(self, sortBy):
        filters = ActionChains(self.driver)

        sortButton = WebDriverWait(self.driver, 20).until(
            lambda x: x.find_element(*SearchResultsPageLocators.SORT_BUTTON))
        filters.scroll_to_element(sortButton)
        filters.move_to_element(sortButton).click()
        filters.perform()

        filtersSecond = ActionChains(self.driver)
        sortOptionParent = WebDriverWait(self.driver, 20).until(
            lambda x: x.find_element(*SearchResultsPageLocators.SORT_OPTIONS))
        sortOptions = WebDriverWait(sortOptionParent, 20).until(
            lambda x: x.find_elements(*SearchResultsPageLocators.SORT_OPTIONS_NAMES))

        for option in sortOptions:
            if option.text == sortBy:
                filtersSecond.scroll_to_element(option)
                filtersSecond.move_to_element(option).click()

        filtersSecond.perform()

    def findHotels(self):
        time.sleep(8)
        hotelsClass = WebDriverWait(self.driver, 20).until(
            lambda x: x.find_element(*SearchResultsPageLocators.HOTEL_OPTIONS_CLASSNAME))
        hotelsName = WebDriverWait(hotelsClass, 20).until(
            lambda x: x.find_elements(*SearchResultsPageLocators.HOTEL_NAMES))
        hotelPrices = WebDriverWait(hotelsClass, 20).until(
            lambda x: x.find_elements(*SearchResultsPageLocators.HOTELS_PRICES))
        hotelTable = [[] for _ in range(len(hotelsName))]

        for h in range(len(hotelsName)):
            hotelTable[h] = [hotelsName[h].text]
            hotelTable[h].append(hotelPrices[h].text)

        hotelBoxes = WebDriverWait(hotelsClass, 20).until(
            lambda x: x.find_elements(*SearchResultsPageLocators.HOTEL_BOXES))
        for i in range(len(hotelBoxes)):
            hotelBox = hotelBoxes[i]
            try:
                hotelScore = WebDriverWait(hotelBox, 20).until(
                    lambda x: x.find_element(*SearchResultsPageLocators.HOTEL_SCORES))
                hotelTable[i].append(hotelScore.text)
            except:
                hotelTable[i].append("NO RATING")

        table = PrettyTable(
            field_names=["Hotel Names", "Hotel Prices", "Hotel Score"]
        )
        table.add_rows(hotelTable)
        print(table)


class ThirdPageResult(BasePage):
    def is_results_found(self):
        return "No result found." not in self.driver.page_source

from selenium.webdriver.common.by import By

# Classes that represents object we want to find.

class MainPageLocators(object): # Will have all locators for the stuff on our "main" page
    CURRENCY_BUTTON = (By.CSS_SELECTOR, "button[data-modal-aria-label=\"Select your currency\"]") # (How we acess, what the value is)

    FIRST_LIST_ITEM = (By.CSS_SELECTOR, 'li[data-label="New York, New York State, United States"]')
    DATE_PICKER = (By.CSS_SELECTOR, 'svg[class="bk-icon -experiments-calendar sb-date-picker_icon-svg"]')

    NUMBER_OF_PEOEPLE = (By.ID, "xp__guests__toggle")
    DECREASE_ADULTS = (By.CSS_SELECTOR, 'button[aria-label="Decrease number of Adults"]')
    INCREASE_KIDS = (By.CSS_SELECTOR, 'button[aria-label="Increase number of Children"]')
    SELECT_AGE = (By.CSS_SELECTOR, 'select[aria-label="Child 1 age"]')
    INCREASE_ROOMS = (By.CSS_SELECTOR, 'button[aria-label="Increase number of Rooms"]')

    SUBMIT = (By.CLASS_NAME, "js-sb-submit-text ")

    def __init__(self, DEPART_DATE = None, RETURN_DATE = None, CURRENCY = None):
        self.CURRENCY = CURRENCY
        self.DEPART_DATE = DEPART_DATE
        self.RETURN_DATE = RETURN_DATE
        self.COUNTRY_BUTTON = (By.CSS_SELECTOR, f'a[data-modal-header-async-url-param="changed_currency=1&selected_currency={CURRENCY}"]')
        self.DEPART_DATE_ELEMENT = (By.CSS_SELECTOR, f'td[data-date="{DEPART_DATE}"')
        self.RETURN_DATE_ELEMENT = (By.CSS_SELECTOR, f'td[data-date="{RETURN_DATE}"')
    
class SearchResultsPageLocators(object):
    INCLUDE_ONESTARS = (By.CSS_SELECTOR, 'div[data-filters-item="class:class=1"]')
    INCLUDE_TWOSTARS = (By.CSS_SELECTOR, 'div[data-filters-item="class:class=2"]')
    INCLUDE_THREESTARS = (By.CSS_SELECTOR, 'div[data-filters-item="class:class=3"]')
    INCLUDE_FOURSTARS = (By.CSS_SELECTOR, 'div[data-filters-item="class:class=4"]')
    INCLUDE_FIVESTARS = (By.CSS_SELECTOR, 'div[data-filters-item="class:class=5"]')
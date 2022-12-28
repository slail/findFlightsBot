from selenium.webdriver.common.by import By

# Classes that represents object we want to find.

class MainPageLocators(object): # Will have all locators for the stuff on our "main" page
    CURRENCY = "EGP"
    CURRENCY_BUTTON = (By.CSS_SELECTOR, "button[data-modal-aria-label=\"Select your currency\"]") # (How we acess, what the value is)
    COUNTRY_BUTTON = (By.CSS_SELECTOR, f'a[data-modal-header-async-url-param="changed_currency=1&selected_currency={CURRENCY}"]')

    FIRST_LIST_ITEM = (By.CSS_SELECTOR, 'li[data-label="New York, New York State, United States"]')
    DATE_PICKER = (By.CSS_SELECTOR, 'svg[class="bk-icon -experiments-calendar sb-date-picker_icon-svg"]')
    
    DEPART_DATE = "2022-12-30"
    RETURN_DATE = "2023-01-17"

    DEPART_DATE_ELEMENT = (By.CSS_SELECTOR, f'td[data-date="{DEPART_DATE}"')
    RETURN_DATE_ELEMENT = (By.CSS_SELECTOR, f'td[data-date="{RETURN_DATE}"')

    NUMBER_OF_PEOEPLE = (By.ID, "xp__guests__toggle")
    DECREASE_ADULTS = (By.CSS_SELECTOR, 'button[aria-label="Decrease number of Adults"]')
    INCREASE_KIDS = (By.CSS_SELECTOR, 'button[aria-label="Increase number of Children"]')
    SELECT_AGE = (By.CSS_SELECTOR, 'select[aria-label="Child 1 age"]')
    INCREASE_ROOMS = (By.CSS_SELECTOR, 'button[aria-label="Increase number of Rooms"]')

    SUBMIT = (By.CLASS_NAME, "js-sb-submit-text ")

class SearchResultsPageLocators(object):
    pass
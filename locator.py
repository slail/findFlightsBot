from selenium.webdriver.common.by import By

# Classes that represents object we want to find.


# Will have all locators for the stuff on our "main" page
class MainPageLocators(object):
    # (How we acess, what the value is)
    CURRENCY_BUTTON = (
        By.CSS_SELECTOR, "button[data-modal-aria-label=\"Select your currency\"]")

    FIRST_LIST_ITEM = (
        By.CSS_SELECTOR, 'li[class="c-autocomplete__item sb-autocomplete__item sb-autocomplete__item-with_photo sb-autocomplete__item__item--elipsis sb-autocomplete__item--icon_revamp sb-autocomplete__item--city "]')
    DATE_PICKER = (
        By.CSS_SELECTOR, 'svg[class="bk-icon -experiments-calendar sb-date-picker_icon-svg"]')

    NUMBER_OF_PEOEPLE = (By.ID, "xp__guests__toggle")
    DECREASE_ADULTS = (
        By.CSS_SELECTOR, 'button[aria-label="Decrease number of Adults"]')
    INCREASE_ADULTS = (
        By.CSS_SELECTOR, 'button[aria-label="Increase number of Adults"]')

    INCREASE_KIDS = (
        By.CSS_SELECTOR, 'button[aria-label="Increase number of Children"]')
    SELECT_AGE = (By.CSS_SELECTOR, 'select[aria-label="Child 1 age"]')
    INCREASE_ROOMS = (
        By.CSS_SELECTOR, 'button[aria-label="Increase number of Rooms"]')

    SUBMIT = (By.CLASS_NAME, "js-sb-submit-text ")

    def __init__(self, DEPART_DATE=None, RETURN_DATE=None, CURRENCY=None):
        self.CURRENCY = CURRENCY
        self.DEPART_DATE = DEPART_DATE
        self.RETURN_DATE = RETURN_DATE
        self.COUNTRY_BUTTON = (
            By.CSS_SELECTOR, f'a[data-modal-header-async-url-param="changed_currency=1&selected_currency={CURRENCY}"]')
        self.DEPART_DATE_ELEMENT = (
            By.CSS_SELECTOR, f'td[data-date="{DEPART_DATE}"')
        self.RETURN_DATE_ELEMENT = (
            By.CSS_SELECTOR, f'td[data-date="{RETURN_DATE}"')


class SearchResultsPageLocators(object):

    SORT_BUTTON = (By.CSS_SELECTOR, 'button[aria-expanded="false"]')
    SORT_OPTIONS = (By.CLASS_NAME, "ff0ad2a91a")
    SORT_OPTIONS_NAMES = (
        By.CSS_SELECTOR, 'div[class="b1e6dd8416 aacd9d0b0a"]')

    SORT_OPTION = (By.CSS_SELECTOR, 'button[data-id="bayesian_review_score"]')

    HOTEL_OPTIONS_CLASSNAME = (By.CLASS_NAME, "d4924c9e74")
    HOTEL_BOXES = (
        By.CSS_SELECTOR, 'div[class="a1b3f50dcd b2fe1a41c3 a7c67ebfe5 d19ba76520 d14b211b4f"]')
    HOTEL_NAMES = (By.CSS_SELECTOR, 'div[class="fcab3ed991 a23c043802"]')
    HOTELS_PRICES = (
        By.CSS_SELECTOR, 'span[data-testid="price-and-discounted-price"]')
    HOTEL_SCORES = (By.CSS_SELECTOR, 'div[class="b5cd09854e d10a6220b4"]')

    FOOTER_ELEMENT = (By.CSS_SELECTOR, 'div[class="d7a0553560"]')

    def __init__(self, STAR_VALUE=None):
        self.STAR_VALUE = STAR_VALUE
        self.INCLUDE_STAR = (
            By.CSS_SELECTOR, f'div[data-filters-item="class:class={STAR_VALUE}"]')

import unittest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service 
from selenium.webdriver.chrome.options import Options
import page
import time

class PythonOrgSearchTTest(unittest.TestCase):

    def setUp(self):
        # options = webdriver.ChromeOptions() 
        # options.add_argument("--headless") 
        # browser = webdriver.Chrome(options=options)
        self.driver = webdriver.Chrome(service = Service('/usp/Local/bin/chromedriver'))
        self.driver.maximize_window()
        self.driver.get("https://www.booking.com/")
        
    def test_One(self):
        mainPage = page.MainPage(self.driver)
        currency = "CAD"
        city = "New York"
        departDate = "2023-01-01"
        returnDate = "2023-01-16"
        ageOfKid = "13"
        stars = (4, 5)
        numberOfRooms = 5

        assert mainPage.is_title_matches();
        mainPage.update_currency(currency)
        mainPage.search_text_element = city
        mainPage.searching_destination(departDate, returnDate, ageOfKid,numberOfRooms)
        search_result_page = page.SearchResultPage(self.driver)

        assert search_result_page.is_results_found();
        secondPage = page.SearchResultPage(self.driver)
        secondPage.apply_filtration(*stars)
        thirdPage = page.ThirdPageResult(self.driver)

        assert thirdPage.is_results_found()
        

    def tearDown(self):
        time.sleep(15)
        self.driver.close()

unittest.main()

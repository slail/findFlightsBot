import unittest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service 
import page
import time

class PythonOrgSearchTTest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service = Service('/usp/Local/bin/chromedriver'))
        self.driver.maximize_window()
        self.driver.get("https://www.booking.com/")
 
    # def test_search_python(self):
    #     mainPage = page.MainPage(self.driver)
    #     assert mainPage.is_title_matches();
    #     mainPage.search_text_element = "pycon"
    #     mainPage.click_go_button()
    #     search_result_page = page.SearchResultPage(self.driver)
    #     assert search_result_page.is_results_found()

    def test_One(self):
        mainPage = page.MainPage(self.driver)
        assert mainPage.is_title_matches();
        mainPage.update_currency()
        mainPage.search_text_element = "New York"
        mainPage.searching_destination()
        search_result_page = page.SearchResultPage(self.driver)
        assert search_result_page.is_results_found()
        

    def tearDown(self):
        time.sleep(10)
        self.driver.close()

unittest.main()

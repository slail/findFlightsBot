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
        currency = input("Enter a currency: (First Three letters, ALL CAPS, Ex. CAD, USD): ")
        city = input("Enter a city: ")
        departDate = input("Enter a DEPART date (In the formate: YEAR-MONTH-DAY, ex. 2023-12-31): ")
        returnDate = input("Enter a RETURN date (In the formate: YEAR-MONTH-DAY, ex. 2023-12-31): ")
        ageOfKid = input("Enter the age of your ONE Kid (max 17): ")
        ### Getting whats STAR Hotels USER wants ###
        stars = []
        numOfStars = input("Enter what STAR hotels you want (type 'q' to quit): ")
        while numOfStars != "q":
            stars.append(numOfStars)
            numOfStars = input("enter what star hotels you want (type 'q' when you're finished): ")
        ### 
        numberOfAdults = int(input("Enter number of adults: "))
        numberOfRooms = int(input("Enter number of rooms: "))
        sortBy = input("Enter how you'd like to sort your hotels by, options are: Top Picks for Families\nHomes & apartments first\nPrice (lowest first)\nBest reviewed & lowest price\nStars (highest first)\nStars (lowest first)\nStar rating and price\nDistance From Downtown\nTop Reviewed\nEnter Here: ")
        assert mainPage.is_title_matches();
        mainPage.update_currency(currency)
        mainPage.search_text_element = city
        time.sleep(1)
        mainPage.searching_destination(departDate, returnDate, ageOfKid, numberOfAdults, numberOfRooms)
        search_result_page = page.SearchResultPage(self.driver)

        assert search_result_page.is_results_found();
        secondPage = page.SearchResultPage(self.driver)
        secondPage.apply_sort(sortBy)
        time.sleep(3)
        for i in range(len(stars)):
            secondPage.apply_stars(stars[i])
        time.sleep(3)
        secondPage.findHotels()


        thirdPage = page.ThirdPageResult(self.driver)
        assert thirdPage.is_results_found()
        

    def tearDown(self):
        self.driver.close()

unittest.main()

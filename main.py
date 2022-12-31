import unittest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
import page
import time


class PythonOrgSearchTTest(unittest.TestCase):

    def setUp(self):

        # !! Options to make it HEADLESS CHROME, run in background !!
        user_agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.83 Safari/537.36"
        options = webdriver.ChromeOptions()
        options.headless = True
        options.add_argument(f'user-agent={user_agent}')
        options.add_argument("--window-size=1920,1080")
        options.add_argument('--ignore-certificate-errors')
        options.add_argument('--allow-running-insecure-content')
        options.add_argument("--disable-extensions")
        options.add_argument("--proxy-server='direct://'")
        options.add_argument("--proxy-bypass-list=*")
        options.add_argument("--start-maximized")
        options.add_argument('--disable-gpu')
        options.add_argument('--disable-dev-shm-usage')
        options.add_argument('--no-sandbox')
        self.driver = webdriver.Chrome(service=Service(
            '/usp/Local/bin/chromedriver'), options=options)

        # !! Options to make it NOT headless !!

        # self.driver = webdriver.Chrome(
        #     service=Service('/usp/Local/bin/chromedriver'))
        # self.driver.maximize_window()

        self.driver.get("https://www.booking.com/")

    def test_One(self):
        mainPage = page.MainPage(self.driver)
        currency = input(
            "Enter a currency: (First Three letters, ALL CAPS, Ex. CAD, USD): ")
        city = input("Enter a city: ")
        departDate = input(
            "Enter a DEPART date (In the formate: YEAR-MONTH-DAY, ex. 2023-12-31): ")
        returnDate = input(
            "Enter a RETURN date (In the formate: YEAR-MONTH-DAY, ex. 2023-12-31): ")
        ageOfKid = input("Enter the age of your ONE Kid (max 17): ")
        ### Getting whats STAR Hotels USER wants ###
        stars = []
        numOfStars = input(
            "Enter what STAR hotels you want (type 'q' to quit): ")
        while numOfStars != "q":
            stars.append(numOfStars)
            numOfStars = input(
                "enter what star hotels you want (type 'q' when you're finished): ")
        ###
        numberOfAdults = int(input("Enter number of adults: "))
        numberOfRooms = int(input("Enter number of rooms: "))
        sortBy = input("Enter how you'd like to sort your hotels by, options are: Top Picks for Families\nHomes & apartments first\nPrice (lowest first)\nBest reviewed & lowest price\nStars (highest first)\nStars (lowest first)\nStar rating and price\nDistance From Downtown\nTop Reviewed\nEnter Here: ")
        assert mainPage.is_title_matches()
        mainPage.update_currency(currency)
        mainPage.search_text_element = city
        time.sleep(1)
        mainPage.searching_destination(
            departDate, returnDate, ageOfKid, numberOfAdults, numberOfRooms)
        search_result_page = page.SearchResultPage(self.driver)

        assert search_result_page.is_results_found()
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


# Booking.com Hotels Finder
##  30 December 2022
#### Slail Billicko Jean Pierre

##### External Libraries used: <a href = "https://pypi.org/project/selenium/" >Selenium</a>, <a href= "https://pypi.org/project/prettytable/">Pretty Table</a>
##### Internal Libraries used: <em>UnitTest, Time</em>

## Project Description
Created a selenium bot that mimic a user's behavior on entering Booking.com, finding a city, choosing depart/return dates, specifiying number of rooms/adults on the trip, applying filters such as 4/5-Star hotels, sorting options like lowest price, and finally displaying (via a table) of the search's page results through the Command Line Interface.
***    

## Program In Action
##### User responses for input fields
<img width = 400 src = "https://i.imgur.com/IUd33tC.png" />

##### The Bot begins to apply these inputs on the site (On the Main Page)
<img width = 500 src = "https://i.imgur.com/dDsRy6d.png" />

##### The Bot continues filtering based on user inputs (On the search Page)
<img width = 400 src = "https://i.imgur.com/IDCZcDD.png" />

##### The Bot captures the first page's list of hotels after applying provided filters
<img width = 400 src = "https://i.imgur.com/b9v7ld9.png" />


## Program Design
• Set up was with a basic UNIT-testing Framework provided for Python Selenium on the documentation. As mentioned on the documentation: 

A page object represents an area where the test interacts within the web application user interface. Benefits of using page object pattern:
  * Easy to read test cases
  * Creating reusable code that can share across multiple test cases
  * Reducing the amount of duplicated code
  * If the user interface changes, the fix needs changes in only one place
  
 Read more: https://selenium-python.readthedocs.io/page-objects.html#
 
 ## Video Demostration - Speed Up
 

https://user-images.githubusercontent.com/57454628/210119738-44ca2121-cc37-4b86-a691-ded8fca8f2f1.mp4



import unittest
from selenium import webdriver
from WebDriverTheInternet import PageElements as p
from WebDriverTheInternet import config as c
from WebDriverTheInternet.WebDriverTheInternet_functions import TheInternet

class testAddRemoveElements(unittest.TestCase , TheInternet):

    def setUp(self):
        self.driver = webdriver.Chrome(executable_path=c.CHROMEDRIVER)

    def testAddRemoveElements(self):
    #Arrange
        self.open_url(p.URLS["Add/Remove Elements"])
        self.find(p.BUTTON_ADD)

    #Act
        self.AddRemoveElements()

    #Assert
        result = self.not_found(p.BUTTON_DELETE)
        assert result == True
        
    def tearDown(self):
        self.driver.close()

if __name__ == '__main__':
    unittest.main()
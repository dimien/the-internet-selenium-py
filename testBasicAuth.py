import unittest
from selenium import webdriver
from WebDriverTheInternet import PageElements as p
from WebDriverTheInternet import config
from WebDriverTheInternet.WebDriverTheInternet_functions import TheInternet

class testBasicAuth(unittest.TestCase, TheInternet):

    def setUp(self):
        path_to_chrome = config.path()
        self.driver = webdriver.Chrome(executable_path=path_to_chrome)

        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_argument('--no-sandbox')

    def testBasicAuth(self):
    #Arrange
        user = "admin"
        password = "admin"
        url = p.URLS['Basic Auth']
        expected_element = p.SUCCESS_AUTH_TEXT
            
    # #Act
        self.BasicAuth(user, password, url)

    # #Assert
        result = self.found(expected_element)
        assert result is True

    def tearDown(self):
        self.driver.close()

if __name__ == '__main__':
    unittest.main()
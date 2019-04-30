from selenium import webdriver
from WebDriverTheInternet.Base import BaseClass
from WebDriverTheInternet import PageElements as p

class TheInternet(BaseClass):
    
    def AddRemoveElements(self):
        """Add and remove button"""
        self.click(p.BUTTON_ADD)
        self.find(p.BUTTON_DELETE)
        self.click(p.BUTTON_DELETE)

    def BasicAuth(self, user, password, link):
        self.user = user
        self.password = password
        url = f"https://{user}:{password}@{link}"

        self.open_url(url)
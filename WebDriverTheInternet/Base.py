from time import sleep

class BaseClass:

    def open_url(self, url):
        self.driver.get(url)
        sleep(2)

    def find(self, item):
        try:
            element = self.driver.find_element_by_xpath(item)
            return element
        except:
            raise Exception(f'Element \"{item}\" not found.')
            return False       
     
    def click(self, item):
        self.find(item).click()

    def send_keys(self, item, data):
        self.find(item).send_keys(data)

    def not_found(self, item):
        try:
            self.find(item)
            return False
        except:
            return True

    def found(self, item):
        try:
            self.find(item)
            return True
        except:
            return False
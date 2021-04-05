import unittest
from  selenium import webdriver
from   time import sleep

class searchEnginesTest(unittest.TestCase):
    def test_google(self):
        self.driver=webdriver.Chrome(executable_path="C:\Drivers\chromedriver.exe")
        self.driver.get("https://www.google.com/")
        print("Title of the page :"+self.driver.title)

    def test_bing(self):
        self.driver = webdriver.Chrome(executable_path="C:\Drivers\chromedriver.exe")
        self.driver.get("https://www.bing.com/")
        print("Title of the page :" + self.driver.title)
        self.driver.close()

if __name__=="__main__":
      unittest.main()
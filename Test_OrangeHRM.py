# unit test Framework

from selenium import webdriver
from time import sleep
import unittest
import HtmlTestRunner

class OrangeHRM(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver=webdriver.Chrome(executable_path="C:\Drivers\Chromedriver.exe")
        cls.driver.maximize_window()
    def test_homepage_Verify(self):
        self.driver.get("https://opensource-demo.orangehrmlive.com/")
        self.assertEqual("OrangeHRM123",self.driver.title,"Webpage title is not matched")

    def test_login(self):
        self.driver.get("https://opensource-demo.orangehrmlive.com/")
        self.driver.find_element_by_name("txtUsername").send_keys("Admin")
        self.driver.find_element_by_name("txtPassword").send_keys("admin123")
        self.driver.find_element_by_name("Submit").send_keys("Admin")
        self.assertEqual("OrangeHRM", self.driver.title, "Webpage title is not matched")
    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()
        print("test completed")

if __name__ =="__main__":
     unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output='C:/Users/bobbu.yaswanth/PycharmProjects/UnitTest Framework/Reports'))
#assert true , Assert false (to check values/expressions)

import unittest
from  selenium import webdriver

class Test(unittest.TestCase):
    def testName(self):
        driver=webdriver.Chrome(executable_path="C:\Drivers\Chromedriver.exe")
        driver.get("https://www.google.com/")
        TitleofWebPage = driver.title
        #self.assertTrue(TitleofWebPage== "Google")
        self.assertFalse(TitleofWebPage=="Google1")


if __name__ =="__main__":
    unittest.main()
#assert isNOne , Assert IsnotNone (to check values/expressions)

import unittest
from  selenium import webdriver

class Test(unittest.TestCase):
    def testName(self):
        driver=webdriver.Chrome(executable_path="C:\Drivers\Chromedriver.exe")
        #self.assertIsNone(driver)
        self.assertIsNotNone(driver)

if __name__ =="__main__":
    unittest.main()
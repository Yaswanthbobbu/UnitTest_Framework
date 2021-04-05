#assert equal , Assertnotequal  (only two parameters)

import unittest
from  selenium import webdriver

class Test(unittest.TestCase):
    def testName(self):
        driver=webdriver.Chrome(executable_path="C:\Drivers\Chromedriver.exe")
        driver.get("https://www.google.com/")
        TitleofWebPage = driver.title
        #self.assertEqual("Google",TitleofWebPage,"Web page is not same")
        self.assertNotEqual("Google123",TitleofWebPage)


if __name__ =="__main__":
    unittest.main()
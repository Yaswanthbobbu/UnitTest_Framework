#assert In , Assert notIn (verifies first element in second)
list set tuples,dictnories,

import unittest
from  selenium import webdriver

class Test(unittest.TestCase):
    def testName(self):
         list={"Python","java","C"}
         #self.assertIn("C",list)
         self.assertNotIn("C++",list)


if __name__ =="__main__":
    unittest.main()
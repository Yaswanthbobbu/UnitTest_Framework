#Skip test, reason, Condition

import unittest

class AppTesting(unittest.TestCase):

    @unittest.SkipTest
    def test_search(self):
        print("this is search test")

    @unittest.skip("Im skipping this test method")
    def test_Advancesearch(self):
        print("THis is Advance test")

    @unittest.skipIf(1==1,"Numbers are not equal")
    def test_Prepaidsearch(self):
        print("This is Prepaid test")

    def test_Postpaidsearch(self):
        print("THis is Postpaid test")

if __name__ =="__main__":
    unittest.main()
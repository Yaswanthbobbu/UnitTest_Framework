# setup setupclass setupmodule
#teardown teardownclass  teardownmodule



def setUpModule( ): #Outside the module
    print("Submodule")


import unittest

class AppTesting(unittest.TestCase):

    @classmethod
    def setUp(self):
        print("This is login test")

    @classmethod
    def tearDown(self):
        print("This is logout test")

    @classmethod
    def setUpClass(cls):
        print("Open the application")

    @classmethod
    def tearDownClass(cls):
        print("Close the application")


    def test_search(self):
        print("THis is search test")

    def test_Advancesearch(self):
        print("THis is Advance test")

    def test_Prepaidsearch(self):
         print("THis is Prepaid test")

    def test_Postpaidsearch(self):
         print("THis is Postpaid test")

    def teardownModule():
        print("End Module")

if __name__ =="__main__":
    unittest.main()



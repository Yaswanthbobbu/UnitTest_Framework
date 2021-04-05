import unittest

class SignUpTest(unittest.TestCase):
    def test_SignUpgmail(self):
        print("This is signup by gmail")
        self.assertTrue(True)

    def test_Signupfacebook(self):
        print("This is signup by Facebook")
        self.assertTrue(True)

    def test_Signuptwitter(self):
        print("This is signup by twitter")
        self.assertTrue(True)

if __name__ =="__main__":
    unittest.main()
import unittest

class LoginTest(unittest.TestCase):
    def test_loginbygmail(self):
        print("This is login by gmail")
        self.assertTrue(True)
    def test_loginbyfacebook(self):
        print("This is login by Facebook")
        self.assertTrue(True)
    def test_loginbytwitter(self):
        print("This is login by twitter")
        self.assertTrue(True)

if __name__ =="__main__":
    unittest.main()
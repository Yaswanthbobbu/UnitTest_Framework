import unittest

class Payment(unittest.TestCase):
    def test_paymentindollar(self):
        print("This is payment in dollar test")
        self.assertTrue(True)
    def test_paymentinrupee(self):
        print("This is payment in rupee test")
        self.assertTrue(True)

if __name__ =="__main__":
    unittest.main()
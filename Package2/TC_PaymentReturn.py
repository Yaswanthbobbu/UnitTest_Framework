import unittest

class PaymentReturn(unittest.TestCase):
    def test_paymentReturnindollar(self):
        print("This is payment Return in dollar test")
        self.assertTrue(True)
    def test_paymentReturninrupee(self):
        print("This is payment return in rupee test")
        self.assertTrue(True)

if __name__ =="__main__":
    unittest.main()
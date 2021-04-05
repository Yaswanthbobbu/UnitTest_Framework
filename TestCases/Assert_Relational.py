#greater,less,greaterthanqual,lessqual

import unittest

class AppTesting(unittest.TestCase):
    def test(self):
        self.assertGreater(10,1)
        self.assertGreaterEqual(2,2)
        self.assertLess(10,100)
        self.assertLessEqual(10,10)


if __name__ =="__main__":
    unittest.main()
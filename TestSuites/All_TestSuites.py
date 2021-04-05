import unittest
from Package1.TC_LoginTest import LoginTest
from Package1.TC_SignupTest import SignUpTest

from Package2.TC_PaymentTest import Payment
from Package2.TC_PaymentReturn import PaymentReturn


tc1 = unittest.TestLoader().loadTestsFromTestCase(LoginTest)
tc2 = unittest.TestLoader().loadTestsFromTestCase(SignUpTest)
tc3 = unittest.TestLoader().loadTestsFromTestCase(Payment)
tc4 = unittest.TestLoader().loadTestsFromTestCase(PaymentReturn)

#Creating Suites
SanityTestsuite = unittest.TestSuite([tc1,tc2])
unittest.TextTestRunner().run(SanityTestsuite)

FunctionalTestSuite= unittest.TestSuite([tc3,tc4])
unittest.TextTestRunner().run(FunctionalTestSuite)

MasterTestsuite = unittest.TestSuite([tc1,tc2,tc3,tc4])
unittest.TextTestRunner().run(MasterTestsuite)
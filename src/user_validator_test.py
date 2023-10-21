import unittest

from src.elections import Constituency, VoterEligibilityValidator


class UserValidatorTest(unittest.TestCase):
    def setUp(self):
        self.testee = VoterEligibilityValidator()

    def test_Bob_valid(self):
        self.assertTrue(self.testee.is_valid('Bob'))

    def test_BobBuilder_valid(self):
        self.assertTrue(self.testee.is_valid('BobTheBuilder'))

    def test_B_invalid(self):
        self.assertFalse(self.testee.is_valid('B'))

    def test_crazy_invalid(self):
        self.assertFalse(self.testee.is_valid('@#%!@#'))

    def test_crazy2_invalid(self):
        self.assertFalse(self.testee.is_valid('333122'))



if __name__ == '__main__':
    unittest.main()

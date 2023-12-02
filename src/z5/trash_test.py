import unittest

from trash import Trash


class TrashTest(unittest.TestCase):

    def setUp(self):
        self.testee = Trash(capacity=6)

    def test_can_add(self):
        self.testee[3] = 10
        self.assertTrue(10 in self.testee)

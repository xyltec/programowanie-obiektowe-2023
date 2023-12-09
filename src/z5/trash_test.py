import unittest

from trash import Trash


class TrashTest(unittest.TestCase):

    def setUp(self):
        self.testee = Trash(capacity=6)

    def test_can_add(self):
        self.testee[3] = 10
        self.assertTrue(10 in self.testee)

    def test_can_iterate(self):
        self.testee[2] = 10
        self.testee[4] = 20

        vals = list(self.testee)
        self.assertEqual(vals, [10, 20])


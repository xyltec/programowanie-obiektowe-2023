import unittest

from src.mug import Mug


class MyTestCase(unittest.TestCase):
    def setUp(self):
        self.mug = Mug('red', 10.)

    def test_is_created(self):
        self.assertIsNotNone(self.mug)
        self.assertEqual(self.mug.get_content_amount(), 0.)


    def test_can_fill_full(self):
        #arrange

        #act
        self.mug.fill('water', self.mug.capacity)

        #assert
        self.assertEqual(self.mug.get_content_amount(), self.mug.capacity)


if __name__ == '__main__':
    unittest.main()

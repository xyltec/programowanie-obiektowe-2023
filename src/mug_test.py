import unittest

from src.mug import Mug


class MyTestCase(unittest.TestCase):
    def setUp(self):
        self.mug = Mug('red', 10.)

    def test_is_created(self):
        self.assertIsNotNone(self.mug)
        self.assertEqual(self.mug.get_content_amount(), 0.)

    def test_can_fill_full(self):
        # arrange

        # act
        self.mug.fill('water', self.mug.capacity)

        # assert
        self.assertEqual(self.mug.get_content_amount(), self.mug.capacity)
        self.assertEqual(self.mug.get_content_type(), 'water')

    def test_cannot_mix_fluids(self):
        # arrange
        self.mug.fill('water', 5.0)

        # act/assert
        with self.assertRaises(RuntimeError):
            self.mug.fill('coffee', 1.0)

    def test_can_add_fluid(self):
        # arrange
        self.mug.fill('water', 5.0)

        # act
        self.mug.fill('water', 5.0)

        # assert
        self.assertEqual(self.mug.get_content_amount(), 10.0)

    def test_can_add_and_remove_fluid(self):
        # arrange
        self.mug.fill('water', 5.0)

        # act
        self.mug.fill('water', 5.0)
        self.mug.pour_out_liquid(7)

        # assert
        self.assertEqual(self.mug.get_content_amount(), 3.0)

    def test_hack1(self):
        # arrange
        self.mug.fill('water', 5.0)

        # act
        self.mug.__content_type = 'wine'  # this will not change what self.content_type represents...

        # assert
        self.assertEqual(self.mug.get_content_type(), 'water')

    def test_filling_with_zero_does_not_change_content_type(self):
        # arrange

        # act
        self.mug.fill('water', 0.0)

        # assert
        self.assertEqual(self.mug.get_content_type(), self.mug.NOTHING)


if __name__ == '__main__':
    unittest.main()

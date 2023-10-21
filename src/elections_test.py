import unittest

from src.elections import Constituency


class ElectionsTest(unittest.TestCase):
    def setUp(self):
        self.testee = Constituency(['PartyA', 'PartyB', 'PartyC'])

    def test_is_created(self):
        self.assertIsNotNone(self.testee)

    def test_can_register(self):
        voter = 'Bob'
        self.testee.register_voter(voter)
        self.assertTrue(self.testee.is_registered(voter))

    def test_registered_can_vote(self):
        pass

    def test_cannot_register_twice(self):
        pass

    def test_vote_twice(self):
        pass

    def test_votes_are_reflected_in_party_totals(self):
        pass

    def test_cannot_vote_for_nonexistent_party(self):
        pass

    def test_cannot_create_two_parties_with_same_name(self):
        pass

    # with validators
    def test_can_create_voter_with_valid_name(self):
        pass

    def test_cannot_create_voter_with_invalid_name(self):
        pass





if __name__ == '__main__':
    unittest.main()

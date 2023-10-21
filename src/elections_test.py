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
        voter = 'Bob'
        self.testee.register_voter(voter)
        self.testee.vote(voter, 'PartyA')

    def test_cannot_register_twice(self):
        voter = 'Bob'
        self.testee.register_voter(voter)
        with self.assertRaises(RuntimeError):
            self.testee.register_voter(voter)

    def test_vote_twice(self):
        self.testee.register_voter('Bob')
        self.testee.vote('Bob', party='PartyA')

        # sprawdzic, ze to wywoluje wyjatek
        with self.assertRaises(RuntimeError):
            self.testee.vote('Bob', party='PartyA')

    def test_votes_are_reflected_in_party_totals(self):
        self.testee.register_voter('Bob1')
        self.testee.vote('Bob1', party='PartyA')
        self.testee.register_voter('Bob2')
        self.testee.vote('Bob2', party='PartyA')
        self.testee.register_voter('Bob3')
        self.testee.vote('Bob3', party='PartyC')

        self.assertEqual(self.testee.get_votes_of_party('PartyA'), 2)
        self.assertEqual(self.testee.get_votes_of_party('PartyB'), 0)
        self.assertEqual(self.testee.get_votes_of_party('PartyC'), 1)

    def test_cannot_vote_for_nonexistent_party(self):
        self.testee.register_voter('Bob1')
        with self.assertRaises(RuntimeError):
            self.testee.vote('Bob1', party='PartyX')

    def test_cannot_create_two_parties_with_same_name(self):
        with self.assertRaises(RuntimeError):
            Constituency(['PartyA', 'PartyA'])

    # with validators
    def test_can_create_voter_with_valid_name(self):
        pass

    def test_cannot_create_voter_with_invalid_name(self):
        pass





if __name__ == '__main__':
    unittest.main()

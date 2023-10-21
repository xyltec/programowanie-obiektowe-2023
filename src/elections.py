class Constituency:

    def __init__(self, parties: list[str]):
        unique_names = set(parties)
        if len(unique_names) != len(parties):
            raise RuntimeError('Party names are not unique')
        self.__voted: dict[str, bool] = {}
        self.__parties = parties
        self.__n_parties = len(parties)
        self.__votes = [0] * self.__n_parties

        # kompozycja
        self.__user_validator = VoterEligibilityValidator()

    def register_voter(self, voter_name: str):
        if not self.__user_validator.is_valid(voter_name):
            raise RuntimeError('User name is not valid')

        if voter_name in self.__voted:
            raise RuntimeError('This person is already registered')
        self.__voted[voter_name] = False  # not voted

    def is_registered(self, voter_name: str) -> bool:
        return voter_name in self.__voted

    def can_vote(self, voter_name: str) -> bool:
        if voter_name not in self.__voted:
            return False
        if self.__voted[voter_name]:
            return False
        return True

    def vote(self, voter_name: str, party: str):
        # throws RuntimeError if voter cannot vote, or has already voted
        if not self.can_vote(voter_name):
            raise RuntimeError(f'Person {voter_name} cannot vote')

        if party not in self.__parties:
            raise RuntimeError('No such party')
        idx = self.__parties.index(party)
        self.__votes[idx] += 1
        self.__voted[voter_name] = True

    def get_votes_of_party(self, party_name: str) -> int:
        if party_name not in self.__parties:
            raise RuntimeError('No such party')
        idx = self.__parties.index(party_name)
        return self.__votes[idx]

    def get_results_as_members_of_parliament(self, parliament_places: int) -> list[int]:
        """
        :param parliament_places: how many places should be split
        :return: for each of the parties (in order) get the number of members of parliament it gets
        """
        # todo: please implenent the D'Hondt method _before_ Oct 15th 7am CEST
        return self.__votes


class VoterEligibilityValidator:

    # docelowo:
    # def is_valid(self, user: User) -> bool:

    def is_valid(self, name: str) -> bool:
        return len(name) >= 2


if __name__ == '__main__':
    con = Constituency(['A', 'B', 'C'])
    con.register_voter('u1')
    con.register_voter('u2')
    con.register_voter('u3')
    con.vote('u1', 'A')
    con.vote('u2', 'A')
    con.vote('u3', 'A')
    print(con.get_results_as_members_of_parliament(10))

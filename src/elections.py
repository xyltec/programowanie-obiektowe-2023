class Constituency:

    def __init__(self, parties: list[str]):
        self.__voted: dict[str, bool] = {}
        self.__parties = parties
        self.__n_parties = len(parties)
        self.__votes = [0] * self.__n_parties

    def register_voter(self, voter_name: str):
        if voter_name in self.__voted:
            raise RuntimeError('This person is already registered')
        self.__voted[voter_name] = False  # not voted

    def is_registered(self, voter_name: str) -> bool:
        pass

    def can_vote(self, voter_name: str) -> bool:
        pass

    def vote(self, voter_name: str, party: str):
        # throws RuntimeError if voter cannot vote, or has already voted
        if voter_name not in self.__voted:
            raise RuntimeError('Person cannot vote')
        if self.__voted[voter_name]:
            raise RuntimeError('Person already voted')
        if party not in self.__parties:
            raise RuntimeError('No such party')
        idx = self.__parties.index(party)
        self.__votes[idx] += 1

    def get_votes_of_party(self, party_name: str) -> int:
        pass

    def get_results_as_members_of_parliament(self, parliament_places: int) -> list[int]:
        """
        :param parliament_places: how many places should be split
        :return: for each of the parties (in order) get the number of members of parliament it gets
        """
        # todo: please implenent the D'Hondt method _before_ Oct 15th 7am CEST
        return self.__votes


class NameValidator:
    def is_valid(self, name:str) -> bool:
        pass

if __name__ == '__main__':
    con = Constituency(['A', 'B', 'C'])
    con.register_voter('u1')
    con.register_voter('u2')
    con.register_voter('u3')
    con.vote('u1', 'A')
    con.vote('u2', 'A')
    con.vote('u3', 'A')
    print(con.get_results_as_members_of_parliament(10))
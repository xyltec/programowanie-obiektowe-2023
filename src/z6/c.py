import random
from string import ascii_lowercase

# Metody statyczne

class User:

    def __init__(self, name: str):
        self.name = name

    @staticmethod
    def get_random_user() -> 'User':
        return User(name=''.join(random.sample(ascii_lowercase, 6)))

    def __repr__(self):
        return self.name


print(User.get_random_user())
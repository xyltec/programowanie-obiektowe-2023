import datetime
from time import sleep


class ExpiringDict:
    def __init__(self, ttl: float):
        self.__dict = dict()
        self.__expiry = dict()
        self.__ttl = ttl

    def __getitem__(self, item):
        now = datetime.datetime.now().timestamp()

        if item not in self.__dict:
            return None

        if now > self.__expiry[item]:
            self.__expiry.pop(item)
            self.__dict.pop(item)
            return None

        return self.__dict[item]

    def __setitem__(self, key, value):
        now = datetime.datetime.now().timestamp()
        expiry = now + self.__ttl

        self.__dict[key] = value
        self.__expiry[key] = expiry


if __name__ == '__main__':
    g = ExpiringDict(ttl=0.5)
    g[10] = 12
    print(g[10])
    sleep(0.4)
    print(g[10])

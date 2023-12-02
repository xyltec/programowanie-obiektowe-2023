from collections.abc import Iterable

a = [1, 2, 3]
b = (1, 2, 3)
c = {1, 2, 3}
d = {"a": 1, "ż": 2}


def select_best_user(users: Iterable[str]) -> str | None:
    # impl....
    for u in users:
        if u.startswith('ż'):
            return u
    return None


if __name__ == '__main__':
    # susers = {'abra', 'kadabra', 'żerdź'}
    susers = ('abra', 'kadabra', 'żerdź')
    print(select_best_user(susers))
    print(select_best_user(d.keys()))

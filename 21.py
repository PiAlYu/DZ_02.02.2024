from functools import lru_cache

def moves(h):
    return h * 2, h * 3

@lru_cache(None)
def game(h):
    if h >= 100:
        return "end"
    if any(game(x) == "end" for x in moves(h)):
        return "p1"
    if all(game(x) == "p1" for x in moves(h)):
        return "v1"
    if any(game(x) == "v1" for x in moves(h)):
        return "p2"
    if all(game(x) == "p1" or game(x) == "p2" for x in moves(h)):
        return "v2"

for i in range(1, 101):
    if game(i) == 'v2':
        print(i, game(i))

from functools import lru_cache

def moves(h):
    return h * 2, h * 3

@lru_cache(None)
def game(h):
    if h >= 100:
        return "end"
    if any(game(x) == "end" for x in moves(h)):
        return "p1"
    if any(game(x) == "p1" for x in moves(h)):
        return "v1"

for i in range(1, 101):
    if game(i) == 'v1':
        print(i, game(i))

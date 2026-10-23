from itertools import permutations

for p in permutations(range(10), 8):
    s, e, n, d, m, o, r, y = p

    if s == 0 or m == 0:
        continue

    SEND = 1000*s + 100*e + 10*n + d
    MORE = 1000*m + 100*o + 10*r + e
    MONEY = 10000*m + 1000*o + 100*n + 10*e + y

    if SEND + MORE == MONEY:
        print(SEND, "+", MORE, "=", MONEY)
        break
        
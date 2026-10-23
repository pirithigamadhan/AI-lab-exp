from collections import deque

def solve():
    q = deque([((3, 3, 1), [])])
    seen = set()
    moves = [(1,0), (2,0), (0,1), (0,2), (1,1)]

    while q:
        (m, c, b), path = q.popleft()

        if (m, c, b) in seen:
            continue
        seen.add((m, c, b))
        path = path + [(m, c, b)]

        if (m, c, b) == (0, 0, 0):
            print(path)
            return

        for x, y in moves:
            nm, nc = (m-x, c-y) if b else (m+x, c+y)
            nb = 1-b

            if 0 <= nm <= 3 and 0 <= nc <= 3:
                if (nm == 0 or nm >= nc) and (nm == 3 or 3-nm >= 3-nc):
                    q.append(((nm, nc, nb), path))

solve()
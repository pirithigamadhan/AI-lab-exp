from collections import deque

def water_jug():
    q = deque([(0, 0)])
    seen = set()

    while q:
        a, b = q.popleft()

        if (a, b) in seen:
            continue
        seen.add((a, b))
        print(a, b)

        if a == 2 or b == 2:
            print("Goal reached!")
            return

        q.extend([
            (4, b), (a, 3), (0, b), (a, 0),
            (a-min(a, 3-b), b+min(a, 3-b)),
            (a+min(b, 4-a), b-min(b, 4-a))
        ])

water_jug()
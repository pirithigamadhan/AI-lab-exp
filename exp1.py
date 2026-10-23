from heapq import heappush, heappop

goal = (1, 2, 3, 4, 5, 6, 7, 8, 0)

def heuristic(state):
    return sum(
        state[i] != 0 and state[i] != goal[i]
        for i in range(9)
    )

def solve(start):
    pq = []
    heappush(pq, (heuristic(start), 0, start, []))
    visited = set()

    while pq:
        f, g, state, path = heappop(pq)

        if state == goal:
            for step in path + [state]:
                print(step[:3])
                print(step[3:6])
                print(step[6:])
                print()
            return

        if state in visited:
            continue
        visited.add(state)

        zero = state.index(0)
        moves = []

        if zero >= 3:
            moves.append(zero - 3)
        if zero < 6:
            moves.append(zero + 3)
        if zero % 3 != 0:
            moves.append(zero - 1)
        if zero % 3 != 2:
            moves.append(zero + 1)

        for pos in moves:
            new_state = list(state)
            new_state[zero], new_state[pos] = (
                new_state[pos], new_state[zero]
            )
            new_state = tuple(new_state)

            if new_state not in visited:
                heappush(
                    pq,
                    (g + 1 + heuristic(new_state),
                     g + 1, new_state, path + [state])
                )

    print("No solution exists.")

start = (1, 2, 3,
         4, 0, 6,
         7, 5, 8)

solve(start)
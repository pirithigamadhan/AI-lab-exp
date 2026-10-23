board = [" "] * 9

def display():
    for i in range(0, 9, 3):
        print(board[i], "|", board[i+1], "|", board[i+2])

def play():
    player = "X"
    for _ in range(9):
        display()
        pos = int(input(player + ", enter position (1-9): ")) - 1

        if pos < 0 or pos > 8 or board[pos] != " ":
            print("Invalid move!")
            continue

        board[pos] = player

        for a, b, c in [(0,1,2), (3,4,5), (6,7,8),
                        (0,3,6), (1,4,7), (2,5,8),
                        (0,4,8), (2,4,6)]:
            if board[a] == board[b] == board[c] != " ":
                display()
                print(player, "wins!")
                return

        player = "O" if player == "X" else "X"

    display()
    print("Draw!")

play()
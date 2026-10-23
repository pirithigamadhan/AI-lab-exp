def minimax(board, isMax):
    if board.count("X") == 3:
        return 1
    if board.count("O") == 3:
        return -1

    if " " not in board:
        return 0

    scores = []
    for i in range(9):
        if board[i] == " ":
            board[i] = "X" if isMax else "O"
            scores.append(minimax(board, not isMax))
            board[i] = " "

    return max(scores) if isMax else min(scores)

board = ["X", "O", "X",
         " ", "O", " ",
         " ", " ", "X"]

print("Best score:", minimax(board, True))
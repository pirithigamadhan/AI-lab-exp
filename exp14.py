def alphabeta(depth, node, alpha, beta, maximizing):
    if depth == 0:
        return node

    if maximizing:
        best = -999
        for child in node:
            best = max(best, alphabeta(depth-1, child, alpha, beta, False))
            alpha = max(alpha, best)
            if beta <= alpha:
                break
        return best
    else:
        best = 999
        for child in node:
            best = min(best, alphabeta(depth-1, child, alpha, beta, True))
            beta = min(beta, best)
            if beta <= alpha:
                break
        return best

tree = [[3, 5], [6, 9]]
print("Best value:", alphabeta(2, tree, -999, 999, True))
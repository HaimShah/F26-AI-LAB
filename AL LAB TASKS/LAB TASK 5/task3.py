import math

def minimax(depth, index, max_turn, scores, target, count):
    if depth == target:
        count[0] += 1
        return scores[index]

    if max_turn:
        left = minimax(depth + 1, index * 2, False, scores, target, count)
        right = minimax(depth + 1, index * 2 + 1, False, scores, target, count)
        return max(left, right)

    left = minimax(depth + 1, index * 2, True, scores, target, count)
    right = minimax(depth + 1, index * 2 + 1, True, scores, target, count)
    return min(left, right)


def alphabeta(depth, index, max_turn, scores, target, alpha, beta, count):
    if depth == target:
        count[0] += 1
        return scores[index]

    if max_turn:
        value = float("-inf")

        for i in range(2):
            result = alphabeta(depth + 1, index * 2 + i, False,
                               scores, target, alpha, beta, count)
            value = max(value, result)
            alpha = max(alpha, value)

            if alpha >= beta:
                break

        return value

    value = float("inf")

    for i in range(2):
        result = alphabeta(depth + 1, index * 2 + i, True,
                           scores, target, alpha, beta, count)
        value = min(value, result)
        beta = min(beta, value)

        if alpha >= beta:
            break

    return value


scores = [9, 2, 5, 3, 9, 2, 5, 3] 
depth = int(math.log2(len(scores)))

minimax_count = [0]
alphabeta_count = [0]

minimax_value = minimax(0, 0, True, scores, depth, minimax_count)

alphabeta_value = alphabeta(
    0, 0, True, scores, depth,
    float("-inf"), float("inf"), alphabeta_count
)

print("Scores:", scores) 
print("Minimax Value:", minimax_value)
print("Minimax Leaves Evaluated:", minimax_count[0])
print("Alpha-Beta Value:", alphabeta_value)
print("Alpha-Beta Leaves Evaluated:", alphabeta_count[0])
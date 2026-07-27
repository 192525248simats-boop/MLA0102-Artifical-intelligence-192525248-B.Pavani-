def alphabeta(values):
    alpha = float('-inf')
    beta = float('inf')

    left = max(values[0], values[1])
    alpha = left

    if alpha >= beta:
        return alpha

    right = max(values[2], values[3])

    result = min(left, right)

    return result


print("Enter 4 leaf node values:")

values = []
for i in range(4):
    values.append(int(input()))

result = alphabeta(values)

print("Optimal Value =", result)

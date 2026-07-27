def minimax(values):
    while len(values) > 1:
        new = []

        # Min level
        for i in range(0, len(values), 2):
            new.append(min(values[i], values[i + 1]))

        if len(new) == 1:
            return new[0]

        values = []

        # Max level
        for i in range(0, len(new), 2):
            values.append(max(new[i], new[i + 1]))

    return values[0]


n = int(input("Enter number of leaf nodes (4 or 8): "))

print("Enter leaf node values:")
values = []

for i in range(n):
    values.append(int(input()))

result = minimax(values)

print("Optimal Value =", result)

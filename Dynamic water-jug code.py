a = 0
b = 0

A = int(input("Enter capacity of Jug A: "))
B = int(input("Enter capacity of Jug B: "))
target = int(input("Enter target amount: "))

while b != target:
    if a == 0:
        a = A
        print("Fill Jug A :", a, b)

    elif b == B:
        b = 0
        print("Empty Jug B:", a, b)

    else:
        transfer = min(a, B - b)
        a = a - transfer
        b = b + transfer
        print("Pour A to B:", a, b)

print("Target reached!")

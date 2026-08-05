# Monkey and Banana Problem
# Simple AI Experiment
# Can be run in Python IDLE

# Initial positions
monkey = "door"
box = "window"
banana = "center"

print("Initial State")
print("Monkey Position :", monkey)
print("Box Position    :", box)
print("Banana Position :", banana)
print()

# Step 1: Monkey goes to the box
print("Step 1: Monkey moves to the box.")
monkey = box

# Step 2: Monkey pushes the box under the banana
print("Step 2: Monkey pushes the box under the banana.")
box = banana
monkey = banana

# Step 3: Monkey climbs onto the box
print("Step 3: Monkey climbs onto the box.")

# Step 4: Monkey picks the banana
print("Step 4: Monkey picks the banana.")

print("\nGoal Achieved!")
print("Monkey successfully got the banana.")

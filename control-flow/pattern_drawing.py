# pattern_drawing.py

size = int(input("Enter the size of the pattern: "))

row = 0

while row < size:
    for _ in range(size):
        print("*", end="")
    print()
    row += 1
# This program draws a square pattern of asterisks based on user input
print("Right angle triangle with Stars")
n = int(input("enter a num"))
for i in range(n):
    for j in range (i+1):
        print("🌟",end=" ")
    print()  

    print("Mirrored Right Angle Triangle with Stars")
n = int(input("Enter a number: "))

for i in range(1, n + 1):
    # Print spaces first
    for j in range(n - i):
        print("  ", end="")  # double space for alignment with 🌟
    # Print stars
    for k in range(i):
        print("🌟", end=" ")
    print()
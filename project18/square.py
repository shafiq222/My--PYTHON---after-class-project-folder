# Program to create square values in a user-defined range
# and separate them into even and odd lists

start = int(input("Enter starting number: "))
end = int(input("Enter ending number: "))

squares = []
even_squares = []
odd_squares = []

for i in range(start, end + 1):
    square = i * i
    squares.append(square)

    if square % 2 == 0:
        even_squares.append(square)
    else:
        odd_squares.append(square)

print("\nSquare values:", squares)
print("Even square values:", even_squares)
print("Odd square values:", odd_squares)

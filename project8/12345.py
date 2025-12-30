# Ask the user how many numbers they want to enter
n = int(input("How many numbers do you want to enter? "))

numbers = []

# Take numbers from the user
for i in range(n):
    num = int(input(f"Enter number {i + 1}: "))
    numbers.append(num)

# Reverse the list
reversed_numbers = numbers[::-1]

# Display results
print("\nOriginal order:", numbers)
print("Reverse order:", reversed_numbers)
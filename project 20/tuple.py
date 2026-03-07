# Program to calculate the product of all numbers in a tuple

# Given tuple
numbers = (2, 3, 4, 5)

# Initialize product variable
product = 1

# Loop through the tuple
for num in numbers:
    product *= num

# Display result
print("The product of all numbers in the tuple is:", product)
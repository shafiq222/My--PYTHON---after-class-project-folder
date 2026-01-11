numbers = [3, 5, 8, 13, 25]

for num in numbers:          # Outer loop: each number
    n = num
    binary = ""

    while n > 0:             # Inner loop: convert that number
        remainder = n % 2
        binary = str(remainder) + binary
        n = n // 2

    print(num, "in binary is", binary)
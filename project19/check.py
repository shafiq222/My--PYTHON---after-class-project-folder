# Step 1: Given test dictionary
test_dict = {
    "apple": 2,
    "banana": 3,
    "orange": 1
}

print("Original Dictionary:")
print(test_dict)


# Step 2: Function to update frequency
def update_frequency(dictionary, key):
    # If key exists, increase count
    if key in dictionary:
        dictionary[key] += 1
    else:
        # If key does not exist, add it with value 1
        dictionary[key] = 1


# Step 3: Example usage
new_value = "apple"   # Try changing this value
update_frequency(test_dict, new_value)

print("\nUpdated Dictionary:")
print(test_dict)

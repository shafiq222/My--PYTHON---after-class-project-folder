# 1. Define the Custom Exception
class InvalidAgeError(Exception):
    """Exception raised for ages outside the logical range."""
    def __init__(self, age, message="Age must be between 0 and 120"):
        self.age = age
        self.message = message
        super().__init__(self.message)

# 2. Define the Validation Function
def validate_age(age):
    if age < 0:
        raise InvalidAgeError(age, "Error: Age cannot be negative.")
    if age > 120:
        raise InvalidAgeError(age, "Error: Age is too high (limit is 120).")
    return True

# 3. Execution Block
print("--- Professional Age Counter ---")

while True:
    try:
        # Prompt user for input
        user_input = input("\nEnter your age (or type 'exit' to quit): ")
        
        # Check if user wants to quit
        if user_input.lower() == 'exit':
            print("Goodbye!")
            break
            
        # Convert to integer (this might raise a ValueError)
        age = int(user_input)
        
        # Check the age (this might raise our InvalidAgeError)
        if validate_age(age):
            print(f"Success! Your age is recorded as: {age}")
            break # Exit loop on success
            
    except InvalidAgeError as e:
        # Catch our custom exception
        print(f"Validation Problem: {e.message}")
        
    except ValueError:
        # Catch errors where the user types "hello" instead of "25"
        print("Input Error: Please enter a whole number.")
        
    finally:
        # This runs every time, regardless of errors
        print("--- Transaction Logged ---")
import random

#  Global Constants and Configuration 

# Define the character sets as constants for better readability and maintenance.
LOWERCASE_LETTERS = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
UPPERCASE_LETTERS = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
NUMBERS = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
SYMBOLS = ['!', '#', '$', '%', '&', '(', ')', '*', '+', '-', '=', '_', '@', '^'] # Added more common symbols

ALL_LETTERS = LOWERCASE_LETTERS + UPPERCASE_LETTERS
ALL_CHARACTERS = ALL_LETTERS + NUMBERS + SYMBOLS

def get_integer_input(prompt: str, min_val: int = 0) -> int:
    """
    Safely handles user input, ensuring it is a non-negative integer.
    Includes a loop to re-prompt the user upon invalid input.
    """
    while True:
        try:
            # Use a stripped input for robustness
            user_input = input(prompt).strip()
            # firstly we will check for non-empty input before converting.
            if not user_input:
                raise ValueError("Input cannot be empty.")

            value = int(user_input)

            if value < min_val:
                print(f" Error: Please enter a number greater than or equal to {min_val}.")
                continue 
            return value

        except ValueError as e:
            # It will catch your non-integer input or a string.
            print(f" Invalid input. Please enter a whole number. Details: {e}")


# Core Logic Function -

def generate_strong_password(num_letters: int, num_symbols: int, num_numbers: int) -> str:
    """
    Generates a strong, random password by combining and shuffling characters
    from the specified character sets.
    """
    password_list = []

    # 1. Add random letters
    # 2. Use random.choices for a more direct way to pick multiple random elements
    # 3. and extend the list in a single step.
    password_list.extend(random.choices(ALL_LETTERS, k=num_letters))

    # 2. Add random numbers
    password_list.extend(random.choices(NUMBERS, k=num_numbers))

    # 3. Add random symbols
    password_list.extend(random.choices(SYMBOLS, k=num_symbols))

    # 4. Final steps: Shuffle and combine
    total_length = len(password_list)

    if total_length == 0:
        return "Error: Password length is zero. Please try again."

    # Perform an in-place shuffle for maximum randomness
    random.shuffle(password_list)

    # Join the list of characters into a final string
    final_password = "".join(password_list)

    return final_password

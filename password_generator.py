import random
import string

def generate_password(length=8):
    # Get the desired length from the user
    if length < 8 or length >16:
        print("Please enter the length between 8 through 16")
        return 
    
    # Character pools
    capital_alpha = string.ascii_uppercase
    small_alpha = string.ascii_lowercase
    digits = string.digits
    special_symbols = string.punctuation
    
    # Ensure first character is a capital letter
    password = random.choice(capital_alpha)
    
    # Define possible sequences for second, third, and fourth characters
    list1 = [
        (small_alpha, digits, special_symbols),
        (small_alpha, special_symbols, digits),
        (digits, small_alpha, special_symbols),
        (digits, special_symbols, small_alpha),
        (special_symbols, small_alpha, digits),
        (special_symbols, digits, small_alpha)
    ]
    
    # Select a random tuple from list
    list1 = random.choice(list1)
    
    # Add second, third, and fourth characters according to the chosen sequence
    for i in list1:
        password += random.choice(i)
    
    # Subtract 4 from the desired length for the fixed characters
    length -= 4
    
    # Add remaining random characters to the password
    for _ in range(length):
        char = string.ascii_letters + string.digits + string.punctuation
        password += random.choice(char)
    
    return password    

# Example usage:
if __name__ == "__main__":
    while True:
        try:
            length = int(input("Enter the desired password length (between 8 and 16): "))
            if 8 <= length <= 16:
                break
            else:
                print("Password length must be between 8 and 16 characters.")
        except ValueError:
            print("Invalid input. Please enter a number.")
        
    password = generate_password(length)
    print("Generated password:", password)

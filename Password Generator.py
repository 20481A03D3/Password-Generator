import secrets
import string

def generate_password(length):
    # Define characters to be used in the password
    characters = string.ascii_letters + string.digits + string.punctuation

    # Generate the password
    password = ''.join(secrets.choice(characters) for _ in range(length))
    
    return password

def main():
    # Prompt the user to specify the desired length of the password
    try:
        password_length = int(input("Enter the desired length of the password: "))
    except ValueError:
        print("Please enter a valid integer for the password length.")
        return

    # Check if the password length is non-negative
    if password_length <= 0:
        print("Password length must be greater than 0.")
        return

    # Generate and display the password
    password = generate_password(password_length)
    print("Generated Password:", password)

if __name__ == "__main__":
    main()

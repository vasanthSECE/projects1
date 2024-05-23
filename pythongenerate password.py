import random
import string

def generate_password(length):
    if length < 1:
        return "Error: Password length should be at least 1"

    # Define possible characters in the password
    characters = string.ascii_letters + string.digits + string.punctuation

    # Generate a random password
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

def main():
    print("Password Generator")

    while True:
        try:
            length = int(input("Enter the desired length of the password: "))
            if length < 1:
                print("Please enter a positive number.")
                continue
        except ValueError:
            print("Invalid input. Please enter a numeric value.")
            continue

        password = generate_password(length)
        print(f"Generated Password: {password}")
        break

if __name__ == "__main__":
    main()

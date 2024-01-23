import random
import string

def generate_password(length):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

def password_generator():
    try:
        length = int(input("Enter the desired length of the password: "))
        if length <= 0:
            print("Please enter a positive length.")
            return
        password = generate_password(length)
        print(f"Generated Password: {password}")

    except ValueError:
        print("Invalid input. Please enter a valid positive integer for the password length.")
    except Exception as e:
        print(f"An error occurred: {e}")
password_generator()
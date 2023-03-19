import random
import string

def generate_password(length=12):
    lowercase_letters = string.ascii_lowercase
    uppercase_letters = string.ascii_uppercase
    digits = string.digits
    special_characters = string.punctuation

    all_characters = lowercase_letters + uppercase_letters + digits + special_characters

    password = ''.join(random.choice(all_characters) for i in range(length))

    return password

num_passwords = int(input("How many passwords do you want to generate? "))
password_length = int(input("How long should the passwords be? "))

for i in range(num_passwords):
    password = generate_password(password_length)
    print("Password", i+1, ":", password)

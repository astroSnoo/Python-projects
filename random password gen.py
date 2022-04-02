import random

characters = "abcdefghijklmnopqrstuvwxyz$%!^&*()?:;@#1234567890ABCDEFGHIJKLMNOPQRSTUVWXYZ"
characters = list(set(characters))
amount = int(input("How many passwords do you want to generate?\n"))
length = int(input("How many characters would you like your pass word to be?\n"))
for i in range(amount):
    password = ""
    for x in range(length):
        password += random.choice(characters)
    print(f"Your new password is {password}")

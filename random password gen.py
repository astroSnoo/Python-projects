import random

characters = "abdefghijklmnopqrstuvwxyz£$%!^&*()?:;@#1234567890ABCDEFGHIJKLMNOPQRSTUVWXYZ"

amount = int(input("How many passwords do you want to generate\n"))
for i in range(amount):
    password = ""
    for x in range(15):
        password += random.choice(characters)
    print(f"Your new password is {password}")
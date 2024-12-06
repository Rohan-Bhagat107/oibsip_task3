import random
import string


print("Enter your details here: ")
pass_length=int(input("How much lenght you want for your password: "))
name=input("Please enter your name: ")
email=input("Please enter your email: ")
chars=string.ascii_letters
chars+=string.digits
chars+=string.punctuation
password=""
for i in range(pass_length):
    next_character=random.choice(chars)
    password+=next_character
print(f"{name}Your random passowrd is: {password}")


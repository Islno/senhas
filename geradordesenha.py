import random

length = 10
characters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890!@#$%^&*()"

password = ""

for i in range(length):
    password += random.choice(characters)

print("Senha gerada: ", password)

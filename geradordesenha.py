import random

tamanho = 10
caracteries = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890!@#$%^&*()"

senha = ""

for i in range(tamanho):
    senha += random.choice(caracteries)

print("Senha gerada: ", senha)

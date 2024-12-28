import random

caracteres = "+-/*!&$#?=@abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"
longitud = int(input("Define la longitud de tu contraseña"))
contrasena = ""

for i in range (longitud):
    contrasena += random.choice(caracteres)

print(contrasena)

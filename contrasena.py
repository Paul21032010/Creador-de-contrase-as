import random
caracteres = "+-/*!&$#?=@abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"
extension = int(input("Escribe de cuantos caracteres quieres que sea la contraseña"))
contrasena = ""
for i in range(extension):
    contrasena += random.choice(caracteres)
print(contrasena)

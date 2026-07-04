import random


cantidad = 29

contrasenas = set()

while len(contrasenas) < cantidad:
    
    contrasena = random.randint(100000, 999999)
    contrasenas.add(contrasena)

print("Contraseñas generadas:\n")

for i, clave in enumerate(sorted(contrasenas), start=1):
    print(f"Persona {i:2}: {clave}")
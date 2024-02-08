# Variables y tipos de datos

first_name = 'Brian Obed'
last_name = "Pérez Hernandez"
full_name = first_name + ' ' + last_name
print(full_name)

# Int, Float, Bool

age = 25
height = 1.75
is_student = False

tipo = type(first_name)
print(tipo)

# No existen las constantes, solo se establece una convención para que no se modifiquen al usar mayúsculas

PI = 3.1416
GRAVITY = 9.8

#Pedir datos al usuario y cambiar tipo de dato
# Operadores relacionales (==, !=, <, >, <=, >=)

name = input('Ingresa tu nombre: ')
age = int(input('Ingresa tu edad: '))
score = float( input('Ingresa tu calificación: '))
active = input('¿Estás activo? (si/no): ') == 'si'

print(type(name), type(age), type(score), type(active))


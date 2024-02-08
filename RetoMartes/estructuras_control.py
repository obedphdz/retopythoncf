# Estructuras de control
# if (elif). match (switch), foreach, while

# Bool se obtiene de:
# Operadores relacionales (==, <,<=,>,>=)
# Operadores lógicos (and (todo verdadero), or (uno verdadero), not(inverso del bool actual))

age = int(input("Ingresa tu edad: "))

if age < 110:
    if age >= 18:
        print("Puedes Votar")
    else:
        print("No puedes votar")
else:
    print("La edad introducida no es valida")


color = "green"

if color == "green":
    print("Puede continuar")
elif color == "yellow":
    print("Alto parcial")
elif color == "red":
    print("Alto Total")
else:
    print("El color no es válido")


match color:
    case "red":
        print("Alto Total")
    case "yellow":
        print("Alto Parcial")
    case "green":
        print("Puede continuar")
    case _:  # Case default
        print("Color no valido")

# foreach -> Cuando sepamos el numero de iteraciones
# While -> cuando NO sepamos el numero de iteraciones

title = "Estructuras de control"
for caracter in title:
    print(caracter)

for number in range(1, 101):
    if number % 2 == 0:  # if not (number %2 == 0)
        print(number)

num = 0
while num < 10:
    print(num)
    num += 1
else:
    print("la condicion NO se cumple")

rand, usenum, max_attends = 15, 0, 0

while usenum != rand or max_attends < 5:
    usenum = int(input("En que numero pienso?: "))
    max_attends += 1
if usenum == rand:
    print('Felicidades, encontraste el numero')
else:
    print('Lo sentimos, no encontraste el numero')
# Funciones
# Para definir una funcion se utiliza la palabra reservada def seguida del
# nombre de la funcion y parentesis, donde iran o no los parametros

# def suma (num1,num2):
#     return num1 + num2

# def resta (num1,num2):
#     return num1 - num2

# def multi (num1,num2):
#     return num1 * num2

# summa = suma(5,9)
# res = resta(25,8)
# mul = multi(50,2)

# print(f'Suma = {summa}')
# print(f'Resta = {res}')
# print(f'Multiplicacion = {mul}')


# Programa para sacar promedio, el usuario aprobará si su promedio es >= 7


def set_calif ():
    calificaciones = []
    for option in range(0,5):
        score = int(input('Ingresa calificacion: '))
        calificaciones.append(score)
    return calificaciones
    

def promedio(calificaciones):
    return sum(calificaciones)/len(calificaciones)

def message(prom):
    if prom >= 7:
        print(f'Aprobaste el curso con {prom}')
    else:
        print(f'Reprobaste el curso con {prom}')


message(promedio(set_calif()))


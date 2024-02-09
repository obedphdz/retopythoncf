# # Tuplas (son inmutables)- diccionarios
# #Las tuplas son por lo regular de longitud pequeña y su inmutabilidad las hace mas seguras para datos dentro del programa

# settings = ('localhost', 3306, 'root', 'password', 'database')
# host, port, username, password, name = settings #Desempaquetado de tuplas
# host, port, _, _, _ = settings # Ignora los valores cuando se sabe el numero de valores siguientes de la tupla
# host, port, *_ = settings # Ignora los valores cuando NO se sabe el numero de valores siguientes de la tupla
# host, *_, database = settings #Ignora los valores entre el primer y ultimo dato de la tupla

# print(len(settings))

# sub_setting = settings[::-1]
# print(sub_setting)

# # Se pueden definir tuplas anidadas

# tuples = (
#     (1,2,3),
#     (4,5,6),
#     (7,8,9)
# )

# for _tuple in tuples:
#     print(_tuple)


# for number1, number2, number3 in tuples:
#     print(number1, number2, number3)


# # La lista y la tupla trabajan a base de indices, sin embargo el diccionario trabaja a base de clave-valor
# # Una llave != string, llave == objeto inmutable
# user = {
#     # llave : valor
#     'name' : 'Obed',
#     'age' : '25',
#     'active' : True,
#     10 : 3.14,
#     True : 'Verdadero',
#     (1,2,3) : 'Tupla'
# }

# print(user)
# print(type(user))

# print(user['name'])

# if 'name' in user:
#     print(user['name'])
# # Este método me asegura que si existe la llave me retorna su valor
# value = user.get('name')
# print(value)
# # En este caso ponemos una alternativa en caso de que no exista la llave
# value = user.get('username', 'No existe la llave')
# print(value)


# # Metodos en los diccionarios: keys (conocemos la coleccion de llaves), values (conocemos la coleccion de valores), items

# print(user.keys())
# print(user.values())
# print(user.items()) #Obetenemos la clave y valor de cada elementp del diccionario

# # Podemos convertir los resultados de estos metodos en tuplas o listas
# print(tuple(user.values()))
# print(list(user.values()))

# for key, value in tuple(user.items()):
#     print(key,value)


user = {
    'id'
}



for k, v in user.items():

    print(f'{k}: {v}')
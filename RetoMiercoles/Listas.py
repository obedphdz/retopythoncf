# #Listas = Estructura de datos

# my_list = [1,3.5,'hola',True,[9,3.1416,'mundo',False]]
# print(my_list)
# print(type(my_list))

# # Es recomendable que las listas solo sean de un tipo de datos
# # para evitar errores y que se declaren en plural
# #indices    0         1         2       3           4
# courses = ['Python', 'Django', 'Flask', 'Ruby', 'Ruby on Rails', 'C#']
# print(courses[2])
# last_index = len(courses)-1
# index = int(input('Ingresa el indice del cual quieres conocer su valor: '))

# if index <= last_index:
#     print(courses[index])
# else:
#     print('Lo sentimos, el indice NO es válido')

# # ------- Creacion de Sub-Listas ---------
# new_list = courses[0:5] 
# # Nos copia el num de indices -1, 
# # si se quieren todos los elementos se usa [:]
# # o se puede usar el siguiente formato [start:stop:skips] -> [0:5:2]
# # para invertir la lista seria [::-1]
# print(new_list)

# # Métodos para listas: 
# # .append (Agrega elementos al final de la lista), 
# courses.append('Javascript')
# courses.append('Typescript')
# courses.append('Swift')

# # .insert (inserta elementos en la posision que se indique y los demas valores se desplazan),
# courses.insert(1,'SQLServer') 
# # extend (Si se quieren agregar varios registros u otra lista esta es una mejor opcion en lugar de append)
# new_courses = ['Java9', 'Docker', 'Unix']
# courses.extend(new_courses) #✅
# # .remove (elimina el elemento de la lista que se indique), 
# courses.remove('Python')
# courses.remove('Flask')
# courses.remove('C#')
# # .count (Nos dice cuantas veces esta el elemento en  el listado),
# courses.count('Rust')
# # Tambien se puede usar este metodo con in y es el mas recomendado, por ejemplo
# print('Laravel' in courses) # False
# print('Swift' in courses) # True

# # .index (Nos dice en que indice se encuentra el elemento)
# print(courses.index('Laravel'))

# value = 'Laravel'
# if value in courses:
#     print('El indice es: ' + str(courses.index(value)))
# else:
#     print('Lo sentimos, el valor no existe dentro del listado')

# # .clear (Limpia toda la lista)
# courses.clear()
# print (courses)
# print(len(courses))

# # Para conocer el indice usamos la func enumerate()
# for index, course in enumerate(courses):
#     print('El valor para ', index, 'es ', course)

# for index, character in enumerate('Hola Mundo'):
#     print(index,character)

users_list = [[1,'Brian','Hernandez',4493956796,'bioph@gmail.com'],[2,'Fernando','Sanchez',4498569788,'fersa@outlook.com']]

for user in users_list:
    print(user)
# Programa que permita registrar a un usuario en el sistema, para ello
# se debe solicitar al usuario su nombre, apellido, No. telefono, correo
# Una vez que se hayan ingresado los datos, se debe imprimir un mensaje
# de bienvenida: "Hola + seguido del nombre completo del usuario +,
# en breve recibirás un correo a + seguido del correo electrónico ."

name = input('Ingresa tu nombre: ')
last_name = input('Ingresa tu apellido: ')
phone = int(input('Ingresa tu número de teléfono: '))
email = input('Ingresa tu correo electrónico: ')

print('Hola ' + name + ' ' + last_name + ', en breve recibirás un correo a ' + email + '.')

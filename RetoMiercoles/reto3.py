registros = int(input("Ingresa el numero de usuarios a registrar: "))
count = 0
users_list = []

while count < registros:
    print(
        "------------------------ Registro Usuario "
        + str(count + 1)
        + " ----------------------------------------"
    )
    name = input("Introduce nombre: ")
    while len(name) < 5 or len(name) > 50:
        print("Nombre(s) invalido")
        name = input("Introduce nombre válido (min 5 caracteres max 50): ")
        if len(name) >= 5 and len(name) <= 50:
            break

    apellidos = input("Introduce apellidos: ")
    while len(apellidos) < 5 or len(apellidos) > 50:
        print("Apellido(s) inválidos")
        apellidos = input("Introduce apellidos válidos (min 5 caracteres max 50): ")
        if len(apellidos) >= 5 and len(apellidos) <= 50:
            break

    phone = input("Telefono: ")
    while len(phone) != 10:
        print("Telefono inválido")
        phone = input("Ingrese Telefono de 10 dígitos: ")
        if len(phone) == 10:
            break

    email = input("E-mail: ")
    while len(email) < 5 or len(email) > 50:
        email = input("Introduce email valido: ")
        if len(email) > 5 and len(email) < 50:
            break
    users_list.append([count+1,name,apellidos,phone,email])
    count += 1
print("===========================================================================")
print("              Se han completado " + str(count) + " Registros")
print("===========================================================================")
for user in users_list:
    print(user)

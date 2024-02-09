resp = 10
users = {}
while resp != 5:
    print(
        "=================================== BIENVENIDX ====================================="
    )
    print(
        "======================= Selecciona un número para continuar ========================"
    )
    print("1.- Registrar Usuario")
    print("2.- Listar ID de usuarios registrados")
    print("3.- Buscar Usuario")
    print("4.- Editar Usuario")
    print("5.- SALIR DEL PROGRAMA")
    resp = int(input("Opcion: "))
    match resp:
        case 1:
            registros = int(input("Ingresa el numero de usuarios a registrar: "))
            count = 0

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
                    apellidos = input(
                        "Introduce apellidos válidos (min 5 caracteres max 50): "
                    )
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
                datos = {
                    "name": name,
                    "apellidos": apellidos,
                    "phone": phone,
                    "email": email,
                }
                users[count] = datos
                count += 1
            print(
                "==========================================================================="
            )
            print("              Se han completado " + str(count) + " Registros")
            print(
                "==========================================================================="
            )
        case 2:
            num_users = len(users)
            print(
                "==========================================================================="
            )
            print("              Se han registrado " + str(num_users) + " Usuarios")
            print(
                "==========================================================================="
            )
            for id_usuario, datos in users.items():
                print(f"ID: {id_usuario}")
                print(f"Nombre: {datos['name']}")
                print(f"Apellidos: {datos['apellidos']}")
                print(f"Telefono: {datos['phone']}")
                print(f"Email: {datos['email']}")
                print("----------------------------------------")
        case 3:
            id_user = int(input("Ingresa el ID del usuario a mostrar: "))
            datos = users[id_user]
            print(f"ID: {id_user}")
            print(f"Nombre: {datos['name']}")
            print(f"Apellidos: {datos['apellidos']}")
            print(f"Telefono: {datos['phone']}")
            print(f"Email: {datos['email']}")
        case 4:
            id_user = int(input("Ingresa el ID del usuario a editar: "))
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
            datos = {
                "name": name,
                "apellidos": apellidos,
                "phone": phone,
                "email": email,
            }
            users[id_user] = datos
            print(f'Usuario {id_user} Actualizado')

print("####################################################################")
print("                         HASTA LA PROXIMA 😊                        ")

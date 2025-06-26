estado = True
lista_usuarios = []
contraseña = ""

def ingresar_usuario():
    nombre = input("Ingrese el nombre del usuario: ")
    if ["nombre"] == nombre:
        print("El nombre ya existe. Intente con otro.")
        return nombre
        
    
    sexo = input("Ingrese el sexo del usuario (M/F/c): ")
    if sexo not in ['M', 'F', 'c']:
        print("Sexo no válido. Debe ser M, F o c.")
        sexo = input("Ingrese el sexo del usuario (M/F/c): ")
        return sexo
        
        
    
    comtraseña = input("Ingrese la contraseña del usuario: ")
    if len(comtraseña) >= 8:
        contraseña.isalpha()
        contraseña.isdigit()
        contraseña.strip()
    else:
        print("La contraseña debe tener al menos 8 caracteres que tengan al menos 1 digito, 1 caracter y sin espacios.")
        return comtraseña
        
    
    lista_usuarios.append({
        "nombre": nombre,
        "sexo": sexo,
        "contraseña": comtraseña
    })
    print("----------------------------")


def buscar_usuario():
    nombre_buscado = input("Ingrese el nombre del usuario a buscar: ")
    encontrado = False
    for usuario in lista_usuarios:
        if usuario["nombre"] == nombre_buscado:
            print(f"Nombre: {usuario['nombre']}")
            print(f"Sexo: {usuario['sexo']}")
            print(f"Contraseña: {usuario['contraseña']}")
            encontrado = True
            break
    if not encontrado:
        print("Usuario no encontrado.")
    print("----------------------------")

def eliminar_usuario():
    nombre_eliminar = input("Ingrese el nombre del usuario a eliminar: ")
    encontrado = False
    for i, usuario in enumerate(lista_usuarios):
        if usuario["nombre"] == nombre_eliminar:
            lista_usuarios.pop(i)
            print("Usuario eliminado.")
            encontrado = True
            break
    if not encontrado:
        print("Usuario no encontrado.")
    print("----------------------------")
        

    





while estado:
    try:
        print("1) ingrese un usuario")
        print("2) buscar usuario")
        print("3) eliminar usuario")
        print("4) salir")
        opcion = int(input("Ingrese una opción: "))
    except ValueError:
        print("Por favor, ingrese un número válido.")
        continue        
        
        


    if opcion == 1:
        ingresar_usuario()

    elif opcion == 2:
        buscar_usuario()

    elif opcion == 3:
        eliminar_usuario()


    elif opcion == 4:
        print("Saliendo del programa...")
        estado = False
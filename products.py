import db
import os
def menu_products():
    flag = True
    while flag:
        print("========== MENÚ DE PRODUCTOS ==========")
        print("Opciones:" 
        +"\n 1. Agregar producto"
        +"\n 2. Listar"
        +"\n 3. Buscar"
        +"\n 4. Eliminar"
        +"\n 5. Actualizar stock (reabastecimiento)"
        +"\n 6. Valor total del inventario"
        +"\n 7. Regresar al menú principal")
        user_option = input("Elija una opción: ")
        match user_option:
            case "1":
                os.system("clear")
                print("========== AGREGAR PRODUCTOS ==========")
                exit()
            case "2":
                os.system("clear")
                print("========== LISTAR PRODUCTOS ==========")
                datos = db.read_rows_from_productos()
                print(datos)
                exit()
            case "3":
                os.system("clear")
                print("========== CATEGORÍAS ==========")
            case "4":
                os.system("clear")
                print("========== PROVEEDORES ==========")
            case "5":
                os.system("clear")
                print("Saliendo del sistema.....")
                exit()
            case _:
                os.system("clear")
                print("Opción incorrecta. Por favor intentelo de nuevo")


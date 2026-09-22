import db
import products
import proveedores
import categories
import os


def main():
    flag = True
    while flag:
        print("========== Inventario de Papelería ==========")
        print("Menú principal" 
        +"\n 1. Vender"
        +"\n 2. Productos"
        +"\n 3. Categorías"
        +"\n 4. Proveedores"
        +"\n 5. Salir del sistema")
        user_option = input("Elija una opción: ")
        match user_option:
            case "1":
                os.system("clear")
                print("========== Venta de productos ==========")
            case "2":
                os.system("clear")
                print("========== PRODUCTOS ==========")
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
if __name__== "__main__":   
    main()
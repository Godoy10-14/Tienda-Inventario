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
        +"\n 1. Vender Productos"
        +"\n 2. Productos"
        +"\n 3. Categorías"
        +"\n 4. Proveedores"
        +"\n 5. Salir del sistema")
        user_option = input("Elija una opción: ")
        match user_option:
            case "1":
                os.system("clear")
                print("========== Venta de productos ==========")
                exist_product = input("Ingrese el nombre del producto (Escribe SALIR si deseas cancelar): ")
                if exist_product == "SALIR":
                    exit()

                dato = db.exists_value_from_products(exist_product.title())
                if not dato:
                    print(f"No se encuentró en el inventario que contenga: {exist_product}")
                    # Si esto se cumple que vuelva a repetir el codigo
                    exit()
                
                option_producto = input("¿Cual es el producto que quieres seleccionar?: ")
                unidad = input("Cuantas unidades desea: ")
                print(db.modificar_unidades_from_productos(int(1),int(unidad)))
                
                print(db.actualizar_productos())
                exit()

            case "2":
                os.system("clear")
                products.menu_products()
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

if __name__== "__main__":   
    main()
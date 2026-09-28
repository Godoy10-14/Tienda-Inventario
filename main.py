import db
import products
import proveedores
import categories
import os

class FueraDelRango(Exception):
    pass
class NumerosNegativos(Exception):
    pass
class CantidadCero(Exception):
    pass
def iterar_productos(datos):
    print("=========================================")
    for index,dato in enumerate(datos, start=1):
        print(f"{index} | Nombre: {dato[1]} | Unidades: {dato[2]} | Precio: {dato[3]}")
    return "========================================="

def venta_productos():
    while True:
        try:
            print("========== Venta de productos ==========")
            exist_product = input("Escriba el nombre del producto (Escribe SALIR si deseas cancelar): ").strip()
            if not exist_product or exist_product.isdigit():
                raise ValueError

            if exist_product == "SALIR":
                os.system("clear")
                main()
            break
        except ValueError:
            os.system("clear")
            print("Error: Eso no es un opción válida")
            venta_productos()

    datos = db.exists_value_from_products(exist_product.title()) # Traer el resultado de la consulta
    if not datos:
        os.system("clear")
        print(f"No se encuentró en el inventario algún artículo que contenga: {exist_product}")
        return venta_productos()

    while True:
        try:
            print(iterar_productos(datos))
            option_producto = int(input("¿Cual es el producto que quieres seleccionar?: "))
            if option_producto < 1 or option_producto > len(datos) :
                raise FueraDelRango
            break
        except FueraDelRango:
            os.system("clear")
            print(f"Ese valor esta fuera del rango.")
        except ValueError:
            os.system("clear")
            print(f"Tienes que ingresar valores numéricos")
            
    fila_elegida = datos[option_producto-1]
    id_seleccionado = fila_elegida[0]
    product_selected = db.actualizar_productos(id_seleccionado)

    while True:
        try:
            print("=========================================")
            unidad = int(input("¿Cuantas unidades desea?: "))
            if unidad < 0:
                raise NumerosNegativos
            elif unidad > product_selected[0][2]:
                raise FueraDelRango
            elif unidad == 0:
                raise CantidadCero
            break
        except CantidadCero:
            os.system("clear")
            print("No puedes ingresear 0")
            print(iterar_productos(datos))
            print(f"Seleccionaste el producto N° {id_seleccionado}")
        except NumerosNegativos:
            os.system("clear")
            print("No puedes ingresas valores negativos")
            print(iterar_productos(datos))
            print(f"Seleccionaste el producto N° {id_seleccionado}")
        except FueraDelRango:
            os.system("clear")
            print("No hay suficiente cantidad la que deseas.")
            print(iterar_productos(datos))
            print(f"Seleccionaste el producto N° {id_seleccionado}")
        except ValueError:
            os.system("clear")
            print("Solo se permiten valores numéricos")
            print(iterar_productos(datos))
            print(f"Seleccionaste el producto N° {id_seleccionado}")
    while True:
        try:
            confirmation = input("¿Deseas confirmar esta venta? | SI | NO |: ")
            if confirmation == "NO":
                os.system("clear")
                main()
            elif confirmation.isdigit():
                raise ValueError
            elif confirmation == "SI":
                break
            else:
                raise FueraDelRango
        except FueraDelRango:
            os.system("clear")
            print("Solo puedes ingresar 2 respuestas válidas. SI o NO")
            print(iterar_productos(datos))
            print(f"Seleccionaste el producto N° {id_seleccionado}")
            print(f"Seleccionaste la cantidad {unidad}")
        except ValueError:
            os.system("clear")
            print("No puedes ingresar dígito numéricos")
            print(iterar_productos(datos))
            print(f"Seleccionaste el producto N° {id_seleccionado}")
            print(f"Seleccionaste la cantidad: {unidad}")
    os.system("clear")
    cantidad_seleccionada = product_selected[0][2] - unidad 
    datos = db.modificar_unidades_from_productos(int(id_seleccionado),int(cantidad_seleccionada))
    print(datos)
    
    product_selected = db.actualizar_productos(id_seleccionado)
    print("---------- TU REGISTRO ACTUALIZADO ----------")
    print(iterar_productos(product_selected))
    while True:
        print("¿Que deseas hacer?"
        +"\n1. Realizar otra venta"
        +"\n2. Volver al menú principal"
        +"\n3. Salir del sistema")
        user_option = input("Elija una opción: ")
        match user_option:
            case "1":
                os.system("clear")
                venta_productos()
            case "2":
                os.system("clear")
                main()
            case "3":
                os.system("clear")
                print("Saliendo del sistema.....")
                exit()
            case _:
                os.system("clear")
                print("Opción incorrecta. Por favor intentelo de nuevo")

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
                venta_productos()
            case "2":
                os.system("clear")
                products.menu_products()
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
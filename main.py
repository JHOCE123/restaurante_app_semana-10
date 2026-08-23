from servicios.restaurante import Restaurante
from servicios.archivo_servicio import ArchivoServicio
from modelos.producto import Producto

def mostrar_menu():
    print("\n--- SISTEMA RESTAURANTE_APP (SEMANA 10) ---")
    print("1. Listar productos")
    print("2. Registrar producto")
    print("3. Buscar producto")
    print("4. Actualizar producto")
    print("5. Eliminar producto")
    print("6. Salir")

def main():
    restaurante = Restaurante()
    archivo_servicio = ArchivoServicio()

    # Cargar productos al iniciar
    productos_cargados = archivo_servicio.cargar_productos()
    restaurante.establecer_productos(productos_cargados)
    print(f"Se cargaron {len(productos_cargados)} productos desde el archivo.")

    while True:
        mostrar_menu()
        opcion = input("Seleccione una opción: ").strip()

        if opcion == "1":
            productos = restaurante.listar_productos()
            if not productos:
                print("No hay productos registrados.")
            else:
                print("\n--- LISTA DE PRODUCTOS ---")
                for p in productos:
                    print(p)

        elif opcion == "2":
            print("\n--- REGISTRAR NUEVO PRODUCTO ---")
            id_prod = input("Ingrese ID del producto: ").strip()
            nombre = input("Ingrese nombre: ").strip()
            try:
                precio = float(input("Ingrese precio: "))
                stock = int(input("Ingrese stock: "))
                
                nuevo_prod = Producto(id_prod, nombre, precio, stock)
                if restaurante.registrar_producto(nuevo_prod):
                    archivo_servicio.guardar_productos(restaurante.listar_productos())
                    print("¡Producto registrado y guardado exitosamente!")
                else:
                    print("Error: Ya existe un producto con ese ID.")
            except ValueError as e:
                print(f"Error en los datos ingresados: {e}")

        elif opcion == "3":
            id_prod = input("Ingrese ID del producto a buscar: ").strip()
            p = restaurante.buscar_producto(id_prod)
            if p:
                print(f"\nProducto encontrado:\n{p}")
            else:
                print("Producto no encontrado.")

        elif opcion == "4":
            print("\n--- ACTUALIZAR PRODUCTO ---")
            id_prod = input("Ingrese ID del producto a actualizar: ").strip()
            p = restaurante.buscar_producto(id_prod)
            if p:
                try:
                    nuevo_precio = float(input("Ingrese nuevo precio: "))
                    nuevo_stock = int(input("Ingrese nuevo stock: "))
                    if restaurante.actualizar_producto(id_prod, nuevo_precio, nuevo_stock):
                        archivo_servicio.guardar_productos(restaurante.listar_productos())
                        print("¡Producto actualizado y guardado exitosamente!")
                except ValueError as e:
                    print(f"Error en los datos ingresados: {e}")
            else:
                print("Producto no encontrado.")

        elif opcion == "5":
            print("\n--- ELIMINAR PRODUCTO ---")
            id_prod = input("Ingrese ID del producto a eliminar: ").strip()
            if restaurante.eliminar_producto(id_prod):
                archivo_servicio.guardar_productos(restaurante.listar_productos())
                print("¡Producto eliminado y guardado actualizado exitosamente!")
            else:
                print("Producto no encontrado.")

        elif opcion == "6":
            print("Saliendo del sistema. ¡Hasta luego!")
            break
        else:
            print("Opción inválida. Intente nuevamente.")

if __name__ == "__main__":
    main()
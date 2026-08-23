import json
import os
from modelos.producto import Producto

class ArchivoServicio:
    def __init__(self, ruta_archivo: str = "datos/productos.json"):
        self.ruta_archivo = ruta_archivo

    def cargar_productos(self) -> list[Producto]:
        productos = []
        directorio = os.path.dirname(self.ruta_archivo)
        if directorio and not os.path.exists(directorio):
            os.makedirs(directorio, exist_ok=True)

        try:
            if not os.path.exists(self.ruta_archivo):
                return []

            with open(self.ruta_archivo, "r", encoding="utf-8") as archivo:
                datos = json.load(archivo)
                for item in datos:
                    try:
                        producto = Producto.de_diccionario(item)
                        productos.append(producto)
                    except (KeyError, ValueError) as e:
                        print(f"Advertencia: Registro omitido por datos incompletos o inválidos ({e}).")

        except FileNotFoundError:
            pass
        except json.JSONDecodeError:
            print("Error: El archivo productos.json tiene un formato JSON inválido.")
        except PermissionError:
            print("Error: Permisos insuficientes para leer el archivo.")

        return productos

    def guardar_productos(self, productos: list[Producto]) -> None:
        try:
            directorio = os.path.dirname(self.ruta_archivo)
            if directorio and not os.path.exists(directorio):
                os.makedirs(directorio, exist_ok=True)

            datos = [prod.a_diccionario() for prod in productos]
            with open(self.ruta_archivo, "w", encoding="utf-8") as archivo:
                json.dump(datos, archivo, indent=4, ensure_ascii=False)
        except PermissionError:
            print("Error: Permisos insuficientes para escribir en el archivo.")
        except Exception as e:
            print(f"Error inesperado al guardar: {e}")
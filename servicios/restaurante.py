from modelos.producto import Producto

class Restaurante:
    def __init__(self):
        self.productos: list[Producto] = []

    def establecer_productos(self, productos: list[Producto]):
        self.productos = productos

    def registrar_producto(self, producto: Producto) -> bool:
        for p in self.productos:
            if p.id_producto == producto.id_producto:
                return False
        self.productos.append(producto)
        return True

    def buscar_producto(self, id_producto: str) -> Producto | None:
        for p in self.productos:
            if p.id_producto == id_producto:
                return p
        return None

    def actualizar_producto(self, id_producto: str, nuevo_precio: float, nuevo_stock: int) -> bool:
        producto = self.buscar_producto(id_producto)
        if producto:
            producto.precio = nuevo_precio
            producto.stock = nuevo_stock
            return True
        return False

    def eliminar_producto(self, id_producto: str) -> bool:
        producto = self.buscar_producto(id_producto)
        if producto:
            self.productos.remove(producto)
            return True
        return False

    def listar_productos(self) -> list[Producto]:
        return self.productos
class Producto:
    def __init__(self, id_producto: str, nombre: str, precio: float, stock: int):
        self.id_producto = id_producto
        self.nombre = nombre
        self.precio = precio
        self.stock = stock

    @property
    def precio(self) -> float:
        return self._precio

    @precio.setter
    def precio(self, valor: float):
        if valor < 0:
            raise ValueError("El precio no puede ser negativo.")
        self._precio = float(valor)

    @property
    def stock(self) -> int:
        return self._stock

    @stock.setter
    def stock(self, valor: int):
        if valor < 0:
            raise ValueError("El stock no puede ser negativo.")
        self._stock = int(valor)

    def a_diccionario(self) -> dict:
        return {
            "id_producto": self.id_producto,
            "nombre": self.nombre,
            "precio": self.precio,
            "stock": self.stock
        }

    @classmethod
    def de_diccionario(cls, datos: dict) -> "Producto":
        return cls(
            id_producto=datos["id_producto"],
            nombre=datos["nombre"],
            precio=datos["precio"],
            stock=datos["stock"]
        )

    def __str__(self) -> str:
        return f"ID: {self.id_producto} | Nombre: {self.nombre} | Precio: ${self.precio:.2f} | Stock: {self.stock}"
class Usuario:
    def __init__(self, nombre: str, rol: str):
        self.nombre = nombre
        self.rol = rol

    def __str__(self) -> str:
        return f"Usuario: {self.nombre} ({self.rol})"
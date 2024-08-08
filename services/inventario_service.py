from repositories.Inventario_repository import InventarioRepository


class InventarioService:
    def __init__(self, repository: InventarioRepository):
        self.repository = repository

    def get_inventario(self, id):
        return self.repository.get_inventario(id)

    def guardar_inventario(self, id_producto, cantidad):
        return self.repository.guardar_inventario(id_producto, cantidad)
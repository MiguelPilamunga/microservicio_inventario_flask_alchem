from abc import ABC, abstractmethod

class InventarioRepository(ABC):
    @abstractmethod
    def get_inventario(self, id):
        pass

    @abstractmethod
    def guardar_inventario(self, id_producto, cantidad):
        pass

from services.inventario_service import InventarioService
from repositories.mysql_inventario_repository import MySQLInventarioRepository

class ServiceFactory:
    @staticmethod
    def crear_inventario_service() -> InventarioService:
        repository = MySQLInventarioRepository()
        return InventarioService(repository)
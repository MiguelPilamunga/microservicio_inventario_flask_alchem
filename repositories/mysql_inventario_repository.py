from init import db
from models.inventario import Inventario
from repositories.Inventario_repository import InventarioRepository


class MySQLInventarioRepository(InventarioRepository):
    def __init__(self):
        self.db = db

    def get_inventario(self, id) -> Inventario:
        return Inventario.query.filter_by(id_producto=id).first()

    def guardar_inventario(self, id_producto, cantidad) -> Inventario:
        inventario = Inventario.query.filter_by(id_producto=id_producto).first()
        if inventario:
            inventario.cantidad = cantidad
        else:
            inventario = Inventario(id_producto=id_producto, cantidad=cantidad)
        db.session.add(inventario)
        db.session.commit()
        return inventario
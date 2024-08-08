from init import db
class Inventario(db.Model):
    __tablename__ = 'inventario'
    id = db.Column(db.Integer, primary_key=True)
    id_producto = db.Column(db.String(50), unique=True, nullable=False)
    cantidad = db.Column(db.Integer, nullable=False)

    def __init__(self , id_producto, cantidad):
        self.id_producto = id_producto
        self.cantidad = cantidad

    def to_dict(self):
        return {
            'id': self.id,
            'id_producto': self.id_producto,
            'cantidad': self.cantidad
        }
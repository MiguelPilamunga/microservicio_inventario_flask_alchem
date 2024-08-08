from flask import Blueprint, jsonify, request
from factories.ServiceFactory import ServiceFactory

inventario_bp = Blueprint('inventario', __name__)
inventario_service = ServiceFactory.crear_inventario_service()

@inventario_bp.route('/<string:id>', methods=['GET'])
def get_inventario(id):
    inventario = inventario_service.get_inventario(id)
    if inventario:
        return jsonify(inventario.to_dict()), 200
    return jsonify({"message": "Inventario no encontrado"}), 404

@inventario_bp.route('/guardar', methods=['POST'])
def guardar_inventario():
    data = request.json
    inventario = inventario_service.guardar_inventario(data['id_producto'], data['cantidad'])
    return jsonify(inventario.to_dict()), 201
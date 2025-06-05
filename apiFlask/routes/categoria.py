from flask import Blueprint, request, jsonify
from database import execute_query

categoria_bp = Blueprint('categoria', __name__)

@categoria_bp.route('/categorias', methods=['GET'])
def get_categorias():
    query = "SELECT * FROM categoria"
    categorias = execute_query(query, fetch=True)
    return jsonify(categorias)


@categoria_bp.route('/categorias', methods=['POST'])
def criar_categoria():
    data = request.json
    query = "INSERT INTO categoria (nome) VALUES (%s) RETURNING id"
    result = execute_query(query, (data['nome'],), fetch=True)
    return jsonify({"id": result[0]['id'], "nome": data['nome']}), 201


@categoria_bp.route('/categorias/<int:id>', methods=['PUT'])
def atualizar_categoria(id):
    data = request.json
    query = """
        UPDATE categoria
        SET nome = %s
        WHERE id = %s
    """
    execute_query(query, (
        data['nome'],
        id
    ))
    return jsonify({"message": "Categoria atualizada com sucesso"})


@categoria_bp.route('/categorias/<int:id>', methods=['DELETE'])
def deletar_categoria(id):
    query = "DELETE FROM categoria WHERE id = %s"
    execute_query(query, (id,))
    return jsonify({"message": "Categoria deletada com sucesso"})
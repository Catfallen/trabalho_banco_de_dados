from flask import Blueprint, request, jsonify
from database import execute_query

usuario_bp = Blueprint('usuario', __name__)

@usuario_bp.route('/usuarios', methods=['GET'])
def get_usuarios():
    query = "SELECT * FROM usuario"
    usuarios = execute_query(query, fetch=True)
    return jsonify(usuarios)


@usuario_bp.route('/usuarios', methods=['POST'])
def criar_usuario():
    data = request.json
    query = """
        INSERT INTO usuario (nome, tipo)
        VALUES (%s, %s) RETURNING id
    """
    result = execute_query(query, (
        data['nome'],
        data['tipo']
    ), fetch=True)
    return jsonify({"id": result[0]['id']}), 201


@usuario_bp.route('/usuarios/<int:id>', methods=['PUT'])
def atualizar_usuario(id):
    data = request.json
    query = """
        UPDATE usuario
        SET nome = %s,
            tipo = %s
        WHERE id = %s
    """
    execute_query(query, (
        data['nome'],
        data['tipo'],
        id
    ))
    return jsonify({"message": "Usuário atualizado com sucesso"})


@usuario_bp.route('/usuarios/<int:id>', methods=['DELETE'])
def deletar_usuario(id):
    query = "DELETE FROM usuario WHERE id = %s"
    execute_query(query, (id,))
    return jsonify({"message": "Usuário deletado com sucesso"})
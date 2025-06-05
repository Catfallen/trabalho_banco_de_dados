from flask import Blueprint, request, jsonify
from database import execute_query

livro_bp = Blueprint('livro', __name__)

@livro_bp.route('/livros', methods=['GET'])
def get_livros():
    query = "SELECT * FROM livro"
    livros = execute_query(query, fetch=True)
    return jsonify(livros)


@livro_bp.route('/livros', methods=['POST'])
def criar_livro():
    data = request.json
    query = """
        INSERT INTO livro (titulo, autor, ano, categoria_id)
        VALUES (%s, %s, %s, %s) RETURNING id
    """
    result = execute_query(query, (
        data['titulo'],
        data.get('autor'),
        data.get('ano'),
        data.get('categoria_id')
    ), fetch=True)
    return jsonify({"id": result[0]['id']}), 201


@livro_bp.route('/livros/<int:id>', methods=['PUT'])
def atualizar_livro(id):
    data = request.json
    query = """
        UPDATE livro
        SET titulo = %s,
            autor = %s,
            ano = %s,
            categoria_id = %s
        WHERE id = %s
    """
    execute_query(query, (
        data['titulo'],
        data.get('autor'),
        data.get('ano'),
        data.get('categoria_id'),
        id
    ))
    return jsonify({"message": "Livro atualizado com sucesso"})


@livro_bp.route('/livros/<int:id>', methods=['DELETE'])
def deletar_livro(id):
    query = "DELETE FROM livro WHERE id = %s"
    execute_query(query, (id,))
    return jsonify({"message": "Livro deletado com sucesso"})
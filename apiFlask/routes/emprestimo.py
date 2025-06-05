from flask import Blueprint, request, jsonify
from database import execute_query

emprestimo_bp = Blueprint('emprestimo', __name__)

@emprestimo_bp.route('/emprestimos', methods=['GET'])
def get_emprestimos():
    query = "SELECT * FROM emprestimo"
    emprestimos = execute_query(query, fetch=True)
    return jsonify(emprestimos)


@emprestimo_bp.route('/emprestimos', methods=['POST'])
def criar_emprestimo():
    data = request.json
    query = """
        INSERT INTO emprestimo (livro_id, usuario_id, data_emprestimo, data_devolucao)
        VALUES (%s, %s, %s, %s) RETURNING id
    """
    result = execute_query(query, (
        data['livro_id'],
        data['usuario_id'],
        data.get('data_emprestimo'),
        data.get('data_devolucao')
    ), fetch=True)
    return jsonify({"id": result[0]['id']}), 201


@emprestimo_bp.route('/emprestimos/<int:id>', methods=['PUT'])
def atualizar_emprestimo(id):
    data = request.json
    query = """
        UPDATE emprestimo
        SET livro_id = %s,
            usuario_id = %s,
            data_emprestimo = %s,
            data_devolucao = %s
        WHERE id = %s
    """
    execute_query(query, (
        data['livro_id'],
        data['usuario_id'],
        data.get('data_emprestimo'),
        data.get('data_devolucao'),
        id
    ))
    return jsonify({"message": "Empréstimo atualizado com sucesso"})


@emprestimo_bp.route('/emprestimos/<int:id>', methods=['DELETE'])
def deletar_emprestimo(id):
    query = "DELETE FROM emprestimo WHERE id = %s"
    execute_query(query, (id,))
    return jsonify({"message": "Empréstimo deletado com sucesso"})
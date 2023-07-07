from flask import Flask, jsonify, request

app = Flask(__name__)

# Exemplo de uma rota para retornar informações de um usuário específico
@app.route('/api/usuario/<int:user_id>', methods=['GET'])
def get_usuario(user_id):
    # Lógica para obter informações do usuário com o ID fornecido
    usuario = obter_usuario_por_id(user_id)

    # Retorna os dados do usuário em formato JSON
    if usuario:
        return jsonify(usuario)
    else:
        return jsonify({'mensagem': 'Usuário não encontrado'}), 404

# Exemplo de uma rota para criar um novo usuário
@app.route('/api/usuario', methods=['POST'])
def criar_usuario():
    # Obtém os dados enviados na requisição
    dados = request.get_json()

    # Lógica para criar um novo usuário com os dados fornecidos
    novo_usuario = criar_novo_usuario(dados)

    # Retorna os dados do novo usuário em formato JSON
    return jsonify(novo_usuario), 201

if __name__ == '__main__':
    app.run()

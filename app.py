# 1. Importar as classes necessárias do Flask
from flask import Flask, jsonify

# 2. Inicializar a aplicação Flask
app = Flask(__name__)

# 3. Criar uma rota de teste usando um "decorator"
@app.route('/api', methods=['GET'])
def hello_world():
    # A função jsonify cria uma resposta JSON, similar ao res.json() do Express
    return jsonify({'message': 'Olá! Bem-vindo à API de Livro de Receitas com Flask!'})

# 4. Bloco para executar o servidor de desenvolvimento
# Esta verificação garante que o servidor só roda quando o script é executado diretamente
if __name__ == '__main__':
    # app.run() inicia o servidor. O modo debug reinicia-o a cada alteração.
    app.run(debug=True, port=5000)
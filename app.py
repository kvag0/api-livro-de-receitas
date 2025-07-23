import os
from flask import Flask, jsonify, request 
from flask_sqlalchemy import SQLAlchemy
from dotenv import load_dotenv

# Carrega as variáveis de ambiente do ficheiro .env
load_dotenv()

app = Flask(__name__)

# Configurações da aplicação
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URL')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Inicializa o SQLAlchemy com a nossa aplicação Flask
db = SQLAlchemy(app)

# Definição do Modelo de Dados para Receita (Recipe)
class Recipe(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    instructions = db.Column(db.Text, nullable=False)
    # Esta é a 'relação' virtual. Permite-nos aceder aos ingredientes de uma receita facilmente.
    # O cascade="all, delete-orphan" significa que, se apagarmos uma receita, os seus ingredientes também serão apagados.
    ingredients = db.relationship('Ingredient', backref='recipe', lazy=True, cascade="all, delete-orphan")

    def to_json(self):
        return {
            'id': self.id,
            'name': self.name,
            'instructions': self.instructions,
            'ingredients': [ingredient.to_json() for ingredient in self.ingredients]
        }

# Definição do Modelo de Dados para Ingrediente (Ingredient)
class Ingredient(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    # Esta é a 'chave estrangeira'. É a coluna que liga um ingrediente à sua receita.
    recipe_id = db.Column(db.Integer, db.ForeignKey('recipe.id'), nullable=False)

    def to_json(self):
        return {
            'id': self.id,
            'name': self.name
        }

# Criar uma rota de teste usando um "decorator"
@app.route('/api/recipes', methods=['POST'])
def create_recipe():
    try:
        # Pega os dados JSON enviados no corpo do pedido
        data = request.get_json()

        # Extrai os dados da receita
        new_recipe = Recipe(
            name=data['name'],
            instructions=data['instructions']
        )

        # Extrai os dados dos ingredientes e os associa à nova receita
        if 'ingredients' in data:
            for ingredient_data in data['ingredients']:
                new_ingredient = Ingredient(
                    name=ingredient_data['name'],
                    recipe=new_recipe  # A 'magia' do SQLAlchemy para associar
                )
                db.session.add(new_ingredient)

        # Adiciona a nova receita à sessão do banco de dados
        db.session.add(new_recipe)
        # Confirma (commit) a transação, salvando tudo no banco de dados
        db.session.commit()

        # Retorna a receita criada como JSON com o status 201 (Created)
        return jsonify(new_recipe.to_json()), 201

    except Exception as e:
        # Em caso de erro, desfaz a transação e retorna uma mensagem de erro
        db.session.rollback()
        return jsonify({'message': 'Erro ao criar receita', 'error': str(e)}), 500


    # Rota para LISTAR todas as receitas
    @app.route('/api/recipes', methods=['GET'])
    def get_recipes():
        try:
            # Busca todas as receitas no banco de dados
            recipes = Recipe.query.all()
            # Converte cada objeto receita para JSON usando o nosso método to_json()
            # e retorna a lista
            return jsonify([recipe.to_json() for recipe in recipes]), 200
        except Exception as e:
            return jsonify({'message': 'Erro ao buscar receitas', 'error': str(e)}), 500

# Bloco para executar o servidor de desenvolvimento
# Esta verificação garante que o servidor só roda quando o script é executado diretamente
if __name__ == '__main__':
    # app.run() inicia o servidor. O modo debug reinicia-o a cada alteração.
    app.run(debug=True, port=5000)
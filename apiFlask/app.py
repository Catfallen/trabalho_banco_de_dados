from flask import Flask
from routes.categoria import categoria_bp
from routes.livro import livro_bp
from routes.usuario import usuario_bp
from routes.emprestimo import emprestimo_bp

app = Flask(__name__)

# Registrar os blueprints
app.register_blueprint(categoria_bp)
app.register_blueprint(livro_bp)
app.register_blueprint(usuario_bp)
app.register_blueprint(emprestimo_bp)

# Rota inicial opcional
@app.route('/')
def index():
    return 'API de Biblioteca funcionando! ✅'

if __name__ == '__main__':
    app.run(debug=True)

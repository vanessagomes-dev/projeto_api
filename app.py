# app.py
from flask import Flask
from routes.users import users_bp

app = Flask(__name__)

# Registrar o Blueprint de usuários
app.register_blueprint(users_bp)

# Endpoint inicial
@app.route('/')
def minha_primeira_api():
    return 'Minha primeira Api!'

if __name__ == '__main__':
    app.run(debug=True)

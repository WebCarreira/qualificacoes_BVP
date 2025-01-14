from flask import Flask, request, render_template, redirect, url_for, session
from flask_bcrypt import Bcrypt
import mysql.connector

app = Flask(__name__)
app.secret_key = 'sua_chave_secreta_aqui'
bcrypt = Bcrypt(app)

# Configuração do banco de dados
db_config = {
    'host': 'localhost',
    'user': 'root',
    'password': '',
    'database': 'sistema_login'
}

# Página inicial com o formulário de login
@app.route('/', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        # Conectar ao banco de dados
        conn = mysql.connector.connect(**db_config)
        cursor = conn.cursor(dictionary=True)

        # Verificar usuário no banco de dados
        cursor.execute("SELECT * FROM usuarios WHERE username = %s", (username,))
        user = cursor.fetchone()

        cursor.close()
        conn.close()

        if user and bcrypt.check_password_hash(user['password'], password):
            session['user'] = username
            return redirect(url_for('dashboard'))
        else:
            return "Nome de usuário ou senha inválidos."

    return render_template('login.html')

# Página protegida para usuários autenticados
@app.route('/dashboard')
def dashboard():
    if 'user' in session:
        return f"Bem-vindo, {session['user']}!"
    return redirect(url_for('login'))

# Rota para logout
@app.route('/logout')
def logout():
    session.pop('user', None)
    return redirect(url_for('login'))

if __name__ == '__main__':
    app.run(debug=True)

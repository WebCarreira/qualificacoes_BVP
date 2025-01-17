from flask import Flask, render_template, request, redirect, url_for, flash
import mysql.connector

app = Flask(__name__)
app.secret_key = 'sua_chave_secreta_aqui'  # Para mensagens flash

# Conexão ao banco de dados
db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Dbc10060190!",
    database="sistema_login"
)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/login', methods=['POST'])
def login():
    username = request.form['username']
    password = request.form['password']

    # Consulta para verificar credenciais
    cursor = db.cursor()
    cursor.execute("SELECT * FROM usuarios WHERE username = %s AND password = %s", (username, password))
    user = cursor.fetchone()

    if user:
        # Login bem-sucedido: redirecionar para a página inicial
        return redirect(url_for('/pagina_inicial'))
    else:
        # Falha no login: exibir mensagem e voltar ao login
        flash('Usuário ou senha inválidos. Tente novamente.')
        return redirect(url_for('home'))

@app.route('/pagina_inicial')
def dashboard():
    return render_template('página_inicial.html')  # Página protegida pós-login

if __name__ == '__main__':
    app.run(debug=True)

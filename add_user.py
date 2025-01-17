import mysql.connector
from flask_bcrypt import Bcrypt

bcrypt = Bcrypt()

db_config = {
    'host': 'localhost',
    'user': 'root',
    'password': 'Dbc10060190!',
    'database': 'sistema_login'
}

username = "admin"
password = "123456"
hashed_password = bcrypt.generate_password_hash(password).decode('utf-8')

conn = mysql.connector.connect(**db_config)
cursor = conn.cursor()

cursor.execute("INSERT INTO usuarios (username, password) VALUES (%s, %s)", (username, hashed_password))
conn.commit()

cursor.close()
conn.close()

print("Usuário criado com sucesso!")

# Front End - é o que você vê
    #HTML, CSS, JavaScript

# Back End - a lógica de funcionamento por trás do site
    # Python

# Framework - Flask - criar o site

# Ambiente virtual - local no seu computador com instalações do projeto

# pip install python-socketio flask-socketio simple-websocket

# Passo 1: Importar o Flask
from flask import Flask, render_template 
from flask_socketio import SocketIO, send

# Passo 2: Criar o seu app
app = Flask(__name__)
socketio = SocketIO(app, cors_allowed_origins="*")

# funcionalidade de enviar mensagem
@socketio.on("message")
def gerenciar_mensagem(mensagem):
    send(mensagem, broadcast=True)


# primeira rota
@app.route("/")
def homepage():
    return render_template("homepage.html")

# rodar o nosso aplicativo
socketio.run(app, host="192.168.0.3")

# Criar o HTML - homepage.html
# websocket - importar o socket e jquery - Biblioteca https://cdnjs.com/libraries
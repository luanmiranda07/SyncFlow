from flask import Flask, render_template, request,redirect,session,flash,url_for

app = Flask(__name__, template_folder="templates", static_folder="static")
app.secret_key = 'syncflow'

class Usuario:
    def __init__(self, nome, nickname, senha):
        self.nome = nome
        self.nickname = nickname
        self.senha = senha


usuario1=Usuario('Luan Miranda', 'luanmiranda', 'dddluan')
usuario2=Usuario('camila ferreira', 'cah', 'ddd')
usuario3=Usuario('guilherme', 'gui', 'dddluan123')

usuarios = {
    usuario1.nickname: usuario1,
    usuario2.nickname: usuario2,
    usuario3.nickname: usuario3
}

@app.route('/')
def index():
    return render_template('home.html')


@app.route('/login')
def login():
    return render_template('login.html')


@app.route('/autenticar', methods=['POST'])
def autenticar():
    if request.form['login'] in usuarios :
        if request.form['senha'] == usuarios[request.form['login']].senha:
            session['usuario'] = usuarios[request.form['login']].nickname
            flash('Login realizado com sucesso!')
            return redirect(url_for('index'))
    
    else:
        flash('Senha incorreta!')
        return redirect(url_for('login'))
if __name__ == "__main__":
    app.run(debug=True)



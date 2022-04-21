from flask import Flask, render_template

app = Flask(__name__)

# criar a 1° pagina do site
# route -> JogosFavoritos.com/contas
# função -> oque voce quer exibir naquela página

@app.route("/")
def homepage():
    return render_template("homepage.html")

@app.route("/contas")
def contas():
    return render_template("contas.html")

@app.route("/usuarios/<nome_usuario>")
def usuarios(nome_usuario):
    return render_template("usuarios.html", nome_usuario=nome_usuario)

#coloca o site no ar
if __name__ == "__main__":
    app.run(debug=True)
    
    
    # servidor do heroku

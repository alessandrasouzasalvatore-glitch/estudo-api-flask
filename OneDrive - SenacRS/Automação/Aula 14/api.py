from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/sobre")
def sobre():
    return render_template("sobre.html")

@app.route("/api")
def api():
    return render_template("api.html")

@app.route("/flask")
def flask():
    return render_template("flask.html")

@app.route("/tecnologias")
def tecnologias():
    return render_template("tecnologias.html")

@app.route("/contato")
def contato():
    return render_template("contato.html")

if __name__ == "__main__":
    app.run(port=5000, debug=True)
from flask import Flask

app = Flask("Kubda")

@app.route("/", methods=["GET", "POST"])
def cadastro():
    return("ON")

from flask import Flask, jsonify, request

app = Flask(__name__)
@app.route("/", methods=("GET",))
def index():
    return jsonify({"status": 200, "message": "API da Loise"})

@app.route("/aleatorios")#decorator de rota
def aleatorios(): #função
    import random
    a = random.randint(49,100)
    return jsonify({"status": 200, "data": a })#retorno

@app.route("/argumentos/<string:nome>")
def argumentos(nome: str):
    return jsonify({"status":200, "data": nome})

@app.route("/argumentos")
def arg_implicito():
    return jsonify({"status": 200, "data": request.args["nome"]})

if __name__ == '__main__':
    app.run(debug=True)

@app.route("/idades", methods=("GET",))
def idades():
    from random_data import pessoas 
    import funcoes
    num = funcoes.maior_de_50(pessoas)
    return jsonify({"status":200, "data": num})

@app.route("/salarios", methods=("GET",))
def salarios():
    from random_data import pessoas
    import funcoes
    num = funcoes.mais_2000(pessoas)
    return jsonify({"status": 200, "data": num})

if __name__ == '_main_':
    app.run(debug=True)
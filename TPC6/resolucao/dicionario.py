from flask import Flask, render_template, request, url_for
import json
import string


app = Flask(__name__)
file = open("docs_auxiliares\\conceitotrad.json", "r", encoding="utf-8")
conceitos=json.load(file)
minusculas = [conceito.lower() for conceito in conceitos] #conceitos convertidos em minúsculas para comparação


@app.route('/')
def home():
    return render_template("home.html")

#filtragem por alfabeto:
#recebe lista do alfabeto em maiúsculas para definição de respetivos botões
#coloca numa lista apenas os primeiros termos que começam com uma determinada letra para referência posterior
@app.route('/conceitos')
def listar_Conceitos():
    alfabeto = list(string.ascii_uppercase)
    primeiros_termos = []
    for letra in alfabeto:
        for conceito  in conceitos:
            if conceito.lower().startswith(letra.lower()):
                primeiros_termos.append(conceito.lower())
                break  # Sai do loop após encontrar o primeiro termo
    return render_template("conceitos.html", conceitos = conceitos, alfabeto = alfabeto, primeiros_termos = primeiros_termos)

#filtragem por palavra:
#recebe o que o utilizador escreveu na barra de pesquisa
#com base nisso, filtra os conceitos que contêm a palavra escrita
@app.route('/conceitos', methods=["POST"])
def pesquisar_Conceito():
    termo = request.form.get("search", "")
    resultados = []
    if termo in minusculas: #averigua se é um conceito: se não for retorna template de erro
        resultados = [conceito for conceito in conceitos if termo.lower() in conceito.lower()]
        return render_template("conceitos.html", resultados= resultados, conceitos = conceitos)
    else:
        return render_template("nao_encontrado.html", termo = termo)

#consulta de descrição e tradução do termo
@app.route('/conceitos/<designacao>')
def consultar_Dados(designacao):
    return render_template("dados.html", termo = designacao, desc = conceitos[designacao]["desc"], en = conceitos[designacao]["en"])


app.run(host="localhost", port=4002, debug=True)
from flask import Flask, render_template, request, url_for
import json
import string
import re

app = Flask(__name__)
file = open("docs_auxiliares\\conceitotrad.json", "r", encoding="utf-8")
conceitos=json.load(file)

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
#com base nisso, filtra os conceitos que contêm a palavra, quer na designação, quer na descrição
@app.route('/conceitos/pesquisar', methods=["POST"])
def pesquisar_Conceito():
    resultados = []
    termo = request.form.get("search")
    for conceito in conceitos:
        if termo.lower() in conceitos[conceito]["desc"].lower():
            resultados.append(conceito)
        elif termo.lower() in conceito.lower():
            resultados.append(conceito)
    if len(resultados)!=0:
        return render_template("pesquisa.html", resultados = resultados, conceitos = conceitos, termo=termo)

    else:
        return render_template("nao_encontrado.html", termo = termo)

#sublinhar o termo, pesquisado pelo utilizador, a fluorescente
def highlight(text, term):
    return re.sub(re.escape(term), f"<mark>{term}</mark>", text, flags=re.IGNORECASE)

app.template_filter('highlight')(highlight)

#consulta de descrição e tradução do termo
@app.route('/conceitos/<designacao>')
def consultar_Dados(designacao):
    return render_template("dados.html", termo = designacao, desc = conceitos[designacao]["desc"], en = conceitos[designacao]["en"])

#adição de novo conceito
@app.route('/conceitos/adicionar', methods=["POST"])
def adicionar_conceitos():
    en = request.form.get("en")
    designacao = request.form.get("designacao")
    descricao = request.form.get("descricao")
    file_out = open("docs_auxiliares\\conceitotrad.json", "w", encoding="UTF-8")
    conceitos[designacao]={"desc": descricao, "en": en}
    json.dump(conceitos, file_out, indent=4, ensure_ascii=False)
    file_out.close()

    return render_template("conceitos.html", conceitos = conceitos)
 
#eliminação de um conceito
@app.route('/conceitos/<designacao>', methods=["DELETE"])
def delete_conceito(designacao):
    file_out = open("docs_auxiliares\\conceitotrad.json", "w", encoding="UTF-8")
    del conceitos[designacao]
    json.dump(conceitos, file_out, indent=4, ensure_ascii=False)
    file_out.close()
    return render_template("conceitos.html", conceitos = conceitos)

#DataTable
@app.route('/table')
def table():
    return render_template("table.html", conceitos = conceitos)

app.run(host="localhost", port=4002, debug=True)
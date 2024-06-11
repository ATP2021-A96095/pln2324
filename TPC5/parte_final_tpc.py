import json
import re

file_conceitos = open("Docs_Auxiliares\\dicionario.json", encoding="utf-8")
file_livro = open("Docs_Auxiliares\\LIVRO.txt", encoding="utf-8")

texto = file_livro.read()
conceitos = json.load(file_conceitos)

blacklist =["de", "e", "para", "pelo", "os", "são", "este", "índice", "secção"]
conceitos_min = {chave.lower():conceitos[chave] for chave in conceitos} 


texto = re.sub(r"\n", "<br>", texto)

#tratamento do ficheiro de termos traduzidos
#criação do dicionário dic_trad {"termo": "tradução"}
t = open("Docs_Auxiliares\\termos_traduzidos.txt", "r", encoding="utf-8")
texto_traduzido = t.read()
texto_traduzido = texto_traduzido.lower()
termo_traducao = re.findall(r"(.+)\s@\s(.+)", texto_traduzido)
dic_trad = dict(termo_traducao)

#criação do dicionário de dicionários, dic_final
dic_final={}

for conceito in conceitos_min:
    if conceito in dic_trad:
        dic_final[conceito]={
                                   "descricao": conceitos_min[conceito],
                                   "en": dic_trad[conceito]
                                }
    else:
        dic_final[conceito]={
                                   "descricao": conceitos_min[conceito],
                                   "en": "Sem tradução."
                                }

   
#geração das etiquetas
def etiquetador(m):
    palavra = m[0]
    p_original = palavra
    palavra = palavra.lower()
    if palavra in dic_final and palavra not in blacklist:
        dic_interno = dic_final[palavra]
        descricao = dic_interno["descricao"]
        traducao = dic_interno["en"]
        etiqueta = f"<a href= '' title = 'Descrição: {descricao}\nTradução: {traducao}'>{p_original}</a>"
        return etiqueta
    else:
        return p_original

expressao = r"[\wçáéâãêúôóí]+"  
texto = re.sub(expressao, etiquetador, texto, flags = re.IGNORECASE)

texto = re.sub(r"\f", "<hr/>", texto)

file_out = open("livro.html", "w", encoding="utf-8")
print(texto, file = file_out)


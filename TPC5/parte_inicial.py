import re
import json

f = open("Docs_Auxiliares\\dicionario_medico.xml", "r", encoding="utf-8")
texto = f.read()

texto = re.sub(r"<text.+?>", r"", texto)
texto = re.sub(r"</text>", r"", texto)
#junção das duas de cima
#texto = re.sub(r"</?text.*?>", r"", texto)

texto = re.sub(r"</?page.*?>", r"", texto)
texto = re.sub(r"\n", r"", texto)


termos = re.findall(r"<b>(.+)</b>", texto) #de bold a bold é conceito
termo_designacao = re.findall(r"<b>(.+?)</b>([^<]+)", texto)

conceitos = dict(termo_designacao)

dic = open("Docs_Auxiliares\\dicionario.json", "w", encoding="utf-8")
json.dump(conceitos, dic, indent=4, ensure_ascii=False)
dic.close()


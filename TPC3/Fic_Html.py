import re
fic = open("dicionario_medico.txt", "r", encoding = "utf-8")
texto = fic.read() #ler o ficheiro


texto = re.sub(r"(\.)\n\n\f([A-RT-Z].+)", r"\1 \2", texto) #descrições quebradas a meio, iniciadas com letra maiúscula, como em quimiotaxia

texto = re.sub(r"([^\.])\n\n\f([a-z0-9].+[\.,]+.+)", r"\1 \2", texto) #descrições quebradas a meio, iniciadas com letra minúscula, como em análise didática
texto = re.sub(r"([^\.])\n\n\f([a-zJ\sâãáàéêóôõúç,;í-]+[\.])", r"\1 \2", texto) #descrições interrompidas com caracteres acentuados
texto = re.sub(r"([^\.])\n\n\f([a-z\sâãáàéêóôõçú;í]+(;.+))", r"\1 \2", texto) #caso semelhante ao de cima mas em que não existe ponto final a terminar a descrição


texto = re.sub(r"\n\n\f([A-RT-Z].+)", r"\n\1", texto) #fazer com que a primeira letra da descrição não seja descartada


#casos particulares

texto = re.sub(r"(\.)\n\n(.+)(feixes)", r"\1 \2 \3", texto) #lidar linhas vazias, na descrição, em termos como sulco
texto = re.sub(r"(ficações terminais dos brônquios, apresentando cal)", r"\1\nSem descrição.\n\n", texto) #tornar ficiforme como termo ao introduzir descrição em ficações...
texto = re.sub(r"(\.)\n\n\f(hallux.+)", r"\1 \2", texto) #fazer com que hallux não seja termo mas sim parte de descrição


texto = re.sub(r"\n\n(.+)", r"\n\n@\1", texto) #colocar @ nos termos
texto = re.sub(r"@(.+)\n\n@", r"@\1\n", texto) #resolver problema de duplo @

texto = re.sub(r"\f", r"", texto) #remoção de restantes form feeds
termo_designacao = re.findall(r"@(.+)\n([^@]+)", texto) #tuplos de termo e designação


#Gerar HTML
imagem_e_titulo = """
<div class='image-and-text'>
    <img src='C:\\Users\\Ana Sousa\\Documents\\GitHub\\pln2324\\TPC3\\i.jpg' alt='Descrição da imagem' style='float: left; width: 450; height: 250; margin-right: 20px;'>
    <div>
        <h1 style='font-size: 46px; text-align: center; font-family: Times New Roman, sans-serif;'><i>Dicionário de Termos Médicos</i></h1>
        <p style='font-size: 20px; text-align: center; font-family: Times New Roman, sans-serif;'>Este dicionário pretende facilitar a consulta para as demais <b>terminologias médicas</b>, estando 
        orientado para um vasto público, desde estudantes, e profissionais, da área, como também pessoas pouco familiarizadas 
        com as noções técnicas.</p>
    </div>
    <div style='clear: both;'></div>
</div>
"""

lista_alfabeto = "<ul style='list-style-type: none; display: inline; text-align: center; background-color: #E6E6FA; padding: 15px; width: 100%; margin: 0;'>"

# Adicionando cada letra do alfabeto como um item de lista
for letra in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ':
    lista_alfabeto += f"<li style='display: inline-block; background-color: #E6E6FA; padding: 12.685px;'>{letra}</li>"
    if letra != "Z":
        lista_alfabeto += " | "
lista_alfabeto += "</ul>"


body = "<body"
for termo in termo_designacao:
    body += "<p> </p>"
    body += f"<h5 style='font-size: 18px; font-family: Times New Roman, sans-serif;'> {termo[0]} </h5>"
    body += f"<p style='font-size: 16px; font-family: Times New Roman, sans-serif;'> {termo[1]} </p>"
    body += "<hr/>"

body += "</body>"
html = imagem_e_titulo + lista_alfabeto + body


file_out = open("aula3.html", "w")
file_out.write(html)
file_out.close()
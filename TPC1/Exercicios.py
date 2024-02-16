#Exercícios de criação de funções

#1 Função que reverte uma string a partir de lista em compreensão
def reverte_c(s):
    return "".join([x for x in list(s[::-1])])

#Versão "normal"
def reverte(s):
    return s[::-1]
#print(reverte("Ana Sousa"))

#2 Função que conta o número de "a" e de "A" de uma string
def contaA(s):
    contaa = 0
    contaA = 0
    for letra in s:
        if "a" == letra:
            contaa += 1
        elif "A" == letra:
            contaA += 1
    print("A string tem {} a's minúsculos".format(contaa))
    print("A string tem {} A's maiúsculos".format(contaA))
#contaA("OlaaA, como estaAAAas")

#Função que conta o número de "a" e de "A" de uma string usando lista em compreensão
def contaA_c(s):
    print("Número de a's minúsculos: {} ".format(len([a for a in s if a == "a"])))
    print("Número de A's maiúsculos: {} ".format(len([aa for aa in s if aa == "A"])))
#contaA_c("OlaaA")

#3 Função que conta o número de vogais de uma string
def vogais(s):
    vogais = ["a", "e", "i", "o", "u"]
    c = 0
    for letra in s.lower():
        if letra in vogais:
            c = c+1
    print("A string tem {} vogais".format(c))

#Função que conta o número de vogais de uma string usando lista em compreensão
def vogais_c(s):
    vogais = ["a", "e", "i", "o", "u"]
    return len([letra for letra in s.lower() if letra in vogais])
#print(vogais_c("Ola mundo"))

#4 Função que converte uma string em minúsculas
def lower(s):
    return s.lower()

#5 Função que converte uma string em maiúsculas
def upper(s):
    return s.upper()

#6 Função que verifica se uma string é capicua
def capicua(s):
    return s == s[::-1]
#print(capicua("13231"))

#7 Função que verifica se duas strings estão balanceadas
def balanceado(s1, s2):
    b = True
    for letra in s1:
        if letra not in s2:
            b = False
    return b
#print(balanceado("ola", "mundo"))

#8 Função que retorna o número de ocorrências de uma string noutra
def ocorrencias(s1, s2):
    return s2.count(s1)
#print(ocorrencias("ola", "ola ola mundo ola"))

#Função que retorna o número de ocorrências de uma string noutra
#sem o uso da função count
def ocorrencias_v2(s1, s2):
    b = 0
    for i in range(0, len(s2)-len(s1)+1):
        if s2[i:len(s1)+i].lower() == s1.lower():
            b+=1
    return b
#print(ocorrencias_v2("ola", "mundo ola"))

#9 Função que verifica se uma string é anagrama da outra
def anagrama(s1, s2):
    s = sorted(s1)
    ss = sorted(s2)
    if s == ss:
        return True
    else:
        return False
#print(anagrama("amor", "roma"))

#10 Função que retorna dicionário com anagramas
import re
file = open("dicionario.txt", encoding = "utf-8")
text = file.read()
text = text.replace(".", " ")
text = text.replace(",", " ")
text = text.replace("-", " ")
text = text.replace(":", " ")
text = text.replace("/", " ")
text = text.replace("'", " ")
text = text.replace(";", " ")
text = text.replace("(", " ")
text = text.replace(")", " ")
text = text.replace("©"," ")
text = re.sub(r'[0-9]+', '', text)
text = text.lower()

#dividir o texto em tokens
tokens = text.split()

#remover repetidos
tokens = list(set(tokens))

#assumindo que não existe a função para verificar que é anagrama
def dic_anagramas(lista):
    anagramas = {}
    for palavra in tokens:
        #excluir caracteres únicos
        if len(palavra) > 1 :
            ordenada = sorted(palavra)

            #um dicionário não aceita uma lista como key por isso temos de gerar a palavra
            normalizada = ''.join(ordenada)

            #testar se já existe chave no dicionário
            if normalizada in anagramas:
                anagramas[normalizada].append(palavra)

            else:
                anagramas[normalizada] = [palavra] 

    return(anagramas)

anagrama = dic_anagramas(tokens)
for chaves, valores in anagrama.items():
    if len(valores) > 1:
        print("Anagramas de '{}': {}".format(chaves, valores))












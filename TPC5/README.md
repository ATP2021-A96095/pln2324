### Trabalho de Casa 4
#### Introdução:
<p align="justify"> O trabalho de casa desta semana teve como objetivo terminar um desafio desenvolvido ao longo da quarta aula da UC. </p>
<p align="justify"> Assim sendo, o projeto em causa refere-se à conversão de um livro, relativo a doenças do aparelho digestivo, previamente num formato <i>pdf</i>, num formato <i>html</i>. Para além disso, através do uso de um dicionário de termos médicos, já utilizado num trabalho de casa anterior, pretende-se que, cada termo do livro, também presente neste dicionário, disponibilize, no momento de <i>hover</i> do rato, a sua respetiva descrição e tradução (da designação) em inglês.</p>
<p align="justify">Para exemplificar, segue-se abaixo uma imagem ilustrativa do resultado final esperado: </p>

<p align="center"> <img src="screenshots\inicial.png"> </p>
<p align="center"><sup> <i>Hover</i> sobre o termo "patologia" </sup> </p>


#### Tratamento dos termos traduzidos:
<p align="justify">Partindo do que já foi realizado na aula, isto é, da conversão do dicionário de termos médicos num ficheiro <i>json</i> e do tratamento do texto contido no livro propriamente dito, o próximo passo consistiu na geração de uma estrutura de dados adequada, relativa aos termos traduzidos.</p>

<p align="justify">Com isto, procedeu-se à abertura do ficheiro <i>txt</i> de termos traduzidos, previamente fornecido, para leitura, tendo sido estabelecido o processo de extração dos termos, e respetivas traduções, através da função <i>findall</i> das expressões regulares:</p>

<p align="center"><b>"termo_traducao = re.findall(r"(.+)\s@\s(.+)", texto_traduzido)"</b></p>
<p align="justify">Aqui, <i>termo_traducao</i> consiste numa lista de tuplos <b>[(termo1, tradução1), (termo2, tradução2), ...]</b> enquanto que <i>texto_traduzido</i> se refere ao resultado do método <i>read</i>, aplicado ao ficheiro inicial <i>txt</i>.</p>

<span style="color:red;">É importante notar que: </span>

* <p align="justify"> <i>texto_traduzido</i> foi convertido para minúsculas, para a comparação entre termos ser efetuada corretamente. </p>
* <p align="justify"> A expressão regular introduzida corresponde a <i><b>(.+)\s@\s(.+)</i></b> uma vez que, no ficheiro <i>txt</i> de termos traduzidos, o seu conteúdo encontra-se presente na seguinte forma:</p>

<p align="center"><b>Conceito @ Tradução</b></p>
<p align="justify">Neste caso, devido à presença de espaços em branco, estes não foram incluídos nos grupos de captura, de maneira a não afetar o processo de comparação. </p>


<p align="justify">Dada por finalizada a criação da lista de tuplos, esta foi diretamente convertida num dicionário, <i>dic_trad</i>, através do método <b><i>dict</i></b>.</p>

#### Criação do dicionário de dicionários:
<p align="justify">Seguidamente, de maneira a atingir o resultado final, foi estabelecido, durante a aula, que deveria ser gerada uma estrutura correspondente a um dicionário de dicionários, cujo conteúdo deve consistir em: </p>

<p align="center"><b>{ Conceito: {"descrição": (descrição do conceito), "en": (tradução em inglês)}, ...}</b></p>

<p align="justify">Tendo isto em conta, o segundo passo consistiu, então, na geração desta estrutura, onde se implementou o seguinte raciocínio: </p>

* <p align="justify">Definição inicial da estrutura final: <i>dic_final = {}</i>;
* <p align="justify">Num ciclo <i>for</i>, percorreu-se cada conceito presente no dicionário de conceitos (ficheiro <i>json</i>), convertido em minúsculas;</p>
* <p align="justify">Caso o conceito em causa pertença às chaves do dicionário de termos traduzidos, <i>dic_trad</i>, o valor da sua chave, no dicionário final, é, também, um dicionário constituído por:</p>
<p align="center"><b>{"descricao": conceitos_min[conceito], "en": dic_trad[conceito]}</b></p>

* <p align="justify">Caso o conceito em causa não pertença às chaves do dicionário de termos traduzidos, <i>dic_trad</i>, o valor da sua chave, no dicionário final, é, também, um dicionário constituído por:</p>
<p align="center"><b>{"descricao": conceitos_min[conceito], "en": "Sem tradução."}</b></p>

<p align="justify"> O último passo, representado acima, foi implementado, dado que se verificou que certos termos não possuem a respetiva tradução em inglês, como se pode observar nos exemplos disponibilizados abaixo: </p>

<p align="center"> <img src="screenshots\semtrad1.png"> </p>
<p align="center"> <img src="screenshots\semtrad2.png"> </p>
<p align="center"> <img src="screenshots\tunica.png"> </p>
<p align="center"> <img src="screenshots\ulp.png"> </p>

#### Alteração da função etiquetador:
<p align="justify">Finalmente, o último passo consistiu na alteração da função <i>etiquetador</i>, desenvolvida ao longo da aula, de maneira a serem introduzidas as traduções das designações. </p>

<p align="justify">Na imagem abaixo, é possível averiguar o código implementado:</p>
<p align="center"> <img src="screenshots\etiquetador.png"> </p>

* <p align="justify">Basicamente, para cada palavra do livro, foi avaliada a sua existência, quer no dicionário final, ou seja, o dicionário de dicionários, quer na <i>blacklist</i> (uma lista definida para palavras que não faziam sentido para a colocação de descrição, como "os", "de", "para", etc)</p>

* <p align="justify">Caso a palavra cumpra as condições requeridas, a respetiva descrição, e tradução, são armazenadas em duas variáveis, para que, no final, seja gerado o elemento âncora, responsável pelo <i>display</i> de texto aquando do <i>hover</i>:</p>
<p align="center"> <img src="screenshots\etiq.png"> </p>

* <p align="justify"> Caso contrário, a palavra em estudo é retornada, sem qualquer etiqueta.</p>
<p align="justify"> O processo final de colocação, ou da etiqueta, ou da palavra original, no ficheiro <i>html</i>, é conseguido graças à função <i>sub</i> das expressões regulares: </p>
<p align="center"><b>texto = re.sub(expressao, etiquetador, texto, flags = re.IGNORECASE)</p></b>

<p align="justify">Onde <i>expressao</i> diz respeito a cada palavra do livro, e, <i>texto</i> a todo o conteúdo deste.</p>

#### Observações:
<p align="justify">Tal como foi referido anteriormente, determinados termos não apresentam a respetiva tradução, como o caso de <b>túnica</b> e <b>úlcera péptica</b>.</p>

<p align="justify">No que se refere à primeira, é possível observar, no ficheiro final, o resultado esperado:</p>
<p align="center"> <img src="screenshots\tuf.png"> </p>

<p align="justify">No entanto, no que se refere à segunda, verifica-se o seguinte:</p>
<p align="center"> <img src="screenshots\upd.png"> </p>

<p align="justify">É possível observar que apenas a palavra "úlcera" se encontra a sublinhado, apresentando, de facto, uma tradução. Conclui-se, portanto, que uma das limitações do código desenvolvido se refere aos <b>termos compostos</b>. Neste caso, não foi possível estabelecer o <i>hover</i> sobre conceitos constituídos por mais do que uma palavra, daí observarem-se casos como este. </p>

#### Conclusões finais:
<p align="justify">O trabalho desta semana foi bastante simples de resolver uma vez que grande parte do processo foi desenvolvido na aula. De resto, o tratamento do ficheiro de termos traduzidos também se revelou bastante acessível devido à sua forma de organização.</p>
<p align="justify">Considero que este projeto permitiu, mais uma vez, colocar em prática conceitos de <i>html</i>, expressões regulares, dicionários, e, ainda, de <i>xml</i>, tendo sido bastante benéfico para a nossa aprendizagem.</p>
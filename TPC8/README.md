## Trabalho de Casa 8
#### Introdução:

<p align="justify">O trabalho de casa desta semana tem como objetivo trabalhar com modelos treinados através do algoritmo <b><i>Word2Vec</b></i>. O algoritmo em causa permite mapear palavras em vetores, de tal forma que, palavras com significados semelhantes, têm representações próximas umas das outras no espaço vetorial.</p>

<p align="justify">Efetivamente, para o treino do modelo, podem ser utilizados diferentes valores de parâmetros de <i>vector_size</i> e <i>epochs</i>, por exemplo, pelo que, no presente trabalho de casa, os valores dos mesmos serão alterados por forma a ser possível atingir melhores resultados.</p>

<p align="justify">Tendo isto em conta, foram fornecidos dois documentos de texto, ambos referentes à saga do <i>Harry Potter</i>, nos quais vai ser aplicado o processo de tokenização, por forma a tornar possível o treino do modelo.</p>

<p align="justify">Assim, ao longo do presente README, serão abordados os diferentes métodos, associados ao modelo <i>Word2Vec</i>, utilizados na procura de palavras similares, bem como na medição dessa similaridade.</p>

<p align="justify">Para além disso, será estabelecida uma comparação entre os casos em que se procedeu a um <b>pré-processamento manual</b> e os casos em que foi utilizado o método <b>tokenize</b>.</p>

#### Documento de Texto 1: Harry Potter - Câmara Secreta
#### Pré-processamento manual
<p align="justify">Para o processamento manual, procedeu-se ao uso da função <i>sub</i> das <i>RegEx</i> por forma a <b>substituir os caracteres de pontuação</b> como "<b>- ? ! . ; , — –</b>", bem como para eliminar as ocorrências do padrão "<b>\t</b>". Todavia, uma vez que foi utilizado o espaço vazio como substituto dos componentes anteriores, nas listas finais, correspondentes a cada frase, verificava-se a sua presença. Assim, por forma a garantir a ausência de qualquer <i>string</i> vazia nas listas, procedeu-se à sua eliminação através do método <i>remove</i>.</p>

#### Geração do Modelo
<p align="justify">Após isto, deu-se início à geração do modelo, tendo sido definidos os seguintes parâmetros:</p>

* <p align="justify">vector_size = 100; </p>
* <p align="justify">window = 5; </p>
* <p align="justify">min_count = 1; </p>
* <p align="justify">sg = 1; </p>
* <p align="justify">epochs = 5; </p>
* <p align="justify">workers = 3. </p>


#### Similaridades

<p align="justify">Com o modelo obtido, foi utilizado, primeiramente, o método <b><i>most_similar</b></i>, usado para encontrar palavras que são similares à que é fornecida para estudo.</p>

<p align="justify">Tendo isto em conta, foi estudada a similaridade relativamente às palavras:</p>

* <p align="justify">Harry</p>
* <p align="justify">Dumbledore</p>
* <p align="justify">Edwiges</p>
* <p align="justify">Voldemort</p>
* <p align="justify">Draco</p>
* <p align="justify">Rony</p>
* <p align="justify">Sonserina</p>
* <p align="justify">Duda</p>

<p align="justify">Por sua vez, estabeleceu-se a medição da similaridade, através do método <b><i>similarity</b></i>, entre os seguintes pares de palavras:</p>

* <p align="justify">Harry + Edwiges</p>
* <p align="justify">Hermione + Edwiges</p>
* <p align="justify">Rony + Edwiges</p>
* <p align="justify">Grifinória + Sonserina</p>
* <p align="justify">Snape + Poção</p>
* <p align="justify">Duda + Dursley</p>

<p align="justify">Tendo sido obtidos, respetivamente, os seguintes resultados:</p>

* <p align="justify">0.918</p>
* <p align="justify">0.927</p>
* <p align="justify">0.894</p>
* <p align="justify">0.976</p>
* <p align="justify">0.974</p>
* <p align="justify">0.993</p>

#### O intruso

<p align="justify">De seguida, foi utilizado o método <b><i>doesnt_match</b></i>, que é usado para encontrar a palavra que "não se encaixa" num conjunto de palavras com base nas suas representações vetoriais.</p>

<p align="justify">Como diferentes conjuntos de palavras, foram fornecidos os seguintes:</p>

* <p align="justify">Riddle + Hermione + Rony</p>
* <p align="justify">Harry + Rony + Hermione</p>
* <p align="justify">Hogwarts + Grifinória + Basilisco</p>
* <p align="justify">Mandrágora + Rowena + Dumbledore</p>

<p align="justify">Onde foram obtidos os intrusos:</p>

* <p align="justify">Riddle</p>
* <p align="justify">Hermione</p>
* <p align="justify">Hogwarts</p>
* <p align="justify">Dumbledore</p>

<p align="justify">"Riddle" é o nome da família de Voldemort, enquanto "Hermione" e "Rony" são amigos de Harry. Portanto, "Riddle" é o intruso.</p>

<p align="justify">Por sua vez, "Harry", "Rony" e "Hermione" são as três personagens principais. Aqui, o intruso é uma escolha subjetiva, mas pode-se argumentar que "Rony" é o intruso por ser um pouco menos central na história do que Harry e Hermione.</p>

<p align="justify">"Hogwarts" é a escola de magia principal, "Grifinória" é uma das casas em Hogwarts, porém, "Basilisco" é uma criatura. Então, "Basilisco" deveria de ser o intruso.</p>

<p align="justify">"Rowena" e "Dumbledore" são personagens importantes na história, enquanto "Mandrágora" é uma planta mágica. Portanto, "Mandrágora" deveria de ser o intruso.</p>

#### Analogias
<p align="justify">Por fim, e retornando ao método <b><i>most_similar</b></i>, procedeu-se à procura de palavras, semanticamente relacionadas com duas palavras desejadas, mas que não podem incluir uma palavra em específico. Por exemplo, </p>
<p align="center">most_similar(positive=["Harry", "Hermione"], negative=["Edwiges"])</p>

<p align="justify"> pretende encontrar palavras que estão semanticamente relacionadas às personagens "Harry" e "Hermione", mas não relacionadas à coruja "Edwiges".</p>

<p align="justify">Assim sendo, foi testado o seguinte:</p>

* <p align="justify">most_similar(positive =["Harry", "Hermione"], negative=["Edwiges"]);</p>

* <p align="justify">most_similar(positive =["Sonserina", "Draco"], negative=["Grifinória"]);</p>

* <p align="justify">most_similar(positive =["Fred", "Jorge"], negative=["Percy"]).</p>

<p align="justify">Como resultado final, obteve-se o seguinte:</p>

* <p align="justify">Rony, 0.95;</p>
* <p align="justify">mesmo, 0.98;</p>
* <p align="justify">Hermione, 0.98.</p>

<p align="justify">Para a primeira analogia, pode afirma-se que o resultado "Rony" está de acordo, uma vez que se trata de uma das personagens principais da série e que está frequentemente associado a Harry e Hermione.</p>

<p align="justify">No segundo caso, "mesmo" é uma surpresa. Parece que o modelo não conseguiu encontrar uma palavra adequada para completar a analogia de forma significativa, o que pode ser devido a um aspeto de limitação do modelo.</p>

<p align="justify">Para a terceira analogia, "Hermione" como resultado parece inadequado. Novamente, parece que o modelo verificou dificuldades em encontrar uma palavra adequada para completar a analogia.</p>

#### Melhoria do modelo
<p align="justify">De maneira a serem obtidos melhores resultados, procedeu-se à mudança dos valores dos parâmetros que se seguem:</p>

* <p align="justify">vector_size = 300</p>
* <p align="justify">epochs = 20</p>
* <p align="justify">sg = 0</p>

<p align="justify">É importante notar que todo o processo seguinte é igual ao que foi implementado anteriormente, isto é, a mesma avaliação de similaridades, de intrusos e de analogias.</p>

<p align="justify">No geral, verifica-se um aumento das limitações do modelo, uma vez que foram obtidos valores de similaridade relativamente inferiores. Enquanto que, para o primeiro modelo, foram obtidos valores por volta dos 0.9 - 0.99, neste caso, estes valores baixaram para cerca de 0.65 - 0.94. O mesmo se pode afirmar relativamente ao estudo das analogias</p>


#### Pré-processamento com a função tokenize

<p align="justify">No caso que se segue, procedeu-se à tokenização do texto através do uso de uma função própria do <i>gensim.utils</i>: a função <b><i>tokenize</b></i>.</p>

<p align="justify">No entanto, todo o restante processo foi exatamente igual ao já enunciado. </p>

<p align="justify">Em termos de valores de similaridade, observou-se uma melhoria, porém, de dimensão reduzida, sendo apenas referente a um aumento de cerca de 0.015.</p>

<p align="justify">Relativamente aos intrusos, neste caso, apenas se verificou um que é diferente do que foi obtido no caso anterior. No que se refere à lista ["hogwarts", "grifinória", "basilisco"], em vez de se obter "hogwarts", foi obtido "grifindória", no entanto, devido às razões já expostas, faria mais sentido ser "basilisco".</p>

<p align="justify">Seguidamente, foi implementada uma melhoria do modelo, através da definição de novos valores dos parâmetros, já enunciados anteriormente, pelo que os valores obtidos foram bastante semelhantes: enquanto que nuns casos se verificou um ligeiro aumento, noutros verificou-se uma ligeira diminuição.</p>

#### Documento de Texto 1: Harry Potter - Pedra Filosofal
#### Pré-processamento manual

<p align="justify">Todo o processo implementado em relação a este texto é exatamente igual aos que já foram implementados anteriormente.</p>

<p align="justify">Assim, no caso das similaridades, os valores obtidos rondam o intervalo 0.86 - 0.98, sendo bastante semelhantes aos que foram obtidos em relação ao texto 1.</p>

<p align="justify">De igual modo, uma alteração dos parâmetros do modelo não permitiu verificar uma melhoria nos resultados finais.</p>

#### Pré-processamento com a função tokenize

<p align="justify">A aplicação da função <i>tokenize</i>, na fase de pré-processamento, permitiu registar resultados bastante semelhantes.</p>

<p align="justify">A posterior implementação de uma mudança nos valores dos parâmetros do modelo, permitiu observar certos aumentos em relação a certas similaridades encontradas, no entanto, estes são mínimos. Assim, no geral, não se verificou uma melhoria significativa.</p>

#### Junção de ambos os textos
<p align="justify">De maneira a estender o processo de análise, procedeu-se à tokenização, através da função <i>tokenize</i>, de ambos os textos presentes nos dois documentos, previamente implementados numa única lista.</p>

<p align="justify">Após análise dos mesmos casos de similaridade, de intrusos e de analogias, enquanto que o primeiro modelo registou valores contidos no intervalo 0.80-0.97, a alteração posterior dos parâmetros do modelo (enunciada no início do README) registou valores bastante inferiores, passando estes a estar no intervalo 0.40-0.80.</p>

#### Conclusão:

<p align="justify">Depois da experimentação de vários valores de parâmetros, chegou-se à conclusão de que o melhor modelo obtido corresponde ao primeiro, com sg = 1, vector_size = 100 e epochs = 5.</p>

<p align="justify">No entanto, não é possível definir qual a melhor forma de pré-processamento, isto é, manual, ou com a aplicação da função <i>tokenize</i>, uma vez que, enquanto determinados pares de palavras registaram valores de similaridade superiores, outros assumiam uma diminuição.</p>

<p align="justify">Penso que a maior dificuldade do trabalho de casa consistiu na definição dos conjuntos de palavras a estudar, uma vez que não tenho qualquer conhecimento acerca da saga do <i>Harry Potter</i>. No entanto, depois de alguma pesquisa consegui implementar alguns casos de estudo, porém, existe a probabilidade de as conclusões retiradas não se encontrarem 100% corretas. </p>

<p align="justify">Todavia, com este trabalho de casa, foi possível experimentar, e aplicar, diferentes métodos do modelo <i>Word2Vector</i>, o que se revelou bastante interessante.</p>
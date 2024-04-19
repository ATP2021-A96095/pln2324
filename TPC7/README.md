## Trabalho de Casa 7
#### Introdução:

<p align="justify"> O trabalho de casa número 7 tem como objetivo aprimorar as funcionalidades implementadas, e acrescentar outras novas, na aplicação <i>web</i> desenvolvida no TPC número 6.</p>

<p align="justify"> Por forma a recordar, a aplicação em causa tem como tema o <b>dicionário de termos médicos</b> constituído pelos conceitos, e respetivas descrições e traduções, já utilizado nas aulas anteriores. Nesta, encontram-se presentes as opções de filtrar os conceitos pela letra inicial, pesquisa (tendo como resultado todos os conceitos que apresentam, na sua nomenclatura, o termo introduzido pelo utilizador) e um menu composto por opções de redirecionamento para outros dicionários médicos, bem como para jogos relativos aos demais conceitos.</p>

<p align="justify"> Tendo isto em conta, as novas funcionalidades a serem acrescentadas incluem:</p>

* <p align="justify">Possibilidade de <b>adição</b> de um novo conceito, onde o utilizador digita a respetiva descrição e tradução;</p>
* <p align="justify">Possibilidade de <b>eliminação</b> de um determinado conceito, estando esta opção vigente na página específica do mesmo;</p>
* <p align="justify">Visualização dos conceitos através de uma <b>DataTable</b> onde é possível estabelecer uma pesquisa que retorna os conceitos que detêm o termo introduzido, ou na designação, ou na descrição;</p>
* <p align="justify">Melhoria da <b>pesquisa</b> implementada no TPC anterior, onde devem ser devolvidos os conceitos que apresentam, o termo introduzido pelo utilizador, ou na designação, ou na descrição.</p>

<p align="justify">Nas imagens abaixo é possível observar o resultado final, obtido para cada uma das funções: </p>

<p align="center"> <img src="screenshots\adicionar.png"></p>
<p align="center"><sup> <b>Adição de um novo conceito</b> </sup> </p>

<p align="center"> <img src="screenshots\apagar.png"></p>
<p align="center"><sup> <b>Eliminação de um determinado conceito</b> </sup> </p>

<p align="center"> <img src="screenshots\datatable.png"></p>
<p align="center"><sup> <b>DataTable</b> </sup> </p>

<p align="center"> <img src="screenshots\filtrapesquisa.png"></p>
<p align="center"><sup> <b>Pesquisa melhorada</b> </sup> </p>

<p align="center"> <img src="screenshots\medicina1.png"></p>
<p align="center"><sup> <b>Resultado da pesquisa para "medicina"</b> </sup> </p>

#### Adição de um novo conceito
<p align="justify">Para concretizar a funcionalidade em causa, foi essencial utilizar um modelo de <b><i>Form</b></i>, obtido através do <i>Bootstrap</i>. Neste, averiguam-se <b>3 <i>labels</i></b> importantes: <b>Designação</b> do termo, <b>Descrição</b> e <b>Tradução</b>, isto é, os campos a serem preenchidos pelo utilizador. Por sua vez, verifica-se, também, um outro componente fundamental, que corresponde ao botão de <b><i>Submit</b></i>.</p>

<p align="justify">Seguidamente, através do estabelecimento de uma nova <i>route</i>, com método <i>POST</i>, os demais valores inseridos pelo utilizador foram obtidos graças a <i><b>request.form.get</i></b>. Assim, torna-se possível a inserção de uma nova chave, no dicionário original, cujo valor corresponde ao dicionário composto pela descrição e tradução.</p>
<p align="justify">No que se refere a este passo, uma ação importante a tomar, diz respeito à escrita do dicionário no ficheiro correspondente, para que, após uma re-inicialização da aplicação, o novo conceito permaneça juntamente com os demais.</p> 

<p align="center"> <img src="screenshots\testeadd.png"></p>
<p align="center"><sup> <b>Adição de um novo conceito</b> </sup> </p>

<p align="justify">Este objetivo foi conseguido da seguinte forma:</p>

<p align="center"> <img src="screenshots\codigo1.png"></p>
<p align="center"><sup> <b>Atualização do ficheiro JSON</b> </sup> </p>

<p align="justify">Por sua vez, o novo conceito inserido passa a localizar-se no final da lista composta pelos demais termos médicos.</p>

<p align="center"> <img src="screenshots\testeadd2.png"></p>
<p align="center"><sup> <b>Resultado da adição de um conceito</b> </sup> </p>
<p align="justify">É importante notar que todo este processo foi desenvolvido durante a aula teórica.</p>

#### Eliminação de um conceito

<p align="justify">Nesta situação, a <i>route</i> associada corresponde à que foi estabelecida relativamente à página específica de um determinado conceito, uma vez que é lá que se encontra o botão apropriado para a ação. No entanto, encontra-se associado um método de <i>DELETE</i>, de modo a tornar possível a funcionalidade em causa.</p>

<p align="justify">De igual modo ao caso anterior, foi estabelecida uma abertura inicial (em modo de escrita) do ficheiro JSON, correspondente aos conceitos, para que, após eliminação do termo desejado, o dicionário atualizado seja escrito novamente no mesmo, através do método <i>dump</i>. Assim assegura-se que, após um reinício da aplicação, o conceito eliminado não está mais presente.</p>

<p align="justify">Este processo foi, também, desenvolvido na aula teórica, tendo sido fundamental estabelecer um <i>JavaScript</i>, onde se encontra a função <b><i>delete_conceito</b></i>, que é chamada com o identificador de um conceito, como argumento, enviando uma requisição <i>delete</i> para o servidor, para excluir o conceito em causa, e, finalmente, redirecionar o utilizador para a página principal dos conceitos.</p>

#### DataTable

<p align="justify">Uma <i>DataTable</i> corresponde a uma tabela em que pode ser selecionado o número de entradas a visualizar, isto é, selecionar, por exemplo, apenas os primeiros 10 conceitos médicos.</p>
<p align="justify">Neste caso, a tabela é composta por <b>3 colunas</b> referentes à <b>nomenclatura</b> dos conceitos propriamente ditos, à sua <b>descrição</b> e à sua respetiva <b>tradução</b>. Esta foi obtida através do <i>jQuery</i>, que permitiu obter, automaticamente, uma opção de pesquisa, que, após introdução de uma determinada palavra, restringe os conceitos exibidos para aqueles que a contêm, ou na sua designação, ou na sua descrição.</p>

<p align="center"> <img src="screenshots\tabelamedicina.png"></p>
<p align="center"><sup> <b>Pesquisa na DataTable</b> </sup> </p>

<p align="justify">Para além disso, em cada coluna, observam-se setas que, após serem selecionadas, permitem demonstrar os últimos conceitos, presentes no dicionário, por ordem alfabética. Caso estas sejam novamente selecionadas, então são demonstrados os primeiros conceitos.</p>

<p align="justify">Para a obtenção desta tabela, foi estabelecido um novo <i>template html</i>, designado <i>table.html</i>, tendo sido necessário fornecer, na sua renderização, o dicionário correspondente aos demais conceitos médicos, para que, a introdução da informação destes, nas respetivas colunas, seja conseguida através de um ciclo <i>for</i>.</p>

<p align="center"> <img src="screenshots\codigo2.png"></p>
<p align="center"><sup> <b>Inserção da informação na DataTable</b> </sup> </p>

<p align="justify">Por sua vez, esta pode ser acessada, quer através da <i>route</i> <b>/table</b>, quer através da opção inserida no menu vigente no topo da aplicação, isto é, a opção <b>“DataTable”</b>. Esta opção foi conseguida através da inserção de um novo item de lista, no interior do elemento <i>div</i> da classe <b><i>collapse navbar-collapse</b></i>, no que se refere ao <i>template layout.html</i> </p>

<p align="justify">Mais uma vez, este processo foi iniciado na aula teórica, no entanto, a fase de povoamento em si, ficou como um dos objetivos para trabalho de casa. De igual modo à funcionalidade anterior, e ainda na aula teórica, foi acrescentado, ao ficheiro <i>JavaScript</i>, uma extensão de código que utiliza o <i>plugin DataTables</i> do <i>jQuery</i> para tornar uma tabela HTML (com id <i>"myTable"</i>) numa tabela interativa com recursos como ordenação, pesquisa e paginação.</p>

<p align="justify">Além do mais, é importante referir que, no <i>template table.html</i>, foi introduzido um botão que permite retornar à página principal de conceitos, aquando da exibição da <i>DataTable</i> resultante, sendo igual aos botões, de igual funcionalidade, já implementados no trabalho de casa anterior.</p>

#### Pesquisa de conceito
<p align="justify">Tal como foi referido anteriormente, a opção de pesquisa tem como objetivo retornar os conceitos que detêm a palavra introduzida pelo utilizador, ou no seu nome, ou na sua descrição.</p>

<p align="justify">Para tal, a <i>route</i> desenvolvida no TPC anterior, foi atualizada para <i>/conceitos/pesquisar</i>, estando associada a um método <i>POST</i>, tal como na funcionalidade de <i>submit</i> de um novo conceito.</p>
<p align="justify">Por sua vez, o outro componente que sofreu, também, alterações, diz respeito à função <b><i>pesquisar_Conceito</i></b>.</p>

<p align="justify">Considere-se que a variável <i>termo</i> corresponde à palavra introduzida pelo utilizador. Esta foi obtida através de <i>termo = request.form.get("search")</i>. Tendo isto em conta, por forma a determinar o resultado a devolver ao usuário, o dicionário, composto por todos os conceitos médicos, foi percorrido graças a um ciclo <i>for</i>, onde:</p>

* <p align="justify">Caso o <i>termo</i>, convertido em minúsculas, esteja presente na descrição do conceito do dicionário a analisar (também convertida em minúsculas), então a nomenclatura do conceito é introduzida numa lista chamada <i>resultados</i>;</p>

* <p align="justify">Caso o <i>termo</i>, convertido em minúsculas, esteja presente na nomenclatura do conceito a analisar (também convertida em minúsculas), esta é  introduzida na lista <i>resultados</i>;</p>

<p align="justify">Por fim, caso o comprimento da lista em causa seja nulo, então o <i>template</i> <i>naoencontrado.html</i> é renderizado, caso contrário, é renderizado o novo <i>template</i> <b><i>pesquisa.html</i></b> que recebe a lista <i>resultados</i> e o dicionário original.</p>

<p align="center"> <img src="screenshots\codigo3.png"></p>
<p align="center"><sup> <b>Função de pesquisa de conceito</b> </sup> </p>

<p align="justify">Neste <i>template</i>, procedeu-se à construção de uma <b>tabela</b>, obtida graças ao <i>Bootstrap</i>, composta por 3 colunas: <b>Designação</b> dos conceitos, <b>Descrição</b> e <b>Tradução</b>. De modo a preenchê-la, a lista <i>resultados</i> é percorrida, através de um ciclo <i>for</i>, pelo que, a respetiva descrição, e tradução, do conceito, são obtidas através de uma consulta ao dicionário fornecido, pelas respetivas chaves necessárias para o efeito.</p>

<p align="center"> <img src="screenshots\codigo4.png"></p>
<p align="center"><sup> <b>Povoamento da tabela resultante da pesquisa</b> </sup> </p>

<p align="justify">De maneira a tornar o resultado mais visualmente agradável, cada ocorrência do termo, introduzido pelo utilizador, quer esteja presente na designação, ou na descrição de um conceito, é destacada (<i>highlighted</i>), através de uma função definida para o efeito: a função <b><i>highlight</b></i>. Esta função recebe dois argumentos: <i>text</i> e <i>term</i>, substituindo todas as ocorrências de <i>term</i> em <i>text</i> por uma versão destacada de <i>term</i>, ao ser envolvido entre tags <i>mark</i>, graças ao uso da função <b><i>sub</i></b> das RegEX. Neste caso, <i>text</i> pode corresponder à descrição ou à designação do conceito. </p>

<p align="center"> <img src="screenshots\testeadd.png"></p>
<p align="center"><sup> <b>Pesquisa melhorada</b> </sup> </p>

<p align="center"> <img src="screenshots\testeadd2.png"></p>
<p align="center"><sup> <b>Pesquisa melhorada - continuação</b> </sup> </p>

<p align="justify">Com isto, para que a função possa ser usada diretamente nos modelos <i>html</i>, sem necessidade de duplicação do código, foi necessário introduzir a linha <i>app.template_filter('highlight')(highlight)</i>, de maneira a registar a função como um filtro.</p>

<p align="justify">Para além disso, foi empregue a <i>flag <b>re.IGNORECASE,</b></i> para que, ocorrências do conceito em maiúsculas, sejam, também, denotadas.</p> 

<p align="center"> <img src="screenshots\codigo5.png"></p>
<p align="center"><sup> <b>Função <i>highlight</i> e respetivo filtro</b> </sup> </p>

<p align="justify">É importante notar que, no momento da chamada da função <i>highlight</i>, no <i>template pesquisa.html</i>, é implementada a marcação <i><b>safe</i></b>, por forma a indicar ao sistema de <i>template</i> que o conteúdo da expressão (isto é, ou da designação do conceito, ou da sua descrição) deve ser tratado como seguro, ou confiável. Isto deve-se ao facto de o sistema, por <i>default</i>, oferecer proteção contra eventuais vulnerabilidades de segurança. Por exemplo, sem esta marcação, o termo introduzido pelo utilizador não é sublinhado a fluorescente, assim, foi fundamental garantir ao sistema que este termo é seguro.</p>


<p align="justify">Para além disso, é de capital importância denotar a presença de <b>2 botões</b> aquando da exibição dos conceitos resultantes do processo de pesquisa: um botão, que, após uma determinada quantidade de <i>scroll</i>, surge na página, por forma a que, após a sua seleção, o utilizador retorne ao início da página; e um botão que permite retornar à página principal de conceitos. Tal como é possível deduzir, estes são exatamente iguais aos que foram implementados no TPC 6, tendo sido obtidos, simplesmente, através de <i>Copy + Paste</i> do código.</p>


#### Outras mudanças
<p align="justify">Comparativamente ao TPC 6, é possível denotar a mudança na estética, no que se refere ao <i>template <b>conceitos.html</b></i>. Neste caso, para cada funcionalidade, isto é, “filtrar por alfabeto”, “adicionar conceito”, “pesquisar conceito” e “conceitos”, foi introduzido um <i>design</i>, ilustrativo de cada uma, composto por um ícone, juntamente com o título, numa mesma linha. Este processo é exatamente igual ao estabelecido no <i>template <b>dados.html</b></i>, no trabalho de casa anterior.</p>


<p align="center"> <img src="screenshots\filtrapesquisa.png"></p>
<p align="center"><sup> <b>Novo Design</b> </sup> </p>


<p align="justify">Adicionalmente, cada secção, relativa a uma determinada funcionalidade, é separada das restantes por uma barra horizontal cinzenta, obtida através da classe do <i>Bootstrap</i> <b>col bg-secondary</b>.</p>

#### Conclusão:

<p align="justify">Penso que o objetivo do trabalho foi atingido com sucesso, não se tendo registado dificuldades de relevância considerável, uma vez que ferramentas como o <i>Bootstrap</i> e <i>jQuery</i> permitiram acelerar o processo.</p>

<p align="justify"> Efetivamente, foi gasta uma maior quantidade de tempo nos ajustes da estética e <i>design</i> da própria aplicação, do que nas funcionalidades propriamente ditas. Isto deve-se ao facto de certas funcionalidades já terem sido desenvolvidas no TPC 6, pelo que foi apenas necessário fazer umas pequenas alterações.</p>

<p align="justify">De resto, sinto-me orgulhosa do produto final, pelo que considero todo este processo enriquecedor para o conhecimento acerca da programação de uma aplicação <i>web</i>.</p>

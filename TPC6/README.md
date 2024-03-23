## Trabalho de Casa 6
#### Introdução:

<p align="justify"> O trabalho de casa desta semana consistiu na <b>implementação de uma aplicação <i>web</i></b>, através da <i>framework</i> <b>Flask</b>, onde foram desenvolvidas páginas <i>html</i>, como <i>templates</i>, de maneira a ser estabelecida uma interface para os utilizadores.</p>

<p align="justify"> Posto isto, a aplicação <i>web</i> tem como <b>tema o dicionário de termos médicos</b>, constituído pelos conceitos, e respetivas descrições e traduções dos mesmos, já utilizado nas aulas anteriores.</p>

<p align="justify">De facto, durante a aula foi possível implementar os <i>templates</i>, 'conceitos.html', 'layout.html' e 'home.html' pelo que ficou estabelecido, como trabalho para casa, a geração de um outro <i>template</i>, porém, específico para cada conceito, sendo fundamental a presença da descrição e tradução do mesmo. Para além disso, foi lançado como desafio a exploração do <b><i>Bootstrap</i></b>, uma ferramenta útil para facilitar todo o processo de desenvolvimento <i>web</i>, de maneira a serem implementados outros componentes, como botões, barras de pesquisa, menus etc.</p>

<p align="justify">Antes de demonstrar o <i>template</i> requerido, vão ser apresentadas, a seguir, as mudanças estabelecidas nos <i>templates</i> desenvolvidos durante a aula.</p>

#### Template Home:
<p align="justify">No <i>template</i> em causa, foram inseridos <b>dois componentes introdutórios</b>: uma <b>imagem</b>, relacionada com o tema em causa, e um simples <b>título</b> de introdução ao tema. Para além disso, a envolver o texto, encontra-se uma <b>animação</b>, obtida do <i>Bootstrap</i>, conhecida por <b><i>Animate Placeholders</b></i>. Esta última consiste, basicamente, em duas barras cuja cor vai desvanescendo, até voltar ao estado inicial, num ciclo infinito.</p>

<p align="justify">Na imagem abaixo é possível observar o resultado final: </p>

<p align="center"> <img src="screenshots\home.png"></p>
<p align="center"><sup> <b>Página Inicial, Home</b> </sup> </p>

<p align="justify">De maneira a atingir este resultado, foi essencial criar um elemento <i>div</i>, de classe <b>grid gap-3</b>, obtida do <i>Bootstrap</i>. Esta classe foi utilizada dado que permite implementar <i>containers</i> com diferentes componentes alinhados num único nível. Para além disso, também foi definido um elemento <i>div</i>, para a imagem, e outro para o título, este em conjunto com a animação, de maneira a ser possível alinhá-los corretamente.</p>

#### Template Layout:
<p align="justify">Na imagem anteriormente apresentada, é possível averiguar a presença de uma barra de navegação, no cabeçalho, e de um rodapé. Relativamente à primeira, esta foi facilmente obtida pelo <i>Bootstrap</i>, após uma pesquisa por <b>'Nav Bar'</b>, e cópia do código presente na secção <b>'Supported Content'</b>. Contudo, certas alterações foram implementadas de maneira a ser gerado um resultado de acordo com o tema:</p>

* <p align="justify">Por exemplo, <b>'Home'</b> é um <b>botão</b> que reencaminha o utilizador para a página definida pelo <i>template</i> apresentado anteriormente. </p>

* <p align="justify">Por sua vez, um clique em <b>'Conceitos'</b> disponibiliza a página constituída por todos os conceitos médicos em estudo, sendo o <i>template</i> correspondente 'conceitos.html'.</p>

* <p align="justify">De seguida, averigua-se a presença de um último botão, <b>'Other Resources'</b> que disponibiliza um <b>menu</b>, após um clique no mesmo: </p>

<p align="center"> <img src="screenshots\other.png"></p>
<p align="center"><sup> <b>Other Resources: Dropdown Menu</b> </sup> </p>

<p align="justify">No entanto, averigua-se que ambos os items presentes no menu, correspondem, também, a botões, que, neste caso, após um clique, disponibilizam um <b>dropend menu</b>.</p>

<p align="justify">Nesta situação, 'Other Resources' tem como objetivo disponibilizar acesso a outros dicionários médicos, disponíveis na <i>web</i>, bem como a determinados jogos e <i>quizzes</i>, relacionados com a terminologia médica.</p>

<p align="center"> <img src="screenshots\other.png"></p>
<p align="center"><sup> <b>Other Resources: Dropdown Menu</b> </sup> </p>
<p align="center"> <img src="screenshots\otherdic.png"></p>
<p align="center"><sup> <b>Outros dicionários e opções</b> </sup> </p>
<p align="center"> <img src="screenshots\othergames.png"></p>
<p align="center"><sup> <b>Jogos & <i>Quizzes</i> e opções</b> </sup> </p>

<p align="justify">Por exemplo, um clique em <b>'Harvard Medical School'</b>, origina uma nova janela, sendo esta relacionada ao <i>website</i> dos termos médicos da <i>Harvard Medical School</i>. Já um clique em <b>'Sporcle'</b>, abre, também, uma nova janela relativa a uma página <i>web</i>, onde é possível realizar vários jogos e <i>quizzes</i>, relacionados com o tema em causa, o que se revela ótimo para estudantes colocarem o estudo em prática.</p>

<p align="justify">Confesso que o processo acima descrito foi bastante complicado e moroso uma vez que não bastou uma simples cópia do código presente no <i>Bootstrap</i>, uma vez que foram utilizados dois tipos de menus distintos: dropdown e dropend. Por exemplo, após definição de uma lista, com a <i>tag</i> <i>ul</i>, da classe <i>dropdown-menu</i>, e posterior definição do primeiro item, com a <i>tag li</i>, da classe <i>dropend</i>, foi estabelecido o botão 'Outros dicionários' através do uso da <i>tag</i> correspondente a um elemento âncora. Seguidamente, foi necessário proceder à definição de uma outra lista, com a <i>tag ul</i>, da classe <i>dropdown-menu</i>, e à correta definição dos itens da lista, onde a indentação do código se revelou extremamente importante para atingir o objetivo final.</p>

<p align="justify">Relativamente ao <b>rodapé</b>, este foi também gerado durante a aula, no entanto, verificou-se que, no final da página relativa aos conceitos, este cobria os últimos termos. Este comportamento teve como causa o uso do parâmetro <i>fixed-bottom</i>, que obriga o elemento a permanecer sempre na parte inferior da página. No entanto, caso este fosse descartado, nas restantes páginas o rodapé passava a localizar-se no seu centro. Como solução, o parâmetro referido foi mantido, porém, no <i>template</i> 'conceitos.html', aquando da listagem dos conceitos, pela classe <i>list-group</i> foi introduzida uma <i>margin bottom</i> de 5, fazendo com que, no final da página, o rodapé esteja separado dos últimos termos, não os sobrepondo.</p>

#### Template Conceitos:
<p align="justify">Tal como já foi referido, o <i>template</i> em causa foi iniciado durante a aula, onde se procedeu à listagem de todos os conceitos presentes no dicionário. Contudo, de maneira a aprimorar a página em si, e a facilitar a utilização da aplicação, por parte do utilizador, foram acrecentados componentes como:</p>

* <p align="justify"> <b>Filtragem por letra inicial</b>: Neste caso, procedeu-se à implementação de botões representativos de cada letra do alfabeto para que, após clique num deles, o utilizador seja redirecionado para a secção da página composta pelos termos iniciados pela letra escolhida.</p>

<p align="justify"> Para tal, no ficheiro <i>Python</i>, no que se refere à função que renderiza o <i>template</i> em causa, no momento de renderização, foram fornecidas uma lista constituída por todas as letras do alfabeto, <b>'alfabeto'</b>, obtida através de <b><i>alfabeto = list(string.ascii_uppercase)</b></i> e uma lista composta pela primeira ocorrência do conjunto de termos iniciados por uma letra específica, <b>'primeiros_termos'</b>.</p>

<p align="justify"> A última lista, acima referida, foi obtida através de:</p>
<p align="center"> <img src="screenshots\primeiros.png"></p>
<p align="center"><sup> <b>Geração da lista 'primeiros_termos'</b> </sup> </p>

<p align="justify">Basicamente, para cada conceito, foi averiguado se o mesmo se iniciava pela letra em estudo, sendo adicionado à lista caso a condição se verificasse. É importante notar a presença do <b>break</b> pois queremos usar como elemento âncora apenas o primeiro termo que começa pela letra requerida pelo utilizador.</p>

<p align="justify">No ficheiro html propriamente dito, os diferentes botões foram originados graças a um ciclo for, que itera sobre a lista 'alfabeto', previamente fornecida, gerando botões, correspondentes a elementos âncora, com <i>href</i> da forma <i><b>href = #letra_em_estudo</i></b>. Por exemplo, o botão relativo à letra "A" tem uma <i>href=#A</i>.</p>

<p align="justify">Numa parte posterior do código, na listagem dos conceitos, caso o conceito em causa pertença à lista dos primeiros termos, então, no elemento âncora do mesmo, é atribuído o <i>id</i> de igual formato ao da <i>href</i> definida. Assim, o utilizador, após clicar numa letra, é direcionado para a secção constituída pelos termos que começam por essa letra.</p>

<p align="justify">No entanto, considere-se um caso em que o utilizador carrega no botão relativo a "Y": caso este pretenda retornar ao topo da página, teria de fazer um <i>scroll</i> exaustivo. Assim, foi implementado um outro componente, neste caso, um <b>botão back to top</b>.</p>

<p align="justify">A implementação deste componente também requis muita pesquisa e dedicação uma vez que foi necessário estabelecer um <i><b>javascript</i></b> para ser possível definir a partir de que momento este botão aparece, dado que não faz sentido aparecer no topo da página (sem qualquer <i>scroll</i>), bem como estabelecer o seu comportamento, isto é, se implementa um <i>smooth scroll</i>, por exemplo.</p>

<p align="center"> <img src="screenshots\script.png"></p>
<p align="center"><sup> <b>JavaScript do Back to Top Button</b> </sup> </p>

<p align="justify">É possível concluir que, caso a posição vertical atual do <i>scroll</i> da janela seja maior do que 150 pixels, o botão surge, pelo que estabelece um <i>smooth scroll</i>.</p>

<p align="justify">Na definição do estilo do botão, foi utilizada uma fonte de <i>icons</i>, neste caso, <b><i>Font Awesome</b></i>, tendo sido extremamente importante adicionar o respetivo <i>link</i> para o ficheiro CSS, da <i>Font Awesome</i>, em 'conceitos.html', mais concretamente dentro do <i>block body</i>. Neste caso, o ícone utilizado diz respeito a uma seta a apontar para cima, como se pode ver na figura abaixo.</p>

<p align="center"> <img src="screenshots\filtroebotao.png"></p>
<p align="center"><sup> <b>Resultado da filtragem pela letra F</b> </sup> </p>

* <p align="justify"> <b>Pesquisa por conceito</b>: Caso o utilizador já saiba o nome do conceito a procurar, ou apenas uma das palavras constituintes, uma vez que a designação do conceito pode conter mais do que uma palavra, foi implementada uma <b>barra de pesquisa</b> que disponibiliza os conceitos que detêm a palavra inscrita.</p>

<p align="center"> <img src="screenshots\pesquisa.png"></p>
<p align="center"><sup> <b>Barra de Pesquisa</b> </sup> </p>

<p align="center"> <img src="screenshots\resultadospesquisa.png"></p>
<p align="center"><sup> <b>Resultados da Pesquisa</b> </sup> </p>

<p align="justify"> Na imagem acima é possível averiguar a presença de vários conceitos que detêm a palavra 'medicina' na sua designação. <b>Contudo</b>, é importante registar que o último conceito não se encontrava assim definido, inicialmente. Isto é: a designação de <b>'medicina esportiva, medicina desportiva'</b>, no dicionário original, correspondia, efetivamente a: <b>'medicina esportiva/medicina desportiva'</b>.</p>


<p align="center"> <img src="screenshots\esportiva.png"></p>
<p align="center"><sup> <b>Nomenclatura inicial</b> </sup> </p>

<p align="justify">Ora, após seleção do mesmo para análise, o seguinte resultado foi gerado:</p>

<p align="center"> <img src="screenshots\erro.png"></p>
<p align="center"><sup> <b>Erro de acesso</b> </sup> </p>

<p align="justify">Efetivamente, a presença da barra fez com que fosse considerado um novo URL, que, de facto, não existe. Para resolver esta questão, no dicionário <i>json</i>, implementado nas aulas, procedeu-se à substituição, manual, de todas as barras contidas, nas designações dos conceitos, por vírgulas ou por dois pontos (dependendo do contexto).</p>

<p align="justify"> Para esta funcionalidade foi necessário definir uma nova função, no ficheiro <i>Python</i>, dada por <b>pesquisar_Conceito</b>, cuja rota associada só será chamada se o <i>request</i>, em HTTP, corresponder a <b><i>POST</b></i> (dado que estão a ser enviados dados do utilizador para o servidor).</p>

<p align="justify">Assim sendo, no <i>template</i> 'conceitos.html', no momento de definição da barra de pesquisa, na classe 'form', foi estabelecido que <b><i>action="{{ url_for('pesquisar_Conceito') }}"</b></i>, de maneira a que os dados resultantes da submissão do utilizador sejam redirecionados para a função em causa, para processamento.</p>

<p align="justify">Nesta função, o termo introduzido foi armazenado em <b><i>termo = request.form.get("search", "")</b></i> (sendo <i>search</i> o nome fornecido à classe de <i>input</i>). Posteriormente, caso este termo esteja presente numa lista composta por todos os conceitos em estudo, é definida uma lista, chamada <b>resultados</b>, que tem como intuito armazenar os conceitos que apresentam o termo em causa na sua nomenclatura. Posto isto, procede-se à renderização do <i>template</i> 'conceitos.html' para que este possa fazer a listagem dos resultados obtidos.</p>

<p align="justify"><b>Contudo</b>, caso o termo especificado não exista, é renderizado um novo <i>template</i>, <b><i>'nao_encontrado.html'</b></i>, em que é disponibilizada uma mensagem de erro. Para além disso, o utilizador tem a hipótese de retornar, quer à página inicial (Home), quer à página composta por todos os conceitos, através dos dois botões disponibilizados. Estes dois botões tiveram de ser definidos num <i>container</i> 'pai', por forma a serem alinhados, em conjunto, no final da página.</p>

<p align="center"> <img src="screenshots\naoencontrado.png"></p>
<p align="center"><sup> <b>Erro na Pesquisa</b> </sup> </p>

#### Template Dados:
<p align="justify">O <i>template</i> 'dados.html' pretende gerar a página específica para um determinado conceito. Assim, é possível concluir que este constitui o <i>template</i> referente ao trabalho de casa.</p>

<p align="justify">Em termos de constituição da página averigua-se o seguinte:</p>

* <p align="justify">Um título inicial, correspondente à <b>designação</b> do conceito;</p>
* <p align="justify">Uma <b>linha</b> de separação de secções;</p>
* <p align="justify">Um <b>ícone</b> de um lápis, seguido pela <b>descrição</b> do conceito;</p>
* <p align="justify">Um <b>ícone</b> representativo da língua inglesa, seguido pela <b>tradução</b> do conceito;</p>
* <p align="justify">Um <b>dropdown menu</b>, onde são disponibilizadas outras línguas de tradução: Espanhol, Francês, Italiano e Espanhol. Após o clique numa determinada linguagem, o utilizador é redirecionado para a janela do <b>Google Tradutor</b>, onde é colocado, automaticamente, o conceito, sendo gerada, assim, a sua tradução. </p>
* <p align="justify">Um <b>botão</b> que permite retornar à página composta por todos os conceitos em estudo;</p>

<p align="center"> <img src="screenshots\termoex.png"></p>
<p align="center"><sup> <b>Estrutura da página para cada conceito</b></sup> </p>

<p align="center"> <img src="screenshots\traducoes.png"></p>
<p align="center"><sup> <b>Dropdown menu das traduções</b></sup> </p>

<p align="justify">A imagem abaixo pretende verificar que, para a colocação de uma imagem, relativa a um ícone, seguida de texto, foi necessário, novamente, o uso de uma <i>grid</i> por forma a alinhar ambos os componentes num único nível.</p>

<p align="center"> <img src="screenshots\gridinicial.png"></p>
<p align="center"><sup> <b>Elemento div inicial</b> </sup> </p>

<p align="center"> <img src="screenshots\primeiralinha.png"></p>
<p align="center"><sup> <b>Primeiro elemento da grid</b> </sup> </p>

<p align="center"> <img src="screenshots\segundalinha.png"></p>
<p align="center"><sup> <b>Segundo elemento da grid</b> </sup> </p>

<p align="justify">É <b>importante</b> notar que os <i>screenshots</i> acima foram tirados durante o processo de desenvolvimento, uma vez que ainda não se encontra presente o <i>dropdown menu</i> de traduções.</p> 

#### Dificuldades:
<p align="justify">Claramente, a introdução da ferramenta <i>Bootstrap</i> permitiu acelerar o processo de desenvolvimento de código HTML e CSS. No entanto, aquando da definição da estrutura da aplicação, certos impasses foram encontrados, tais como: como combinar um submenu no interior de um menu e como implementar um botão <i>Back to Top</i> que apenas aparece mediante uma certa distância de <i>scroll</i>. Apesar de este último se revelar bastante desafiador, a sua implementação permitiu aprender, um pouco, acerca da estruturação e definição de um <i>JavaScript</i>, algo benéfico para o conhecimento.</p>

<p align="justify">Confesso que as maiores dificuldades consistiram na definição dos valores dos diferentes parâmetros, uma vez que não se pretende que as páginas sofram uma desformatação aquando da abertura noutros dispositivos. Apesar de me esforçar para tal não acontecer, como através do uso de % em vez de pixels, ou de rem no lugar de pixels, no tamanho das fontes de texto, certos elementos ainda sofrem alguma desformatação no momento de diminuição do tamanho da janela, pelo que é algo que necessito de melhorar futuramente.</p>

<p align="justify">No entanto, apesar disso, foi possível 'brincar' com valores de certos parâmetros, já disponibilizados pela ferramenta, como, por exemplo, na escolha de uma cor de <i>background</i> dos botões, e na escolha de uma nova cor quando é efetuado o <i>hover</i> sobre os mesmos, o que permite tornar o processo mais visualmente agradável.</p>


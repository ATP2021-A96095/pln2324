### Trabalho de Casa 4
#### Introdução:

<p align="justify">O trabalho de casa desta semana teve como intuito explorar, com maior profundidade, os conceitos envolvidos no mundo do <i><b>HTML</i></b> e do <i><b>CSS</i></b>. Dito isto, o objetivo principal consistiu na criação de um ficheiro HTML inspirado num dos <i>hobbies</i> dos alunos. </p>

<p align="justify">Pessoalmente, a minha escolha foi imediata uma vez que pratico este <i>hobby</i> desde que sou pequenina: <b>o desenho</b>. Desde que me lembro, sempre recorri a folhas e lápis de cor para passar o meu tempo e me abstrair do mundo real, e, à medida que fui crescendo, a exposição às mais diversas variedades de pintura despertou, ainda mais, o meu interesse. </p>

#### Estrutura geral:
<p align="justify">Assim sendo, o meu ficheiro HTML engloba: </p>

*  <p align="justify">Um <b>cabeçalho</b>, constituído por uma imagem, e um nome, relacionado com o tema, neste caso, <i>Ana's gallery</i>; </p>

* <p align="justify">Uma <b>barra horizontal</b>, semelhante a um <i>mini menu</i>, constituído por três opções, à escolha do utilizador, que lhe permitem direcionar diretamente para a parte da página que contém o tema selecionado. As opções são: <b><i>About Me</b></i>, <b>Técnicas</b> e <b>Inspirações</b>. </p>

* <p align="justify">As mais diversas secções, relativas a cada uma das opções do menu disponibilizado, onde é possível observar desenhos de técnicas específicas.</p>

* <p align="justify">Uma parte final, específica para o tema de inspirações artísticas, em que são disponibilizados diversos exemplos de inspiração, como também soluções que permitem contornar eventuais situações de <i>art block</i>.</p>

#### Implementação do código:
#### Tags Iniciais
<p align="justify">Para dar início à criação do ficheiro, foram implementadas <i>tags</i> de capital importância, tais como: <i><b>!DOCTYPE html</i></b>, essencial para garantir que o navegador em causa interpreta o código corretamente e entende a versão de HTML que está a ser utilizada.</p>
<p align="justify">A própria <i>tag</i> <b><i>html</b></i>, uma vez que define o início e o fim do documento, envolvendo todo o conteúdo presente na página.</p>
<p align="justify">É ainda importante notar a presença de <i><b>meta charset="UTF-8"</b></i>, extremamente importante na especificação da codificação dos caracteres do documento HTML, como, neste caso, UTF-8, dado que foram utilizados caracteres acentuados.</p>

<p align="justify">Seguidamente, por forma a implementar todas as regras de estilo, a serem incluídas no documento, foram utilizadas as <i>tags</i> <i>head</i> e <i>style</i>. A primeira é uma secção obrigatória, especialmente num documento HTML, que contém informações e metadados sobre o mesmo, que não são diretamente visíveis na página. Por exemplo, é dentro desta <i>tag</i> que são incluídos todos os estilos CSS, no entanto, este requisito necessita, também, da <i>tag</i> <i>style</i>.</p>

<p align="justify">No entanto, entre as duas <i>tags</i>, definidas acima, foi, ainda, implementada a <i>meta tag</i> <i><b>meta name="viewport" content="width=device-width, initial-scale=1"</b></i>, que tem como função controlar o comportamento de visualização da página noutros dispositivos móveis. Mais especificamente, <i>width=device-width</i> define a largura de uma janela, ou da área visível de um ecrã, como a largura do dispositivo, e, <i>initial-scale=1</i>, define a escala inicial da página, quando carregada no dispositivo, para 1, fazendo com que a página seja disponibilizada numa escala 1:1 noutros dispositivos, sem sofrer qualquer tipo de <i>zoom</i>.</p>

#### Regras de Estilo CSS
<p align="justify">Com isto, é possível dar início à escrita das regras de estilo CSS propriamente ditas. No CSS, uma regra de estilo é também definida como uma classe, sendo esta composta por um seletor, que identifica os elementos aos quais a regra se aplica, seguida por um bloco de declarações, que especificam os estilos a serem aplicados aos elementos HTML. Assim, com estas classes, é possível proceder à reutilização de determinados estilos. </p>

#### Cabeçalho:
* <p align="justify"><b><i>container</b></i> e <b><i>centered</b></i>: Ambas as classes foram utilizadas no que diz respeito à geração do cabeçalho, definido como a sobreposição de texto numa determinada imagem de fundo.</p>
<p align="justify">Os <i>containers</i> em CSS, também conhecidos como o elemento pai de um elemento filho, são usados para o agrupamento de conteúdo, pelo que, neste caso, o <i>container</i> estabelecido, engloba a imagem e o texto, apresentando as propriedades <b><i>position: relative</b></i>, o que significa que o posicionamento absoluto dos elementos filhos será relativo a este, e <b><i>text-align: center</b></i> que centraliza o texto dentro do <i>container</i>.</p>

<p align="justify">A classe <i>centered</i> foi implementada na definição do estilo do texto a ser sobreposto na imagem de fundo. Algumas propriedades definidas foram: <i><b>position: absolute:</i></b> que define a posição do texto como absoluta em relação ao <i>container</i> "pai"; <i><b>top: 50%:</i></b> que define a posição superior do texto como 50% da altura do <i>container</i> e <i><b> transform: translate(-50%, -50%):</i></b> onde é usada a função <i><b>translate()</i></b> para mover o texto 50%, tanto na direção horizontal, como na vertical, o que tem como efeito centralizar, vertical, e horizontalmente, o texto em relação ao <i>container</i>.</p>

<p align="justify">Na função <i>translate</i> os valores negativos são usados no movimento do conteúdo na direção oposta, quer ao eixo x, como também ao eixo y: -50%, no eixo x, move o elemento para a esquerda, e -50%, no eixo y, move o elemento para cima.</p>

#### Menu Horizontal:
* <p align="justify"><b><i>container-below</b></i>: Esta classe corresponde ao elemento "pai" de todo o menu horizontal, representado como uma barra de fundo azul, composto por três opções para seleção. Assim, foram essenciais duas propriedades de maneira a centralizar os "filhos", horizontalmente, no mesmo: <b><i>display: flex</b></i> (onde os elementos são organizados numa linha) e <i><b>justify-content: center</b></i> (onde os elementos são alinhados e centralizados ao longo do eixo principal do <i>container</i>). </p>

* <p align="justify"><b><i>item</b></i>, <b><i>item a</b></i> e <b><i>item a:hover</b></i>: Todas estas classes foram empregues para a definição de cada elemento constituinte do <i>container-below</i>.</p>

<p align="justify">A primeira refere-se a cada item presente no <i>container</i>, isto é, cada opção suscetível de ser selecionada pelo utilizador, que é representado por um retângulo com texto centralizado, vertical, e horizontalmente. Assim, algumas propriedades definidas foram a largura e altura de cada retângulo, e a margem entre ambos. Para além disso, estabeleceu-se <i><b>display: inline-flex:</i></b> que define o elemento como um <i>container</i> <i>flexbox</i>, com <i>layout</i> em linha; <i><b>justify-content: center</i></b>, que alinha o conteúdo horizontalmente no centro do <i>container flexbox</i> e <i><b>cursor: pointer</i></b>, que altera o cursor do rato, passando este a ser representado por uma mão, quando se encontra sobre o elemento, indicando que o mesmo é "clicável".</p>

<p align="justify">A segunda regra de estilo é aplicada a elementos âncora, contidos dentro de elementos da classe <i>item</i>, garantindo que o texto, relativo às opções a serem clicadas com o rato, herda a cor do texto definida para o elemento "pai", neste caso, <i>item</i>. Esta decisão foi tomada uma vez que, numa primeira implementação, a cor <i>default</i> do texto era azul, pelo que se tornava mais escura, após o clique do rato. Assim, com esta classe, é assegurado que a cor do texto corresponde sempre ao preto.</p>

<p align="justify">A terceira classe é específica para as situações em que o rato se movimenta sobre as opções do menu, garantindo, também, que a cor do texto se mantenha igual à do elemento "pai".</p>

<p align="justify"><b>NOTA:</b> Os elementos âncora, abordados anteriormente, representados pela <i>tag</i> <b><i>a</b></i>, têm como principal função a criação de <i>hiperlinks</i> numa página <i>web</i>. Neste caso, foram definidos como os três items presentes no menu horizontal, permitindo que os utilizadores sejam direcionados para a secção da página requerida pelos mesmos.</p>

<p align="justify">Para concretizar o objetivo anterior, a cada elemento âncora estabelecido, foi atribuído um <i><b>id</i></b>, como identificador da secção da página, tal como em: </p>

<p align="center"> <img src="screenshots\Captura de ecrã 2024-03-08 182656.png"> </p>


<p align="justify">Com isto, basta apenas definir um <i>hiperlink</i>, usando o <i>id</i> previamente definido, que permite saltar para a parte da página em questão, como em: </p>

<p align="center"> <img src="screenshots\Captura de ecrã 2024-03-08 182556.png"> </p>

#### Introdução à técnica Pontilhismo:
* <p align="justify"><b><i>text-with-dots</b></i>, <b><i>dots-container</b></i>, <b><i>dot</b></i> e <b><i>@keyframes fadeIn</b></i>: Todas as classes são relativas ao início da secção relativa à técnica pontilhismo, onde a ideia foi introduzir um título, neste caso, "Pontilhismo", seguido por um conjunto de pontos, a ocupar a largura total da página, em animação, isto é, desvanescendo infinitamente.</p>

<p align="justify">A primeira engloba toda a secção constituída por ambos o texto e conjunto de pontos; a segunda todo o <i>container</i> que envolve todos os pontos, e a última cada elemento, ou seja, cada ponto, em que uma das propriedades fundamentais trata-se de <i><b>display: inline-block</i></b>, que faz com que os pontos sejam compilados em linha, porém, com propriedades de largura, altura, margem, etc. Para além disso, a estes últimos foi atribuída a animação <i><b>fadeIn</i></b>, onde os elementos vão aparecendo, e desaparecendo, infinitamente, de 5 em 5 segundos.</p>

<p align="justify">A animação foi conseguida pela regra <i><b>@keyframes</i></b>, definindo e especificando os passos intermediários da animação. Por exemplo, <b>0% {opacity: 0;}</b>, refere-se ao estado inicial da animação, em que a opacidade do elemento é 0, isto é, totalmente transparente.</p>

#### Introdução à técnica Colorido:
* <p align="justify"><b><i>centered_colorido</b></i>: a ideia é semelhante ao que foi estabelecido como cabeçalho, isto é, a introdução à técnica Colorido engloba uma imagem, neste caso uma barra de cores, com texto sobreposto.</p>

#### Secções dos desenhos e respetivas descrições:
* <p align="justify"><b><i>text-image</b></i> e <b><i>texto</b></i>: usadas, especificamente, nas secções em que são demonstrados os desenhos e as suas respetivas descrições. A primeira refere-se a toda a secção que engloba ambos os elementos, pelo que a segunda foi particularmente definida em relação ao texto que faz parte dessa secção.</p>

<p align="justify">Neste caso particular, foi necessário implementar 3 elementos <i><b>div</i></b> na página. Um elemento <i>div</i> representa uma divisão, ou secção genérica, de um documento HTML passíveis de serem aplicadas regras de estilo.</p>
<p align="justify">Posto isto, foi implementado um elemento <i>div</i> relativo à classe <i>text-image</i>, representando, assim, a secção genérica desenho + descrição, e, dentro deste, outros dois elementos:
um relativo à imagem, de maneira a fazer com que esta se localize num dos lados da página, e outro relativo à descrição, de maneira a fazer com que este se encontre, ao mesmo nível, mas no lado contrário ao da imagem.</p>
<p align="justify">Consoante a ordem de escrita dos elementos relativos à imagem e texto, foi possível alternar a ordem de posicionamento dos mesmos ao longo do documento: isto é, se inicialmente uma imagem se localiza à esquerda e a sua descrição à direita, então, a seguir farei com que a imagem passe a encontrar-se à direita e a descrição à esquerda.</p>

#### Secção Inspirações:
* <p align="justify"><b><i>info_insp</b></i>, semelhante a <i>text-image</i>, porém, a propriedade <i>gap</i> foi alterada para 0, uma vez que o objetivo era estabelecer a junção de diversas imagens na introdução da secção Inspirações.</p>

<p align="justify">Por exemplo, a primeira imagem abaixo, quando introduzida no documento, não ocupava a largura total da página, contudo, para contornar essa situação, esta classe foi definida para que, com a colocação, repetida, de 3 imagens, estas pudessem ser interpretadas como uma só.</p>

<p align="center"> 
<img src="fotos\flores.jpg"> 
</p>


* <p align="justify"><b><i>texto-borda</b></i>: esta classe permite representar um texto com uma borda retangular, em torno do mesmo, tendo sido utilizada numa parte mais final do documento.</p>

* <p align="justify"><b><i>li</b></i>, <b><i>::marker</b></i> e <b><i>::custom-mark</b></i> são relativas a uma lista com marcações, onde a primeira se refere ao estilo dos elementos da lista, tendo sido estabelecido como marcador o símbolo "✓". A segunda, conhecida como <i><b>marker selector</i></b> permite selecionar o marcador do item e definir parâmetros como a sua cor, enquanto que a última se refere ao <i>highlight</i> de um determinado texto, dentro de um elemento <i>mark</i>, onde foi estabelecida a cor do sublinhado. </p>

<p align="justify">Estando definidas todas as regras de estilo, é possível proceder ao encerramento das <i>tags</i> <i>head</i> e <i>style</i> e dar início à produção do documento em si, através da <i>tag</i> <i>body</i>.</p>

<p align="justify">Tal como foi referido, todo este processo foi conseguido pela conjugação de diversos elementos <i>div</i>, específicos de determinadas classes, de maneira a ser obtida a estrutura pretendida.</p>

<p align="justify">Por exemplo, no caso da animação estabelecida, foi necessário incorporar, dentro de um elemento <i>div</i> da classe <i>text-with-dots</i>, um elemento <i>div</i> da classe <i>dots-container</i>, e, por sua vez, dentro deste, 15 elementos <i>div</i> da classe <i>dot</i>. Este número elevado deve-se ao facto de se pretender ocupar toda a largura da página.</p>

#### Considerações Finais:
<p align="justify">Este trabalho de casa foi mais um desafio que exigiu um elevado nível de dedicação uma vez que o nível de conhecimento, e prática, em HTML e CSS era praticamente nulo. Consequentemente, foram gastas diversas horas na aprendizagem de todo o funcionamento global deste mundo, incluindo os mais diversos elementos e parâmetros existentes.</p>
<p align="justify">No que diz respeito a estes últimos, penso que a maior dificuldade consistiu na determinação dos parâmetros a usar em determinadas classes, devido ao elevado número de opções. Para além disso, muitos destes geraram alguma confusão no entendimento da sua função, uma vez que, pelo menos para mim, atuavam de forma semelhante, como <i>align-items</i> e <i>justify-content</i>.</p>
<p align="justify">No geral, todo o processo consistiu num jogo entre os valores dos diversos parâmetros, de maneira a ser atingida a estrutura desejada do documento.</p>
<p align="justify">No entanto, apesar de ter sido um processo laboroso, uma vez implementados os elementos iniciais do ficheiro HTML, o resto do procedimento revelou-se bastante semelhante, pelo que, a própria prática permitiu consolidar e acelerar a obtenção do documento.</p>
<p align="justify">Em suma, sinto-me bastante satisfeita com o resultado final, sobretudo com a animação presente e as âncoras definidas. Penso que o tema em si levou a que o ficheiro se tornasse visualmente agradável, uma vez que foram conjugados diversos elementos, como os pontos (já referidos), a barra colorida e as bordas das imagens.</p> 
<p align="justify">Na secção abaixo, é possível observar alguns <i>screenshots</i> do resultado final:</p>

<p align="center"> <img src="screenshots\\Captura de ecrã 2024-03-08 171942.png"> </p>
<p align="center"><sup> Cabeçalho Introdutório </sup> </p>

<p align="center"> <img  src="screenshots\\Captura de ecrã 2024-03-08 172013.png"> </p>
<p align="center"><sup> Secção About Me </sup> </p>

<p align="center"> <img src="screenshots\\Captura de ecrã 2024-03-08 172122.png"> </p>
<p align="center"><sup> Introdução à técnica Pontilhismo </sup> </p>

<p align="center"> <img src="screenshots\\Captura de ecrã 2024-03-08 172148.png"> </p>
<p align="center"><sup> Desenhos e Descrição da técnica Pontilhismo </sup> </p>

<p align="center"> <img src="screenshots\\Captura de ecrã 2024-03-08 172217.png"> </p>
<p align="center"><sup> Secção dos desenhos a cores </sup> </p>

<p align="center"> <img src="screenshots\\Captura de ecrã 2024-03-08 172240.png"> </p>
<p align="center"><sup> Continuação da secção dos desenhos a cores </sup> </p>

<p align="center"> <img src="screenshots\\Captura de ecrã 2024-03-08 172308.png"> </p>
<p align="center"><sup> Secção das Inspirações </sup> </p>

<p align="center"> <img src="screenshots\\Captura de ecrã 2024-03-08 172336.png"> </p>
<p align="center"><sup> Continuação da secção das Inspirações </sup> </p>

<p align="center"> <img src="screenshots\\Captura de ecrã 2024-03-08 172354.png"> </p>
<p align="center"><sup> Parte final do documento </sup> </p>
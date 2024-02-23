### Trabalho de Casa 2
<p align="justify"> O tema deste segundo trabalho de casa diz respeito a <b>Expressões Regulares</b>, também conhecidas por <i>RegEx</i>, tendo por vista a implementação das suas diversas funções durante a resolução de 10 exercícios. </p>
 

<p align="justify"> Posto isto, no que concerne às alíneas <b>1.1 a 1.5</b>, a sua resolução revelou-se bastante simples dado que foi apenas necessária a implementação direta das funções <i>match, search, findall, sub </i> e <i>split</i>. </p>

<p align="justify"> No entanto, dado que as funções <i>match</i> e <i>search</i> apresentam um <i>output</i> do género:</p>
<p align="center"><i><b>'re.Match object; span=(0, 5), match='hello''</i></b></p>

 <p align="justify"> Procedi ao estabelecimento de uma função mais geral para ambas, <b><i>hello_match</b></i> e <b><i>hello_search</i></b>, de forma a ser fornecido um resultado mais simples para o utilizador. </p>

 <p align="justify">Assim, é retornado <i>True</i>, caso se verifique o pretendido, ou, caso contrário, <i>False</i>.</p>
 <p align="justify"> É importante notar que tal também poderia ser obtido através do uso do <i>print,</i> como: <i><b>'print("True" if re.match("hello", line1) else "False")'</i></b> Em contrapartida, esta consideração implica a escrita da mesma expressão para as restantes linhas de exemplo, isto é, <i>line2</i> e <i>line3</i>.</p>

<p align="justify"> Os restantes exercícios envolveram o desenvolvimento de funções, também de rápida resolução, onde tiveram de ser estabelecidos determinados padrões.</p>
 <p align="justify"> No que se refere a estes, penso que o correspondente ao <b>exercício 7</b> se revelou mais moroso, em termos de interpretação e determinação, contudo, no final, foi obtido o seguinte:
 <p align="center"><b><i>' r"^[a-z]\w*$"'.</b></i></p> 
 
 <p align="justify">- <b>r</b> trata-se de uma prática recomendada, pois garante que os padrões sejam interpretados corretamente;</p>
<p align="justify">- <b>^</b> assegura a obrigatoriedade do nome começar por uma letra que, quando se trata do nome de uma variável, deve ser minúscula; </p>
<p align="justify">- <b>*</b>
pois uma variável pode ser, muitas vezes, constituída por uma única letra ou, então, por mais letras, números, ou, ainda, <i>underscore (\w)</i>. </p>

<p align="justify">O raciocínio envolvido em ambos os exercícios <b>3</b> e <b>5</b> foi semelhante, uma vez que as listas, retornadas pelas funções <i>RegEx</i>, foram percorridas por um ciclo <i>for</i>. No primeiro, verifica-se um contador, por cada vez que se verifica a palavra "eu", e, no segundo, uma variável em que se vai somando o valor de cada um dos números.</p>

<p align="justify">Por último, dado que o enunciado do <b>exercício 10</b> estabelecia que a função a desenvolver recebe uma lista de códigos postais válidos, defini uma função a ter isso em conta.</p> 

<p align="justify">No entanto, caso esta interpretação não seja a correta, procedi à definição de uma outra função que implica a validação do número introduzido como código postal.</p> 
<p align="justify">O raciocínio envolveu percorrer cada elemento da lista, através de um ciclo <i>for</i>, pelo que, após verificação da sua validade, os elementos são divididos pelo hífen, através da função <i>split</i>. Tendo em conta a lista devolvida por esta função, o primeiro elemento desta (primeiros 4 dígitos) foi definido como primeiro elemento de um <b>tuplo</b>, e o segundo (últimos 3 dígitos), como segundo elemento do tuplo. Pode-se concluir, assim, que o resultado final é uma lista de pares, neste caso, de tuplos: <b>[('4700', '000'), ('1234', '567')] </b></p>

<p align="justify">No geral, considero que este TPC permitiu consolidar o papel que cada uma das funções <i>RegEx</i> desempenha, bem como colocar em prática a <i>syntax</i> das expressões em si.</p>
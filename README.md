<h2 align="center">P1 - Estrutura-de-Dados</h2>

<div align="center">
<img src="https://user-images.githubusercontent.com/47799542/227817195-8da4f449-55d6-42d4-a613-32d9047b6489.png" width="700px" />
</div>

<p align="center" >Universidade: Universidade de Vassouras</p>
<p align="center" >Curso de graduação: Engenharia de Software</p>
<p align="center" >Disciplina: Estrutura de Dados</p>
<p align="center" >Período: 3º período</p>
<p align="center" >Professor: Marcio Alexandre Dias Garrido</p>
<p align="center">Integrantes: João Vitor Figueiredo França, Tiago Monteiro Tertuliano da Silva, Cleyton de Carvalho Souza, Gabriel de Souza Lima, João Victor Lopes dos Santos</p>
<br>
<br>
<br>
<br>
<br>
<br>
<p> De acordo com o projeto 1, deveria ser criado um programa que não apenas faz a leitura dos itens dentro de uma lista apresentada, mas também que os organiza em ordem crescente e decrescente, imprimindo logo em seguida a notação Big'O do resultado de forma gráfica.</p>
<p> Conforme o desafio proposto, foi feito um algoritmo que organiza os elementos das listas apresentadas em ordem crescente e decrescente, em seguida, plota tudo em um gráfico com o a notação Big'O do resutaldo em evidência. Para isso, utilizamos duas bibliotecas, sendo elas a "Time" para a cronometragem do tempo de abertura do código e a "matplotlib" para a impressão do gráfico.</p>
<div align="center">
<img src="https://user-images.githubusercontent.com/47799542/227818451-62e8f927-1dfe-4a10-8e64-34d05310ee22.png" width="700px" />
</div>
<p> Em seguida, pegamos a lista apresentada com todas as sublistas e adicionamos ao código, criando outra lista que receberia o valor de todas as sublistas somadas, o que as juntaria em apenas uma.</p>
<div align="center">
<img src="https://user-images.githubusercontent.com/47799542/227819033-68dc4428-cd8d-4982-a7ee-460117fc5ebe.png" width="700px" />
</div>
<p>Após termos todos os valores juntos em um só lugar, criamos três listas vazias, sendo elas: "lista_crescente", "lista_decrescente" e "Tempos" para armazenarem os valores. Logo após abrirmos o "For", utilizamos a variável "start" que recebe o comando "time.perf_counter()" para iniciar a cronometragem do programa. Após isso, preenchemos essas listas usando o "elementos2.sort()" para ordenar a lista em ordem crescente e "elementos2.sort(reverse=True)" para ordenar em ordem decrescente, sempre utilizando o ".append" para enviar os valores as respectivas listas. Por gim, fechamos com a variável "End" que recebe o "time.perf_counter()" para encerrar a contagem. Fazemos o cálculo e adicionamos a lista vazia usando o .append, concluindo a montagem dos valores.</p>
<div align="center">
<img src="https://user-images.githubusercontent.com/47799542/227820144-3eea8d44-2d2b-470d-92d9-94479034c2aa.png" width="700px" />
</div>
<p>Finalizamos o programa chamando as listas dentro dos códigos de abertura do gráfico usando a biblioteca "matplotlib" com alguns textos para descrever as posições da tabela.</p>
<div align="center">
<img src="https://user-images.githubusercontent.com/47799542/227820831-93f073c1-9ed6-4ad4-a3c9-b0825af1ed27.png" width="700px" />
</div>

nome = input("qual e o seu nome: ") # input = é uma função integrada em Python que permite ao programa receber dados do usuário por meio do teclado. O texto dentro dos parênteses é exibido como um prompt para o usuário, indicando o que ele deve digitar. O valor digitado pelo usuário é então armazenado na variável "nome".
  print (f"seu nome e {nome}")
print("nome") # print = é uma função integrada em Python que exibe informações na tela. Ela pode ser usada para mostrar texto, variáveis ou resultados de expressões. O conteúdo a ser exibido é colocado entre parênteses e pode ser formatado usando f-strings para incluir variáveis de forma mais legível.
# O código acima é um exemplo de como usar a função input para receber o nome do usuário e, em seguida, exibir o nome usando a função print. O programa solicitará ao usuário que digite seu nome, armazenará esse valor na variável "nome" e, em seguida, exibirá uma mensagem formatada com o nome do usuário.

ano_nascimento = int(input("fala a do seu ano de nacimento seu: ")) # int(input = serve para ler uma entrada de texto do usuário (console) e convertê-la imediatamente em um número inteiro
  ano_atual = 2026
idade = ano_atual - ano_nascimento
  print(f"a sou idade e {idade} anos e agora eu sei onde vc mora.")
# O código acima é um exemplo de como usar a função input para receber o ano de nascimento do usuário, convertê-lo para um inteiro usando a função int, calcular a idade com base no ano atual e exibir o resultado formatado usando f-strings. O programa solicitará ao usuário que digite seu ano de nascimento, calculará a idade e exibirá uma mensagem informando a idade do usuário.

notas = [999, 9, 99, 9] # nota = um tipo de variavel
  media = sum(notas) / len(notas) # sum = de somar elementos / len  é um método integrado utilizado para retornar o número de itens
print(f"media é: {media:.2f}") # 2 = sumeros da soma / f = Permite que o Python interprete o que está dentro das chave
# O código acima é um exemplo de como calcular a média de uma lista de notas usando as funções sum e len. A função sum é usada para somar todos os elementos da lista "notas", enquanto a função len é usada para contar o número de elementos na lista. O resultado da média é formatado para exibir apenas duas casas decimais usando f-strings.

numero1 = input("digute o numero") # input =  receber dados inseridos pelo usuário via teclado
  numero2 = int(numero1) # int() = é uma função integrada em Python que converte um valor para um número inteiro. Ela pode ser usada para converter strings que representam números em inteiros, ou para converter outros tipos de dados em inteiros, se possível. Se a conversão não for possível, a função lançará um erro.
print(numero2*2) # numero1 = a variável que armazena a entrada do usuário como uma string (texto)
# O código acima é um exemplo de como usar a função input para receber um número do usuário, convertê-lo para um inteiro usando a função int e, em seguida, multiplicar esse número por 2 antes de exibir o resultado. O programa solicitará ao usuário que digite um número, realizará a conversão e exibirá o dobro desse número na tela.

numero3 = int(input("digite outro numero seu"))
  numero4 = int(input("digite outro numero seu"))
soma = numero3 + numero4
  print(f"a soma dos numeros e: {soma}") # soma = o processo de adicionar dois ou mais números para obter um resultado total, conhecido como soma. A soma é uma operação matemática fundamental que envolve a combinação de valores para encontrar um total.
# O código acima é um exemplo de como usar a função input para receber dois números do usuário, convertê-los para inteiros usando a função int, realizar a operação de soma e exibir o resultado formatado usando f-strings. O programa solicitará ao usuário que digite dois números, calculará a soma desses números e exibirá o resultado na tela.

numero5 = int(input("digite outro numero seu"))
  numero6 = int(input("digite outro numero seu"))
subtracao = numero5 - numero6
  print(f"a subtração dos numeros e: {subtracao}") # subtração = o processo de encontrar a diferença entre dois números, onde um número é subtraído do outro. O resultado da subtração é chamado de diferença.
 # O código acima é um exemplo de como usar a estrutura de controle de fluxo if-else para verificar se uma pessoa é maior ou menor de idade com base na variável "idade". Se a idade for maior ou igual a 18, o programa imprimirá "vc e maior de idade". Caso contrário, ele imprimirá "vc e menor de idade".

if idade >= 18: # if = é uma estrutura de controle de fluxo em Python que permite executar um bloco de código apenas se uma condição específica for verdadeira. A sintaxe básica do if é: if condição: bloco de código. O bloco de código dentro do if será executado somente se a condição for avaliada como verdadeira.
    print("vc e maior de idade") # print = é uma função integrada em Python que exibe informações na tela. Ela pode ser usada para mostrar texto, variáveis ou resultados de expressões. O conteúdo a ser exibido é colocado entre parênteses e pode ser formatado usando f-strings para incluir variáveis de forma mais legível.
else: # else = é uma parte opcional de uma estrutura de controle de fluxo em Python que é executada quando a condição do if é avaliada como falsa. A sintaxe básica do else é: else: bloco de código. O bloco de código dentro do else será executado somente se a condição do if for falsa.
    print("vc e menor de idade") # print = é uma função integrada em Python que exibe informações na tela. Ela pode ser usada para mostrar texto, variáveis ou resultados de expressões. O conteúdo a ser exibido é colocado entre parênteses e pode ser formatado usando f-strings para incluir variáveis de forma mais legível.
  # O código acima é um exemplo de como usar a estrutura de controle de fluxo if-else para verificar se uma pessoa é maior ou menor de idade com base na variável "idade". Se a idade for maior ou igual a 18, o programa imprimirá "vc e maior de idade". Caso contrário, ele imprimirá "vc e menor de idade".
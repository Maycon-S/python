nome = input("qual e o seu nome: ") # input = é uma função integrada em Python que permite ao programa receber dados do usuário por meio do teclado. O texto dentro dos parênteses é exibido como um prompt para o usuário, indicando o que ele deve digitar. O valor digitado pelo usuário é então armazenado na variável "nome".
  print (f"seu nome e {nome}")
print("nome") # print = é uma função integrada em Python que exibe informações na tela. Ela pode ser usada para mostrar texto, variáveis ou resultados de expressões. O conteúdo a ser exibido é colocado entre parênteses e pode ser formatado usando f-strings para incluir variáveis de forma mais legível.
# O código acima é um exemplo de como usar a função input para receber o nome do usuário e, em seguida, exibir o nome usando a função print. O programa solicitará ao usuário que digite seu nome, armazenará esse valor na variável "nome" e, em seguida, exibirá uma mensagem formatada com o nome do usuário.

# semana 1

ano_nascimento = int(input("fala a do seu ano de nacimento seu: ")) # int(input = serve para ler uma entrada de texto do usuário (console) e convertê-la imediatamente em um número inteiro
  ano_atual = 2026
idade = ano_atual - ano_nascimento
  print(f"a sou idade e {idade} anos e agora eu sei onde vc mora.")
# O código acima é um exemplo de como usar a função input para receber o ano de nascimento do usuário, convertê-lo para um inteiro usando a função int, calcular a idade com base no ano atual e exibir o resultado formatado usando f-strings. O programa solicitará ao usuário que digite seu ano de nascimento, calculará a idade e exibirá uma mensagem informando a idade do usuário.


notas = [999, 9, 99, 9] # nota = um tipo de variavel
  media = sum(notas) / len(notas) # sum = de somar elementos / len  é um método integrado utilizado para retornar o número de itens
print(f"media é: {media:.2f}") # 2 = sumeros da soma / f = Permite que o Python interprete o que está dentro das chave
# O código acima é um exemplo de como calcular a média de uma lista de notas usando as funções sum e len. A função sum é usada para somar todos os elementos da lista "notas", enquanto a função len é usada para contar o número de elementos na lista. O resultado da média é formatado para exibir apenas duas casas decimais usando f-strings.



numero1 = input("digite o numero") # input =  receber dados inseridos pelo usuário via teclado
  numero2 = int(numero1) # int() = é uma função integrada em Python que converte um valor para um número inteiro. Ela pode ser usada para converter strings que representam números em inteiros, ou para converter outros tipos de dados em inteiros, se possível. Se a conversão não for possível, a função lançará um erro.
print(numero2*2) # numero1 = a variável que armazena a entrada do usuário como uma string (texto)
# O código acima é um exemplo de como usar a função input para receber um número do usuário, convertê-lo para um inteiro usando a função int e, em seguida, multiplicar esse número por 2 antes de exibir o resultado. O programa solicitará ao usuário que digite um número, realizará a conversão e exibirá o dobro desse número na tela.

# semana 2

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
  
# semana 3 a 5

sim ou não = input("vc e um robo sim ou não?")
if sim ou não == "sim":
    print("vc ta de brincadeira comigo?")
else:
    print("vc não e um robo")

nota = float(input('Qual é a sua nota: '))

if 6 <= nota <= 10:
    print("Aprovado")
elif 0 <= nota < 6:
    print("Reprovado")
else:
    print("Nota inválida :(")


numero = int(input("Digite um número: "))

if numero % 2 == 0: # O operador % é o operador de módulo em Python, que retorna o resto da divisão entre dois números. No caso do código, ele está sendo usado para verificar se o número digitado pelo usuário é par ou ímpar. Se o resultado da operação numero % 2 for igual a 0, significa que o número é par, caso contrário, é ímpar.
    print(f"{numero} é par")
else:
    print(f"{numero} é ímpar")
    

def comparar_precos(): # def = é uma palavra-chave em Python usada para definir uma função. Ela é seguida pelo nome da função e parênteses, que podem conter parâmetros. O bloco de código dentro da função é indentado e será executado quando a função for chamada. As funções são usadas para organizar o código em blocos reutilizáveis, permitindo que você execute um conjunto de instruções várias vezes sem precisar reescrever o código. 
    preco1 = float(input(f"Preço do produto1 na Loja A: R$ "))

    preco2 = float(input(f"Preço do produto2 na Loja B: R$ "))

    if preco1 < preco2:
        print(f"\n A Loja A está mais barata: produto1 por R$ {preco1:.2f}")
    elif preco2 < preco1: # elif = é uma estrutura de controle de fluxo em Python que permite verificar múltiplas condições sequencialmente. Ele é usado para testar uma condição adicional se a condição anterior for falsa. A sintaxe básica do elif é: elif condição: bloco de código. O bloco de código dentro do elif será executado somente se a condição do if e todas as condições anteriores forem avaliadas como falsas.
        print(f"\n A Loja B está mais barata: produto2 por R$ {preco2:.2f}")
    else:
        print("\n🤝 Os preços são iguais!")

comparar_precos()



preco = float(input("Digite o preço do produto: R$ "))
desconto = preco * 0.10  # Calcula 10% de desconto * O valor do desconto é obtido multiplicando o preço original por 0.10, que representa 10% em forma decimal.
preco_final = preco - desconto

print(f"O produto custa R${preco:.2f}, com 10% de desconto fica R${preco_final:.2f}")
# O código acima é um exemplo de como calcular o preço final de um produto após aplicar um desconto de 10%. O programa solicita ao usuário que digite o preço do produto, calcula o valor do desconto multiplicando o preço por 0.10 (que representa 10%), subtrai o desconto do preço original para obter o preço final e, em seguida, exibe o resultado formatado usando f-strings para mostrar os valores com duas casas decimais.


# semana 6

 if idade >= 18: # if = é uma estrutura de controle de fluxo em Python que permite executar um bloco de código apenas se uma condição específica for verdadeira. A sintaxe básica do if é: if condição: bloco de código. O bloco de código dentro do if será executado somente se a condição for avaliada como verdadeira.
    print("vc e maior de idade") # print = é uma função integrada em Python que exibe informações na tela. Ela pode ser usada para mostrar texto, variáveis ou resultados de expressões. O conteúdo a ser exibido é colocado entre parênteses e pode ser formatado usando f-strings para incluir variáveis de forma mais legível.
    elif idade < 18: # elif = é uma estrutura de controle de fluxo em Python que permite verificar múltiplas condições sequencialmente. Ele é usado para testar uma condição adicional se a condição anterior for falsa. A sintaxe básica do elif é: elif condição: bloco de código. O bloco de código dentro do elif será executado somente se a condição do if e todas as condições anteriores forem avaliadas como falsas.
    print("vc e menor de idade") # print = é uma função integrada em Python que
    else: # else = é uma parte opcional de uma estrutura de controle de fluxo em Python que é executada quando a condição do if é avaliada como falsa. A sintaxe básica do else é: else: bloco de código. O bloco de código dentro do else será executado somente se a condição do if for falsa.
    print("") # print = é uma função integrada em Python que ex

# semana 7


if senha == senha_confirmacao: # if = é uma estrutura de controle de fluxo em Python que permite executar um bloco de código apenas se uma condição específica for verdadeira. A sintaxe básica do if é: if condição: bloco de código. O bloco de código dentro do if será executado somente se a condição for avaliada como verdadeira.
 print("senha confirmada com sucesso") # if = é uma estrutura de controle de fluxo em Python que permite executar um bloco de código apenas se uma condição específica for verdadeira. A sintaxe básica do if é: if condição: bloco de código. O bloco de código dentro do if será executado somente se a condição for avaliada como verdadeira.
 
## == é um operador de comparação em Python que verifica se dois valores são iguais. Ele retorna True se os valores forem iguais e False caso contrário. Por exemplo, se você quiser verificar se a variável "senha" é igual à variável "senha_confirmacao", você escreveria "senha == senha_confirmacao". O operador de igualdade é comumente usado em estruturas de controle de fluxo, como if statements, para tomar decisões com base na comparação de valores.
# O código acima é um exemplo de como usar a estrutura de controle de fluxo if para verificar se a senha digitada pelo usuário é igual à senha de confirmação. Se as senhas forem iguais, o programa imprimirá "senha confirmada com sucesso". Caso contrário, ele não fará nada (ou você pode adicionar um else para lidar com o caso em que as senhas não correspondem).
# () [] {} = são símbolos usados em Python para diferentes propósitos. Os parênteses () são usados para agrupar expressões, definir tuplas e chamar funções. Os colchetes [] são usados para definir listas, acessar elementos de listas e criar compreensões de listas. As chaves {} são usadas para definir dicionários, conjuntos e criar compreensões de dicionários. Cada um desses símbolos tem um papel específico na sintaxe do Python e é importante usá-los corretamente para evitar erros de sintaxe.
# . = é um operador de acesso a atributos em Python. Ele é usado para acessar métodos, atributos ou propriedades de um objeto. Por exemplo, se você tiver um objeto chamado "objeto" e quiser acessar um método chamado "metodo", você usaria a sintaxe "objeto.metodo()". O ponto é essencial para indicar que você está acessando algo relacionado ao objeto específico.
# : = é um símbolo usado em Python para indicar o início de um bloco de código
# , = é um símbolo usado em Python para separar elementos em uma lista, tupla, dicionário ou outros tipos de dados compostos. Ele é usado para indicar que os elementos estão separados e pertencem ao mesmo conjunto. Por exemplo, em uma lista, você pode usar vírgulas para separar os itens: [1, 2, 3]. Em um dicionário, as vírgulas são usadas para separar as chaves e valores: {"chave1": "valor1", "chave2": "valor2"}. O uso correto da vírgula é importante para garantir a sintaxe correta do código e evitar erros de interpretação.
# = é um símbolo usado em Python para atribuir um valor a uma variável. Ele é usado para indicar que o valor à direita do símbolo deve ser armazenado na variável à esquerda. Por exemplo, se você quiser atribuir o valor 10 a uma variável chamada "x", você escreveria "x = 10". O símbolo de igual é fundamental para a atribuição de valores em Python e é amplamente utilizado em todo o código para criar e modificar variáveis.
# == é um operador de comparação em Python que verifica se dois valores são iguais. Ele retorna True se os valores forem iguais e False caso contrário. Por exemplo, se você quiser verificar se a variável "a" é igual a 5, você escreveria "a == 5". O operador de igualdade é comumente usado em estruturas de controle de fluxo, como if statements, para tomar decisões com base na comparação de valores.

# semanha 8

# bloco de nota v1

notas = [] # notas = um tipo de variavel
for i in range(4): # for = é uma estrutura de controle de fluxo em Python
    nota = float(input(f"Digite a nota {i + 1}: ")) # input = é uma função integrada em Python que permite ao programa receber dados do usuário por meio do teclado. O texto dentro dos parênteses é exibido como um prompt para o usuário, indicando o que ele deve digitar. O valor digitado pelo usuário é então armazenado na variável "nota". / float() = é uma função integrada em Python que converte um valor para um número de ponto flutuante (decimal). Ela pode ser usada para converter strings que representam números em ponto flutuante, ou para converter outros tipos de dados em ponto flutuante, se possível. Se a conversão não for possível, a função lançará um erro.
    notas.append(nota) # append() = é um método de lista em Python que adiciona um elemento ao final da lista. Ele é usado para expandir a lista com novos itens. Por exemplo, se você tiver uma lista chamada "notas" e quiser adicionar uma nova nota a essa lista, você usaria "notas.append(nota)". O método append é útil para construir listas dinamicamente à medida que você recebe novos dados ou deseja adicionar elementos a uma lista existente.
media = sum(notas) / len(notas) # sum = de somar elementos / len  é um método integrado utilizado para retornar o número de itens
print(f"A média das notas é: {media:.2f}") # 2 = sumeros da soma / f = Permite que o Python interprete o que está dentro das chave
# O código acima é um exemplo de como calcular a média de uma lista de notas usando as funções sum e len. A função sum é usada para somar todos os elementos da lista "notas", enquanto a função len é usada para contar o número de elementos na lista. O resultado da média é formatado para exibir apenas duas casas decimais usando f-strings. O programa solicitará ao usuário que digite quatro notas, armazenará essas notas em uma lista, calculará a média e exibirá o resultado na tela.

# bloco de nota v2

?/
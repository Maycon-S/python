nome = input("qual e a porra do seu nome: ") # input = é uma função integrada em Python que permite ao programa receber dados do usuário por meio do teclado. O texto dentro dos parênteses é exibido como um prompt para o usuário, indicando o que ele deve digitar. O valor digitado pelo usuário é então armazenado na variável "nome".
print (f"seu nome e {nome}")
print("nome") # print = é uma função integrada em Python que exibe informações na tela. Ela pode ser usada para mostrar texto, variáveis ou resultados de expressões. O conteúdo a ser exibido é colocado entre parênteses e pode ser formatado usando f-strings para incluir variáveis de forma mais legível.

ano_nascimento = int(input("fala a porra do seu ano de nacimento seu lixo")) # int(input = serve para ler uma entrada de texto do usuário (console) e convertê-la imediatamente em um número inteiro
ano_atual = 2026
idade = ano_atual - ano_nascimento
print(f"a sou idade e {idade} anos e agora eu sei onde vc mora.")

notas = [999, 9, 99, 9] # nota = um tipo de variavel
media = sum(notas) / len(notas) # sum = de somar elementos / len  é um método integrado utilizado para retornar o número de itens
print(f"media é: {media:.2f}") # 2 = sumeros da soma / f = Permite que o Python interprete o que está dentro das chave

numero1 = input("digute a porra do numero") # input =  receber dados inseridos pelo usuário via teclado
numero2 = int(numero1) # int = para representar e manipular números inteiros
print(numero2*2) # numero1 = a variável que armazena a entrada do usuário como uma string (texto)

numero3 = int(input("digite outro numero seu"))
numero4 = int(input("digite outro numero seu"))
soma = numero3 + numero4
print(f"a soma dos numeros e: {soma}") # soma = o processo de adicionar dois ou mais números para obter um resultado total, conhecido como soma. A soma é uma operação matemática fundamental que envolve a combinação de valores para encontrar um total.

numero5 = int(input("digite outro numero seu"))
numero6 = int(input("digite outro numero seu"))
subtracao = numero5 - numero6
print(f"a subtração dos numeros e: {subtracao}") # subtração = o processo de encontrar a diferença entre dois números, onde um número é subtraído do outro. O resultado da subtração é chamado de diferença.

ss
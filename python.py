nome = input("qual e a porra do seu nome: ")
print (f"seu nome e {nome}")
print("nome")

ano_nascimento = int(input("fala a porra do seu ano de nacimento seu lixo")) # int(input = serve para ler uma entrada de texto do usuário (console) e convertê-la imediatamente em um número inteiro
ano_atual = 2026
idade = ano_atual - ano_nascimento
print(f"a sou idade e {idade} anos e agora eu sei onde vc mora.")

notas = [999, 9, 99, 9] # nota = um tipo de variavel
media = sum(notas) / len(notas) # sum = de somar elementos / len  é um método integrado utilizado para retornar o número de itens
print(f"media é: {media:.2f}") # 2 = sumeros da soma / f = Permite que o Python interprete o que está dentro das chave

numero1 = input("digute a porra do numero") # input =  receber dados inseridos pelo usuário via teclado
numero2 = int(numero1) # int = para representar e manipular números inteiros
print(numero2*2)

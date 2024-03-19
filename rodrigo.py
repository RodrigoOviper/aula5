#11/03/2024

olá = "Olá"
nome = "Sammy Davis"
dia = 11
mês = "abril"
ano = 1981
quando = "você nasceu"
de = "de"
# print(olá,nome,quando,dia,mês,ano)

#print(12, 45)
#print(12, 45, sep="/", end="")
#print(12, 45, sep="/", end=".")
#print(1, 2, sep="", end="")
#print(3, 4, sep="", end="")
#print("*"*30)
#print("calculadora")
#print("Olá, mundo!", "135", "fila")

# CONDICIONAIS.
# 1) if (se)
# 2) else (então)
# 3) elif (else + if) (sendo)
#
#
# # exemplo
# informação_usuário = str((input("Você deseja "Entrar" ou "Sair" do programa?"))
#
# if informação_usuário == "Entrar":
# print("Sistema acessado com sucesso!")
# else:
# print("Você não acessou o sistema!")


#Novo Exemplo

# entrada_usuário = str(input('Digite "E" para entrar' ' ou "S" para sair:'))
# if entrada_usuário == "E":
#     print("Bem vindo ao sistema!")
# elif entrada_usuário =="S":
#     print("Você saiu do sistema!")
# else:
#     print('Você não digitou nem "E" e nem "S".')

"""
Operadores Relacionais ou de comparação.

1) igual : ==
2) maior: >
3) menor: <
4) maior ou igual: >=
5) menor ou igual: <=
6) diferente: !=

"""

# Igual
#igual = "a" == "a"
#print(igual)

# Maior
#maior = 2 > 1
#print(maior)

# Menor
#menor = 50 < 30
#print(menor)

# Maior ou igual
#maior_ou_igual = 1 > 2
#print(maior_ou_igual)

# Diferente
#diferente = 1 != 1
#print(diferente)

"""
Operadores lógicos
e (and)
X (True) anda Y (False) = False 
X (False) and Y (True) = False
X (False) and Y (False) = False
X (True) and Y (True) = True


OU (or)
X (True) or Y (False) = True
X (False) or Y (True) = True
X (True) or Y (True) = True
X (False) or Y (False) = False


Negação (not)
X (True) not X = False
X (False) not X = True
"""

# E = and
#x = True
#y = True
#resultado = x and y
# print(resultado)

# ou = or
# x = True
# y = True
# resultado = x or y
# print(resultado)

# not = not
# x = False
# x1 = not x
# resultado = x not x1
#print(resultado)
#
# # exercícios:
# """
# 1) Faça um programa que peça a temperatura em graus Celsius, transforme e mostre em graus Fahrenheit!
# """
#
# Temperatura_graus_celsius = int(input("digite a temperatura em graus celsius:"))
# Transformação = (temperatura_graus_celsius * (9/5)) + 32
# print("a temperatura em graus fahrenheit é: " transformação "F")
#
#
# # """
# # 2) Faça um programa que peça as 4 notas bimestrais a mostre a média.
#  """

#nota1 = float(input("digite a nota 1: "))
#nota2 = float(input("digite a nota 2: "))
#nota3 = float(input("digite a nota 3: "))
#nota4 = float(input("digite a nota 4: "))
#média = (nota1 + nota2, nota3, nota4) / 4
#print(" a sua média bimestral é: ".média)




#
#
#
#
# """
# 3) faça um programa com o cálculo do IMC de uma pessoa e confirme se a relação está no peso ideal, abaixo ou acima.
# """
#
# "IMC saudável = 18,5 and 24,9"
# "ICM sobrepeso = 25 and 29,5"
# "IMC obeso = 30 and 34,9"
#
#
#
#
#
#
#
#
# """
# 4) Faça um programa que o peça 2 números e diga o qual é o maior.
# """
#
# "numero 15 = 15"
# "numero 35 = 35"
#
#
#
#
# """
# 5) Faça um programa que peça um número e diga se ele é positivo ou negativo.
# """
#
# "numero "
#
#
#
# Temperatura_graus_celsius = int(input("digite a temperatura em graus celsius:"))
# Temperatura_graus_celsius = (Temperatura_graus_celsius * 1.8) + 32
# print("a temperatura é", Temperatura_graus_celsius)
# nota1 = float(input("digite a nota1"))
# nota2 = float(input("digite a nota2"))
# nota3 = float(input("digite a nota3"))
# nota4 = float(input("digite a nota4"))
# media = (nota1 + nota2 + nota3 + nota4) / 4
# print("a sua media final é", media)
# if media>=6:
#     print("voce está aprovado")
# else :
#     print("nao foi dessa vez")

#Exercicio 3

# Faça um Programa que calcule o IMC da pessoa e passe a seguinte informação
#
# Se o IMC for maior que 25

# potenciação **
# peso = float(input("digite o seu peso"))
# altura = float(input("digite a sua altura"))
# imc = peso / altura**2
# print(imc)
# if imc<= 18.4:
#  print("voce esta abaixo do peso")
# elif imc >= 18.5 and imc <= 24.9:
#     print("voce esta no peso normal")
# elif imc>= 25.0 and imc<= 29.9:
#     print("voce está em sobrepeso")
# else:
#  print ("voce está com obsidade mórbida")

# "diga qual é o maior numero"
#
# numero1 = int(input("digite um numero qualquer:"))
# numero2 = int(input("digite um numero qualquer"))
# if numero1> numero2:
#  print("o numero", numero1,"é maior queo", numero2)
# elif numero1< numero2:
#     print("o numero", numero1, "é menor que o numero", numero2)
# else :
#     print("os numeros sao iguais")

#Peça para o usuario um numero e informe se ele é positivo ou negativo
#
# numero = float(input("digite um numero"))
# if numero>=0
#     print("o numero é positivo")
# elif numero == 0:
#     print("o numero é igual a zero")
# else:
#     print ("o numero é negativo")

"""
Desenvolva um programa que calcule o reajuste salarial do funcionário

1) salário de até 2.000 até 20%
2) salário entre 2.000 e 3,500 aumento de 15%
3) salário entre 3,500 e 5,000 aumento de 15%
4) salário maior que 5.000 5%

o que o programa deseja buscar ?

salário atual
percentual de aumento
valor R$ de aumento
novo salário  incluindo aumento

codedwars
"""
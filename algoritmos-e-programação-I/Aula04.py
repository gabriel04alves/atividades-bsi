# 1) Inicializar um vetor de inteiros com números de 0 a 99.
array = []
print(f'Array no início: {array}')
for i in range(0, 100): 
  array.append(i)
print(f'Array no final: {array}')


# 2) Escreva um algoritmo que leia um conjunto de 10 notas, armazene-as em uma variável
# composta chamada NOTA e calcule e imprima a sua média.
notas = []
for i in range(0,10):
  notas.append(float(input(f'Informe a nota {i+1}: ')))
print(f'Notas:{notas} \nMédia das notas: {(sum(notas)/len(notas)):.2f}')


# 3) Repita o algoritmo acima, porém imprima quantos valores estão acima da média.
notas = []
acimaDaMedia = []
for i in range(0,10):
  nota = float(input(f'Informe a nota {i+1}: '))
  notas.append(nota)
  if nota >= 7.00:
    acimaDaMedia.append(nota)
print(f'\nNotas:{notas} \nMédia das notas: {(sum(notas)/len(notas)):.2f}')
print(f'\n{len(acimaDaMedia)} valores são acima da média(7.00).')


# 4) Faça um algoritmo que leia um vetor que contém as notas de 30 alunos. Imprima o maior
# valor, o menor valor, a média da turma e a quantidade de notas abaixo da média.
numNotas = int(input('Informe a quantidade de notas: '))
notas = []
abaixoDaMedia = []
for i in range(0,numNotas): 
  nota = float(input(f'Informa a nota {i+1}: '))
  notas.append(nota)
  if nota < 7:
    abaixoDaMedia.append(nota)
print(f'\nO maior valor é {max(notas)};')
print(f'O menor valor é {min(notas)};')
print(f'A média das notas é {(sum(notas)/len(notas)):.2f};')
print(f'{len(abaixoDaMedia)} notas são abaixo da média.')


# 5) Ler um vetor de 100 elementos numéricos e verificar se existem elementos iguais a 30. Se
# existirem, escrever as posições em que estão armazenados.
from random import *
vetor = []
trinta = []
for i in range(0,100):
  num = randrange(0,100)
  vetor.append(num)
  if num == 30:
    trinta.append(num)
print(f'\nExistem {len(trinta)} elementos iguais a 30.')
print(f'Vetor: {vetor}.')


# 6) Fazer um algoritmo que calcule e escreva o somatório dos valores armazenados numa variável
# composta unidimensional (vetor) A, de 100 elementos numéricos a serem lidos do dispositivo
# de entrada.
from random import *
vetor = []
for i in range(0,100):
  num = randrange(0, 100000)
  vetor.append(num)
print(f'\nSoma dos elementos {sum(vetor)}')
print(f'Vetor: {vetor}.')


# 7) Escreva um algoritmo que leia um vetor de 200 valores numéricos reais e os imprima na
# ordem contrária em que foi lida.
from random import *
vetor = []
for i in range(0,200):
  num = randrange(0, 100000)
  vetor.append(num)
print(f'\nVetores: {vetor}.')
vetor.reverse()
print(f'Vetores ao contrario: {vetor}.')


# 8) Escreva um algoritmo para fazer a soma de dois vetores de 10 elementos reais lidos do
# teclado. O primeiro elemento do primeiro vetor deverá ser adicionado ao primeiro elemento do
# segundo vetor e, o resultado deverá ser acumulado em um terceiro vetor também de 10
# elementos. Imprimir os três vetores conforme layout de impressão abaixo:
# VETOR 1: __ __ __ __ __ __ __ __ __ __
# VETOR 2: __ __ __ __ __ __ __ __ __ __
# VETOR 3: __ __ __ __ __ __ __ __ __ __
vetor1 = []
vetor2 = []
vetor3 = []
for i in range(0, 10):
  vetor1.append(randrange(0, 100))
for i in range(0, 10):
  vetor2.append(randrange(0, 100))
for i in range(0, 10):
  vetor3.append(vetor1[i]+vetor2[i])
print(f"Vetor 1: {vetor1}")
print(f"Vetor 2: {vetor2}") 
print(f"Vetor 3: {vetor3}")


# 9) Fazer um algoritmo que:
# a) Leia duas variáveis compostas unidimensionais, contendo, cada uma, 25 elementos numéricos;
# b) intercale os elementos desses dois conjuntos formando uma nova variável composta
# unidimensional de 50 elementos;
# c) Escreva o resultado obtido.
from random import *
vetor1 = []
vetor2 = []
somaVetores = []
for i in range(0, 25):
  vetor1.append(randrange(0, 100))
for i in range(0, 25):
  vetor2.append(randrange(0, 100))
print(f'Vetores 1 e 2: {vetor1 + vetor2}.')
print(f'\nVetor 1: {vetor1};')
print(f'Vetor 2: {vetor2};')
for i in range(0, 25):
  somaVetores.append(vetor1[i] + vetor2[i]) 
print(f'\nVetor 1 + vetor 2: {somaVetores}.')


# 10) Escreva um algoritmo que:
# a) leia 100 valores numéricos e os armazene numa variável composta unidimensional A;
# b) calcule e escreva: S =  99∑i=0 i/aᵢ, onde ai é o i-ésimo valor armazenado na variável A;
# c) calcule e escreva quantos termos da série acima têm o numerador menor do que o
# denominador.



# 11) Faça um algoritmo que leia um conjunto de 10 elementos reais e os coloque em um vetor.
# Construa um segundo vetor formado da seguinte maneira:
# • Os elementos de ordem par são os correspondentes do primeiro vetor multiplicados por 3.
# • Os elementos de ordem ímpar são os correspondentes do primeiro vetor divididos por 2.
# • Imprima os dois vetores.
from random import *
vetor1 = []
vetor2 = []
for i in range(0, 10):
  vetor1.append(randint(0,5000))
for i in range(len(vetor1)):
  if (i+1)%2 == 0:
    vetor2.append(vetor1[i]*3)
  else: vetor2.append(vetor1[i]/2)
print(f'Vetor 1: {vetor1}; \nVetor 2: {vetor2}.')



# 12) Escreva um algoritmo que:
# a) leia um conjunto A de 20 elementos a partir de uma unidade de entrada;
# b) calcule e imprima o valor de S, onde:
# S = (A[0] - A[19])² + (A[1] - A[18])² + ... + (A[9] - A[10])²



# 13) Escreva um algoritmo que:
# a) leia uma frase de 50 caracteres;
# b) conte quantos brancos existem na frase;
# c) conte quantas vezes a letra “A” aparece;
# d) imprima o que foi calculado nos itens b e c.
limiteCaracteres = 50
frase = ''
branco = 0
A = 0
while True:
    frase = input(f'Digite algo (limite de {limiteCaracteres} caracteres): '.format(limiteCaracteres))
    if len(frase) <= limiteCaracteres:
        break
    else:
        print('A entrada excede o limite de caracteres. Tente novamente.')
for i in range(len(frase)):
  if frase[i] == ' ':
    branco += 1
  elif frase[i] == 'A' or frase[i] == 'a':
    A += 1
print(f'Frase: {frase};')
print(f'Tamanho da frase: {len(frase)};')
print(f'Espaços em branco: {branco};')
print(f'Letras "A": {A};')



# 14) Um armazém trabalha com 100 mercadorias diferentes identificadas pelos números inteiros de
# 0 a 99. O dono do armazém anota a quantidade de cada mercadoria vendida durante o mês.
# Ele tem uma tabela mensal que indica para cada mercadoria o preço de venda. Escreva o
# algoritmo para calcular o faturamento mensal do armazém, isto é:
# faturamento = 99∑i=0(quantidadeᵢ*preçoᵢ)
# As tabelas de preço e quantidade são fornecidas em dois vetores.



# 15) Classificar um vetor numérico VET de 20 elementos em ordem crescente.
from random import *
vetor = []
for i in range(0,20):
  vetor.append(randint(0,100))
print(f'Lista original: {vetor}')
print(f'Lista com elementos ordenados: {sorted(vetor)}')


# 16) Dado um vetor de 128 elementos, verificar se existe um elemento igual a K (chave) no vetor.
# Se existir, imprimir a posição onde foi encontrada a chave; se não; imprimir a mensagem:
# “CHAVE K NÃO ENCONTRADA”. O vetor A e a chave K são lidos a partir de uma unidade de
# entrada.
from random import *
import random
import string
vetor = []
chave = input('Digite a chave: ')
chaveQtd = 0
chavePosicao = []
for i in range(0,128):
  valor = random.choice(string.ascii_letters + string.digits)
  vetor.append(valor)
  if valor == chave:
    chaveQtd += 1
    chavePosicao.append(i+1) 
  else: continue
print(f'Vetor: {vetor}')
print(f'Chave: {chave} | Quantidade de chaves: {chaveQtd} | Posições da chave: {chavePosicao}')


# 17) Refaça o algoritmo acima otimizando-o usando uma técnica conhecida por Pesquisa Binária.
# Suponha primeiramente que o vetor já esteja ordenado. Procuramos então o elemento K
# dividindo o vetor em duas partes e testando em qual das duas partes ele deveria estar.
# Procede-se então, da mesma forma para a parte provável, e assim sucessivamente.
# Obs.: na pesquisa sequencial simples (problema 16), o número médio de comparações que
# devem ser feitas até encontrar a chave é N/2, onde N é o número de elementos do vetor. No
# nosso caso, no algoritmo 16, teríamos, em média, 128/2 = 64 comparações. Na pesquisa
# binária, o número máximo de comparações é log2N. Teríamos, então, log2128=7 comparações,
# no máximo.



# 18) Faça um algoritmo qualquer que leia uma matriz A de 15 linhas por 25 colunas e imprima o
# seu conteúdo.
import random
linhas = []
for i in range(0, 15):
  linha = []
  for x in range(0, 25):
    valor = random.randint(10,99)
    linha.append(valor)
  linhas.append(linha)
print(f'Matriz:')
for linha in linhas:
  for valor in linha: 
    print(valor, end=" | ")
  print('')


# 19) Dada uma matriz B, de 10 linhas por 20 colunas, escrever um algoritmo que calcula e imprima
# o somatório dos elementos da quinta linha.
import random
linhas = []
for i in range(0, 10):
  linha = []
  for x in range(0, 20):
    valor = random.randint(10,99)
    linha.append(valor)
  linhas.append(linha)
print(f'Soma dos elementos da 5° linha: {sum(linhas[4])}')
print(f'\nMatriz: ')
for linha in linhas:
  for valor in linha: 
    print(valor, end=" | ")
  print('')


# 20) Dada uma tabela de 4 x 5 elementos, calcular a soma de cada linha e a soma de todos os
# elementos.
import random
linhas = []
print(f'Matriz: ')
for i in range(0, 4):
  linha = []
  for x in range(0, 5):
    valor = random.randint(10,99)
    linha.append(valor)
  linhas.append(linha)
  for valor in linha: 
    print(valor, end=" | ")
  print('')
cont = 0
somaTudo = 0 
print()
for linha in linhas: 
  cont += 1
  somaTudo += sum(linha)
  print(f'Soma dos elementos da linha {cont}: {sum(linha)}')
print(f'\nSoma de todos os elementos: {somaTudo}')


# 21) Elabore um algoritmo que leia uma matriz 4 x 4 e escreva a matriz resultante após ter
# multiplicado os elementos da diagonal principal por uma constante k.
import random
constante = float(input('Digite a constante: '))
linhas = []
print(f'\nMatriz:')
for i in range(0, 4):
  linha = []
  for x in range(0, 4):
    valor = random.randint(10,99)
    linha.append(valor)
  linhas.append(linha)
for linha in linhas:
  for valor in linha: 
    print(valor, end=" | ")
  print('')
print(f'\nElementos da diagonal principal multiplicados por 5: ')
for i in range(4):
  linhas[i][i] *= constante
for linha in linhas:
  for valor in linha:
    print(f'{valor:.1f}', end=" | ")
  print('')


# 22) Escreva um algoritmo que:
# a) leia uma matriz quadrada 20 x 20 de elementos reais;
# b) divida cada elemento de uma linha da matriz pelo elemento da diagonal principal dessa linha;
# c) imprima a matriz assim modificada;
import random
linhas = []
for i in range(0, 20):
  linha = []
  for x in range(0, 20):
    valor = random.randint(10,99)
    linha.append(valor)
  linhas.append(linha)
print(f'\nMatriz: ')
for linha in linhas:
  for valor in linha: 
    print(valor, end=" | ")
  print('')
print('')
print(f'\nElementos divididos pelo valor da diagonal principal: ')
for i in range(20):
    diagonal = linhas[i][i]
    for z in range(20):
        linhas[i][z] /= diagonal
print('\nMatriz modificada:')
for linha in linhas:
    for valor in linha:
        print(f'{valor:.2f}', end=' | ')
    print('')


# 23) Faça um algoritmo que:
# a) leia uma matriz 10 x 10 de elementos inteiros;
# b) imprima essa matriz;
# c) calcule e imprima a soma dos elementos situados abaixo da diagonal principal da matriz,
# incluindo os elementos da própria diagonal principal.
import random
linhas = []
for i in range(0, 10):
  linha = []
  for x in range(0, 10):
    valor = random.randint(10,99)
    linha.append(valor)
  linhas.append(linha)
print(f'\nMatriz: ')
for linha in linhas:
  for valor in linha: 
    print(valor, end=" | ")
  print('')
print('')
soma = 0
for i in range(10):
    for z in range(10):
        if z <= i:
            soma += linhas[i][z]
print(f"Soma dos elementos abaixo da diagonal principal: {soma}")


# 24) Escreva um algoritmo que leia duas matrizes reais de dimensão 3 x 5, calcule e imprima a sua
# soma.
import random
linhas1 = []
print(f'Matriz 1: ')
for i in range(0, 3):
  linha1 = []
  for x in range(0, 5):
    valor1 = random.randint(10,99)
    linha1.append(valor1)
  linhas1.append(linha1)
  for valor1 in linha1:
    print(valor1, end=" | ")
  print('')
linhas2 = []
print(f'\nMatriz 2: ')
for i in range(0, 3):
  linha2 = []
  for x in range(0, 5):
    valor2 = random.randint(10,99)
    linha2.append(valor2)
  linhas2.append(linha2)
  for valor2 in linha2:
    print(valor2, end=" | ")
  print('')
linhasSoma = []
print(f'\nMatriz 1 + matriz 2: ')
for i in range(len(linhas1)):
  linhaSoma = []
  for j in range(len(linhas1[i])):
    valorSoma = linhas1[i][j] + linhas2[i][j]
    linhaSoma.append(valorSoma)
  linhasSoma.append(linhaSoma)
  for valorSoma in linhaSoma:
    print(valorSoma, end=" | ")
  print('')


# 25) Dada uma matriz MAT de 4 x 5 elementos, faça um algoritmo para somar os elementos de
# cada linha gerando o vetor SOMALINHA. Em seguida, somar os elementos do vetor SOMALINHA
# na variável TOTAL que deve ser impressa no final.
import random
somalinha = []
linhas = []
print(f'Matriz: ')
for i in range(0, 4):
  linha = []
  for x in range(0, 5):
    valor = random.randint(10,99)
    linha.append(valor)
  linhas.append(linha)
  somalinha.append(sum(linha))
  for valor in linha:
    print(valor, end=" | ")
  print('')
print('')
for j in range(0, 4):
  print(f'Vetor somalinha {j+1}: {somalinha[j]}')
print(f'\nSoma de todas as linhas: {sum(somalinha)}')


# 26) Escreva um algoritmo para calcular e imprimir a soma de duas matrizes. Seja matriz A (m x n)
# e a matriz B (n x p). Deverão ser impressas as matrizes A, B e a matriz produto obtida (C).
# Obs.: (Cᵢⱼ = n-1∑k=0 Aᵢₖ * Bₖⱼ)(i=0,1,...,m-1)(j=0,1,...,p-1)



# 27) A tabela dada a seguir contém vários itens que estão estocados em vários armazéns de uma
# companhia. É fornecido, também, o custo de cada um dos produtos armazenados.
# ARMAZÉM 1: 1200 3700 3737
# ARMAZÉM 2: 1400 4210 4224
# ARMAZÉM 3: 2000 2240 2444
# CUSTO (R$): 260,00 420,00 330,00
# Fazer um algoritmo que:
# a) leia o estoque inicial;
# b) determine e imprima quantos itens estão armazenados em cada armazém;
# c) qual o armazém que possui a maior quantidade de produto 2 armazenado;
# d) o custo total de:
#     d.1) cada produto em cada armazém;
#     d.2) estoque em cada armazém;
#     d.3) cada produto em todos os armazéns.
import random
import sys
inserirDados = int(input('Escolha entre inserir os dados manualmente ou gerar aleatórios (1 || 2): '))
entrada = []
if inserirDados == 1:
    for j in range(3):
        for z in range(3):
            valor = int(input(f'Insira a quantidade do produto {z+1} no armazém {j+1}: '))
            entrada.append(valor)
elif inserirDados == 2:
    for _ in range(9):
        valor = random.randint(10, 99)
        entrada.append(valor)
else:
    print('Escolha inválida, tente novamente')
    sys.exit()
linhas = []
print(f'\nMatriz:')
print('Produto | Armazém 1 | Armazém 2 | Armazém 3')
for i in range(0, 3):
    linha = []
    print(f'   {i+1}    |', end=' ')
    for x in range(0, 3):
        valor = entrada[i * 3 + x]
        linha.append(valor)
        print(f'{valor:<10}', end=' | ')
    linhas.append(linha)
    print('')
custoProduto = []
if inserirDados == 1:
    for i in range(3):
        custo = float(input(f'Insira o custo do produto {i+1} (R$): '))
        custoProduto.append(custo)
elif inserirDados == 2:
    for _ in range(3):
        custo = random.randint(10, 200)
        custoProduto.append(custo)
print("\nCustos dos produtos:")
for i in range(3):
    print(f"Produto {i+1}: R$ {custoProduto[i]}")
print('')
for i in range(3):
    totalProdutoArmazem = sum(linhas[j][i] for j in range(3))
    print(f"No armazém {i+1}, a quantidade total de produtos é: {totalProdutoArmazem} unidades.")
maiorQtdProduto2 = 0
armazemMaiorQtdProduto2 = 0
for i in range(3):
    qtdProduto = linhas[i][1]
    if qtdProduto > maiorQtdProduto2:
        maiorQtdProduto2 = qtdProduto
        armazemMaiorQtdProduto2 = i + 1
print(f"O armazém com a maior quantidade de produto 2 é o {armazemMaiorQtdProduto2}.")
custoTotalArmazem = [0, 0, 0]
custoTotalEstoque = [0, 0, 0]
custoTotalProduto = 0
for i in range(3):
    for j in range(3):
        qtdProduto = linhas[i][j]
        custoProduto_armazem = qtdProduto * custoProduto[j]
        custoTotalArmazem[i] += custoProduto_armazem
        custoTotalEstoque[j] += custoProduto_armazem
        custoTotalProduto += custoProduto_armazem
print("\nCustos:")
for i in range(3):
    print(f"Armazém {i+1}:")
    for j in range(3):
        print(f"Custo do produto {j+1}: R$ {linhas[i][j]} x R$ {custoProduto[j]} = R$ {linhas[i][j] * custoProduto[j]}")
    print(f"Custo total do armazém: R$ {custoTotalArmazem[i]}")
    print(f"Custo total do estoque: R$ {custoTotalEstoque[i]}")
    print("")
print(f"Custo total de todos os produtos em todos os armazéns: R$ {custoTotalProduto}")


# 28) Faça um algoritmo que monte uma estrutura de dados homogênea 10 x 30, onde o conteúdo
# de cada elemento é igual à soma dos valores de seus índices.
matriz = []
for i in range(0, 10):
    linha = []
    for j in range(0, 30):
        valor = i + j
        linha.append(valor)
    matriz.append(linha)
print("Matriz:")
for linha in matriz:
    for valor in linha:
        print(valor, end=" | ")
    print('')


# 29) Ler duas matrizes A e B, cada uma com 7 linhas e 1 coluna. Construir uma matriz C de 7 x 2,
# onde a primeira coluna deverá ser formada pelos elementos da matriz A e a segunda coluna
# deverá ser formada pelos elementos da matriz B.
import random
inserirDados = int(input('Escolha entre inserir os dados manualmente ou gerar aleatórios (1 || 2): '))
matrizA = []
matrizB = []
if inserirDados == 1:
    for j in range(7):
        valorA = int(input(f'Insira um valor para a matriz A na posição {j+1}: '))
        matrizA.append([valorA])
    for j in range(7):
        valorB = int(input(f'Insira um valor para a matriz B na posição {j+1}: '))
        matrizB.append([valorB])
elif inserirDados == 2:
    for i in range(7):
        valorA = random.randint(10, 99)
        matrizA.append([valorA])
    for i in range(7):
        valorB = random.randint(10, 99)
        matrizB.append([valorB])
print("\nMatriz A:")
for linha in matrizA:
    print(linha[0])
print("\nMatriz B:")
for linha in matrizB:
    print(linha[0])
matrizC = []
for k in range(7):
    linha = [matrizA[k][0], matrizB[k][0]]
    matrizC.append(linha)
print("\nMatriz C:")
for linha in matrizC:
    for valor in linha:
        print(valor, end=" ")
    print()


# 30) Suponha que nos é dada uma matriz de inteiros A com m=20 linhas e n=30 colunas, e um
# vetor de inteiros X com n=30 elementos. Deseja-se gerar um novo vetor de inteiros Y, formado
# a partir das seguintes operações:
# Y[0] = A[0][0] * X[0] + A[0][1] * X[1] + ... + A[0][n-1] * X[n-1]
# Y[1] = A[1][0] * X[0] + A[1][1] * X[1] + ... + A[1][n-1] * X[n-1]
# ...
# Y[m-1] = A[m-1][0] * X[0] + A[m-1][1] * X[1] + ... + A[m-1][n-1] * X[n-1]
# Escreva os dados de entrada (os valores de A e X) seguidos pelos valores dos elementos de Y.



# 31) Preencher e imprimir os elementos de uma matriz A10 x 6 de elementos reais com valores tais
# que:
# • Se I < J, A[I][J] = I / J;
# • Se I = J, A[I][J] = 0;
# • Se I > J, A[I][J] = J / I;
matriz = [[0] * 6 for _ in range(10)]
for i in range(10):
    for j in range(6):
        if i < j:
            matriz[i][j] = i / j
        elif i > j:
            matriz[i][j] = j / i
for i in range(10):
    for j in range(6):
        print(matriz[i][j], end=" | ")
    print()

# 32) Uma matriz X[n][4] contém informações sobre alunos de uma universidade. Os índices das
# linhas são os números de matrícula e os elementos da 1a, 2a, 3a e 4a colunas são,
# respectivamente, idade, sexo (0 ou 1), curso (no. do curso) e nota. Fazer um algoritmo para
# obter o aluno do sexo 0, curso 6, que obteve a melhor nota. Supor a inexistência de empate.
import random
inserirDados = input("Escolha entre inserir os dados manualmente ou gerar aleatórios (1 || 2): ")
if inserirDados != "1" and inserirDados != "2":
    inserirDados = "1"
qtdAlunos = int(input("Quantidade de alunos: "))
matrizX = []
for i in range(qtdAlunos):
    print(f"\nDados do Aluno {i+1}:")
    if inserirDados == "1":
        idade = int(input("Idade: "))
        sexo = int(input("Sexo (0 ou 1): "))
        curso = int(input("Curso (número do curso): "))
        nota = float(input("Nota: "))
    elif inserirDados == "2":
        idade = random.randint(18, 30)
        sexo = random.randint(0, 1)
        curso = random.randint(1, 10)
        nota = round(random.uniform(0, 10), 1)
        print(f"Idade: {idade}")
        print(f"Sexo: {sexo}")
        print(f"Curso: {curso}")
        print(f"Nota: {nota}")
    else: break
    matrizX.append([idade, sexo, curso, nota])
melhorNota = -1
aluno = 0
for linha in matrizX:
    if linha[1] == 0 and linha[2] == 6 and linha[3] > melhorNota:
        melhorNota = linha[3]
        aluno = linha
if aluno:
    print("\nAluno do sexo 0, curso 6, com a melhor nota:")
    matricula = matrizX.index(aluno) + 1
    print(f"Matrícula: {matricula}")
    print(f"Idade: {aluno[0]}")
    print(f"Nota: {aluno[3]}")
else:
    print("\nNenhum aluno do sexo 0, curso 6 encontrado.")


# 33) Faça um algoritmo que leia uma matriz QUANT de 10 linhas por 10 colunas e imprima as
# seguintes características:
# a) dê o somatório dos quadrados da 1a coluna;
# b) dê o somatório dos cubos da 2a linha;
# c) dê o somatório dos elementos da diagonal principal;
# d) dê o somatório total dos 100 elementos.
import random
inserirDados = input("Escolha entre inserir os dados manualmente ou gerar aleatórios (1 || 2): ")
if inserirDados != "1" and inserirDados != "2":
    inserirDados = "1"
matriz = []
if inserirDados == "1":
    print("Preencha a matriz manualmente:")
    for i in range(10):
        linha = []
        for j in range(10):
            valor = int(input(f"Informe o valor para a posição ({i+1},{j+1}): "))
            linha.append(valor)
        matriz.append(linha)
else:
    print("Preenchendo a matriz aleatoriamente:")
    for i in range(10):
        linha = []
        for j in range(10):
            valor = random.randint(10, 99)
            linha.append(valor)
        matriz.append(linha)
print("\nMatriz:")
for linha in matriz:
    for valor in linha:
        print(valor, end=" | ")
    print()
somaQuadrados = 0
for linha in matriz:
    somaQuadrados += linha[0] ** 2
somaCubos = 0
for valor in matriz[1]:
    somaCubos += valor ** 3
somaDiagonal = 0
for i in range(10):
    somaDiagonal += matriz[i][i]
somaTotal = 0
for linha in matriz:
    for valor in linha:
        somaTotal += valor
print("\nCaracterísticas da matriz:")
print(f"a) Somatório dos quadrados da 1ª coluna: {somaQuadrados}")
print(f"b) Somatório dos cubos da 2ª linha: {somaCubos}")
print(f"c) Somatório dos elementos da diagonal principal: {somaDiagonal}")
print(f"d) Somatório total dos 100 elementos: {somaTotal}")


# 34) Sabe-se que a multiplicação de duas matrizes A e B só é possível se o número de colunas da
# matriz A for igual ao número de linhas da matriz B. Assim, se A é uma matriz m x n e B uma
# matriz n x p, a multiplicação será possível e o produto será uma matriz Cm x p. O produto
# matricial pode ser muito útil em várias aplicações como, por exemplo, na situação descrita a
# seguir.
# Uma certa fábrica produziu dois tipos de motores M1 e M2 nos meses de janeiro a dezembro e
# o número de motores produzidos foi registrado na tabela a seguir (m1, m2):
# JAN: 30 20; FEV: 5 10; MAR 7: 15; ...; DEZ: 18 25.
# O setor de controle de vendas tem uma tabela do custo e do lucro (em milhares de reais) obtidos
# com cada motor.
# Custo x Lucro: 
# M1 | 10 | 3
# M2 | 15 | 2
# Para saber o custo e o lucro nos meses de janeiro a dezembro, basta que se faça o produto
# matricial das duas tabelas.
# Portanto, fazer um algoritmo que, a partir da produção mensal de motores M1 e M2 e seus
# respectivos custos e lucros, calcule o custo e o lucro em cada um dos meses e o custo e lucro
# anuais.
producaoMensal = [[30, 20], [5, 10], [7, 15], [12, 8], [9, 14], [16, 22], [20, 17], [13, 19], [11, 9], [21, 23], [24, 27]]
custoLucro = [[10, 3], [15, 2]]
if len(producaoMensal[0]) != len(custoLucro):
    print("Erro: As dimensões das matrizes não são compatíveis para a multiplicação.")
else:
    custoMensal = []
    lucroMensal = []
    for i in range(len(producaoMensal)):
        linhaCusto = []
        linhaLucro = []
        for j in range(len(custoLucro[0])):
            valorCusto = producaoMensal[i][0] * custoLucro[0][j]
            valorLucro = producaoMensal[i][1] * custoLucro[1][j]
            linhaCusto.append(valorCusto)
            linhaLucro.append(valorLucro)
        custoMensal.append(linhaCusto)
        lucroMensal.append(linhaLucro)
    custoAnual = [sum(coluna) for coluna in zip(*custoMensal)]
    lucroAnual = [sum(coluna) for coluna in zip(*lucroMensal)]
    print("Custo e Lucro Mensal:")
    for i in range(len(producaoMensal)):
        print(f"Mês {i+1}: Custo = {custoMensal[i]}, Lucro = {lucroMensal[i]}")
    print("\nCusto e Lucro Anual:")
    print(f"Custo Anual: {custoAnual}")
    print(f"Lucro Anual: {lucroAnual}")
# 1) Faça uma função para converter uma temperatura em graus Fahrenheit para
# Celsius. A temperatura em Fahrenheit é o dado de entrada e a temperatura em
# Celsius é o dado de saída. Utilize a fórmula C = (F - 32) * 5/9, onde F é a
# temperatura em Fahrenheit e C é a temperatura em Celsius.
fahrenheit = float(input('Digite a temperatura em Fahrenheit: '))
celsius = 0

def fahrenheitToCelsius(fahrenheit):
  celsius = (fahrenheit - 32) * (5/9)
  return celsius

print(f'A temperatura é: {fahrenheit:.0f}°F | {fahrenheitToCelsius(fahrenheit):.0f}°C')


# 2) Faça uma função que calcule a hipotenusa. Os catetos são os dados de entrada e
# a hipotenusa é o dado de saída.
# hipotenusa = (catetoA² + catetoB²)**(1/2)
cateto1 = float(input('Digite o valor do primeiro cateto: '))
cateto2 = float(input('Digite o valor do segundo cateto: '))

def pitagoras(cateto1, cateto2):
  hipotenusa = ((cateto1**2)+(cateto2**2))**(1/2)
  return hipotenusa

print(f'Catetos: {cateto1} e {cateto2} | Hipotenusa: {pitagoras(cateto1, cateto2):.2f}')


# 3) Escreva um programa para ler as notas das duas avaliações de um aluno no
# semestre. Faça uma função que receba as duas notas por parâmetro e calcule e
# escreva a média semestral e a mensagem “PARABÉNS! Você foi aprovado!”
# somente se o aluno foi aprovado (considere 6.0 a média mínima para aprovação).
notas = [float(input('Informe a primeira nota: ')), float(input('Informe a segunda nota: '))]
media = 0

def calcularMedia(notas):
  media = sum(notas)/len(notas)
  return media

print(f'A média das duas notas do aluno é: {calcularMedia(notas)}')


# 4) Faça um programa que leia a altura e o sexo (codificado da seguinte forma:
# 1-feminino 2-masculino) de uma pessoa. Depois faça uma função chamada
# pesoideal que receba a altura e o sexo via parâmetro e que calcule e retorne seu
# peso ideal, utilizando as seguintes fórmulas:
# • para homens: (72.7 * h) – 58
# • para mulheres: (62.1 * h) – 44.7
# Observação: Altura = h (na fórmula acima).
sexo = int(input('Informe o genero da pessoa (1 - feminino | 2 - masculino): '))
altura = float(input('Informe a altura da pessoa (metros): '))
peso = 0

def pesoIdeal(sexo, altura):
  if sexo == 1: 
    peso = (62.1 * altura) - 44.7
    return peso
  elif sexo == 2: 
    peso = (72.7 * altura) - 58
    return peso
  else: print('erro!')

print(pesoIdeal(sexo, altura))


# 5) Escreva um programa para ler o número de lados de um polígono regular e a
# medida do lado (em cm). Faça uma função que receba como parâmetro o número
# de lados e a medida do lado deste polígono e calcule e imprima o seguinte:
# • Se o número de lados for igual a 3, escrever TRIÂNGULO e o valor do seu
# perímetro.
# • Se o número de lados for igual a 4, escrever QUADRADO e o valor da sua área.
# • Se o número de lados for igual a 5, escrever PENTÁGONO.
# Observação: Considere que o usuário só informará os valores 3, 4 ou 5.
qtdLados = int(input('Informe a quantidade de lados do seu polígo regular (3, 4 ou 5): '))
medidaLados = int(input('Informe a medida dos lados do poligono regular (metros): '))

def definirPoligo(qtdLados, medidaLados):
  if qtdLados == 3: 
    return f'TRIÂNGULO | Perímetro: {medidaLados * qtdLados}'   
  elif qtdLados == 4: 
    return f'QUADRADO | Área = {medidaLados * medidaLados}'
  elif qtdLados == 5: 
    return f'PENTÁGONO'
  else: return f'erro'

print(f'{definirPoligo(qtdLados, medidaLados)}')


# 6) Escreva uma função que recebe 2 números inteiros n1 e n2 como entrada e
# retorna a soma de todos os números inteiros contidos no intervalo [n1,n2]. Use
# esta função em um programa que lê n1 e n2 do usuário e imprime a soma.
import numpy as np
n1 = float(input('Informe o primeiro valor: '))
n2 = float(input('Informe o segundo valor: '))

def somaInteirosIntervalo(n1, n2):
  inteiros = []
  for i in np.arange(n1,n2):
    inteiros.append(i)
  return sum(inteiros)

print(f'Soma dos inteiros no intervalo: {somaInteirosIntervalo(n1, n2)}')


# 7) Escreva uma função que receba um número inteiro e imprima o mês
# correspondente ao número. Por exemplo, 2 corresponde a “fevereiro”. O
# procedimento deve mostrar uma mensagem de erro caso o número recebido não
# faça sentido. Gere também um programa que leia um valor e chame a função
# criada.
numero = int(input("Insira um número inteiro entre 1 e 12: "))
def imprimirMes(numero):
    meses = {
        1: "Janeiro",
        2: "Fevereiro",
        3: "Março",
        4: "Abril",
        5: "Maio",
        6: "Junho",
        7: "Julho",
        8: "Agosto",
        9: "Setembro",
        10: "Outubro",
        11: "Novembro",
        12: "Dezembro"
    }
    if numero in meses:
        print(meses[numero])
    else:
        print("Número inválido. Por favor, insira um número entre 1 e 12.")

imprimirMes(numero)


# 8) Escreva uma função que receba um número natural e imprima os três primeiros
# caracteres do dia da semana correspondente ao número. Por exemplo, 7
# corresponde a “SAB”. O procedimento deve mostrar uma mensagem de erro caso
# o número recebido não corresponda a um dia da semana. Gere também um
# programa que utilize essa função, chamando-a, mas antes lendo um valor para
# passagem de parâmetro.
numero = int(input("Insira um número int entre 1 e 7: "))

def imprimirDiaSemana(numero):
    diasSemana = {
        1: "DOM",
        2: "SEG",
        3: "TER",
        4: "QUA",
        5: "QUI",
        6: "SEX",
        7: "SAB"
    }
    if numero in diasSemana:
        print(diasSemana[numero])
    else:
        print("Número inválido. Por favor, insira um número entre 1 e 7.")

imprimirDiaSemana(numero)


# 9) Escreva uma função que receba dois números inteiros x e y. Essa função deve
# verificar se x é divisível por y. No caso positivo, a função deve retornar 1, caso
# contrário zero. Escreva também um programa para testar tal função.
def divisivel(x, y):
    if x % y == 0:
        return 1
    else:
        return 0

x = int(input("Digite o valor de x: "))
y = int(input("Digite o valor de y: "))

resultado = divisivel(x, y)
if resultado == 1:
    print(f"{x} é divisível por {y}")
else:
    print(f"{x} não é divisível por {y}")

# 10) Criar uma função que calcule e retorne o MAIOR entre dois valores recebidos como
# parâmetros. Um programa para testar tal função deve ser criado.
def calcularMaior(valor1, valor2):
    if valor1 > valor2:
        return valor1
    else:
        return valor2

valor1 = float(input("Digite o primeiro valor: "))
valor2 = float(input("Digite o segundo valor: "))
maior = calcularMaior(valor1, valor2)
print(f"O maior valor entre {valor1} e {valor2} é: {maior}")

# 11) Crie uma função que realize a conversão de Polegadas (pol) para Centímetros
# (cm), onde pol é passado como parâmetro e cm é retornado. Sabe-se que 1
# polegada tem 2.54 centímetros. Crie também um programa para testar tal função.
pol = float(input("Digite o valor em polegadas: "))

def polToCm(pol):
    cm = pol * 2.54
    return cm
    
print(f"{pol} polegadas equivalem a {polToCm(pol)} centímetros.")
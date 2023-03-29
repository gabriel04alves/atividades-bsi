# Aula 01 - Introdução ao Python


# 1) Faça um programa que peça dois números inteiros e imprima a soma desses dois números.
int1 = int(input('Digite um número inteiro: '))
int2 = int(input('Digite um número inteiro: '))
print(f'{int1} + {int2} = {int1 + int2}')


# 2) Escreva um programa que leia um valor em metros e o exiba convertido em milímetros.
valorMetros = float(input('Digite o valor em metros: '))
valorMilimetros = valorMetros * 1000
print(f'{valorMilimetros}')


# 3) Escreva um programa que leia a quantidade de dias, horas, minutos e segundos do usuário. Calcule o total em segundos.
dias = int(input('Digite a quantidade de dias: '))
horas = int(input('Digite a quantidade de horas: '))
minutos = int(input('Digite a quantidade de minutos: '))
segundos = int(input('Digite a quantidade de segundos: '))

diasToSeg = (((dias*24)*60)*60)
horasToSeg = ((horas*60)*60)
minutosToSeg = (minutos*60)

somaTudo = diasToSeg + horasToSeg + minutosToSeg + segundos

print(f'A duração total do evento em segundos foi: {somaTudo}')


# 4) Faça um programa que calcule o aumento de um salário. Ele deve solicitar o valor do salário e a porcentagem do aumento. Exiba o valor do aumento e do novo salário.
salario = float(input('Informe o valor do salario: '))
aumento = float(input('Informe o valor do aumento em %: '))/100

valorAumento = salario*aumento
salarioTotal = salario + (salario * aumento)

print(f'O valor do aumento é R${valorAumento:.2f}, e o salario total é: R${salarioTotal:.2f}.')


# 5) Solicite o preço de uma mercadoria e o percentual de desconto. Exiba o valor do desconto e o preço a pagar.
precoMercadoria = float(input('Qual o preço da mercadoria? '))  
valorDesconto = float(input('Informe o percentual(%) de desconto: '))/100

desconto = precoMercadoria * valorDesconto
precoFinal = precoMercadoria - desconto 

print(f'O valor do desconto é R${desconto:.2f}. O preço total a pagar é: R${precoFinal:.2f}')


# 6) Calcule o tempo de uma viagem de carro. Pergunte a distância a percorrer e a velocidade média esperada para a viagem.
distancia = float(input('Informe a distância percorrida em km: '))
velocidadeMedia = float(input('Informe a velocidade média em km/h: '))

tempo = distancia / velocidadeMedia

print(f'A duração da viagem foi {tempo} horas.')


# 7) Converta uma temperatura digitada em Celsius para Fahrenheit. F = 9*C/5 + 32 . Faça agora o contrário, de Fahrenheit para Celsius.
tempCelsius = int(input('Informe a temperatura em celsius: '))

tempFahr = (tempCelsius*1.8)+32

print(f'A temperatura é {tempFahr}°F.')


# 8) Escreva um programa que pergunte a quantidade de km percorridos por um carro alugado pelo usuário, assim como a quantidade de dias pelos quais o carro foi alugado. Calcule o preço a pagar, sabendo que o carro custa R$ 60,00 por dia e R$ 0,15 por km rodado.
distancia = float(input('Informe a distância que o carro percorreu em km: '))
dias = int(input('Informe a quantidade de dias que o carro o carro foi alugado: '))

valorDistancia = distancia * 0.15
valorDias = dias*60
valorTotal = valorDistancia + valorDias

print(f'O valor total a pagar é {valorTotal:.2f}.')


# 9) Escreva um programa para calcular a redução do tempo de vida de um fumante. Pergunte a quantidade de cigarros fumados por dia e quantos anos ele já fumou. Considere que um fumante perde 10 minutos de vida a cada cigarro, calcule quantos dias de vida um fumante perderá. Exiba o total de dias.
cigarrosDia = int(input('Informe a quantidade de cigarros fumados por dia: '))
fumanteAnos = int(input('Informe quantos você já fumou: '))

quantMinutos = cigarrosDia * 10
quantDias = ((quantMinutos/60)/24)
totalPerdido = quantDias * ((fumanteAnos*12)*30)

print(f'Perdeu {totalPerdido} dias de vida por fumar.')


# 10) Sabendo que str( ) converte valores numéricos para string, calcule quantos dígitos há em 2 elevado a um milhão.
numero = str(2**(1*10**3))
print(len(numero))
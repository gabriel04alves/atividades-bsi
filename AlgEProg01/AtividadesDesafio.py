# ---- Parte 1 ----

# 1. Fazer um algoritmo para ler o valor do lado de um quadrado e mostrar sua área( lado2 ) e seu perímetro ( 4 x lado ).
lado = float(input('Informe o valor de um dos lados do quadrado: '))

area = lado**2
perimetro = lado*4

print(f'Área: {area}, perimetro: {perimetro}.')


# 2. Elaborar um algoritmo para ler o nome e a quantidade de filhos de uma pessoa. Mostrar a mensagem: “Fulano tem 5 filhos.”
nome = input('Qual o seu nome?')
qtdFilhos = input('Quantos filhos que você possui: ')

print(f'{nome} possui {qtdFilhos} filhos.')


# 3. Fazer um algoritmo para ler os valores da base e altura de um retângulo e mostrar seu perímetro ( 2 x ( base + altura ) ) e sua área ( base x altura ).
base = float(input('Informe a base do triângulo: '))
altura = float(input('Informe a altura: '))

perimetro = (base*altura)


# 4. Fazer um algoritmo para ler o valor do lado de um cubo e mostrar sua área ( 6 x lado2) e seu volume (lado3).
lado = float(input('Informe o valor de um lado do cubo: '))

area = (lado**2)
volume = lado**3

print(f'Área: {area}, volume: {volume}.')


# 5. Elaborar um algoritmo para ler dois números e mostrar o quociente e o resto da divisão inteira do primeiro pelo segundo número.
lado = float(input('Informe o valor de um lado do cubo: '))

area = (lado**2)
volume = lado**3

print(f'Área: {area}, volume: {volume}.')


# 6. Criar um algoritmo para ler a base e a altura de um triângulo e mostrar a sua área ( ( base x altura ) / 2 ).
base = float(input('Informe a base do triângulo: '))
altura = float(input('Informe a altura: '))

area = (base*altura)/2

print(f'Área: {area}')


# 7. Construir um algoritmo para ler o raio de uma circunferência e mostrar o perímetro ( 2 x π x raio ) e a área ( π x raio2). Utilize o π como constante.
import math
raio = float(input('Insira o raio: '))

perimetro = 2 * math.pi  * raio
area = math.pi * raio**2



# ---- Parte 2 ----



# 9) Faça um algoritmo que calcule o volume de uma lata de óleo. Escreva o resultado. FÓRMULA: volume = p * raio2 * altura
import math
lataRaio = int(input('Informe o raio da lata: '))
lataAltura = int(input('Informe a altura da lata: '))

volume = math.pi * (lataRaio**2) * lataAltura

print(volume)


# 10) Faça um algoritmo que leia as 3 notas de um aluno e calcule e escreva a média final deste aluno. Considerar que a média é ponderada e que o peso das notas é: 2,3 e 5, respectivamente.
nota1 = int(input('Informe a primeira nota: '))
nota2 = int(input('Informe a segunda nota: '))
nota3 = int(input('Informe a terceira nota: '))

mediaAluno = (( (nota1 * 2) + (nota2 * 3) + (nota3 * 5) )/10)

print(f'A media é: {mediaAluno}')


# 11) Faça um algoritmo que leia as coordenadas de dois pontos, P1 (x1, y1) e P2 (x2, y2) respectivamente, e calcule e escreva a distância entre eles. 
class ponto:
    X = 0
    Y = 0 

ponto1 = ponto()
ponto1.X = int(input('informe o valor de X do p1:'))
ponto1.Y = int(input('informe o valor de y do p1:'))

ponto2 = ponto()
ponto2.X = int(input('informe o valor de X do p2:'))
ponto2.Y = int(input('informe o valor de y do p2:'))

distancia = (((ponto2.X - ponto1.X)**2) + ((ponto2.Y - ponto1.Y)**2))**(1/2)

print(f'a distancia entre os pontos é {distancia}')


# 12) Um sistema de equações lineares da forma: |ax + by = c | dx + ey = f ...pode ser resolvido utilizando-se as seguintes fórmulas: x=(ce-bf)/(ae-bd) y = (af - cd) / (ae - bd) Faça um algoritmo que leia os valores a, b, c, d, e, f, e calcule x e y.
a = int(input('informe a: '))
b = int(input('informe b: '))
c = int(input('informe c: '))
d = int(input('informe d: '))
e = int(input('informe e: '))
f = int(input('informe f: '))

x = ((c*e)-(b*f))/((a*e)-(b*d))
y = ((a*f)-(c*d))/((a*e)-(b*d))

print(f'X = {x} \nY = {y}')


# 13) O custo ao consumidor de um carro novo é a soma do custo de fábrica com a percentagem do distribuidor e dos impostos (aplicados ao custo de fábrica). Supondo que a percentagem do distribuidor seja de 28% e os impostos de 45%, escrever um algoritmo que leia o custo de fábrica de um carro e escreva o custo ao consumidor.
custoFabrica = float(input('informe o custo de fábrica: '))

custoFinal = custoFabrica + (custoFabrica*0.28) + (custoFabrica*0.45)

print(f'O custo final é: R${custoFinal}')


# 14) Faça um algoritmo que leia a idade de uma pessoa expressa em dias e mostre-a expressa em anos, meses e dias.
import math
idadeDias = int(input('Informe a idade em dias: '))

idadeMeses = idadeDias/30
idadeAnos = idadeMeses/12

print(f'a idade é: {math.floor(idadeDias)} dias, {math.floor(idadeMeses)} meses e {math.floor(idadeAnos)} anos.')


# 15) Faça um algoritmo que leia o tempo de duração de um evento em uma fábrica expressa em segundos e mostre-o expresso em horas, minutos e segundos.
import math
eventoSegundos = int(input('informe a duração do evento em segundos: '))

eventoMinutos = eventoSegundos / 60
eventoHoras = eventoMinutos / 60

print(f'o evento durou: {math.floor(eventoHoras)} horas, {math.floor(eventoMinutos)} minutos e {math.floor(eventoSegundos)} segundos.')


# 16) O governador acaba de liberar R$ 1.000.000.000,00 para construção de casas populares. Cada casa custa o equivalente a 90 salários mínimos. Faça um algoritmo que leia o valor do salário mínimo e calcule a quantidade de casas que podem ser construídas com o recurso liberado.
import math
salarioMin = int(input('informe o valor do salario minimo: '))

valorCasa = salarioMin * 90
quantCasa = 1000000000 / valorCasa

print(f'Quantidade de casas: {math.floor(quantCasa)}.')


# 17) Faça um algoritmo que leia o salário bruto mensal de um funcionário, calcule e mostre os valores conforme modelo abaixo: Salário Bruto: R$X // (-) IR (15%):R$X // (-) INSS (11%):R$X // (-) Sindicato (3%):R$X //  Salário Líquido :R$X 
import math
salarioBruto = float(input('Informe o valor do salario bruto: '))

ir = salarioBruto * 0.15
inss = salarioBruto * 0.11
sindicato = salarioBruto * 0.03
salarioLiq = salarioBruto - (ir+inss+sindicato)

print(f'ir: {math.floor(ir)}\ninss: {math.floor(inss)}\nsindicato: {math.floor(sindicato)}\nsalario liquido: {salarioLiq}')


# 18) Maria quer saber quantos litros de gasolina precisa colocar em seu carro e quanto vai gastar para fazer uma viagem até a casa de sua irmã. Faça um algoritmo que leia: A distância da casa de Maria até sua irmã; O consumo do carro de Maria (KM rodados / litro); O preço da gasolina (litro). E mostre as informações que Maria necessita.
distancia = float(input('Informe a distancia (em Km): '))
consumo = float(input('Informe o consumo de gasolina (em litros) por cada 1km rodado: '))
precoGaso = float(input('Informe o preco da gasolina: '))

qtdGaso = distancia / consumo
gasto = qtdGaso * precoGaso

print(f'a quantidade gasolina que precisa abastecer é: {qtdGaso:.2f} litros \nvai gastar: R${gasto:.2f}')


# 19) Faça um algoritmo que leia as medidas dos 4 lados de um terreno, o preço de um mourão e o preço de um metro de arame farpado. Deve ser escrito: o número de mourões necessários para cercar o terreno, colocando um mourão a cada 3 metros; o gasto total, o gasto em mourões e o gasto em arame, supondo que a cerca seja feita com 4 fios de arame.
import math
lado1 = int(input('Qual a medida do primeiro lado do terreno? '))
lado2 = int(input('Qual a medida do segundo lado do terreno? '))
lado3 = int(input('Qual a medida do terceiro lado do terreno? '))
lado4 = int(input('Qual a medida do quarto lado do terreno? '))
precoMourao = int(input('Qual o preco de um mourão? '))
precoArame = int(input('Qual o preco de um metro de arame farpado? '))

perimetro = lado1 + lado2 + lado3 + lado4

quantMourao = perimetro/3
gastoMourao = quantMourao * precoMourao

quantArame = perimetro*4
gastoArame = quantArame*precoArame

print(f'\nA quantidade mouroes necessarios é: {math.floor(quantMourao):.2f} \nO gasto com mouroes sera de: R${math.ceil(gastoMourao):.2f} \n  \nO gasto com arame sera de: R${math.ceil(gastoArame):.2f} e o \n \nO gasto total sera: R${math.ceil(gastoMourao + gastoArame):.2f}')


# 20) São dados de entrada sobre um automóvel: modelo, marca, ano, km inicial, km final, litros de combustível consumidos, preço por litro. Faça um algoritmo que escreva os dados de saída da seguinte forma:
# modelo_______________________ marca______________ ano________
# distância percorrida ________________
# litros de combustível consumidos _____________
# preço por litro R$ _____________
# total a pagar R$ ______________
# km por litro __________
modeloCarro = str(input('Informe o modelo: '))
marcaCarro = str(input('Informe o marca: '))
anoCarro = int(input('Informe o ano de fabricação: '))
kmInicial = float(input('Informe o km inicial: '))
kmFinal = float(input('Informe o km final: '))
consumoCarro = float(input('Informe o consumo de combustível (em litros) por cada 1km rodado: '))
precoComb = float(input('Informe o preco do combustível: '))

distancia = kmFinal - kmInicial 

qtdComb = distancia * consumoCarro
gastoComb = qtdComb * precoComb

print(f'\nModelo: {modeloCarro}, marca: {marcaCarro}, ano: {anoCarro:.0f} \n \nDistância percorrida: {distancia:.2f} Km \nKm por litro: {consumoCarro:.2f} \nConsumo de combustível: {qtdComb:.2f} litros \nPreço por litro: R${precoComb:.2f} \n \nTotal a pagar: R${gastoComb:.2f}')



# ---- Parte 3 ----



# 1. Faça um Programa que mostre a mensagem "Alo mundo" na tela.
print('Hello world')


# 2. Faça um Programa que peça um número e então mostre a mensagem O número informado foi [número].
numero = float(input('Informe um número: '))
print(f'O número informado foi: {numero}')


#3. Faça um Programa que peça dois números e imprima a soma.
num1 = float(input('Informe um número: '))
num2 = float(input('Informe outro número: '))
print(f'A soma dos números informados é: {num1 + num2}')


#4. Faça um Programa que peça as 4 notas bimestrais e mostre a média.
nota1 = float(input('Informe a primeira nota do bimestre: '))
nota2 = float(input('Informe a segunda nota do bimestre: '))
nota3 = float(input('Informe a terceira nota do bimestre: '))
nota4 = float(input('Informe a quarta nota do bimestre: '))

media = (nota1 + nota2 + nota3 + nota4)/4

print(f'A média é: {media}')


# 5. Faça um Programa que converta metros para centímetros.
metros = float(input('Informe um valor em metros: '))
centimetros = metros * 100
print(f'Metros: {metros} --> Centimetros: {centimetros}')


# 6. Faça um Programa que peça o raio de um círculo, calcule e mostre sua área.
import math
raio = float(input('Informe o raio de um círculo: '))
area = math.pi * raio**2
print(f'A área do circulo é: {area:.2f}')


# 7. Faça um Programa que calcule a área de um quadrado, em seguida mostre o dobro desta área para o usuário. 
lado = float(input('Informe um dos lados do quadrado: '))
area = lado*2 
areaDobro = (lado*2)*2
print(f'O dobro da area desse quadrado é: {areaDobro}')


#8.Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês. Calcule e mostre o total do seu salário no referido mês.
salarioHora = float(input('Informe quanto você ganha por hora: '))
horasTrabalhadasMes = float(input(f'Informe quantas horas você trabalhou no mês: '))

salarioMes = salarioHora * horasTrabalhadasMes

print(f'O salário no mês foi de R${salarioMes:.2f}')


# 11.Faça um Programa que peça 2 números inteiros e um número real. Calcule e mostre: a. o produto do dobro do primeiro com metade do segundo . b. a soma do triplo do primeiro com o terceiro. c. o terceiro elevado ao cubo.
int1 = int(input('Informe um valor inteiro: '))
int2 = int(input('Informe outro valor inteiro: '))
real1 = float(input('Informe um valor real: '))

a = int1 + (int2/2)
b = (int1 * 3) + real1
c = real1**3

print(f'A) {a}; B) {b}, C) {c}')


# 12. Tendo como dados de entrada a altura de uma pessoa, construa um algoritmo que calcule seu peso ideal, usando a seguinte fórmula: (72.7*altura) - 58
altura = float(input('Informe a altura: '))
pesoIdeal = (72.7*altura) + 58
print(f'O peso ideal é {pesoIdeal}Kg.')


# 16. Faça um programa para uma loja de tintas. O programa deverá pedir o tamanho em metros quadrados da área a ser pintada. Considere que a cobertura da tinta é de 1 litro para cada 3 metros quadrados e que a tinta é vendida em latas de 18 litros, que custam R$ 80,00. Informe ao usuário a quantidades de latas de tinta a serem compradas e o preço total.
import math
area = float(input('Informe o tamanho da área a ser pintada em m²: '))
qtdLatas = math.ceil((area / 3) / 18) 
preco = qtdLatas * 80
print(f'\nQuantidade de latas: {qtdLatas} \nPreço total: {preco:.2f}')


# 17. Faça um Programa para uma loja de tintas. O programa deverá pedir o tamanho em metros quadrados da área a ser pintada. Considere que a cobertura da tinta é de 1 litro para cada 6 metros quadrados e que a tinta é vendida em latas de 18 litros, que custam R$ 80,00 ou em galões de 3,6 litros, que custam R$ 25,00.Informe ao usuário as quantidades de tinta a serem compradas e os respectivos preços em 3 situações: comprar apenas latas de 18 litros; comprar apenas galões de 3,6 litros; misturar latas e galões, de forma que o preço seja o menor. Acrescente 10% de folga e sempre arredonde os valores para cima, isto é, considere latas cheias.
import math
area = float(input('Informe o tamanho da área a ser pintada em m²: '))
qtdLatas = math.ceil(area / 6)
preco = qtdLatas * 80
print(f'\nQuantidade de latas: {qtdLatas} \nPreço total: {preco:.2f}')


# 18. Faça um Programa para uma loja de tintas. O programa deverá pedir o tamanho em metros quadrados da área a ser pintada. Considere que a cobertura da tinta é de 1 litro para cada 6 metros quadrados e que a tinta é vendida em latas de 18 litros, que custam R$ 80,00 ou em galões de 3,6 litros, que custam R$ 25,00. Informe ao usuário as quantidades de tinta a serem compradas e os respectivos preços em 3 situações: comprar apenas latas de 18 litros; comprar apenas galões de 3,6 litros; misturar latas e galões, de forma que o preço seja o menor. Acrescente 10% de folga e sempre arredonde os valores para cima, isto é, considere latas cheias.
import math
area = float(input('Informe o tamanho da área a ser pintada em m²: '))*1.1

qtdLatas = math.ceil(area / (18 * 6))
precoLata = qtdLatas * 80
print(f'Você vai precisar de {qtdLatas} latas. Isso vai custar R${precoLata:.2f}')

qtdGaloes = math.ceil(area / (3.6 * 6))
precoGalao = qtdGaloes * 80
print(f'Você vai precisar de {qtdGaloes} galões. Isso vai custar R${precoGalao:.2f}')

qtdLatas = area // 108
qtdGaloes = math.ceil((area % 108) / 21.6) 
print(f'Você usara {qtdLatas} de 18 litros e {qtdGaloes} de 3,6 litros. O que custará R${(qtdLatas * 80 + qtdGaloes * 25):.2f}')  


# 19. Faça um programa que peça o tamanho de um arquivo para download (em MB) e a velocidade de um link de Internet (em Mbps), calcule e informe o tempo aproximado de download do arquivo usando este link (em minutos).
tamanhoMb = float(input('Informe o tamanho do arquivo em MB: '))
velocidadeInternet = float(input('Informe a velocidade de um link de internet em Mbps: '))
tempo = (tamanhoMb / (velocidadeInternet / 8)) / 60
print(f'O tempo é aproximadamente {tempo} minutos.')
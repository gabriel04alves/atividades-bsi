# 1. Faça um algoritmo que: • leia 20 números inteiros; • escreva os números que são negativos; • escreva a média dos números positivos.
contador = int(input('Defina o tamanho do contador: '))
nums = []
negativos = []
positivos = []

for i in range(contador): 
  num = int(input('Digite um número: '))
  nums.append(num)
for num in nums:
  if num < 0:
    negativos.append(num)
  elif num > 0: 
    positivos.append(num)
media = sum(positivos)/len(positivos)

print(f'Negativos: {negativos}')
print(f'Média dos positivos: {media}')


# 2. Faça um algoritmo que leia 15 números inteiros e escreva, para cada número lido, se é par ou ímpar.
contador = int(input('Defina o tamanho do contador: '))
nums = []
pares = []
impares = []

for i in range(contador): 
  nums.append(int(input('Digite um número inteiro: ')))

for num in nums: 
  if num % 2 == 0:
    pares.append(num)
  else: impares.append(num)

print(f'Pares: {pares} \nÍmpares: {impares}')


# 3. Dado um conjunto de valores inteiros positivos, determinar qual o menor e qual o maior valor do conjunto. Um número com valor “0” (zero) indica o fim dos dados e não deve ser considerado.
contador = int(input('Defina o tamanho do contador: '))
nums = []

for x in range(contador):
    num = int(input('Digite um número inteiro: '))
    if num != 0:
        nums.append(num)
    else:
        print('0 = fim.')
        break

print(f'Maior valor: {max(nums)}\n Menor valor: {min(nums)}')


# 4. Faça um algoritmo que calcule e escreva a soma dos números pares e a soma dos números ímpares entre 1 e 100.
pares = []
impares = []

for i in range(0,101):
  if i % 2 == 0:
    pares.append(i)
  else: impares.append(i)
print(f'Soma dos pares: {sum(pares)}\nSoma dos ímpares: {sum(impares)}')


# 5. Faça um algoritmo que leia a altura de 20 pessoas e calcule a média aritmética das alturas.
qtdPessoas = int(input('Informe a quantidade de pessoas: '))
somaAlturas = 0

for i in range(qtdPessoas): 
  altura = float(input('Informe a altura da pessoa: '))
  somaAlturas += altura
print(f'A média das alturas é {somaAlturas/qtdPessoas}')


# 6. Faça um algoritmo que leia n valores inteiros e escreva quantos desses valores são negativos.
qtdValores = int(input('Informe a quantidade de valores que deseja informar: '))
cont = 0

for i in range(qtdValores): 
  valor = int(input('Informe um valor: '))
  if valor < 0:
    cont += 1
print(f'Foram informados {cont} valores negativos.')


# 7. Faça um algoritmo que leia a quantidade de tinta que uma caneta, e enquanto a caneta tiver tinta para escrever, escreva “Enquanto tem tinta a caneta escreve...”. Considere que a cada comando de escrita a caneta gasta 2% da tinta que possui.
qtdTinta = float(input('Informe a quantidade de tinta da caneta: '))
tinta = qtdTinta

while qtdTinta > 0:
  print(f'Enquanto tem tinta a caneta escreve... {qtdTinta}')
  qtdTinta -= (0.02 * tinta)
print('FIM.')


# 8. Faça um algoritmo que leia n pares de valores, sendo o primeiro valor o número de inscrição do atleta e o segundo a altura (em cm) do atleta. Escreva: • o número de inscrição e a altura do atleta mais alto; • o número de inscrição e a altura do atleta mais baixo; • a altura média do grupo de atletas.
qtdAtletas = int(input('Informe a quantidade de atletas: '))
atletas = []

for i in range(qtdAtletas):
  numInscricao = int(input('Digite o número de inscrição do atleta: ')) 
  altura = float(input('Digite a altura do atleta (em cm): '))
  atleta = {'numInscricao': numInscricao, 'altura': altura}
  atletas.append(atleta)
maisAlto =  max(atletas, key=lambda x: x['altura'])
maisBaixo = min(atletas, key=lambda x: x['altura'])
somaAlturas = sum(atleta['altura'] for atleta in atletas)
mediaAlturas = somaAlturas / qtdAtletas
print(f"\nMédia de altura dos atletas: {mediaAlturas}")
print(f"\nAtleta mais alto - número: {maisAlto['numInscricao']}, altura: {maisAlto['altura']}cm")
print(f"Atleta mais baixo - número: {maisBaixo['numInscricao']}, altura: {maisBaixo['altura']}cm")


# 9. Faça um algoritmo que calcule e imprima os valores de y, onde: y = (3+2x+6x²)/(1+9x+16x²), para x variando de 1.0 até 5.0, em intervalos de 0.1 unidades.
import numpy as np
x = np.arange(1, 5.1, 0.1)
y = (3+2*x+(6*x**2))/(1+9*x+(16*x**2))
print(y)


# 10. Construir um algoritmo que calcule o fatorial de um número N.
num = int(input('Informe um número: '))

for n in range(1, num):
  num *= n
  print(num)


# 11. Faça um algoritmo que calcule e escreva a soma da seguinte série de 100 termos: 1 + 2 + 3 + 4 + ... +100
sum = 0
for i in range(1,101):
  sum = i+sum
  print(sum)


# 12. Faça um algoritmo que calcule e escreva a soma da seguinte série de 100 termos: (1/1) + (1/2) + (1/3) + ... + (1/100)
sum = 0
base = 0
for i in range(1,101):
  sum += 1/i
  print(sum)


# 13. Fazer um algoritmo para calcular o valor de S, dado por:
# S = (1/N) + (2/N-1) (3/N-2) + ... + (N-1/2) + (N/1) sendo N lido.



# 14. O valor aproximado do número p pode ser calculado usando-se a série:
# S = 1 - (1/3³) + (1/5³) + (1/7³) + (1/9³) - ...
# sendo o valor de pi = ³√Sx32. Faça um algoritmo que calcule e escreva o valor de p usando os 51 primeiros termos da série.



# 15. Fazer um algoritmo que calcule e escreva a soma dos 20 primeiros termos da série:
# (100/0!) + (99/1!) + (98/2!) + (97/3!) + ...



# 16. Fazer um algoritmo que calcule e imprima o valor de ex através da série:
# eˣ = x⁰ + (x¹/1!) + (x²/2!) + (x³/3!) + ...
# Considerar para efeitos de cálculo os 30 primeiros termos. O algoritmo deverá ler o valor de x.



# 17. Foi feita uma pesquisa de audiência de canal de TV em n casas de um determinado bairro de Joinville, em um certo dia do mês. Na pesquisa foi utilizado um coletor de dados portátil. Para cada casa visitada, foi fornecido o número do canal (4, 5, 9, 12) e o número de pessoas que estavam assistindo a TV naquele horário, considerando que
# em cada casa só existia uma televisão. Em casas onde a televisão estava desligada, foi registrado zero para o número do canal e para o número de pessoas. Faça um algoritmo que calcule e escreva, para cada emissora, o percentual de audiência.



# 18. Uma companhia de teatro planeja dar uma série de espetáculos. A direção calcula que, a R$ 5,00 o ingresso, serão vendidos 120 ingressos. Com a diminuição de R$ 0,50 no preço dos ingressos, espera-se que haja um aumento de 26 ingressos vendidos. As despesas estão estipuladas em R$ 200,00 independente do número de ingressos vendidos. 
# Faça um algoritmo que escreva uma tabela contendo o preço do ingresso, o número de ingressos e o lucro esperado em função do preço do ingresso, fazendo-se variar este preço de R$ 5,00 a R$ 1,00 de R$ 0,50 em R$ 0,50. Escreva também o lucro máximo esperado, o preço e o número de ingressos correspondentes.



# 19. Faça um algoritmo que leia n números inteiros e escreva, para cada número lido, os divisores e quantidade de divisores.
# EXEMPLO: número lido = 12; divisores = 1, 2, 3, 4, 6, 12; quantidade divisores = 6



# 20. Uma máquina de biscoito está com problemas. Quando ligada, após 1 hora ela quebra 1 biscoito, na segunda hora ela quebra 3 biscoitos, na hora seguinte ela quebra 3 vezes a quantidade de biscoitos quebrados na hora anterior, e assim por diante.
# Faça um algoritmo que calcule quantos biscoitos são quebrados no final de cada dia (a máquina opera 16 horas por dia).



# 21. Uma turma tem 50 alunos. Faça um algoritmo que: • leia para cada aluno o seu nome e idade; • escreva os nomes dos alunos que tem 18 anos; • escreva a quantidade de alunos que tem idade acima de 20 anos.



# 22. Faça um algoritmo que: • leia, para n pessoas, a altura e o sexo (sexo = 'M' ou sexo = 'm' para masculino e sexo = 'F' ou sexo = 'f' para feminino); • escreva a média da altura das mulheres; • escreva a média da altura da turma.



# 23. Uma loja de departamentos oferece para seus clientes um determinado desconto de acordo com o valor da compra efetuada. O desconto é de 20% caso o valor da compra seja maior que R$ 500,00 e de 15% caso seja menor ou igual. 
# Faça um algoritmo que leia, para cada cliente, nome, endereço e valor da compra e escreva o total a pagar. Um nome de cliente igual a ULTIMO indica o fim da entrada de dados.



# 24. Faça um algoritmo que leia valores, sendo que cada valor representa a idade de uma pessoa. Calcule e escreva a idade média do grupo de pessoas. Só devem ser computados no cálculo valores maiores do que zero. O algoritmo deve apresentar ao usuário a seguinte mensagem:
# deseja digitar mais um valor: s (SIM) / n (NAO)?, antes de prosseguir com a entrada de dados.



# 25. Um hotel cobra R$ 50,00 de diária por hóspede e mais uma taxa de serviços. A taxa de serviços é de:
# • R$ 7,50 por diária, caso o número de diárias seja menor que 15; • R$ 6,50 por diária, caso o número de diárias seja igual a 15; • R$ 5,00 por diária, caso o número de diárias seja maior que 15.
# Faça um algoritmo que apresente as seguintes opções ao recepcionista: 1. encerrar a conta de um hóspede; 2. verificar número de contas encerradas; 3. finalizar a execução.
# Caso a opção escolhida seja a primeira, leia o nome e o número de diárias do hóspede e escreva o nome e total a ser pago. Caso a opção escolhida seja a segunda, informe o número de hóspedes que deixaram o hotel (número de contas encerradas).



# 26. Um determinado material radioativo perde metade de sua massa a cada 50 segundos. Dada a sua massa inicial em Kg, faça um algoritmo que determine o tempo necessário
# para que essa massa se torne menor que 0,5 gramas. Escreva a massa inicial, a massa final e o tempo.



# 27. Um motorista acaba de voltar de um feriado prolongado. Antes de sair de viagem e imediatamente após retornar, o motorista encheu o tanque do veículo e registrou as medidas do odômetro. Em cada parada feita durante a viagem, foi registrado o valor do odômetro e a quantidade de combustível comprado para reabastecer o veículo (suponha que o tanque ficou vazio e foi enchido a cada parada). 
# Faça um algoritmo que leia o número total de reabastecimentos feitos (incluindo o primeiro) e os dados registrados relativos à compra de combustível. Calcule e escreva:
# a) a quilometragem obtida por litro de combustível entre cada par de paradas; b) a quilometragem média obtida por litro de combustível em toda a viagem.



# 28. Em uma disputa de pingue-pongue os pontos são anotados como D, ponto para o jogador do lado direito, e E, ponto para o jogador do lado esquerdo da mesa. Faça um
# algoritmo que leia o código do ponto de cada jogada e determine o vencedor. A partida encerra quando:
# a) um dos jogadores chegar a 21 pontos e a diferença de pontos entre os jogadores for maior ou igual a dois; b) o jogador com mais de 21 pontos conseguir uma diferença de dois pontos sobre o adversário, caso a primeira condição não seja atendida.



# 29. Os regulamentos de uma competição de pesca impõem um limite no peso total de pesca de um dia. Faça um algoritmo que leia o limite diário (em quilogramas) e então leia o peso (em gramas) de cada peixe e escreva o peso total da pesca obtido até
# aquele ponto. Quando o limite diário for excedido escreva uma mensagem e encerre a execução do algoritmo. O algoritmo deve ainda apresentar ao usuário a seguinte mensagem: informar o peso de mais um peixe: s (SIM) / n (NÃO)? antes de prosseguir com a entrada de dados.



# 30. Foi feita uma pesquisa do consumo mensal de energia elétrica em uma determinada cidade. Para cada consumidor, são fornecidos os seguintes dados: 
# número de identificação do consumidor, quantidade de kWh consumidos durante o mês, código do tipo de consumidor (R - residencial, C - comercial, I - industrial). Faça um algoritmo que:
# a) leia o preço do kWh por tipo de consumidor; b) leia os dados de n consumidores; c) escreva o número de identificação e o total a pagar, para cada consumidor; 
# d) escreva a quantidade total de KWh consumida para cada um dos três tipos de consumidores; e) escreva a quantidade média geral de consumo.



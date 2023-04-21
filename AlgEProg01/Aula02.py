# --- Lista de exercícios de estrutura de decisão --- 


# 2. Ler um valor e escrever se é positivo, negativo ou zero.
valor = float(input('Digite um valor: '))
if valor >= 1: 
  print(f'{valor} é positivo.')
elif valor <= -1:
  print(f'{valor} é negativo.')
else: print(f'{valor} é zero.')


# 3. Ler um valor e escrever a mensagem É MAIOR QUE 10! se o valor lido for maior que 10, caso contrário escrever NÃO É MAIOR QUE 10!
valor = float(input('Digite um valor: '))
if valor > 10: 
  print(f'{valor} é maior que 10!')
else: print(f'{valor} não é maior que 10!.')


# 4. Calcule a soma de dois números, se o resultado for maior que 10, mostre-o na tela.
num1 = float(input('Digite um valor: '))
num2 = float(input('Digite outro valor: '))
soma = num1 + num2
if soma > 10:
  print(f'A soma é maior que 10: {soma}.')
else: print(f'O resultado não maior que 10, portanto, não será exibido.')


# 5. Entrar com um número e informar se ele é divisível por 5.
valor = float(input('Digite um valor: '))
resto = valor%5
if resto == 0:
  print(f'{valor} é divisível por 5')
else: print(f'{valor} não é divisível por 5')


# 6. Construir um algoritmo que indique se o número digitado está entre 20 e 90 ou não.
valor = float(input('Digite um valor: '))
if valor > 20 and valor < 90: 
  print(f'{valor} está entre 20 e 90.')
else: print(f'{valor} não está entre 20 e 90.')


# 7. Ler o ano atual e o ano de nascimento de uma pessoa. Escrever uma mensagem que diga se ela poderá ou não votar este ano (não é necessário considerar o mês em que a pessoa nasceu).
anoAtual = float(input('Digite o ano atual: '))
anoNasc = float(input('Digite o ano de nascimento: '))

idade = anoAtual - anoNasc
tempoParaVotar = 16 - idade 

if idade >= 16: 
  print(f'O cidadão já pode exercer seu direito de voto.')
else: print(f'O cidadão ainda não pode votar. Poderá votar daqui a {tempoParaVotar:.0f} Ano.')


# 8. Entrar com o ano de nascimento de uma pessoa e imprimir a idade dela. Verificar se o ano digitado é válido.
anoAtual = float(input('Digite o ano atual: '))
anoNasc = float(input('Digite o ano de nascimento: '))
idade = anoAtual - anoNasc

if anoNasc > anoAtual: 
  print(f'O ano de nascimento é inválido.')
else: print(f'Idade: {idade:.0f}')


# 9. Entrar com a idade de uma pessoa e exibir a mensagem; Maior de idade, menor de idade ou acima de 65 anos.
anoAtual = float(input('Digite o ano atual: '))
anoNasc = float(input('Digite o ano de nascimento: '))

idade = anoAtual - anoNasc
tempoParaMaior = 18 - idade 

if idade >= 18 and idade < 65: 
  print(f'A pessoa já é maior de idade.')
elif idade >= 65: 
  print(f'A pessoa já é maior de idade e tem mais de 65 anos.')
else: print(f'A pessoa ainda não é maior de idade, se tornara em {tempoParaMaior:.0f} Ano.')


# 10. Ler as notas da 1a . e 2a . avaliações de um aluno. Calcular a média aritmética simples e escrever uma mensagem que diga se o aluno foi ou não aprovado (considerar que se a nota for igual ou maior que 6 o aluno é aprovado). Escrever também a média calculada.
nota1 = float(input('Informe a primeira nota (0-10): '))
nota2 = float(input('Informe a segunda nota (0-10): '))
media = (nota1 + nota2)/2
if media >= 6: 
  print(f'{media}. Aprovado.')
else: print(f'{media}. Reprovado.')


# 11. Escrever um algoritmo para ler duas notas de um aluno e escrever na tela a palavra “Aprovado” se a média das duas notas for maior ou igual a 7,0. Caso a média seja inferior a 7,0, o programa deve ler a nota do exame e calcular a média final. Se esta média for maior ou igual a 5,0, o programa deve escrever “Aprovado”, caso contrário deve escrever “Reprovado”.
nota1 = float(input('Informe a primeira nota (0-10): '))
nota2 = float(input('Informe a segunda nota (0-10): '))
media = (nota1 + nota2)/2
if media <= 7:
  exame = float(input('Informe a nota no exame final (0-10): '))
  mediaFinal = (nota1 + nota2 + exame)/3
  if mediaFinal >= 7: 
    print(f'{mediaFinal}. Aprovado por exame.')
  else: print(f'{mediaFinal}. Reprovado')
else: print(f'{media}. Aprovado')


# 12. Escrever um algoritmo para ler a quantidade de horas aula dadas por dois professores e o valor por hora recebido por cada um. Mostrar na tela qual dos professores tem salário total maior.
valorHora = float(input('Digite quanto o professor recebe por hora de aula: '))
qtdHorasAula1 = float(input('Digite quantas horas o professor1 lecionou no mês: '))
qtdHorasAula2 = float(input('Digite quantas horas o professor2 lecionou no mês: '))
salarioHora1 = valorHora * qtdHorasAula1
salarioHora2 = valorHora * qtdHorasAula2
if salarioHora1 > salarioHora2: 
  print(f'O professor 1 teve uma salário total maior.')
elif salarioHora2 > salarioHora1: 
  print(f'O professor 2 teve uma salário total maior.')
else: print(f'Os professores receberam um salário total igual.')


# 13. Faça um algoritmo que leia um número inteiro e mostre uma mensagem indicando se este número é par ou ímpar.
valor = int(input('Digite um númeor inteiro: '))
resto = valor%2
if resto == 0: 
  print('O valor é par.')
else: print('O valor é ímpar.')


# 14. Ler o nome de 2 times e o número de gols marcados na partida. Escrever o nome do vencedor. Caso não haja vencedor deverá ser impressa a palavra EMPATE.
time1 = input('Informe o nome da equipe 1: ')
time2 = input('Informe o nome da equipe 2: ')
gols1 = int(input(f'Informe quantos gols o(a) {time1} fez: '))
gols2 = int(input(f'Informe quantos gols o(a) {time2} fez: '))
if gols1 > gols2:
  print(f'{time1} venceu {time2} pelo placar de {gols1}x{gols2}.')
elif gols2 > gols1: 
  print(f'{time2} venceu {time1} pelo placar de {gols1}x{gols2}.')
else: print(f'O jogo terminou empatado em {gols1}x{gols2}.')


# 15. Entrar com a sigla do estado de uma pessoa e imprimir uma das mensagens: “Carioca, Paulista, Mineiro ou Outros”
estado = input('Informe a sigla do estado: ').upper()
if estado == 'RJ':
  print('Carioca')
elif estado == 'SP':
  print('Paulista')
elif estado == 'MG':
  print('Mineiro')
elif estado == 'SC':
  print('Catarinense')
else: print('Outros')


# 16. Um comerciante comprou um produto e quer vendê-lo com um lucro de 45% se o valor da compra for menor que R$ 20,00; Caso contrário, o lucro será de 30%. Entrar com o valor do produto e imprimir o valor da venda.
precoProduto = float(input('Preço do produto (R$): '))
if precoProduto < 20: 
  precoProdutoLucro = precoProduto + (precoProduto * 0.45)
  print(f'O preço do produto com lucro do comerciante será: {precoProdutoLucro}')
else:
  precoProdutoLucro = precoProduto + (precoProduto * 0.30)
  print(f'O preço do produto com lucro do comerciante será: {precoProdutoLucro}')


# 17. Entrar com um número de 1 a 12 e exibir o mês correspondente.
num = int(input('Informe um número entre 1 e 12: '))
mes = {
    1: 'janeiro', 2: 'fevereiro', 3: 'março', 4: 'abril', 
    5: 'maio', 6: 'junho', 7: 'julho', 8: 'agosto',
    9: 'setembro', 10: 'outubro', 11: 'novembro', 12: 'dezembro'
}
mesNum = mes[num]
print(f'O mês que corresponde a {num} é {mesNum}.')


# 18. Faça um algoritmo que verifique se uma letra digitada é vogal ou consoante.



# 19. Ler 2 valores (considere que não serão lidos valores iguais) e escrever o maior deles.



# 20. Ler 2 valores (considere que não serão lidos valores iguais) e escrevê-los em ordem crescente.



# 21. Ler 3 valores (considere que não serão informados valores iguais) e escrever o maior deles.



# 22. Ler 3 valores (considere que não serão informados valores iguais) e escrever a soma dos 2 maiores.



# 23. Ler 3 valores (considere que não serão informados valores iguais) e escrevê-los em ordem crescente.



# 24. Faça um algoritmo que leia as duas notas parciais obtidas por um aluno numa disciplina ao longo de um semestre, e calcule a sua média. A atribuição de conceitos obedece à tabela abaixo:
# Média de Aproveitamento Conceito: Entre 9.0 e 10.0 A; Entre 7.5 e 9.0 B; Entre 6.0 e 7.5 C; Entre 4.0 e 6.0 D; Entre 4.0 e zero E; O algoritmo deve mostrar na tela as notas, a média, o conceito correspondente e a mensagem “APROVADO” se o conceito for A, B ou C ou “REPROVADO” se o conceito for D ou E.



# 25. Escrever um algoritmo para ler dois valores e uma das seguintes operações a serem executadas (codificadas da seguinte forma: 1 – Adição, 2 – Subtração, 3 – Multiplicação e 4 – Divisão). Calcular e escrever o resultado dessa operação sobre os dois valores lidos.



# 26. Faça um algoritmo para calcular as raízes reais de uma equação quadrática: ax2 + bx + c = 0. Uma equação quadrática só tem raiz reais se (b2 - 4ac) for maior ou igual a zero. O algoritmo deverá informar as seguintes situações:
# • Se o delta calculado for negativo, a equação não possui raízes reais. Informe ao usuário e encerre o programa; • Se o delta calculado for igual a zero a equação possui apenas uma raiz real, informe-a ao usuário; • Se o delta for positivo, a equação possui duas raiz reais, informe-as ao usuário.



# 27. Faça um algoritmo que leia 3 valores a, b, c, e verifique se podem ser os comprimentos dos lados de um triângulo. Em caso afirmativo, verifique se é “triângulo equilátero”, “triângulo isósceles” ou “triângulo escaleno”. Em caso negativo, escreva uma mensagem: “os valores lidos não formam um triângulo”. 
# Considere que: • o comprimento de cada lado de um triângulo é menor que a soma dos comprimentos dos outros lados; • um triângulo equilátero tem três lados iguais; • um triângulo isósceles tem dois lados iguais e um diferente; • um triângulo escaleno tem três lados diferentes.



# 28. Escreva um algoritmo que leia 4 valores (opção, a, b, c), onde opção é um valor inteiro e positivo e a, b, c são quaisquer valores reais. Escreva os valores lidos da seguinte maneira:
# se opção = 1 Þ escreva os 3 valores a, b, c em ordem crescente; se opção = 2 Þ escreva os 3 valores a, b, c em ordem decrescente; se opção = 3 Þ escreva os 3 valores de forma que o maior valor entre a, b, c fica entre os outros 2;



# 29. Uma empresa decidiu conceder um aumento de salário a seus funcionários de acordo com a tabela:
# em R$ | Índice de Aumento
# salário  =< 400.00 | 15%
# 400.00 < salário =< 700.00 | 12%
# 700.00 < salário =< 1000.00 | 10%
# 1000.00 < salário =< 1500.00 | 7%
# 1500.00 < salário =< 2000.00 | 4%
# salário > 2000.00 | sem aumento
# Faça um algoritmo que leia o salário atual de um funcionário e escreva o índice de aumento e o valor do salário corrigido.



# 30. Faça um algoritmo para calcular o reajuste salarial de um funcionário, de acordo com os critérios abaixo: • se salário é inferior a R$ 10.000,00 deve ter um reajuste de 55%; • se salário está entre R$ 10.000,00 (inclusive) e R$ 25.000,00 (inclusive) deve ter um reajuste de 20%; • se salário é superior a R$ 25.000,00 deve ter um reajuste de 20%.



# 31. Faça um algoritmo para controle de temperatura de um forno que derrete alumínio. O programa deverá perguntar qual a temperatura que o alumínio deverá ser trabalhado e operar nas seguintes condições:
# • Se temperatura for inferior ou igual 500°C enviar uma mensagem para tela "Temperatura Inválida"; • Se temperatura for menor do que 700°C enviar uma mensagem para tela "Aquecimento Ligado em 100%"; • Se temperatura for menor do que 735°C enviar uma mensagem para tela "Aquecimento Ligado em 50%"; • Se temperatura for maior ou igual 735°C enviar uma mensagem para tela "Aquecimento Desligado"; • Se temperatura for maior do que 780ºC enviar uma mensagem para tela "Superaquecimento'.
# Os valores digitados devem ser inteiros e inferiores a 1000.



# 32. Faça um algoritmo que permita a entrada de um valor de 1 a 4. Em seguida, leia dois valores. Calcular e imprimir:
# • Se valor digitado for o, calcular e exibir a soma dos números • Se valor digitado for 1, calcular e exibir a subtração dos números • Se valor digitado for 2, calcular e exibir a multiplicação dos números • Se valor digitado for 3, calcular e exibir a divisão dos números • Se valor digitado for 4, calcular e exibir a média dos números e Diferente de 1,2,3 ou 4, exibir a mensagem “Valor errado. Programa encerrado sem cálculos”



# 33. Escrever um algoritmo que leia valores inteiros em duas variáveis distintas e se o resto da divisão da primeira pela segunda for 1 mostre a soma dessas variáveis mais o resto da divisão; se for 2 escreva se o primeiro e o segundo valor são pares ou ímpares; se for igual a 3 multiplique a soma dos valores lidos pelo primeiro; se for igual a 4 divida à soma dos números lidos pelo segundo, se este for diferente de zero. Em qualquer outra situação mostre o quadrado dos números lidos.



# 34. Escreva um algoritmo que leia as idades de 2 homens e 2 mulheres (considere que as idades dos homens serão sempre diferentes, bem como as das mulheres). Calcule e escreva a soma das idades do homem mais velho com a mulher mais nova, e o produto das idades do homem mais novo com a mulher mais velha.



# 35. Existem números de 4 dígitos (entre 1000 e 9999) que obedecem à seguinte característica: se dividirmos o número em dois números de dois dígitos, um composto pela dezena e pela unidade, e outro pelo milhar e pela centena, e, ao somarmos estes dois novos números gerando um terceiro, o quadrado deste terceiro número é exatamente o número original de quatro dígitos. Por exemplo:
# 2025 -> dividindo: 20 e 25 -» somando temos 45 -> 45º = 2025.
# Escreva um programa para ler um número e verificar se ele obedece a esta característica.



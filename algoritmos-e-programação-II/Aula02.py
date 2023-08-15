data = {
    'Zico': 70,
    'Junior': 69,
    'Nunes': 69,
    'Leandro': 64,
    'Gabriel': 26,
    'Bruno Henrique': 32,
    'Arrascaeta': 29,
}

print('CRUD simples com nomes e idades!')
print('\nAções: 1 - Add nova pessoa, 2 - Atualizar dados de pessoa, 3 - Excluir pessoa, 4 - Ler todos os dados ')

while True: 
  acao = int(input('Insira o valor correspondente a ação desejada: '))

  def newPerson(name, age):
    if name in data: 
      print(f'\nNão foi possível realizar a ação, o valor já existe!')
    else:
      data[name] = age
    
  def updatePerson(name, newName, newAge):
    if name in data: 
      data[newName] = data.pop(name)
      data[newName] = newAge
    else:
      print('Não foi possível encontrar essa pessoa nos dados.')

  def deletePerson(name):
    del data[name]

  def viewAll(boolean):
    print(f'\nTodos os dados:')
    for name, age in data.items():
      print(f'{name}: {age} anos de idade.')
    print(f'\nEstatisticas: ')
    print(f'Total: {len(data)} pessoas;')
    print(f'Média das idades: {round(sum(data.values())/len(data.values()))} anos;')
    print(f'Pessoa mais velha: {max(data, key=data.get)}, {max(data.values())} anos;')
    print(f'Pessoa mais nova: {min(data, key=data.get)}, {min(data.values())} anos;')
    personJ = []
    for name in data.keys():
      if name[0] == 'J':
        personJ.append(name)
    print(f'Pessoas cujo nome começa com a letra "J": {", ".join(personJ)}.')

  if acao == 1:
    name = input('Digite o nome: ').strip()
    age = int(input('Digite a idade: '))
    newPerson(name, age)

  elif acao == 2:
    name = input('Digite o nome: ').strip()
    newName = input('Digite o novo nome: ')
    newAge = int(input('Digite a nova idade: '))
    updatePerson(name, newName, newAge)

  elif acao == 3:
    name = input('Digite o nome que deseja deletar dos dados: ').strip()
    deletePerson(name)

  elif acao == 4:
    viewAll(True)
  
  next = int(input('\nDeseja continuar(1) ou parar(2)? '))
  if next == 2: 
    break
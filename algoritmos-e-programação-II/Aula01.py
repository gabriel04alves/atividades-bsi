# Crie um jogo que embaralhe uma palavra e a mostre ao jogador. O objetivo dele é
# acertar a palavra em no máximo 5 tentativas. Informe sempre quantas tentativas ele
# ainda tem. Se ele acertar, dê os parabéns; se errar dê uma palavra de ânimo (de
# preferência não fixa). Ao final, mostre a palavra correta e o número de tentativas que
# ele utilizou.Incluir escolha de temas para as palavras (cidades, cores, times, países, objetos, etc.)
# e níveis de dificuldade (ex: iniciante, intermediário, avançado).


import random
from random import shuffle
temas = {
    "cidades": [['Joinville', 'Araquari', 'Curitiba'], ['Rio de Janeiro', 'Madrid', 'New York', 'Paris', 'Roma'], ['Dallas', 'Bilbao', 'Nice', 'Verona']],
    "frutas": [['Maçã', 'Banana', 'Pera'], ['Abacate', 'Melancia', 'Acerola'], ['Pitaia', 'Jabuticaba', 'Carambola']],
    "animais": [['Macaco', 'Cão', 'Gato'],['Passarinho', 'Marreco', 'Camelo'],['Hipopotamo', 'Jaguatirica', 'Iguana']]
}

tentativas = 5
palavraAnimo = ['Não desista!', 'Mais sorte na próxima!', 'Não pare por aqui!']
print('Tente adivinhar a palavra embaralhada!')
tema = input(f'\nEscolha um tema ({"; ".join(temas.keys())}): ').strip()
dificuldade = int(input(f'Escolha o nível de dificuldade (1, 2, 3): '))

palavrasTemaDificuldade = temas[tema][dificuldade-1]
shuffle(palavrasTemaDificuldade)
palavra = palavrasTemaDificuldade[0]
listaEmbaralhada = list(palavra)
random.shuffle(listaEmbaralhada)
palavraEmbaralhada = "".join(listaEmbaralhada)
palavraEmbaralhada = palavraEmbaralhada.lower()

while True:
  tentativa = input(f'\nParavra embaralhada: {palavraEmbaralhada}. Tente advinhar: ')
  if tentativas > 1:
    if tentativa.lower() == palavra.lower():
      print(f'\nParabéns! Você acertou a palavra embaralhada.')
      break
    elif tentativa != palavra:
      tentativas -= 1
      print(f'\n{random.choice(palavraAnimo)}')
      print(f'Tentativa errada, você ainda possui {tentativas} tentativas.')
      continue
  else:
    print(f'\nVocê não possui mais tentativas! A resposta é {palavra}.')
    break
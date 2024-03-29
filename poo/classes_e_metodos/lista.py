#01:
class Ball():
  __ball = ''

  def __init__(self, color, circ, material):
    self.color = color
    self.circ = circ
    self.material = material

  def changeColor(self, new_color):
    self.color = new_color

  def showColor(self):
    return self.color

ball = Ball(color='Red', circ = 10, material="plastic")
print(f"Ball's color: {ball.showColor()}.")

ball.changeColor('Black')
print(f"New color: {ball.showColor()}.")


#02
class Square():
  __square = ''

  def __init__(self, sideSize):
    self.sideSize = sideSize

  def changeSideSize(self, newSideSize):
    self.sideSize = newSideSize

  def sideValue(self):
    return self.sideSize

  def calcArea(self):
    return self.sideSize ** 2

square = Square(sideSize=20)
print(f"Side size: {square.sideValue()}")
print(f"Area: {square.calcArea()}")


#03
class Rectangle:
    def __init__(self, base, height, sizeFloor, sizeBaseBoard):
        self.base = base
        self.height = height
        self.sizeFloor = sizeFloor
        self.sizeBaseBoard = sizeBaseBoard

    def returningSides(self):
        return self.base, self.height

    def changeSides(self, newBase, newHeight):
        self.base = newBase
        self.height = newHeight
  
    def calcArea(self):
        area = self.base * self.height
        return area
  
    def calcPerimeter(self):
        perimeter = (self.base + self.height) * 2
        return perimeter

    def calcFloor(self, area):
        quantityFloor = area / self.sizeFloor
        return quantityFloor

    def calcBaseBoard(self, perimeter):
        quantityBaseBoard = perimeter / self.sizeBaseBoard
        return quantityBaseBoard

base = int(input('Defina o valor da base do retângulo: '))
height = int(input('Defina o valor da altura do retângulo: '))
sizeFloor = int(input('Defina o tamanho de cada piso: '))
sizeBaseBoard = int(input('Defina o tamanho de cada rodapé: '))

rectangle = Rectangle(base=base, height=height, sizeFloor=sizeFloor, sizeBaseBoard=sizeBaseBoard)

area = rectangle.calcArea()
perimeter = rectangle.calcPerimeter()

print(f'\nA área é de: {area}. \nO perímetro é de {perimeter}.')
print(f'\nA quantidade de piso que preciso, com base nas medidas informadas, é de: {rectangle.calcFloor(area)}. \nA quantidade de rodapé necessário, com base nas medidas informadas, é de: {rectangle.calcBaseBoard(perimeter)}')


#04
class Person:
    def __init__(self, name, age, weight, height):
        self.name = name
        self.age = age
        self.weight = weight
        self.height = height

    def grow_old(self, years):
        self.age += years
        if self.age < 21:
            self.height += 0.5 * years

    def gain_weight(self, weight_gain):
        self.weight += weight_gain

    def lose_weight(self, weight_lost):
        self.weight -= weight_lost

    def grow_taller(self, height_cm):
        self.height += height_cm

person = Person(name="Gabri", age=19, weight=60, height=170)

print("Primeiros dados:")
print("Name:", person.name)
print("Age:", person.age)
print("Weight:", person.weight)
print("Height:", person.height)

person.grow_old(2)
person.grow_taller(2)

print("\nDepois de 2 anos:")
print("Age:", person.age)
print("Height:", person.height)

person.gain_weight(5)
person.lose_weight(3)

print("\nNovo peso:", person.weight)


#05
class CheckingAccount:
    def __init__(self, account_number, account_holder_name, balance=0):
        self.account_number = account_number
        self.account_holder_name = account_holder_name
        self.balance = balance

    def changeHolderName(self, new_name):
        self.account_holder_name = new_name

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance -= amount
        else:
            print("Saldo insuficiente.")

account = CheckingAccount(account_number="12345", account_holder_name="Gabriel")

print("Número da conta:", account.account_number)
print("Nome do titular da conta:", account.account_holder_name)
print("Saldo inicial:", account.balance)

account.changeHolderName("Gabri")
print("Novo nome do titular da conta:", account.account_holder_name)

account.deposit(500)
print("Saldo após depósito:", account.balance)

account.withdraw(200)
print("Saldo após saque:", account.balance)

account.withdraw(400)
print("Saldo após tentativa de saque:", account.balance)
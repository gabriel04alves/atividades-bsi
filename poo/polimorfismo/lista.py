#01 
class Animal:
    def speak(self):
        pass
class Dog(Animal):
    def speak(self):
        return "Woof"
class Cat(Animal):
    def speak(self):
        return "Meow"

class Fish(Animal):
    def speak(self):
        return "fish don't talk"

dog = Dog()
cat = Cat()
fish = Fish()
print("Dog says:", dog.speak())
print("Cat says:", cat.speak())
print("Fish says:", fish.speak())

#02 
class AnimalBase:
    def speak(self):
        pass
class Dog(AnimalBase):
    def speak(self):
        return "Woof!"
class Cat(AnimalBase):
    def speak(self):
        return "Meow!"

animals = [Dog(), Cat()]  
for animal in animals:
    print(animal.speak()) 

#03
class Carro():
  def dirigir(self):
    pass
class CarroGasolina(Carro):
  def dirigir(self):
    return "VRUUUUUM"
class CarroEletrico(Carro):
  def dirigir(self):
    return "vruum"
def dirigindo(carro):
  print(carro.dirigir())

gasolina = CarroGasolina()
eletrico = CarroEletrico()
dirigindo(gasolina)
dirigindo(eletrico)

#04
from math import pi

class Shape():
  def area(self):
    pass
class Circle(Shape):
  def __init__(self, radius):
    self.radius = radius
  def area(self):
    return pi * self.radius ** 2
  def name(self):
    return "circle"
class Square(Shape):
  def __init__(self, side):
    self.side = side
  def area(self):
    return self.side ** 2
  def name(self):
    return "square"

shapes = [Circle(3), Square(2)]

for shape in shapes:
  print(f"The area of the {shape.name()} is: {shape.area()}")

#05
class Employee():
  def pay_salary(self):
    pass
class HourlyEmployee(Employee):
  def __init__(self, hours_worked, hourly_rate):
    self.hours_worked = hours_worked
    self.hourly_rate = hourly_rate
  def pay_salary(self):
    return self.hourly_rate * self.hours_worked
class MonthlyEmployee(Employee):
  def __init__(self, salary):
    self.salary = salary
  def pay_salary(self):
    return self.salary
  
employees = [HourlyEmployee(40, 20), MonthlyEmployee(2000)]

for employee in employees:
  print(f"R${employee.pay_salary():.2f}")


#06
class BankAccount:
    def __init__(self, balance=0):
        self.balance = balance
    def deposit(self, amount):
        self.balance += amount
    def withdrawal(self, amount):
        if self.balance >= amount:
            self.balance -= amount
        else:
            print("Insufficient balance for the withdrawal.")

class SavingsAccount(BankAccount):
    def __init__(self, balance=0, interest_rate=0.03):
        super().__init__(balance)
        self.interest_rate = interest_rate
    def apply_interest(self):
        self.balance *= (1 + self.interest_rate)

class CheckingAccount(BankAccount):
    def __init__(self, balance=0, interest_rate=0.01):
        super().__init__(balance)
        self.interest_rate = interest_rate
    def apply_interest(self):
      self.balance *= (1 + self.interest_rate)

savings_account = SavingsAccount(balance=1000)
checking_account = CheckingAccount(balance=2000)
savings_account.deposit(500)
checking_account.withdrawal(300)
print(f"Balance of Savings Account: R${savings_account.balance:.2f}")
print(f"Balance of Checking Account: R${checking_account.balance:.2f}")
savings_account.apply_interest()
checking_account.apply_interest()
print(f"Balance of Savings Account after interest: R${savings_account.balance:.2f}")
print(f"Balance of Checking Account after interest: R${checking_account.balance:.2f}")

#07
class User():
    def __init__(self):
        self.points = 0
        self.num_articles = 0
    def set_num_articles(self, num):
        self.num_articles = num
    def get_num_articles(self):
        return self.num_articles
    def calculate_score(self):
        pass
class Author(User):
    def calculate_score(self):
        return self.num_articles * 10 + 20
class Editor(User):
    def calculate_score(self):
        return self.num_articles * 6 + 15

author1 = Author()
author1.set_num_articles(8)
author1_score = author1.calculate_score()
print(f"Author's score: {author1_score}")
editor1 = Editor()
editor1.set_num_articles(15)
editor1_score = editor1.calculate_score()
print(f"Editor's score: {editor1_score}")

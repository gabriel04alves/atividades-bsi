#01 
class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

  def printInfo(self):
    return f"Name: {self.name}\nAge: {self.age}"

class Student(Person):
  def __init__(self, name, age, grade):
    super().__init__(name, age)
    self.grade = grade

  def printInfo(self):
     return f"Name: {self.name}\nAge: {self.age}\nGrade: {self.grade}"

person1 = Person(name="Gabriel", age=19)
print(person1.printInfo())
print()
student1 = Student(name="Gabriel", age=19, grade=10)
print(student1.printInfo())

#02
class Vehicle:
  def __init__(self, brand, model, year):
    self.brand = brand
    self.model = model
    self.year = year

  def printInfo(self):
    return f"Brand: {self.brand}\nModel: {self.model}\nYear: {self.year}"

class Car(Vehicle):
  def __init__(self, brand, model, year, doorCount, engineDisplacement):
    super().__init__(brand, model, year)
    self.doorCount = doorCount
    self.engineDisplacement = engineDisplacement

  def printInfo(self):
    return f"Brand: {self.brand}\nModel: {self.model}\nYear: {self.year}\nDoor count: {self.doorCount}\nEngine displacement: {self.engineDisplacement}"

class Motorcycle(Vehicle):
  def __init__(self, brand, model, year, doorCount, engineDisplacement):
    super().__init__(brand, model, year)
    self.doorCount = doorCount
    self.engineDisplacement = engineDisplacement

  def printInfo(self):
    return f"Brand: {self.brand}\nModel: {self.model}\nYear: {self.year}\nDoor count: {self.doorCount}\nEngine displacement: {self.engineDisplacement}"

car1 = Car("Ford", "Mustang", 1970, 2, "5.0 L")
print(car1.printInfo())
print()
moto1 = Motorcycle("Harley-Davidson", "Fat Boy 114", 2024, 0, "1.868 cm³")
print(moto1.printInfo())

#03
class Animal():
  def __init__(self, name, weight):
    self.name = name
    self.weight = weight

  def eat(self):
    return f"Name: {self.name}\nWeight: {self.weight}kg\n{self.name} is eating!"

class Dog(Animal):
  def __init__(self, name, weight):
    super().__init__(name, weight)

  def bark(self):
    if self.weight < 6:
      return f"Name: {self.name}\nWeight: {self.weight}kg\nwoof"
    if self.weight >= 6:
      return f"Name: {self.name}\nWeight: {self.weight}kg\nWOOF!!!"

class Cat(Animal):
  def __init__(self, name, weight):
    super().__init__(name, weight)

  def meow(self):
    if self.weight < 6:
      return f"Name: {self.name}\nWeight: {self.weight}kg\nmeow"
    if self.weight >= 6:
      return f"Name: {self.name}\nWeight: {self.weight}kg\nMEOW!!!"

animal1 = Animal("Zé", 3)
print(animal1.eat())
print()
animal2 = Dog("Zé 02", 4)
print(animal2.bark())
print()
animal3 = Dog("Zé 03", 8)
print(animal3.bark())
print()

#04 
class Person():
  def __init__(self, name, age):
    self.name = name
    self.age = age

  def showInformation(self):
    return f"Name: {self.name}\nAge: {self.age} years"

class Employee(Person):
  def __init__(self, name, age, salary):
    super().__init__(name, age)
    self.salary = salary

  def increase(self, percentage):
    self.percentage = percentage
    new_salary = self.salary + (self.salary * (self.percentage/100))
    return f"Name: {self.name}\nAge: {self.age} years\nSalary: R${self.salary:.2f}\nNew salary: R${new_salary:.2f}"

person1 = Person("Zé", 20)
print(person1.showInformation())
print()
employee1 = Employee("Zé", 20, 1000)
print(employee1.increase(25))

#05
class Shape():
  def area(self):
    pass

class Rectangle(Shape):
  def __init__(self, length, width):
    self.length = length
    self.width = width

  def area(self):
    area = self.length * self.width
    return area

class Circle(Shape):
  def __init__(self, radius):
    self.radius = radius

  def area(self):
    import math
    area = math.pi * self.radius ** 2
    return area

rectangle1 = Rectangle(10, 5)
print(f"Area of the rectangle: {rectangle1.area()} cm")
print()
circle1 = Circle(2)
print(f"Area of the circle: {circle1.area()} cm")

#06
class CheckingAccount():
  def __init__(self, number, balance, client):
    self.__number = number
    self.__balance = balance
    self.__client = client

  def deposit(self, amount):
    self.__balance += amount
    return self.__balance

  def withdraw(self, amount):
    if (self.__balance - amount) >= 0:
      self.__balance -= amount
      return f"Withdrawal successful\nCurrent balance: R${self.__balance:.2f}"
    else:
      return "Insufficient balance"

  def getBalance(self):
    return self.__balance

class SpecialAccount(CheckingAccount):
  def __init__(self, number, balance, client, limit):
    super().__init__(number, balance, client)
    self.__limit = limit

  def withdraw(self, amount):
    if (self.getBalance() - amount) >= 0:
      self._CheckingAccount__balance -= amount
      return f"Withdrawal successful\nCurrent balance: R${self.getBalance():.2f}"
    else:
      return "Insufficient balance"

class SavingsAccount(CheckingAccount):
  def __init__(self, number, balance, client, minimumBalance):
    super().__init__(number, balance, client)
    self.__minimumBalance = minimumBalance

  def withdraw(self, amount):
    if (self.getBalance() - amount) >= 0:
      self._CheckingAccount__balance -= amount
      return f"Withdrawal successful\nCurrent balance: R${self.getBalance():.2f}"
    else:
      return "Insufficient balance"

  def updateBalance(self):
    return f"Current balance: {self.getBalance()}"

  def getMinimumBalance(self):
    return self.__minimumBalance

class InvestmentAccount(CheckingAccount):
  def __init__(self, number, balance, client, investmentDay, period):
    super().__init__(number, balance, client)
    self.__investmentDay = investmentDay
    self.__period = period

  def updateBalance(self):
    return f"Current balance: {self.getBalance()}"

print("Checking Account")
account1 = CheckingAccount(111, 100, "Zé")
print(account1.deposit(10))
print(account1.withdraw(10))
print(account1.getBalance())
print("\nSpecial Account")
account2 = SpecialAccount(112, 1000, "Zé 02", 2000)
print(account2.withdraw(2))
print(account2.withdraw(2000000))
print("\nSavings Account")
account3 = SavingsAccount(113, 100, "Zé 03", 10)
print(account3.withdraw(2))
print(account3.updateBalance())
print(account3.getMinimumBalance())
print("\nInvestment Account")
account4 = InvestmentAccount(114, 1000, "Zé 04", 2, 4)
print(account4.updateBalance())

#07
class Employee():
  def __init__(self, code, name, email, salary):
    self.__code = code
    self.__name = name
    self.__email = email
    self.__salary = salary

  def getSalary(self):
    return self.__salary

  def increaseSalary(self, percentage):
    self.percentage = percentage
    increase = self.__salary + ((self.percentage/100)*self.__salary)
    return f"Increase: R${increase:.2f}"

class Manager(Employee):
  def __init__(self, code, name, email, salary, benefit):
    super().__init__(code, name, email, salary)
    self.__benefit = benefit

  def increaseSalary(self, percentage):
    self.percentage = percentage
    increase = self.__benefit + (self.getSalary() + (self.getSalary()*(self.percentage/100)))
    return f"Increase: R${increase:.2f}"

class Intern(Employee):
  def __init__(self, code, name, email, salary, discount):
    super().__init__(code, name, email, salary)
    self.__discount = discount

  def increaseSalary(self, percentage):
    self.percentage = percentage
    increase = (self.getSalary() + (self.getSalary()*(self.percentage/100))) - self.__discount
    return f"Increase: R${increase:.2f}"

print("Employee:")
employee1 = Employee(1, "Zé", "ze@gmail.com", 1000)
print(employee1.increaseSalary(20))
print("\nManager:")
manager1 = Manager(2, "Zé", "ze@gmail.com", 10000, 100)
print(manager1.increaseSalary(20))
print("\nIntern:")
intern1 = Intern(3, "Zé", "ze@gmail.com", 1000, 10)
print(intern1.increaseSalary(10))

#08
class Ticket():
  def __init__(self, value):
    self.value = value

  def printValue(self):
    print(f"R${self.value:.2f}")

class VIP(Ticket):
  def __init__(self, value, additional):
    super().__init__(value)
    self.additional = additional

  def printValue(self):
    self.value += self.additional
    print(f"R${self.value:.2f}")

class Normal(Ticket):
  def ticketType(self):
    print("Normal Ticket")

class LowerBox(VIP):
  def __init__(self, value, additional, location):
    super().__init__(value, additional)
    self.location = location

  def printLocation(self):
    print(f"Lower Box location: {self.location}")

class UpperBox(VIP):
  def __init__(self, value, additional, location):
    super().__init__(value, additional)
    self.location = location

  def getValue(self):
    self.value += self.additional
    print(f"R${self.value:.2f}")

print("Ticket 1:")
ticket1 = Ticket(20)
ticket1.printValue()
print("\nTicket 2:")
ticket2 = VIP(20, 10)
ticket2.printValue()
print("\nTicket 3:")
ticket3 = Normal(20)
ticket3.ticketType()
print("\nTicket 4:")
ticket4 = LowerBox(20, 10, "xxxx")
ticket4.printLocation()
print("\nTicket 5:")
ticket5 = UpperBox(20, 10, "xxxx")
ticket5.getValue()

#09
class Employee():
  def __init__(self, name, address, phone, email):
    self.name = name
    self.address = address
    self.phone = phone
    self.email = email

  def displayData(self):
    return f"Name: {self.name}\nAddress: {self.address}\nPhone: {self.phone}\nEmail: {self.email}"

class Assistant(Employee):
  def __init__(self, name, address, phone, email, registration):
    super().__init__(name, address, phone, email)
    self.registration = registration

  def getRegistration(self):
    return self.registration

class Technician(Assistant):
  def __init__(self, name, address, phone, email, registration, bonus):
    super().__init__(name, address, phone, email, registration)
    self.bonus = bonus

  def displayData(self):
    print(f"Registration: {self.getRegistration()}\nName: {self.name}")

class Administrative(Assistant):
  def __init__(self, name, address, phone, email, registration, shift, nightBonus):
    super().__init__(name, address, phone, email, registration)
    self.shift = shift
    self.nightBonus = nightBonus

  def displayData(self):
    print(f"Registration: {self.getRegistration()}\nName: {self.name}")

print("Employee:")
employee1 = Employee("Zé", "Rua xxx", "9999999", "ze@gmail.com")
print(employee1.displayData())
print("\nAssistant:")
assistant1 = Assistant("Zé", "Rua xxx", "9999999", "ze@gmail.com", 1)
print(f"Registration: {assistant1.getRegistration()}")
print("\nTechnician:")
technician1 = Technician("Zé", "Rua xxx", "9999999", "ze@gmail.com", 2, 3)
technician1.displayData()
print("\nAdministrative:")
administrative1 = Administrative("Zé", "Rua xxx", "9999999", "ze@gmail.com", 3, "Night", 100)
administrative1.displayData()

#10
class Person():
  def __init__(self, name, age):
    self.__name = name
    self.__age = age

class Rich(Person):
  def __init__(self, name, age, money):
    super().__init__(name, age)
    self.__money = money

  def goShopping(self):
    return "Rich! Goes shopping!"

class Poor(Person):
  def __init__(self, name, age):
    super().__init__(name, age)

  def work(self):
    return "Poor! Work to improve!"

class Miserable(Person):
  def __init__(self, name, age):
    super().__init__(name, age)

  def beg(self):
    return "Miserable! Work to improve!"

print("Rich")
rich = Rich("a", 20, 100000000)
print(rich.goShopping())
print("\nPoor")
poor = Poor("b", 30)
print(poor.work())
print("\nMiserable")
miserable = Miserable("c", 30)
print(miserable.beg())
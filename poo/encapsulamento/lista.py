# Questão 01: alternativa D

# Exercícios de codificação:

# 02:
class User(): 
  __firstName = ''

  def setFirstName(self, firstName):
    self.__firstName = firstName

  def getFirstName(self):
    return self.__firstName

user1 = User()
user1.setFirstName('Joe')
print(user1.getFirstName())

# 02:
class Employee:
    def __init__(self, name, salary, project):
        self.name = name
        self.__salary = salary
        self.project = project

    def work(self):
        print(f'{self.name} is working on project {self.project}')

    def show(self):
        print(f'\nEmployee Details: \nName: {self.name} \nSalary: ${self.__salary:.2f}')

employee1 = Employee("Gabriel", 5000, "Project X")

employee1.work()

employee1.show()

# 03:
class Robot:
    def __init__(self, name, yearBuilt):
        self.__name = name
        self.__yearBuilt = yearBuilt

    def sayHello(self):
        print(f'Hello! I am the robot {self.__name}, built in the year {self.__yearBuilt}')

    def setName(self, name):
        self.__name = name

    def setYearBuilt(self, yearBuilt):
        self.__yearBuilt = yearBuilt

    def getName(self):
        return self.__name

    def getYearBuilt(self):
        return self.__yearBuilt

myRobot = Robot('Robot X', 2024)

myRobot.sayHello()

print('Robot name:', myRobot.getName())
print('Robot s year of construction:', myRobot.getYearBuilt())

myRobot.setName('Robot Y')
myRobot.setYearBuilt(2024)

myRobot.sayHello()

# 04:
class Laptop:
    def __init__(self):
        self.__price = 0

    def getPrice(self):
        return self.__price

    def setPrice(self, new_price):
        self.__price = new_price

myLaptop = Laptop()

print('Laptop price:', myLaptop.getPrice())

myLaptop.setPrice(3999)

print('\nNew laptop price:', myLaptop.getPrice())

# 05:
class Person:
    def __init__(self):
        self.__firstName = ''
        self.__lastName = ''

    def getFirstName(self):
        return self.__firstName

    def setFirstName(self, first_name):
        self.__firstName = first_name

    def getLastName(self):
        return self.__lastName

    def setLastName(self, last_name):
        self.__lastName = last_name

person = Person()

person.setFirstName('João')
person.setLastName('Carvalho')

print(f'First Name: {person.getFirstName()}')
print(f'Last Name: {person.getLastName()}')
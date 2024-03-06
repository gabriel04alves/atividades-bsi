# Questão 01: alternativa C

# Exercícios de Codificação:

# Atividade 01:
class User():
    firstName = ''
    lastName = ''

    def hey(self):
        return f'Hey {self.firstName} {self.lastName}'
    
user = User()
user.firstName = 'Gabriel'
user.lastName = 'Alves'
print(user.hey())
print(f'\nFirst name test: \nHey {user.firstName}')


newUser = User()
newUser.firstName = 'Jonnie'
newUser.lastName = 'Bravo'
print(f'{newUser.hey()}')


# Atividade 02:
class UserB:
    def __init__(self, firstName, lastName):
        self.firstName = firstName
        self.lastName = lastName

    def getFullName(self):
        return f'{self.firstName} {self.lastName}'
    

userMain = UserB('Gabriel', 'Alves')
print(f'getFullName = {userMain.getFullName()}')
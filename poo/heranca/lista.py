class User:
    def __init__(self):
        self.__nameUser = ""

    def setNameUser(self, name):
        self.__nameUser = name

    def getNameUser(self):
        return self.__nameUser

class Admin(User):
    def writeName(self):
        return "Admin"

    def sayHello(self):
        return f"Hello {self.getNameUser()}"

admin1 = Admin()
admin1.setNameUser("Baltazar")
print(admin1.sayHello()) 
# 1) b
# 2) a 
# 3) b 
# 4) a

# 5:
class User:
  name = " "
  lastName = " "
  
  def hello(self):
    return f'Hello! {self.name} {self.lastName}'

user1 = User()
user2 = User()
user2.name = "Gabriel"
user2.lastName = "Alves"
print(f'{user1.hello()}! \n{user2.name} {user2.lastName} \n{user2.hello()}')
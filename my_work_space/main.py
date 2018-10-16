from setting import session

from user import *


user = User()
user.name = '太郎'
user.age = '20'
user.email = 'tets@gmail.com'
users = session.add(user)
session.commit()


users = session.query(User).all()
for user in users :
    print(user.name)

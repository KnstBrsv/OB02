from user import User
from admin import Admin

admin1 = Admin(1, "Bob")
user1 = User(2, "Tom")
user2 = User(3, "Todd")
user3 = User(4, "Tim")
user4 = User(5, "Tina")
user5 = User(6, "Terry")

admin1.add_user(user1)
admin1.add_user(user2)
admin1.add_user(user3)
admin1.add_user(user4)
admin1.add_user(user5)

print(admin1)

admin1.change_user_level(user1, "advanced")

print(f"Авторизованные пользователи: {admin1.auth_users()}")

admin1.remove_user(user3)

print(f"Авторизованные пользователи: {admin1.auth_users()}")


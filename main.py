from user import User
from admin import Admin

# Создание пустого списка пользователей
users = []

# Создание администратора
admin = Admin(6, "Алексей")

# Администратор добавляет пользователей в систему
admin.add_user(users, User(1, "Анна"))
admin.add_user(users, User(2, "Борис"))
admin.add_user(users, User(3, "Виктор"))
admin.add_user(users, User(4, "Галина"))
admin.add_user(users, User(5, "Дмитрий"))

# Вывод списка пользователей после добавления
print("Список пользователей после добавления:")
for user in users:
    print(user)

# Администратор повышает уровень доступа у двух пользователей
admin.promote_user(users[0])  # Повышаем Анну
admin.promote_user(users[1])  # Повышаем Бориса

# Вывод списка после повышения уровня доступа
print("\nСписок пользователей после повышения::")
for user in users:
    print(user)

# Администратор удаляет одного пользователя
admin.remove_user(users, 3)  # Удаляем Виктора

# Вывод списка пользователей после удаления
print("\nСписок пользователей после удаления:")
for user in users:
    print(user)
from user import User

class Admin(User):
    def __init__(self, user_id, name):
        super().__init__(user_id, name)
        self._access_level = 'admin'

    def add_user(self, user_list, user):
        if isinstance(user, User):
            user_list.append(user)
            print(f"Пользователь {user.get_name()} был добавлен администратором {self.get_name()}.")
        else:
            print("Invalid user object.")

    def remove_user(self, user_list, user_id):
        for user in user_list:
            if user.get_user_id() == user_id:
                user_list.remove(user)
                print(f"Пользователь {user.get_name()} был удалён администратором {self.get_name()}.")
                return
        print(f"No user with ID {user_id} found.")

    def promote_user(self, user):
        if isinstance(user, User):
            if user.get_access_level() == 'user':
                user._access_level = 'advanced'  # Повышаем уровень доступа
                print(f"Пользователю {user.get_name()} повышен уровень доступа до advanced.")
            else:
                print(f"Пользователь {user.get_name()} уже имеет повышенный уровень доступа.")
        else:
            print("Invalid user object.")

    def __str__(self):
        return f"Администратор (ID: {self._user_id}, Name: {self._name}, Access Level: {self._access_level})"
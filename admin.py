from user import User


class Admin(User):
    def __init__(self, id, name):
        super().__init__(id, name)
        self.__user_level = "admin"
        self.users = []

    def __str__(self):
        return f"Администратор: {self.get_user_name()}, табельный номер: {self.get_user_id()}, уровень доступа: {self.__user_level}"
    def add_user(self, user):
        self.users.append(user)

    def remove_user(self, user):
        self.users.remove(user)

    def change_user_level(self, user, new_level):
        user._set_user_level(new_level)
        print(f"Администратор {self.get_user_name()} изменил уровень доступа пользователя {user.get_user_name()} на {new_level}.")

    def auth_users(self):
        for user in self.users:
            print(
                f"Пользователь {user.get_user_name()}, табельный номер: {user.get_user_id()}, уровень доступа: {user.get_user_level()}")

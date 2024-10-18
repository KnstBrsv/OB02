class User:
    def __init__(self, id, name):
        self.__user_id = id
        self.__user_name = name
        self.__user_level = "user"


    def get_user_id(self):
        return self.__user_id

    def get_user_name(self):
        return self.__user_name

    def get_user_level(self):
        return self.__user_level

    def _set_user_level(self, user_level):
        self.__user_level = user_level

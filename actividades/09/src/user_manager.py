class UserAlreadyExistsError(Exception):
    pass


class UserManager:
    def __init__(self):
        self.users = {}

    def add_user(self, username, password):
        if self.user_exists(username):
            raise UserAlreadyExistsError(f"El usuario '{username}' ya existe.")
        self.users[username] = password

    def user_exists(self, username):
        return username in self.users

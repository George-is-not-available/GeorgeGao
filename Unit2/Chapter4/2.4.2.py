class User:
    """
    The User class represents a basic user in the system.
    """
    def __init__(self, username, email):
        self.username = username
        self.email = email

    def __str__(self):
        return f"User: {self.username}, Email: {self.email}"


class Vip(User):
    """
    The Vip class is a subclass of the User class, representing a user with VIP privileges.
    """
    def __init__(self, username, email, vip_level):
        super().__init__(username, email)
        self.vip_level = vip_level

    def __str__(self):
        return f"VIP User: {self.username}, Email: {self.email}, VIP Level: {self.vip_level}"

class User:
    _id_counter = 1

    def __init__(self, name):
        self.id = User._id_counter
        self.name = name
        User._id_counter += 1

    def __str__(self):
        return f"User ({self.id}, {self.name})"
from models.item import Item


class Order:
    def __init__(self, user):
        self.user = user
        self.items = []

    def add_item(self, item):
        self.items.append(item)

    def total(self):
        return sum(item.price for item in self.items)

    def __str__(self):
        return f" Order of {self.user.name} for {self.total()} $"    
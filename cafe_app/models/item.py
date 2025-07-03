class Item:
    def __init__(self, name, price):
        self.name = name
        self._price = price

    @property
    def price(self):
        return self._price

    def __str__(self):
        return f"{self.name} - {self.price} $"
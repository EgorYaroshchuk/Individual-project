from typing import Protocol

class MenuItemProtocol(Protocol):
    def to_dict(self) -> dict:
        """Перетворює об'єкт страви на словник для збереження."""
        ...

    def __str__(self) -> str:
        """Повертає текстове представлення страви."""
        ...

class Dish:
    def __init__(self, name, price, category, weight):
        self.name = name
        self.price = price
        self.category = category
        self.weight = weight

    def __str__(self):
        return f"{self.name} ({self.category}) - {self.weight} г, {self.price} грн"

    def to_dict(self):
        return {
            "name": self.name,
            "price": self.price,
            "category": self.category,
            "weight": self.weight
        }

    @staticmethod
    def from_dict(data):
        return Dish(data['name'], data['price'], data['category'], data['weight'])

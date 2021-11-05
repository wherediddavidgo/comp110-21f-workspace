"""Messing with classes and objects."""


class Pizza:
    """Models a pizza."""

    # Attributes
    size: str
    toppings: int
    extra_cheese: bool


    def price(self, tax: float) -> float:
        """Calculates price of pizza."""
        total: float = 0.0
        
        if self.size == "large":
            total += 10.0
        else:
            total += 8.0
        
        total += self.toppings * 0.75

        if self.extra_cheese:
            total += 1.0
        
        total += tax
        
        return total


a_pizza: Pizza = Pizza()
a_pizza.size = "large"
a_pizza.toppings = 3
a_pizza.extra_cheese = False

print(f"Price: ${a_pizza.price()}")
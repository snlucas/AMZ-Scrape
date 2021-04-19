class Product:
    def __init__(self, name, description, price, img, rate, brand, is_prime):
        self.name = name
        self.description = description
        self.price = price
        self.img = img
        self.rate = rate
        self.brand = brand
        self.is_prime = is_prime

    def __str__(self):
        return f"""
################
{self.name}\n
{self.brand}\n\n
{self.description}\n
{self.price}\n
{self.rate} stars\n\n
Prime: {self.is_prime}
################
"""

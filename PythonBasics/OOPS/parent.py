class BaseCarModel:
    price = 1000000 # base price of the car model

    def __init__(self, model_name, year):
        self.model_name = model_name
        self.year = year

    def display_info(self):
        return f"Model: {self.model_name}; Year: {self.year}"

    def get_price(self):
        return self.price

# Example usage:
car1 = BaseCarModel("Sedan LX", 2025)

print(f"Base price of the car is: ${car1.get_price()}")
print(f"Car info: {car1.display_info()}")



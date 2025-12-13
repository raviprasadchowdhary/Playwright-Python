from PythonBasics.OOPS.parent import BaseCarModel


class DeluxeCarModel(BaseCarModel):
    deluxe_price = 200000 + BaseCarModel.price  # deluxe price of the car variant

    def __init__(self, model_name, year, isSunroof):
        super().__init__(model_name, year)
        self.feature = "Sunroof" if isSunroof else "No Sunroof"

    def display_info(self):
        base_info = super().display_info()
        return f"{base_info}; Feature: {self.feature}"

    def get_price(self):
        return self.deluxe_price


# Example usage:
car2 = DeluxeCarModel("Sedan LX Deluxe", 2025, isSunroof=True)

print(f"Deluxe model price is: ${car2.get_price()}")
print(f"Car info: {car2.display_info()}")

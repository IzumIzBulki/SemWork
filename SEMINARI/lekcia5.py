

class Car:

    def __init__(self, model: str, color: str, volume: float):
        self.model = model
        self.color = color
        self.volume = volume
    def present(self):
        return f"Machin {self.model}, {self.color} цвета с объемом {self.volume}"
    def gas(self):
        print("BrrrrBrrrr")

    def __str__(self):
        return f"Machin {self.model}, {self.color} цвета с объемом {self.volume}"

    def __repr__(self):
        return f"Machin {self.model}, {self.color} цвета с объемом {self.volume}"

ferrari = Car("F355", "red", 6.0)

bmw = Car("M3", "black", 5.0)
ferrari.sport = True
ferrari.gas()

print(ferrari.color)
print(ferrari.sport)
print(bmw.color)

print(ferrari.present())
print(bmw.present())

print(ferrari)
print(bmw)
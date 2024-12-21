class car:
    def __init__(self, brand, color):
        self.brand = brand
        self.color = color

brand1 = car ("mitsubishi", "grey")
brand2 = car ("suzuki", "blue")
print(f"original color: {brand1.brand} {brand1.color}")
brand1.color = "pink"
print(f"updated value: {brand2.brand} {brand2.color}")



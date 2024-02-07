class Cat:
# Konstruktors
    def __init__(self, name, age, eye_color):
        self.name = name
        self.age = age
        self.eye_color = 'gray'

cat1 = Cat('Emi', 2, 'Brown')
cat2 = Cat('Rony', 5, 'Green')

print(f"{cat1.name} {cat1.age} {cat1.eye_color}")
print(f"{cat2.name} {cat2.age} {cat2.eye_color}")

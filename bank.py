class Client:
    def __init__(self, name, surname, age):
        self.name = name
        self.surname = surname
        self.age = age

    def introduce(self):
        print(f"Labdien, mani sauc {self.name} {self.surname}, un man ir {self.age} gadi.")

client1 = Client('Anna', 'Bērziņa', 25)
client2 = Client('Oskars', 'Ozoliņš', 16)

Client.introduce(client1)
Client.introduce(client2)
